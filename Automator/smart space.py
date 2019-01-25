runpy3 () {
/anaconda3/bin/python << 'EOF' - "$@"

import sys
import pangu
import clipboard
import pyautogui

for f in sys.argv:

	target = clipboard.paste()
	result = pangu.spacing_text(target)
	clipboard.copy(result)

	pyautogui.keyDown('command')
	pyautogui.press('v')
	pyautogui.keyUp('command')

EOF
}

runpy3 "$@"
