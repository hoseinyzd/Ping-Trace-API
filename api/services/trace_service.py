import subprocess

def trace_host(host: str) -> str:
    try:
        result = subprocess.run(
            ["traceroute", "-m", "10", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.decode("utf-8")
    except Exception as e:
        return f"Error: {e}"
