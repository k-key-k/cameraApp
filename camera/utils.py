import cv2
from tkinter import filedialog


def list_cameras(max_devices=5):
    available = []
    for i in range(max_devices):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available.append(i)
            cap.release()
    return available


def browse_path(entry_widget):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg")],
        title="Выберите путь сохранения"
    )
    if file_path:
        entry_widget.delete(0, "end")
        entry_widget.insert(0, file_path)
