import subprocess

cmd = subprocess.run(["ls","-l"], capture_output=True, text=True)

print(cmd)
