import subprocess

result = subprocess.run(["python", "main.py", "3 + 7 * 2"], capture_output=True, text=True)
print(result.stdout)