runpy3 () {
/usr/local/bin/python3 << 'EOF' - "$@"

import sys
from bs4 import BeautifulSoup
import re
import clipboard
import pyautogui

for f in sys.argv:
	target = clipboard.paste()

	soup = BeautifulSoup(''.join(target))

	clipboard.copy(soup.prettify())

	pyautogui.keyDown('command')
	pyautogui.press('v')
	pyautogui.keyUp('command')
EOF
}

runpy3 "$@"