import cv2
import os
from tkinter import messagebox


def start_stream(device_index, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
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
        cv2.imshow("Стрим (нажмите 'q' для выхода)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if last_frame is not None:
        cv2.imwrite(save_path, last_frame)
        messagebox.showinfo("Готово", f"Последний кадр сохранен:\n{save_path}")
