import subprocess

def ping_host(host: str) -> bool:
    try:
        result = subprocess.run(
            ["ping", "-c", "2", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except Exception:
        return False
