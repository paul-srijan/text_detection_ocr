import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

image_path = r'D:/OPEN CV projects/text-detection-python-easyocr/data/test2.png'
img = cv2.imread(image_path)

if img is None:
    print("❌ Failed to load image. Check path or file name.")
    exit()

reader = easyocr.Reader(['en'], gpu=False)

text_ = reader.readtext(img)

threshold = 0.25

for t_ in text_:
    bbox, text, score = t_

    if score > threshold:
        cv2.rectangle(img, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 2)
        cv2.putText(img, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
