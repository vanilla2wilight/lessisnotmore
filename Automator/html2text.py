import html2text
import clipboard

target = clipboard.paste()

clipboard.copy(html2text.html2text(target))