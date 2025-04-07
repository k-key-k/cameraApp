import cv2
import os
from tkinter import messagebox
from camera.utils import get_timestamped_filename, select_folder


def start_stream(device_index):
    save_dir = select_folder()
    if not save_dir:
        messagebox.showwarning("Внимание", "Папка не выбрана. Поток не будет сохранён.")
        return

    os.makedirs(save_dir, exist_ok=True)
    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        messagebox.showerror("Ошибка", "Не удалось открыть устройство.")
        return

    last_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        last_frame = frame
        cv2.imshow("Stream (press 'q' to close window)", frame)
        if (cv2.waitKey(1) & 0xFF in (ord('q'), ord('й'))):
            break

    cap.release()
    cv2.destroyAllWindows()
    if last_frame is not None:
        filename = get_timestamped_filename()
        save_path = os.path.join(save_dir, filename)
        cv2.imwrite(save_path, last_frame)
        messagebox.showinfo("Готово", f"Последний кадр сохранен:\n{save_path}")
