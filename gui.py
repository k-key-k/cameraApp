import tkinter as tk
from tkinter import ttk, messagebox
from camera.utils import list_cameras
from camera.snapshot import take_snapshot
from camera.stream import start_stream


def run_gui():
    root = tk.Tk()
    root.title("Захват изображения")
    root.resizable(False, False)

    camera_var = tk.StringVar()
    action_var = tk.StringVar(value="Снимок")

    tk.Label(root, text="Выберите устройство:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    camera_menu = ttk.Combobox(root, textvariable=camera_var, state="readonly")
    camera_menu['values'] = list_cameras()
    camera_menu.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Действие:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    ttk.Combobox(root, textvariable=action_var, values=["Снимок", "Стрим"]).grid(row=1, column=1, padx=5, pady=5)

    def run_action():
        try:
            index = int(camera_var.get())
            if action_var.get() == "Снимок":
                take_snapshot(index)
            else:
                start_stream(index)
        except ValueError:
            messagebox.showwarning("Внимание", "Выберите корректное устройство.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    tk.Button(root, text="Выполнить", command=run_action).grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()