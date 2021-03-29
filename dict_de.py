# SPDX-FileCopyrightText: 2020, Bitboy85
#
# SPDX-License-Identifier: MIT

"""
=======================================================
# The index of the array represents the 8-bit ascii code.
# The tupple of each index represents the keys needed to be pressed for this ascii character
# For example: on german layouts @ is written by ALT_R(AltGr) + q
# keycodes of 0x00 are ignored, those represent non-printable chars or characters which cannot be entered by key combination
#
# Deadkeys: For characters which require some keypresses one after another, for example â is written on a german layout by
# pressing ^ followed by a just use a double-tuple as keycode. so â is done with: "â" : ((0x35),(0x04)),

* Author(s): Bitboy85
"""

from adafruit_hid.keycode import Keycode

asciiToKeycode = {
	" " : (0x2c),		                # SPACE
	"!" : (0x1e, Keycode.LEFT_SHIFT),	# !
	'"' : (0x1f, Keycode.LEFT_SHIFT),	# "
	"#" : (0x31),                       # #
	"$" : (0x21, Keycode.LEFT_SHIFT),   # $
	"%" : (0x22, Keycode.LEFT_SHIFT),   # %
	"&" : (0x23, Keycode.LEFT_SHIFT),   # &
	"'" : (0x31, Keycode.LEFT_SHIFT),   # '
	"(" : (0x25, Keycode.LEFT_SHIFT),   # (
	")" : (0x26, Keycode.LEFT_SHIFT),   # )
	"*" : (0x30, Keycode.LEFT_SHIFT),   # *
	"+" : (0x30),                       # +
	"," : (0x36),                       # ,
	"-" : (0x38),                       # -
	"." : (0x37),                       # .
	"/" : (0x24, Keycode.LEFT_SHIFT),   # /
	"0" : (0x27),                       # 0
	"1" : (0x1e),                       # 1
	"2" : (0x1f),                       # 2
	"3" : (0x20),                       # 3
	"4" : (0x21),                       # 4
	"5" : (0x22),                       # 5
	"6" : (0x23),                       # 6
	"7" : (0x24),                       # 7
	"8" : (0x25),                       # 8
	"9" : (0x26),                       # 9
	":" : (0x37, Keycode.LEFT_SHIFT),   # :
	";" : (0x36, Keycode.LEFT_SHIFT),   # ;
	"<" : (0x64),                       # <
	"=" : (0x27, Keycode.LEFT_SHIFT),   # =
	">" : (0x64, Keycode.LEFT_SHIFT),   # >
	"?" : (0x2d, Keycode.LEFT_SHIFT),   # ?
	"@" : (0x14, Keycode.RIGHT_ALT),    # @
	"A" : (0x04, Keycode.LEFT_SHIFT),   # A
	"B" : (0x05, Keycode.LEFT_SHIFT),   # B
	"C" : (0x06, Keycode.LEFT_SHIFT),   # C
	"D" : (0x07, Keycode.LEFT_SHIFT),   # D
	"E" : (0x08, Keycode.LEFT_SHIFT),   # E
	"F" : (0x09, Keycode.LEFT_SHIFT),   # F
	"G" : (0x0a, Keycode.LEFT_SHIFT),   # G
	"H" : (0x0b, Keycode.LEFT_SHIFT),   # H
	"I" : (0x0c, Keycode.LEFT_SHIFT),   # I
	"J" : (0x0d, Keycode.LEFT_SHIFT),   # J
	"K" : (0x0e, Keycode.LEFT_SHIFT),   # K
	"L" : (0x0f, Keycode.LEFT_SHIFT),   # L
	"M" : (0x10, Keycode.LEFT_SHIFT),   # M
	"N" : (0x11, Keycode.LEFT_SHIFT),   # N
	"O" : (0x12, Keycode.LEFT_SHIFT),   # O
	"P" : (0x13, Keycode.LEFT_SHIFT),   # P
	"Q" : (0x14, Keycode.LEFT_SHIFT),   # Q
	"R" : (0x15, Keycode.LEFT_SHIFT),   # R
	"S" : (0x16, Keycode.LEFT_SHIFT),   # S
	"T" : (0x17, Keycode.LEFT_SHIFT),   # T
	"U" : (0x18, Keycode.LEFT_SHIFT),   # U
	"V" : (0x19, Keycode.LEFT_SHIFT),   # V
	"w" : (0x1a, Keycode.LEFT_SHIFT),   # W
	"X" : (0x1b, Keycode.LEFT_SHIFT),   # X
	"Y" : (0x1d, Keycode.LEFT_SHIFT),   # Y
	"Z" : (0x1c, Keycode.LEFT_SHIFT),   # Z
	"[" : (0x25, Keycode.RIGHT_ALT),    # [
	"\\" : (0x2d, Keycode.RIGHT_ALT),   # bslash \
	"]" : (0x26, Keycode.RIGHT_ALT),    # ]
	"^" : (0x35),                       # ^
	"_" : (0x38, Keycode.LEFT_SHIFT),   # _
	"`" : (0x2e, Keycode.LEFT_SHIFT),   # `
	"a" : (0x04),                       # a
	"b" : (0x05),                       # b
	"c" : (0x06),                       # c
	"d" : (0x07),                       # d
	"e" : (0x08),                       # e
	"f" : (0x09),                       # f
	"g" : (0x0a),                       # g
	"h" : (0x0b),                       # h
	"i" : (0x0c),                       # i
	"j" : (0x0d),                       # j
	"k" : (0x0e),                       # k
	"l" : (0x0f),                       # l
	"m" : (0x10),                       # m
	"n" : (0x11),                       # n
	"o" : (0x12),                       # o
	"p" : (0x13),                       # p
	"q" : (0x14),                       # q
	"r" : (0x15),                       # r
	"s" : (0x16),                       # s
	"t" : (0x17),                       # t
	"u" : (0x18),                       # u
	"v" : (0x19),                       # v
	"w" : (0x1a),                       # w
	"x" : (0x1b),                       # x
	"y" : (0x1d),                       # y
	"z" : (0x1c),                       # z
	"{" : (0x24, Keycode.RIGHT_ALT),    # {
	"|" : (0x64, Keycode.RIGHT_ALT),    # |
	"}" : (0x27, Keycode.RIGHT_ALT),    # }
	"~" : (0x30, Keycode.RIGHT_ALT),    # ~
	"DEL" : (0x4c),				        # DEL
    "€" : (0x08, Keycode.RIGHT_ALT),    # €
    "§" : (0x20, Keycode.LEFT_SHIFT),   # §
    "©" : (0x06, Keycode.LEFT_SHIFT, Keycode.RIGHT_ALT), # ©
    "°" : (0x35, Keycode.LEFT_SHIFT),   # °
    "²" : (0x1f, Keycode.RIGHT_ALT),    # ²
    "³" : (0x20, Keycode.RIGHT_ALT),    # ³
    "´" : (0x2e),                       # ´
    "µ" : (0x10, Keycode.RIGHT_ALT),    # µ
    "Ä" : (0x34, Keycode.LEFT_SHIFT),   # Ä
    "Ö" : (0x33, Keycode.LEFT_SHIFT),   # Ö
    "Ü" : (0x2f, Keycode.LEFT_SHIFT),   # Ü
    "ß" : (0x2d),                       # ß
    "ä" : (0x34),                       # ä
    "ö" : (0x33),                       # ö
    "ü" : (0x2f),                       # ü
    "â" : ((0x35),(0x04)),
}

"""
	"BS"  : (0x2a),             # BS	Backspace
	"TAB" : (0x2b),             # TAB	Tab
	"LF"  : (0x28),             # LF	Enter
	"CR"  : (0x00),             # CR

    (0x00), # ý
    (0x00), # þ
    (0x00)  # ÿ
    (0x00), # ÷
    (0x00), # ø
    (0x00), # ù
    (0x00), # ú
    (0x00), # û
    (0x00), # å
    (0x00), # æ
    (0x00), # ç
    (0x00), # è
    (0x00), # é
    (0x00), # ê
    (0x00), # ë
    (0x00), # ì
    (0x00), # í
    (0x00), # î
    (0x00), # ï
    (0x00), # ð
    (0x00), # ñ
    (0x00), # ò
    (0x00), # ó
    (0x00), # ô
    (0x00), # õ
    (0x00), # à
    (0x00), # á
    (0x00), # â
    (0x00), # ã
    (0x00), # Ý
    (0x00), # Þ
    (0x00), # ×
    (0x00), # Ø
    (0x00), # Ù
    (0x00), # Ú
    (0x00), # Û
    (0x00), # Å
    (0x00), # Æ
    (0x00), # Ç
    (0x00), # È
    (0x00), # É
    (0x00), # Ê
    (0x00), # Ë
    (0x00), # Ì
    (0x00), # Í
    (0x00), # Î
    (0x00), # Ï
    (0x00), # Ð
    (0x00), # Ñ
    (0x00), # Ò
    (0x00), # Ó
    (0x00), # Ô
    (0x00), # Õ
    (0x00), # ¶
    (0x00), # ·
    (0x00), # ¸
    (0x00), # ¹
    (0x00), # º
    (0x00), # »
    (0x00), # ¼
    (0x00), # ½
    (0x00), # ¾
    (0x00), # ¿
    (0x00), # À
    (0x00), # Á
    (0x00), # Â
    (0x00), # Ã
    (0x00), # ±
    (0x00), # ª
    (0x00), # «
    (0x00), # ¬
    (0x00), # ®
    (0x00), # ¯
    (0x00), # ¨
    (0x00), # ‚
    (0x00), # ƒ
    (0x00), # „
    (0x00), # …
    (0x00), # †
    (0x00), # ‡
    (0x00), # ˆ
    (0x00), # ‰
    (0x00), # Š
    (0x00), # ‹
    (0x00), # Œ
    (0x00), # 
    (0x00), # Ž
    (0x00), # ‘
    (0x00), # ’
    (0x00), # “
    (0x00), # ”
    (0x00), # •
    (0x00), # –
    (0x00), # —
    (0x00), # ˜
    (0x00), # ™
    (0x00), # š
    (0x00), # ›
    (0x00), # œ
    (0x00), # ž
    (0x00), # Ÿ
    (0x00), # ¡
    (0x00), # ¢
    (0x00), # £
    (0x00), # ¤
    (0x00), # ¥
    (0x00), # ¦
"""
