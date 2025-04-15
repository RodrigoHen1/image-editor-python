# image-editor-python

This Python script processes images by applying the following effects:
- Smooth filter
- Grayscale conversion
- Brightness enhancement
- Contrast enhancement

The processed images are saved in a separate output directory.

---

## 📂 Folder Structure

. ├── enhance_images.py ├── imgs/ # Input folder: place your original images here └── editedImgs/ # Output folder: processed images will be saved here

yaml
Copiar
Editar

> **Note:** You must create the `imgs/` folder and place your images inside before running the script. The `editedImgs/` folder will be created automatically if it doesn’t exist.

---

## ▶️ How to Run

1. Make sure you have **Python** and **Pillow** installed:

```bash
pip install pillow
Run the script:

bash
Copiar
Editar
python enhance_images.py
Processed images will be saved in the editedImgs/ folder with _edited added to the filename.
