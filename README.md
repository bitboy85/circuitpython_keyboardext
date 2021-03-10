# circuitpython_keyboardext
keyboard with layout change

This implementation allows to add and change different keyboard layouts to be used with circuit python.
It supports latin-1 char set https://en.wikipedia.org/wiki/ISO/IEC_8859-1

# Installation
Just copy keyboardext.py, en_us.py and the layout you want to your lib/adafruit_hid folder on your circuitpython device.

# Example
```python
import usb_hid

from adafruit_hid import keyboardext
from adafruit_hid import keycode

kbd = keyboardext.Keyboardext(usb_hid.devices)
kbd.setLayout("de_de")
kbd.write("# German: #_:;<>|^!$%&/()=?`zY°ÜÖÄüöäßµ²³")
kbd.send(0x28)
kbd.setLayout("en_us")
kbd.write("# German: #_:;<>|^!$%&/()=?`zY°ÜÖÄüöäßµ²³")
```

# known issues
The € symbol is not part of the charset above, so by now i can't be used within the write method of the keyboard.
Of course it can be send as single command.
kbd.send(keycode.Keycode.E, keycode.Keycode.RIGHT_ALT)

char mapping in the provided keyboard layouts may be incomplete (but easy to fix)
