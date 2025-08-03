# 📝 Text Detection from Images using EasyOCR and OpenCV

This project uses [EasyOCR](https://github.com/JaidedAI/EasyOCR) to detect and extract text from images, and uses OpenCV for visualization by drawing bounding boxes around detected text areas.

---

## ✅ Features

* Read and detect English text from images.
* Draw bounding boxes around detected text.
* Filter results using a confidence score threshold.
* Visualize results using `matplotlib`.

---

## 🖼️ Example Output

| Input Image                | Output with Detected Text                   |
| -------------------------- | ------------------------------------------- |
| ![Input](./data/test2.png) | ![Output](./output/result.png) *(If saved)* |


---

## 📂 Directory Structure

```
text-detection-easyocr/
│
├── data/
│   └── test2.png               # Input image
├── text_detection.py           # Main script
├── README.md                   # This file
└── requirements.txt            # Dependencies
```

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/text-detection-easyocr.git
cd text-detection-easyocr
```

2. **Create Virtual Environment (Optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install easyocr opencv-python matplotlib numpy
```

---

## ▶️ Usage

Place your image in the `data/` folder, then run:

```bash
python text_detection.py
```

The detected text will be printed and visualized in a pop-up window.

---

## 🧠 How It Works

* Loads an image using OpenCV.
* Uses `EasyOCR.Reader` to detect text in the image.
* Draws bounding boxes for texts with confidence > `0.25`.
* Displays the image using `matplotlib`.

---

## 📌 Parameters

* **Language**: English (`'en'`)
* **GPU**: Set to `False` (can be set to `True` if supported).
* **Threshold**: Default is `0.25`. Adjust for filtering low-confidence detections.

---

## 📦 `requirements.txt`

```txt
easyocr
opencv-python
matplotlib
numpy
```

---

## 🔧 Future Improvements

* Save output images with bounding boxes.
* Add CLI arguments for dynamic image input and threshold.
* Batch processing for multiple images.
* Export detected text to `.txt` or `.csv`.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

