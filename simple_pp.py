import win32ui
import pytesseract
import asyncio
from pygame import mixer  # Load the popular external library
from random import randint
from pyclick import HumanClicker

from treys import Card
from snowie import FACING_RAISE, OPEN_POSITION
from PIL import Image, ImageFilter
from ctypes import windll
from win32 import win32gui
mixer.init()
mixer.music.load('C:/Users/Monka/poker/majorkeyalert.mp3')

FOLD_BUTTON_LOCATION = (305, 556)
CALL_BUTTON_LOCATION = (362, 559)
FOLD_BUTTON_RGB = (91, 147, 191)
NINE_PLAYER_LOCAL_LOCATION = ()
STAKE_LOCATION_RGB = (0, 255, 0)
STAKE_DIMENSION = (50, 30)
STAKE_LOCATIONS = [
    (207, 405),
    (120, 351),
    (110, 222),
    (188, 146),
    (275, 200),
    (285, 329),
]

ACTIVE_CHIP_RGB = (43, 43, 24)
ACTIVE_CHIP_LOCATIONS = [
    (248, 515),
    (109, 415),
    (104, 215),
    (252, 115),
    (396, 214),
    (391, 415),
]
DEALER_BUTTON_RGB = (168, 20, 20)
DEALER_BUTTON_LOCATIONS = [
    (220, 417),
    (142, 341),
    (153, 213),
    (241, 160),
    (318, 235),
    (309, 365),
]
COMMUNITY_CARDS_LOCATION = (160, 278)
HOLE_CARDS_LOCATIONS = [
    (130, 543),
    (150, 543),
]
HOLE_CARD_SUIT_LOCATIONS = [
    (133, 564),
    (153, 564),
]
RGB_TO_SUIT = {
    (3, 3, 3): 's',
    (71, 71, 71): 'c',
    (204, 52, 4): 'h',
    (204, 44, 4): 'd',
}

CARD_DIMENSION = (12, 16)
CARD_RGB = (252, 252, 252)

def pixel_search(image, xy, value, x_wide=0):
    x, y = xy
    for _x in range(x-1-x_wide, x+2+x_wide):
        for _y in range(y-1, y+2):
            if image.getpixel((_x, _y)) == value:
                return _x, _y
        return None


def find_dealer_index(image):
    for index, xy in enumerate(DEALER_BUTTON_LOCATIONS):
        if pixel_search(image, xy, DEALER_BUTTON_RGB):
            return index
    return -1


def find_active_indexes(image):
    active_indexes = set()
    for index, xy in enumerate(ACTIVE_CHIP_LOCATIONS):
        if pixel_search(image, xy, ACTIVE_CHIP_RGB, x_wide=14):
            active_indexes.add(index)
            continue
    for index, xy in enumerate(STAKE_LOCATIONS):
        if image.getpixel(xy) == STAKE_LOCATION_RGB:
            active_indexes.add(index)
    return set(active_indexes)


def find_action_index(image):
    action_indexes = []
    for index, xy in enumerate(ACTIVE_CHIP_LOCATIONS):
        x, y = xy
        r, g, b = image.getpixel((x, y - 7))
        if r > 100 and g < 52:
            action_indexes.append(index)

    assert(len(action_indexes) <= 1)
    if action_indexes:
        return action_indexes[0]
    else:
        return -1


def parse_money_string(money_string):
    money_string = money_string.replace(',', '').replace('K', '000')
    try:
        return int(money_string)
    except ValueError:
        print('failed to parse "%s", assuming ALL-IN (0)' % money_string)
        return 0


def monochrome(image, invert=True):
    pixels = image.load()
    for i in range(image.size[0]): # for every pixel:
        for j in range(image.size[1]):
            r, g, b = pixels[i,j]
            if invert:
                if r > 100 and g > 100 and b > 100:
                    pixels[i, j] = (0, 0, 0)
                else:
                    pixels[i, j] = (255, 255, 255)
            else:
                if r > 200 and g > 200 and b > 200:
                    pixels[i, j] = (255, 255, 255)
                else:
                    pixels[i, j] = (0, 0, 0)
    return image


def retrieve_chip_stacks(image, active_indexes):
    stacks = {}
    for index in active_indexes:
        try:
            x, y = pixel_search(image, ACTIVE_CHIP_LOCATIONS[index], ACTIVE_CHIP_RGB, x_wide=14)
        except TypeError:
            # all in
            stacks[index] = 0
            continue
        _image = image.crop((x - 60, y - 7, x - 5, y + 10))
        _image = _image.resize((_image.size[0]*10, _image.size[1]*10), Image.ANTIALIAS)
        _image = monochrome(_image)
        config = "--psm 6 -c tessedit_char_whitelist=,0123456789K"
        stack_string = pytesseract.image_to_string(_image, config=config) # expensive
        stacks[index] = parse_money_string(stack_string)
    return stacks


def retrieve_stake_sizes(image):
    stakes = {}
    for index, xy in enumerate(STAKE_LOCATIONS):
        if image.getpixel(xy) != STAKE_LOCATION_RGB:
            continue
        x, y = xy
        _image = image.crop((x, y, x + STAKE_DIMENSION[0], y + STAKE_DIMENSION[1]))
        _image = _image.resize((_image.size[0]*10, _image.size[1]*10), Image.ANTIALIAS)
        _image = monochrome(_image)
        config = "--psm 6 -c tessedit_char_whitelist=,0123456789K"
        stake_string = pytesseract.image_to_string(_image, config=config) # expensive
        stakes[index] = parse_money_string(stake_string)
    return stakes


def interpret_card(image, _image, x, y):
    _image = _image.resize((_image.size[0]*10, _image.size[1]*10), Image.ANTIALIAS)
    _image = monochrome(_image, invert=False)
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


def retrieve_community_cards(image):
    community_cards = []
    for index in range(5):
        x, y = COMMUNITY_CARDS_LOCATION
        x += 20 * index
        if image.getpixel((x, y)) != CARD_RGB:
            break
        _image = image.crop((x, y, x + CARD_DIMENSION[0], y + CARD_DIMENSION[1]))
        card_string = interpret_card(image, _image, x + 3, y + 21)
        if not card_string:
            break
        community_cards.append(card_string)
    return community_cards


def count_community_cards(image):
    # todo: broken, will see 4 as 5
    n = 0
    for index in range(5):
        x, y = COMMUNITY_CARDS_LOCATION
        x += 20 * index
        if image.getpixel((x, y)) != CARD_RGB:
            break
        n += 1
    return n


def capture_screen(hwnd, w, h):
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
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
    else:
        return None

class PokerWatcher:
    def __init__(self, hwnd, x, y, w, h, screen_path=None):
        self.hc = HumanClicker()
        self.hwnd = hwnd
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen_path = screen_path
        self.dealer_index = -1
        self.action_index = -1
        self.active_indexes = set()
        self.stacks = {}
        self.stakes = {}
        self.hole_cards = []
        self.community_cards = []
        self.action_history = ''


    def start(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.async_start())
        loop.run_forever()


    async def async_start(self):
        while True:
            await asyncio.sleep(0.2)
            if self.screen_path is None:
                screen_image = capture_screen(self.hwnd, self.w, self.h)
            else:
                screen_image = Image.open("test.png")

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
            if (a, b) in FACING_RAISE[5][4][0] or (b, a) in FACING_RAISE[5][4][0]:
                print('CALL')
                mixer.music.play()
            elif (a, b) in OPEN_POSITION[3][0] or (b, a) in OPEN_POSITION[3][0]:
                print('CALL IF 2000')
                mixer.music.play()
            else:
                x, y = FOLD_BUTTON_LOCATION
                r, g, b = screen_image.getpixel((x-3, y-3))
                if b > 150:
                    self.hc.move((x+self.x+randint(0, 3), y+self.y+randint(0, 3)),2)
                    self.hc.click()
                    await asyncio.sleep(2)
                else:
                    mixer.music.play()
                    x, y = CALL_BUTTON_LOCATION
                    self.hc.move((x+self.x+randint(0, 3), y+self.y+randint(0, 3)),2)
                    self.hc.click()
                    await asyncio.sleep(2)


    async def perform_action(self):
        # load self.action_history to ai and get react_preflop
        pass


    def update(self, new_hand=False):
        if new_hand:
            self.action_history = ''
        if self.screen_path is None:
            screen_image = capture_screen(self.hwnd, self.w, self.h)
            if screen_image:
                screen_image.save("test.png")
        else:
            screen_image = Image.open("test.png")

        dealer_index = find_dealer_index(screen_image)
        if dealer_index == -1:
            print("Failed to find dealer index")
            return False
        self.dealer_index = dealer_index
        print("dealer_index=%s" % self.dealer_index)

        active_indexes = find_active_indexes(screen_image)
        if not active_indexes:
            print("Failed to find active indexes")
            return False
        self.active_indexes = active_indexes
        print("active_indexes=%s" % self.active_indexes)

        action_index = find_action_index(screen_image)
        if action_index == -1:
            print("Failed to find action index")
            return False
        self.action_index = action_index
        print('action_index=%s' % self.action_index)

        self.stacks = retrieve_chip_stacks(screen_image, self.active_indexes)
        print('stacks=%s' % self.stacks)

        self.stakes = retrieve_stake_sizes(screen_image)
        print('stakes=%s' % self.stakes)

        # hole_cards = retrieve_hole_cards(screen_image)
        # if not hole_cards:
        #     print("Failed to retrieve hole cards")
        #     return False
        # self.hole_cards = hole_cards
        # print('hole_cards=%s' % self.hole_cards)

        # self.community_cards = retrieve_community_cards(screen_image)
        # print("community_cards=%s" % self.community_cards)

        return True


def enum_window_callback(hwnd, extra):
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


def normal_mode():
    win32gui.EnumWindows(enum_window_callback, None)


def debug_mode():
    print('debug mode')
    pw = PokerWatcher(None, 0, 0, 806, 629, screen_path="test.png")
    pw.start()

normal_mode()