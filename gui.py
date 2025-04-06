import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from camera.utils import list_cameras, browse_path
from camera.snapshot import take_snapshot
from camera.stream import start_stream


def run_gui():
    root = tk.Tk()
    root.title("Захват изображения")

    camera_var = tk.StringVar()
    action_var = tk.StringVar(value="Снимок")

    tk.Label(root, text="Выберите устройство:").grid(row=0, column=0, sticky="w")
    camera_menu = ttk.Combobox(root, textvariable=camera_var, state="readonly")
    camera_menu['values'] = list_cameras()
    camera_menu.grid(row=0, column=1)

    tk.Label(root, text="Действие:").grid(row=1, column=0, sticky="w")
    ttk.Combobox(root, textvariable=action_var, values=["Снимок", "Стрим"]).grid(row=1, column=1)

    tk.Label(root, text="Путь сохранения:").grid(row=2, column=0, sticky="w")
    path_entry = tk.Entry(root, width=30)
    path_entry.grid(row=2, column=1)
    tk.Button(root, text="Обзор...", command=lambda: browse_path(path_entry)).grid(row=2, column=2)

    def run_action():
        try:
            index = int(camera_var.get())
            path = path_entry.get()
            if not path:
                messagebox.showwarning("Внимание", "Укажите путь для сохранения.")
                return
            if action_var.get() == "Снимок":
                take_snapshot(index, path)
            else:
                start_stream(index, path)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    tk.Button(root, text="Выполнить", command=run_action).grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()
