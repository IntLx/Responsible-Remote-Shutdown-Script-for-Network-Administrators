import os

def shutdown_remote_computer(hostname):
    try:
        os.system(f"shutdown /s /m \\\\{hostname} /t 0 /f")
        print(f"Shutdown command sent to {hostname}")
    except Exception as e:
        print(f"Error shutting down remote computer: {e}")

# Replace "remote-computer-name" with the actual hostname or IP address of the remote computer
remote_computer = "YOUR IP OR HOST NAME HERE"

shutdown_remote_computer(remote_computer)
