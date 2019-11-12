from PIL import Image
import urllib.request
import io
import ocr_on_text

URL = "https://pbs.twimg.com/media/EH1rvtEWkAA4GD3.jpg:large"

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

text = ocr_on_text.get_text(f)
print(text)