import jsbeautifier
import clipboard
import pyautogui

target = clipboard.paste()

opts = jsbeautifier.default_options()
opts.type = "html"

res = jsbeautifier.beautify(target, opts)

clipboard.copy(res)