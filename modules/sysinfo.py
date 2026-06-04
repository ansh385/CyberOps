import platform
import socket
import psutil


def show_sysinfo():

    print("\n========== SYSTEM INFO ==========\n")

    print("Hostname      :", socket.gethostname())
    print("Operating Sys :", platform.system())
    print("Release       :", platform.release())
    print("Machine       :", platform.machine())
    print("Processor     :", platform.processor())

    print(
        "CPU Usage     :",
        psutil.cpu_percent(interval=1),
        "%"
    )

    print(
        "RAM Usage     :",
        psutil.virtual_memory().percent,
        "%"
    )

    print("\n=================================\n")