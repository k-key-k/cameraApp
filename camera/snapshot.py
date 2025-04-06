import cv2
from tkinter import messagebox
import os


def take_snapshot(device_index, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cap = cv2.VideoCapture(device_index)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(save_path, frame)
        messagebox.showinfo("Успех", f"Снимок сохранен:\n{save_path}")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить изображение.")
    cap.release()
