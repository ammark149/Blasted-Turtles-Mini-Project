import os
import time
import subprocess
from dotenv import load_dotenv

load_dotenv()

def run_remote_ssh(command):
    """Executes a command on the remote server using native system SSH."""
    host = os.getenv("REMOTE_HOST")
    user = os.getenv("REMOTE_USER")
    
    # No passwords needed! SSH will automatically use your local ~/.ssh/ keys
    ssh_cmd = ["ssh", f"{user}@{host}", command]
    
    result = subprocess.run(ssh_cmd, capture_output=True, text=True)
    
    return result.returncode, result.stdout, result.stderr

def refresh_docker_env():
    print("--- Remote Docker Management ---")
    project_dir = "/home/centos/mini_project"
    
    commands = [
        # 1. Forcefully stop and remove ALL containers on the server
        "sudo docker ps -aq | xargs -r sudo docker rm -f",
        
        # 2. Navigate to the directory and start the stack fresh
        f"cd {project_dir} && sudo docker compose up -d"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        status, out, err = run_remote_ssh(cmd)
        
        if status != 0:
            print(f"Error executing '{cmd}':\n{err}")
            return False
            
    print("Docker stack is up. Waiting 10s for Postgres...")
    time.sleep(10)
    return True

if __name__ == "__main__":
    refresh_docker_env()