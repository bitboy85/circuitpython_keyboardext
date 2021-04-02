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
# pressing ^ followed by a just use a python list as keycode. so â is done with: "â" : [(0x35),(0x04)],
#
* Author(s): Bitboy85
"""

R_ALT   = 0xE6
L_SHIFT = 0xE1

asciiToKeycode = [
	(0x00),             # NUL
	(0x00),             # SOH
	(0x00),             # STX
	(0x00),             # ETX
	(0x00),             # EOT
	(0x00),             # ENQ
	(0x00),             # ACK
	(0x00),             # BEL
	(0x2a),             # BS	Backspace
	(0x2b),             # TAB	Tab
	(0x28),             # LF	Enter
	(0x00),             # VT
	(0x00),             # FF
	(0x00),             # CR
	(0x00),             # SO
	(0x00),             # SI
	(0x00),             # DEL
	(0x00),             # DC1
	(0x00),             # DC2
	(0x00),             # DC3
	(0x00),             # DC4
	(0x00),             # NAK
	(0x00),             # SYN
	(0x00),             # ETB
	(0x00),             # CAN
	(0x00),             # EM
	(0x00),             # SUB
	(0x00),             # ESC
	(0x00),             # FS
	(0x00),             # GS
	(0x00),             # RS
	(0x00),             # US

	(0x2c),		        # SPACE
	(0x1e, L_SHIFT),	# !
	(0x1f, L_SHIFT),	# "
	(0x31),             # #
	(0x21, L_SHIFT),    # $
	(0x22, L_SHIFT),    # %
	(0x23, L_SHIFT),    # &
	(0x31, L_SHIFT),    # '
	(0x25, L_SHIFT),    # (
	(0x26, L_SHIFT),    # )
	(0x30, L_SHIFT),    # *
	(0x30),             # +
	(0x36),             # ,
	(0x38),             # -
	(0x37),             # .
	(0x24, L_SHIFT),    # /
	(0x27),             # 0
	(0x1e),             # 1
	(0x1f),             # 2
	(0x20),             # 3
	(0x21),             # 4
	(0x22),             # 5
	(0x23),             # 6
	(0x24),             # 7
	(0x25),             # 8
	(0x26),             # 9
	(0x37, L_SHIFT),    # :
	(0x36, L_SHIFT),    # ;
	(0x64),             # <
	(0x27, L_SHIFT),    # =
	(0x64, L_SHIFT),    # >
	(0x2d, L_SHIFT),    # ?
	(0x14, R_ALT),      # @
	(0x04, L_SHIFT),    # A
	(0x05, L_SHIFT),    # B
	(0x06, L_SHIFT),    # C
	(0x07, L_SHIFT),    # D
	(0x08, L_SHIFT),    # E
	(0x09, L_SHIFT),    # F
	(0x0a, L_SHIFT),    # G
	(0x0b, L_SHIFT),    # H
	(0x0c, L_SHIFT),    # I
	(0x0d, L_SHIFT),    # J
	(0x0e, L_SHIFT),    # K
	(0x0f, L_SHIFT),    # L
	(0x10, L_SHIFT),    # M
	(0x11, L_SHIFT),    # N
	(0x12, L_SHIFT),    # O
	(0x13, L_SHIFT),    # P
	(0x14, L_SHIFT),    # Q
	(0x15, L_SHIFT),    # R
	(0x16, L_SHIFT),    # S
	(0x17, L_SHIFT),    # T
	(0x18, L_SHIFT),    # U
	(0x19, L_SHIFT),    # V
	(0x1a, L_SHIFT),    # W
	(0x1b, L_SHIFT),    # X
	(0x1d, L_SHIFT),    # Y
	(0x1c, L_SHIFT),    # Z
	(0x25, R_ALT),      # [
	(0x2d, R_ALT),      # bslash \
	(0x26, R_ALT),      # ]
	(0x35),             # ^
	(0x38, L_SHIFT),    # _
	(0x2e, L_SHIFT),    # `
	(0x04),             # a
	(0x05),             # b
	(0x06),             # c
	(0x07),             # d
	(0x08),             # e
	(0x09),             # f
	(0x0a),             # g
	(0x0b),             # h
	(0x0c),             # i
	(0x0d),             # j
	(0x0e),             # k
	(0x0f),             # l
	(0x10),             # m
	(0x11),             # n
	(0x12),             # o
	(0x13),             # p
	(0x14),             # q
	(0x15),             # r
	(0x16),             # s
	(0x17),             # t
	(0x18),             # u
	(0x19),             # v
	(0x1a),             # w
	(0x1b),             # x
	(0x1d),             # y
	(0x1c),             # z
	(0x24, R_ALT),      # {
	(0x64, R_ALT),      # |
	(0x27, R_ALT),      # }
	(0x30, R_ALT),      # ~
	(0x4c),				# DEL
    (0x00), # [NOT printable] in some docs shown as € symbol, but not so in python
    (0x00), # [not printable]
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
    (0x00), # [not printable]
    (0x00), # [not printable]
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
    (0x00), # [not printable]
    (0x00), # ž
    (0x00), # Ÿ
    (0x00), # [not printable]
    (0x00), # ¡
    (0x00), # ¢
    (0x00), # £
    (0x00), # ¤
    (0x00), # ¥
    (0x00), # ¦
    (0x20, L_SHIFT),    # §
    (0x00), # ¨
    (0x00), # ©
    (0x00), # ª
    (0x00), # «
    (0x00), # ¬
    (0x00), # [not printable]
    (0x00), # ®
    (0x00), # ¯
    (0x35, L_SHIFT),    # °
    (0x00), # ±
    (0x1f, R_ALT),      # ²
    (0x20, R_ALT),      # ³
    (0x2e),             # ´
    (0x10, R_ALT),      # µ
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
    (0x34, L_SHIFT),     # Ä
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
    (0x33, L_SHIFT),    # Ö
    (0x00), # ×
    (0x00), # Ø
    (0x00), # Ù
    (0x00), # Ú
    (0x00), # Û
    (0x2f, L_SHIFT),    # Ü
    (0x00), # Ý
    (0x00), # Þ
    (0x2d),             # ß
    (0x00), # à
    (0x00), # á
    (0x00), # â
    (0x00), # ã
    (0x34),             # ä
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
    (0x33),             # ö
    (0x00), # ÷
    (0x00), # ø
    (0x00), # ù
    (0x00), # ú
    (0x00), # û
    (0x2f),             # ü
    (0x00), # ý
    (0x00), # þ
    (0x00)  # ÿ
] 
