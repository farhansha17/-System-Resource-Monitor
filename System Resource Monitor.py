import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Resource Monitor")
        self.root.geometry("400x400")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.cpu_label = ttk.Label(root, text="CPU Usage:")
        self.cpu_label.pack(pady=5)
        self.cpu_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.cpu_progress.pack()

        self.ram_label = ttk.Label(root, text="RAM Usage:")
        self.ram_label.pack(pady=5)
        self.ram_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.ram_progress.pack()

        self.disk_label = ttk.Label(root, text="Disk Usage:")
        self.disk_label.pack(pady=5)
        self.disk_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.disk_progress.pack()

        self.battery_label = ttk.Label(root, text="Battery: Loading...")
        self.battery_label.pack(pady=5)

        self.temp_label = ttk.Label(root, text="CPU Temperature: N/A")
        self.temp_label.pack(pady=5)

        self.update_thread = threading.Thread(target=self.update_stats)
        self.update_thread.daemon = True
        self.update_thread.start()

    def update_stats(self):
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            battery = psutil.sensors_battery()

            try:
                temps = psutil.sensors_temperatures()
                core_temps = temps.get("coretemp") or temps.get("cpu-thermal") or temps.get("acpitz")
            except AttributeError:
                core_temps = None

            self.cpu_progress["value"] = cpu
            self.cpu_label.config(text=f"CPU Usage: {cpu}%")

            self.ram_progress["value"] = ram
            self.ram_label.config(text=f"RAM Usage: {ram}%")

            self.disk_progress["value"] = disk
            self.disk_label.config(text=f"Disk Usage: {disk}%")

            if battery:
                percent = battery.percent
                plugged = "Plugged In" if battery.power_plugged else "On Battery"
                self.battery_label.config(text=f"Battery: {percent}% ({plugged})")

            if core_temps:
                current_temp = core_temps[0].current
                self.temp_label.config(text=f"CPU Temperature: {current_temp}°C")
            else:
                self.temp_label.config(text="CPU Temperature: N/A")

            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()