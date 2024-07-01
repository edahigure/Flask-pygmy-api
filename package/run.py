#!/usr/bin/env python3
import os
import sys
import time
import signal
import traceback
import subprocess

PYGMY_API_ARGS = ['gunicorn', '-b 127.0.0.1:9119', '-w 1', 'pygmy.rest.wsgi:app']
process = []

def print_err(proc, timeout=2):
    try:
        print(proc.communicate(timeout=timeout))
    except subprocess.TimeoutExpired:
        pass

try:
    print("Starting API development server at http://127.0.0.1:9119/")
    process.append(subprocess.Popen(PYGMY_API_ARGS, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    print_err(process[-1])

    # Infinite loop to keep the script running
    while True:
        time.sleep(1)  # Sleep to reduce CPU usage
        # Add additional logic if needed, e.g., monitoring subprocess output

except KeyboardInterrupt:
    print("Keyboard interrupt received. Exiting.")
except Exception as e:
    traceback.print_exc()
finally:
    print("Terminating subprocesses...")
    for proc in process:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    print("Cleanup done.")
