import pangu
import clipboard
import pyautogui
	
target = clipboard.paste()
result = pangu.spacing_text(target)
clipboard.copy(result)

pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
