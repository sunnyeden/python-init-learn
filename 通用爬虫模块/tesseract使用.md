#### Tesseract是一个将图像翻译成文字的OCR库[光学文字识别]

#### 安装

```python
pip install pytesseract
```

#### 使用识别验证码[不能太多干扰元素才能成功]

```python
# encoding = utf-8
import pytesseract
from PIL import Image

image = Image.open("./test.png")

print(pytesseract.image_to_sting(image))
```
