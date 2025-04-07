import cv2
from datetime import datetime
from tkinter import Tk, filedialog


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


def get_timestamped_filename(extension="jpg"):
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S") + f".{extension}"


def select_folder():
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Выберите папку для сохранения изображений")
    root.destroy()
    return folder
