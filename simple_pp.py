import win32ui
import pytesseract
import asyncio

from pygame import mixer
from random import randint
from pyclick import HumanClicker
from treys import Card
from hand_picker import hand_pick_range
from PIL import Image
from ctypes import windll
from win32 import win32gui
from offsets import *


mixer.init()
mixer.music.load('./majorkeyalert.mp3')


def find_action_index(image):
    action_indexes = []
    for index, xy in enumerate(ACTIVE_CHIP_LOCATIONS):
        x, y = xy
        r, g, b = image.getpixel((x, y - 7))
        if r > 100 and g < 52:
            # reddish area means action time
            action_indexes.append(index)

    assert(len(action_indexes) <= 1)
    if action_indexes:
        return action_indexes[0]
    return -1


def convert_to_monochrome(image):
    pixels = image.load()
    for i in range(image.size[0]): # for every pixel:
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            if r > 200 and g > 200 and b > 200:
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
    return image


def interpret_card(image, _image, x, y):
    _image = _image.resize((_image.size[0]*10, _image.size[1]*10), Image.ANTIALIAS)
    _image = convert_to_monochrome(_image)
    config = "--psm 6 -c tessedit_char_whitelist=JQKA0123456789"
    try:
        rank_string = pytesseract.image_to_string(_image, config=config)[0] # expensive
    except IndexError:
        return None
    if rank_string == '1':
        rank_string = 'T'
    try:
        suit_string = RGB_TO_SUIT[image.getpixel((x, y))]
    except (TypeError, KeyError):
        return None
    card_string = rank_string + suit_string
    return card_string


def retrieve_hole_cards(image):
    hole_card_images = [(image.crop((hole_card_location[0], hole_card_location[1], hole_card_location[0] + CARD_DIMENSION[0], hole_card_location[1] + CARD_DIMENSION[1]))) for hole_card_location in HOLE_CARDS_LOCATIONS]
    hole_cards = []
    for index, _image in enumerate(hole_card_images):
        suit_x, suit_y = HOLE_CARD_SUIT_LOCATIONS[index]
        card_string = interpret_card(image, _image, suit_x, suit_y)
        if not card_string:
            return None
        hole_cards.append(card_string)
    return [Card.new(c) for c in hole_cards]


def count_community_cards(image):
    # todo: broken, will see 4 as 5
    # but we don't care at the moment since we only care about preflop
    n = 0
    for index in range(5):
        x, y = COMMUNITY_CARDS_LOCATION
        x += 20 * index
        if image.getpixel((x, y)) != CARD_RGB:
            break
        n += 1
    return n


def capture_screen(hwnd, w, h):
    # https://stackoverflow.com/questions/19695214/python-screenshot-of-inactive-window-printwindow-win32gui
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        return im
    return None


class PokerWatcher:
    def __init__(self, hwnd, x, y, w, h):
        self.hc = HumanClicker()
        self.hwnd = hwnd
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.range = hand_pick_range()


    def start(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.async_start())
        loop.run_forever()


    async def move_and_click(self, x, y):
        self.hc.move((x+self.x+randint(0, 3), y+self.y+randint(0, 3)), 2)
        self.hc.click()
        await asyncio.sleep(2)


    async def async_start(self):
        while True:
            await asyncio.sleep(0.2)
            screen_image = capture_screen(self.hwnd, self.w, self.h)

            if count_community_cards(screen_image) > 0:
                print('count_community_cards continue')
                continue

            action_index = find_action_index(screen_image)
            if action_index != 0:
                print('wait for player action')
                continue

            hole_cards = retrieve_hole_cards(screen_image)
            if not hole_cards:
                print("Failed to retrieve hole cards")
                continue


            (a, b) = hole_cards
            if (a, b) in self.range or (b, a) in self.range:
                mixer.music.play()
            else:
                x, y = FOLD_BUTTON_LOCATION
                r, g, b = screen_image.getpixel((x-3, y-3))
                if b > 150:
                    await self.move_and_click(x, y)
                else:
                    mixer.music.play()
                    x, y = CALL_BUTTON_LOCATION
                    await self.move_and_click(x, y)


def ypp_window_callback(hwnd, _extras):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    window_title = win32gui.GetWindowText(hwnd)
    if 'Puzzle Pirates - ' in window_title:
        print('Window found! location=(%d, %d), size=(%d, %d)' % (x, y, w, h))
        pw = PokerWatcher(hwnd, x, y, w, h)
        pw.start()


if __name__ == "__main__":
    win32gui.EnumWindows(ypp_window_callback, None)
