# 📸 Camera App — захват изображения с устройства

Простое GUI-приложение на Python, которое позволяет:

✅ выбрать доступную камеру  
✅ сделать снимок или запустить стрим  
✅ сохранить изображение в указанную папку  

---

## 🚀 Быстрый запуск

📦 **Скачать .exe (без установки Python):**

👉 [Скачать .exe](https://github.com/k-key-k/cameraApp/releases/latest)

После загрузки:
- запусти `main.exe`
- выбери камеру и действие

---

## 🧰 Запуск из исходников

1. Установи Python 3.9+  
2. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запусти:
   ```bash
   python main.py
   ```
## 💾 Сохранение
Все изображения сохраняются туда, куда укажет пользователь через диалог.

## 🖼 Превью интерфейса
<img src="screenshots/ui_example1.png" alt="GUI Screenshot" width="500"/>

## 🧱 Структура проекта
```
camera_app/
├── main.py
├── gui.py
├── camera/
│   ├── utils.py
│   ├── snapshot.py
│   ├── stream.py
│   └── __init__.py
├── camera_images/
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠 Сборка `.exe` (если хочешь сам)
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --name app_name main.py
```
Файл появится в `dist/app_name.exe`
