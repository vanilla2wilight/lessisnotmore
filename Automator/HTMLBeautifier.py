runpy3 () {
/usr/local/bin/python3 << 'EOF' - "$@"

import sys
from html5print import HTMLBeautifier
import clipboard
import pyautogui
#你的其他模块

for f in sys.argv:
	target = clipboard.paste()

	clipboard.copy(HTMLBeautifier.beautify(target, 4))

	pyautogui.keyDown('command')
	pyautogui.press('v')
	pyautogui.keyUp('command')
EOF
}

runpy3 "$@"