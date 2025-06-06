import os
import platform
import subprocess

def print_system_uptime():
    system = platform.system()
    uptime = ""
    try:
        if system == "Windows":
            # Use 'net stats srv' and parse output
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    uptime = line.strip()
                    break
            else:
                uptime = "Could not determine uptime on Windows."
        elif system == "Linux":
            # Use /proc/uptime
            with open("/proc/uptime", "r") as f:
                seconds = float(f.readline().split()[0])
                mins, secs = divmod(int(seconds), 60)
                hours, mins = divmod(mins, 60)
                days, hours = divmod(hours, 24)
                uptime = f"System Uptime: {days}d {hours}h {mins}m {secs}s"
        elif system == "Darwin":
            # macOS
            output = subprocess.check_output("uptime", shell=True, text=True)
            uptime = output.strip()
        else:
            uptime = "Unsupported OS"
    except Exception as e:
        uptime = f"Error determining uptime: {e}"

    print(uptime)

if __name__ == "__main__":
    print_system_uptime()
