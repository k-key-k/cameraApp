import cv2
from tkinter import messagebox
import os
from camera.utils import get_timestamped_filename, select_folder


def take_snapshot(device_index):
    save_dir = select_folder()
    if not save_dir:
        messagebox.showwarning("Внимание", "Папка не выбрана. Поток не будет сохранён.")
        return

    os.makedirs(save_dir, exist_ok=True)
    cap = cv2.VideoCapture(device_index)
    ret, frame = cap.read()
    if ret:
        filename = get_timestamped_filename()
        save_path = os.path.join(save_dir, filename)
        cv2.imwrite(save_path, frame)
        messagebox.showinfo("Успех", f"Снимок сохранен:\n{save_path}")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить изображение.")
    cap.release()
