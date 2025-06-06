import platform
import subprocess

def get_windows_uptime():
    try:
        result = subprocess.run(
            ["net", "stats", "srv"],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.splitlines():
            if "Statistics since" in line:
                return line.strip()
        return "Could not determine uptime on Windows."
    except Exception as e:
        return f"Error determining uptime on Windows: {e}"

def get_linux_uptime():
    try:
        with open("/proc/uptime", "r") as f:
            seconds = float(f.readline().split()[0])
            mins, secs = divmod(int(seconds), 60)
            hours, mins = divmod(mins, 60)
            days, hours = divmod(hours, 24)
            return f"System Uptime: {days}d {hours}h {mins}m {secs}s"
    except Exception as e:
        return f"Error determining uptime on Linux: {e}"

def get_macos_uptime():
    try:
        result = subprocess.run(
            ["uptime"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error determining uptime on macOS: {e}"

def print_system_uptime():
    system = platform.system()
    if system == "Windows":
        uptime = get_windows_uptime()
    elif system == "Linux":

