# System Resource Monitor

A Python desktop application that monitors CPU, RAM, Disk, Battery, and CPU temperature in real time using a graphical interface built with Tkinter.

## 🔧 Features

- 🧠 CPU usage monitor  
- 🧠 RAM usage monitor  
- 💾 Disk usage monitor  
- 🔋 Battery status and percentage  
- 🌡️ CPU temperature (if supported by OS and hardware)  
- 🪟 Clean and simple GUI using Tkinter

## 📦 Requirements

- Python 3.x  
- `psutil` module

Install required packages:

```bash
pip install psutil
```

## 🚀 How to Run

Clone the repository or copy the script, then run:

```bash
python system_monitor.py
```


## 👤 Author

**Developed by:** Farhan Shahul

## ⚠️ Notes

- CPU temperature monitoring may not be available on all systems.
- The app uses `psutil`'s `sensors_temperatures()` which works on certain Linux/Windows machines with appropriate sensors.

---

⭐ Feel free to fork this project, give it a star, or suggest improvements!
