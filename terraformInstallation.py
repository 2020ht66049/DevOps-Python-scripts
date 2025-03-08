#!/usr/bin/env python3

import subprocess
import sys

def run_command(command):
    """Executes a shell command and prints output in real-time."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    for line in process.stdout:
        print(line, end="")

    process.wait()

    if process.returncode != 0:
        print(f"Error executing command: {command}", file=sys.stderr)
        for line in process.stderr:
            print(line, end="", file=sys.stderr)
        sys.exit(1)

def install_terraform():
    """Installs Terraform on a Linux system."""
    print("Downloading and adding HashiCorp GPG key...")
    run_command("wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg")
    
    print("Adding Terraform repository...")
    run_command("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main\" | sudo tee /etc/apt/sources.list.d/hashicorp.list")
    
    print("Updating package lists and installing Terraform...")
    run_command("sudo apt update && sudo apt install -y terraform")
    
    print("Terraform installation completed successfully.")

if __name__ == "__main__":
    install_terraform()

Code Explaination:
==================
**Understanding the Python Script for Installing Terraform**

### Overview
This Python script is designed to automate the installation of Terraform on a Linux-based system. It uses shell commands to download the necessary files, add a repository, and install Terraform. The script also includes error handling to ensure successful execution.

---

### 1. Shebang Line
```python
#!/usr/bin/env python3
```
- This line tells the operating system to execute the script using Python 3.
- The `env` command ensures that the correct Python 3 interpreter is used, regardless of its installation path.

---

### 2. Importing Required Modules
```python
import subprocess
import sys
```
- `subprocess`: Allows the execution of shell commands from within Python.
- `sys`: Provides system-related functions, including exiting the script upon errors.

---

### 3. Function: `run_command(command)`
```python
def run_command(command):
    """Executes a shell command and prints output in real-time."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    for line in process.stdout:
        print(line, end="")

    process.wait()

    if process.returncode != 0:
        print(f"Error executing command: {command}", file=sys.stderr)
        for line in process.stderr:
            print(line, end="", file=sys.stderr)
        sys.exit(1)
```
#### Explanation:
- Uses `subprocess.Popen()` to execute shell commands.
- Captures both `stdout` (standard output) and `stderr` (standard error).
- Prints command output line by line.
- Waits for the command to complete using `process.wait()`.
- If the command fails (`returncode != 0`), it prints the error message and exits the script using `sys.exit(1)`.

---

### 4. Function: `install_terraform()`
```python
def install_terraform():
    """Installs Terraform on a Linux system."""
    print("Downloading and adding HashiCorp GPG key...")
    run_command("wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg")
    
    print("Adding Terraform repository...")
    run_command("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main\" | sudo tee /etc/apt/sources.list.d/hashicorp.list")
    
    print("Updating package lists and installing Terraform...")
    run_command("sudo apt update && sudo apt install -y terraform")
    
    print("Terraform installation completed successfully.")
```
#### Explanation:
1. **Download HashiCorp GPG Key**
   - `wget` downloads the HashiCorp GPG key.
   - The key is converted to a compatible format using `gpg --dearmor`.
   - It is stored in `/usr/share/keyrings/`.

2. **Add Terraform Repository**
   - Uses `dpkg --print-architecture` to get system architecture.
   - Uses `lsb_release -cs` to get the OS release name.
   - Adds the Terraform repository to `/etc/apt/sources.list.d/`.

3. **Update and Install Terraform**
   - Runs `sudo apt update` to refresh package lists.
   - Installs Terraform using `sudo apt install -y terraform`.

---

### 5. Script Execution
```python
if __name__ == "__main__":
    install_terraform()
```
- Ensures that `install_terraform()` only runs when the script is executed directly.
- If the script is imported as a module, it won’t execute automatically.

---

### **Summary**
- This script **automates Terraform installation** on a Debian-based Linux system.
- It ensures proper **error handling** using `run_command()`.
- The script follows best practices, including **using GPG keys for package verification**.

By running this script, a user can quickly and efficiently install Terraform without manual intervention.

To execute the script:
```bash
python3 script_name.py
```

