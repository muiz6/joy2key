import hid

from pynput.keyboard import Controller, Key

MY_DEVICE = (0x0810, 0x0001)

kb = Controller()

r5_keys = {
    Key.up,
    Key.down,
    Key.left,
    Key.right,
    "a",
    "s",
    "z",
    "x",
}

r6_keys = {"q", "w", Key.enter, Key.shift_r}

r5_map = {
    15: [],
    0: [Key.up],
    2: [Key.right],
    4: [Key.down],
    6: [Key.left],
    31: ["s"],
    47: ["x"],
    79: ["z"],
    143: ["a"],
    1: [Key.up, Key.right],
    3: [Key.right, Key.down],
    5: [Key.down, Key.left],
    7: [Key.left, Key.up],
    16: ["s", Key.up],
    18: ["s", Key.right],
    20: ["s", Key.down],
    22: ["s", Key.left],
    32: ["x", Key.up],
    34: ["x", Key.right],
    36: ["x", Key.down],
    38: ["x", Key.left],
    63: ["s", "x"],
    64: ["z", Key.up],
    66: ["z", Key.right],
    68: ["z", Key.down],
    70: ["z", Key.left],
    95: ["s", "z"],
    111: ["z", "x"],
    128: ["a", Key.up],
    130: ["a", Key.right],
    132: ["a", Key.down],
    134: ["a", Key.left],
    159: ["a", "s"],
    175: ["a", "x"],
    207: ["a", "z"],
    17: ["s", Key.up, Key.right],
    19: ["s", Key.right, Key.down],
    21: ["s", Key.down, Key.left],
    23: ["s", Key.left, Key.up],
    33: ["x", Key.up, Key.right],
    35: ["x", Key.right, Key.down],
    37: ["x", Key.down, Key.left],
    39: ["x", Key.left, Key.up],
    48: ["s", "x", Key.up],
    50: ["s", "x", Key.right],
    52: ["s", "x", Key.down],
    54: ["s", "x", Key.left],
    65: ["z", Key.up, Key.right],
    67: ["z", Key.right, Key.down],
    69: ["z", Key.down, Key.left],
    71: ["z", Key.left, Key.up],
    80: ["s", "z", Key.up],
    82: ["s", "z", Key.right],
    84: ["s", "z", Key.down],
    86: ["s", "z", Key.left],
    96: ["z", "x", Key.up],
    98: ["z", "x", Key.right],
    100: ["z", "x", Key.down],
    102: ["z", "x", Key.left],
    129: ["a", Key.up, Key.right],
    131: ["a", Key.right, Key.down],
    133: ["a", Key.down, Key.left],
    135: ["a", Key.left, Key.up],
    144: ["a", "s", Key.up],
    146: ["a", "s", Key.right],
    148: ["a", "s", Key.down],
    150: ["a", "s", Key.left],
    160: ["a", "x", Key.up],
    162: ["a", "x", Key.right],
    164: ["a", "x", Key.down],
    166: ["a", "x", Key.left],
    191: ["a", "s", "x"],
    192: ["a", "z", Key.up],
    194: ["a", "z", Key.right],
    196: ["a", "z", Key.down],
    198: ["a", "z", Key.left],
    223: ["a", "s", "z"],
    239: ["a", "z", "x"],
    81: ["s", "x", Key.up, Key.right],
    83: ["s", "x", Key.right, Key.down],
    85: ["s", "x", Key.down, Key.left],
    87: ["s", "x", Key.left, Key.up],
    97: ["z", "x", Key.up, Key.right],
    99: ["z", "x", Key.right, Key.down],
    101: ["z", "x", Key.down, Key.left],
    103: ["z", "x", Key.left, Key.up],
    112: ["s", "z", "x", Key.up],
    114: ["s", "z", "x", Key.right],
    116: ["s", "z", "x", Key.down],
    118: ["s", "z", "x", Key.left],
    145: ["a", "s", Key.up, Key.right],
    147: ["a", "s", Key.right, Key.down],
    149: ["a", "s", Key.down, Key.left],
    151: ["a", "s", Key.left, Key.up],
    176: ["a", "s", "x", Key.up],
    178: ["a", "s", "x", Key.right],
    180: ["a", "s", "x", Key.down],
    182: ["a", "s", "x", Key.right],
    193: ["a", "z", Key.up, Key.right],
    195: ["a", "z", Key.right, Key.down],
    197: ["a", "z", Key.down, Key.left],
    199: ["a", "z", Key.left, Key.up],
    208: ["a", "s", "z", Key.up],
    210: {"a", "s", "z", Key.right},
    212: ["a", "s", "z", Key.down],
    214: ["a", "s", "z", Key.left],
    224: ["a", "z", "x", Key.up],
    226: ["a", "z", "x", Key.right],
    228: ["a", "z", "x", Key.down],
    230: ["a", "z", "x", Key.right],
    255: ["a", "s", "z", "x"],
    113: ["s", "z", "x", Key.up, Key.right],
    115: ["s", "z", "x", Key.right, Key.down],
    117: ["s", "z", "x", Key.down, Key.left],
    119: ["s", "z", "x", Key.left, Key.up],
    177: ["a", "s", "x", Key.up, Key.right],
    179: ["a", "s", "x", Key.right, Key.down],
    181: ["a", "s", "x", Key.down, Key.left],
    183: ["a", "s", "x", Key.left, Key.up],
    209: ["a", "s", "z", Key.up, Key.right],
    211: ["a", "s", "z", Key.right, Key.down],
    213: ["a", "s", "z", Key.down, Key.left],
    215: ["a", "s", "z", Key.left, Key.up],
    225: ["a", "z", "x", Key.up, Key.right],
    227: ["a", "z", "x", Key.right, Key.down],
    229: ["a", "z", "x", Key.down, Key.left],
    231: ["a", "z", "x", Key.left, Key.up],
    240: ["a", "s", "z", "x", Key.up],
    242: ["a", "s", "z", "x", Key.right],
    244: ["a", "s", "z", "x", Key.down],
    246: ["a", "s", "z", "x", Key.left],
    241: ["a", "s", "z", "x", Key.up, Key.right],
    243: ["a", "s", "z", "x", Key.right, Key.down],
    245: ["a", "s", "z", "x", Key.down, Key.left],
    247: ["a", "s", "z", "x", Key.left, Key.up],
}


r6_map = {
    0: [],
    1: ["q"],
    2: ["w"],
    16: [Key.shift_r],
    32: [Key.enter],
    3: ["q", "w"],
    17: ["q", Key.shift_r],
    18: ["w", Key.shift_r],
    33: ["q", Key.enter],
    34: ["w", Key.enter],
    48: [Key.enter, Key.shift_r],
    19: ["q", "w", Key.shift_r],
    35: ["q", "w", Key.enter],
    49: ["q", Key.enter, Key.shift_r],
    50: ["w", Key.enter, Key.shift_r],
    51: ["q", "w", Key.enter, Key.shift_r],
}

r5_pressed = set()
r6_pressed = set()


def main():
    for device in hid.enumerate():
        print(
            f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}"
        )

    gamepad = hid.device()
    gamepad.open(*MY_DEVICE)
    gamepad.set_nonblocking(True)

    while True:
        report = gamepad.read(64)

        if report:
            print(report)
            handle_report_5(r5_map[report[5]])
            handle_report_6(r6_map[report[6]])


def handle_report_5(keys):
    for key in r5_keys:
        if key in keys and key not in r5_pressed:
            kb.press(key)
            r5_pressed.add(key)

        if key not in keys and key in r5_pressed:
            kb.release(key)
            r5_pressed.remove(key)


def handle_report_6(keys):
    for key in r6_keys:
        if key in keys and key not in r6_pressed:
            kb.press(key)
            r6_pressed.add(key)

        if key not in keys and key in r6_pressed:
            kb.release(key)
            r6_pressed.remove(key)


if __name__ == "__main__":
    main()
