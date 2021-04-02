# SPDX-FileCopyrightText: 2021, Bitboy85
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
# pressing ^ followed by a just use a python list as keycode. so â is done with: "â" : [(0x35),(0x04)],

* Author(s): Bitboy85
"""

R_ALT   = 0xE6
L_SHIFT = 0xE1

asciiToKeycode = {                            
	" " : (0x2c),		    # SPACE
	"!" : (0x1e, L_SHIFT),	# !
	'"' : (0x1f, L_SHIFT),	# "
	"#" : (0x31),           # #
	"$" : (0x21, L_SHIFT),  # $
	"%" : (0x22, L_SHIFT),  # %
	"&" : (0x23, L_SHIFT),  # &
	"'" : (0x31, L_SHIFT),  # '
	"(" : (0x25, L_SHIFT),  # (
	")" : (0x26, L_SHIFT),  # )
	"*" : (0x30, L_SHIFT),  # *
	"+" : (0x30),           # +
	"," : (0x36),           # ,
	"-" : (0x38),           # -
	"." : (0x37),           # .
	"/" : (0x24, L_SHIFT),  # /
	"0" : (0x27),           # 0
	"1" : (0x1e),           # 1
	"2" : (0x1f),           # 2
	"3" : (0x20),           # 3
	"4" : (0x21),           # 4
	"5" : (0x22),           # 5
	"6" : (0x23),           # 6
	"7" : (0x24),           # 7
	"8" : (0x25),           # 8
	"9" : (0x26),           # 9
	":" : (0x37, L_SHIFT),  # :
	";" : (0x36, L_SHIFT),  # ;
	"<" : (0x64),           # <
	"=" : (0x27, L_SHIFT),  # =
	">" : (0x64, L_SHIFT),  # >
	"?" : (0x2d, L_SHIFT),  # ?
	"@" : (0x14, R_ALT),    # @
	"A" : (0x04, L_SHIFT),  # A
	"B" : (0x05, L_SHIFT),  # B
	"C" : (0x06, L_SHIFT),  # C
	"D" : (0x07, L_SHIFT),  # D
	"E" : (0x08, L_SHIFT),  # E
	"F" : (0x09, L_SHIFT),  # F
	"G" : (0x0a, L_SHIFT),  # G
	"H" : (0x0b, L_SHIFT),  # H
	"I" : (0x0c, L_SHIFT),  # I
	"J" : (0x0d, L_SHIFT),  # J
	"K" : (0x0e, L_SHIFT),  # K
	"L" : (0x0f, L_SHIFT),  # L
	"M" : (0x10, L_SHIFT),  # M
	"N" : (0x11, L_SHIFT),  # N
	"O" : (0x12, L_SHIFT),  # O
	"P" : (0x13, L_SHIFT),  # P
	"Q" : (0x14, L_SHIFT),  # Q
	"R" : (0x15, L_SHIFT),  # R
	"S" : (0x16, L_SHIFT),  # S
	"T" : (0x17, L_SHIFT),  # T
	"U" : (0x18, L_SHIFT),  # U
	"V" : (0x19, L_SHIFT),  # V
	"W" : (0x1a, L_SHIFT),  # W
	"X" : (0x1b, L_SHIFT),  # X
	"Y" : (0x1d, L_SHIFT),  # Y
	"Z" : (0x1c, L_SHIFT),  # Z
	"[" : (0x25, R_ALT),    # [
	"\\" : (0x2d, R_ALT),   # bslash \
	"]" : (0x26, R_ALT),    # ]
	"^" : (0x35),           # ^
	"_" : (0x38, L_SHIFT),  # _
	"`" : (0x2e, L_SHIFT),  # `
	"a" : (0x04),           # a
	"b" : (0x05),           # b
	"c" : (0x06),           # c
	"d" : (0x07),           # d
	"e" : (0x08),           # e
	"f" : (0x09),           # f
	"g" : (0x0a),           # g
	"h" : (0x0b),           # h
	"i" : (0x0c),           # i
	"j" : (0x0d),           # j
	"k" : (0x0e),           # k
	"l" : (0x0f),           # l
	"m" : (0x10),           # m
	"n" : (0x11),           # n
	"o" : (0x12),           # o
	"p" : (0x13),           # p
	"q" : (0x14),           # q
	"r" : (0x15),           # r
	"s" : (0x16),           # s
	"t" : (0x17),           # t
	"u" : (0x18),           # u
	"v" : (0x19),           # v
	"w" : (0x1a),           # w
	"x" : (0x1b),           # x
	"y" : (0x1d),           # y
	"z" : (0x1c),           # z
	"{" : (0x24, R_ALT),    # {
	"|" : (0x64, R_ALT),    # |
	"}" : (0x27, R_ALT),    # }
	"~" : (0x30, R_ALT),    # ~
    "€" : (0x08, R_ALT),    # €
    "§" : (0x20, L_SHIFT),  # §
    "©" : (0x06, L_SHIFT, R_ALT), # ©
    "°" : (0x35, L_SHIFT),  # °
    "²" : (0x1f, R_ALT),    # ²
    "³" : (0x20, R_ALT),    # ³
    "´" : (0x2e),           # ´
    "µ" : (0x10, R_ALT),    # µ
    "Ä" : (0x34, L_SHIFT),  # Ä
    "Ö" : (0x33, L_SHIFT),  # Ö
    "Ü" : (0x2f, L_SHIFT),  # Ü
    "ß" : (0x2d),           # ß
    "ä" : (0x34),           # ä
    "ö" : (0x33),           # ö
    "ü" : (0x2f),           # ü
    "â" : [(0x35),(0x04)],           # â
    "ê" : [(0x35),(0x08)],           # ê
    "î" : [(0x35),(0x0c)],           # î
    "ô" : [(0x35),(0x12)],           # ô
    "û" : [(0x35),(0x18)],           # û
    "Â" : [(0x35),(0x04, L_SHIFT)],  # Â
    "Ê" : [(0x35),(0x08, L_SHIFT)],  # Ê
    "Î" : [(0x35),(0x0c, L_SHIFT)],  # Î
    "Ô" : [(0x35),(0x12, L_SHIFT)],  # Ô
    "Û" : [(0x35),(0x18, L_SHIFT)],  # Û
    "á" : [(0x2e),(0x04)],           # á
    "é" : [(0x2e),(0x08)],           # é
    "í" : [(0x2e),(0x0c)],           # í
    "ó" : [(0x2e),(0x12)],           # ó
    "ú" : [(0x2e),(0x08)],           # ú
    "Á" : [(0x2e),(0x04, L_SHIFT)],  # Á
    "É" : [(0x2e),(0x08, L_SHIFT)],  # É
    "Í" : [(0x2e),(0x0c, L_SHIFT)],  # Í
    "Ó" : [(0x2e),(0x12, L_SHIFT)],  # Ó
    "Ú" : [(0x2e),(0x08, L_SHIFT)],  # Ú
    "à" : [(0x2e, L_SHIFT),(0x04)],  # à
    "è" : [(0x2e, L_SHIFT),(0x08)],  # è
    "ì" : [(0x2e, L_SHIFT),(0x0c)],  # ì
    "ò" : [(0x2e, L_SHIFT),(0x12)],  # ò
    "ù" : [(0x2e, L_SHIFT),(0x08)],  # ù
    "À" : [(0x2e, L_SHIFT),(0x04, L_SHIFT)],  # À
    "È" : [(0x2e, L_SHIFT),(0x08, L_SHIFT)],  # È
    "Ì" : [(0x2e, L_SHIFT),(0x0c, L_SHIFT)],  # Ì
    "Ò" : [(0x2e, L_SHIFT),(0x12, L_SHIFT)],  # Ò
    "Ù" : [(0x2e, L_SHIFT),(0x08, L_SHIFT)],  # Ù
}

"""
    Characterlist for copy-paste

	"BS"  : (0x2a),         # BS	Backspace
	"TAB" : (0x2b),         # TAB	Tab
	"LF"  : (0x28),         # LF	Enter
	"CR"  : (0x00),         # CR
	"DEL" : (0x4c),			# DEL
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
