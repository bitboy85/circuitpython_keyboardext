# circuitpython_keyboardext

This implementation allows to send strings as keyboard input for different layouts.
As Layout ether a python dictionary or a list can be used. See provided layouts as example.

* List: Uses less memory and has latin-1 charset https://en.wikipedia.org/wiki/ISO/IEC_8859-1
* Dictionary: Charset can be self defined (based on UTF-8) uses a bit more memory but depends on how many characters are defined.

Both variants allow to use deadkeys, for eample ^ followed by a to get the â character.

NOTE: Latin-1 has no € symbol



# Requirement
This library needs adafruit_hid installed in the lib folder of your device.
Used on a Pi Pico, it uses about 12kb of ram.

# Installation
Just copy keyboardext.py, en_us.py and the layout you want to your lib/keyboardext folder on your circuitpython device.
If you need extra space on your device you can safely delete the existing keyboard.py and keyboard_layout_us.py

# Example
```python
import usb_hid

from keyboardext.keyboardext import Keyboardext
from adafruit_hid.keycode import Keycode

kbd = Keyboardext(usb_hid.devices)
kbd.set_layout("de_de")
kbd.write("# German: #_:;<>|^!$%&/()=?`zY°ÜÖÄüöäßµ²³")
kbd.send(Keycode.ENTER)
kbd.set_layout("en_us")
kbd.write("# German: #_:;<>|^!$%&/()=?`zY°ÜÖÄüöäßµ²³")
```

# Current Layouts
* en_us   - list
* de_de   - list, dictionary

# Add new layout
Adding a new layout is easy. Just copy an existing layout file like de_de.py, edit the key combinations and use it with 
```python
kbd.setLayout(yourfilename) 
```
# Known issues
The € symbol is not part of the charset above, so by now i can't be used within the write method of the keyboard.
Of course it can be send as single command.
```python
kbd.send(keycode.Keycode.E, keycode.Keycode.RIGHT_ALT)
```
char mapping in the provided keyboard layouts may be incomplete (but easy to fix)

# Tested device
- Raspberry Pi pico; Adafruit CircuitPython 6.2.0-beta.2
