import subprocess

def get_docker_version():
    try:
        # Run the "docker --version" command
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True, check=True)

        # Get the version information from the command output
        docker_version = result.stdout.strip()

        # Print the Docker version
        print("Docker Version:", docker_version)

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur when running the command
        print(f"Error: {e}")

if __name__ == "__main__":
    get_docker_version()

Explaination:
**Understanding the Python Script to Get Docker Version**

### **Overview**
This Python script retrieves and prints the installed Docker version by running the `docker --version` command using the `subprocess` module.

---

### **1. Importing Required Module**
```python
import subprocess
```
- The `subprocess` module is used to execute shell commands from within the Python script.

---

### **2. Function: `get_docker_version()`**
```python
def get_docker_version():
    try:
        # Run the "docker --version" command
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True, check=True)

        # Get the version information from the command output
        docker_version = result.stdout.strip()

        # Print the Docker version
        print("Docker Version:", docker_version)
    
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur when running the command
        print(f"Error: {e}")
```

#### **Explanation:**
1. **Runs the `docker --version` command** using `subprocess.run()`:
   - `capture_output=True`: Captures the command's output.
   - `text=True`: Ensures the output is returned as a string (instead of bytes).
   - `check=True`: Raises an exception if the command fails.

2. **Extracts and prints the Docker version**:
   - `result.stdout.strip()` removes any leading or trailing whitespace.
   - The version is printed to the console.

3. **Handles errors using `try-except`**:
   - If the `docker --version` command fails (e.g., Docker is not installed), `subprocess.CalledProcessError` is raised.
   - The script catches the error and prints an error message.

---

### **3. Script Execution**
```python
if __name__ == "__main__":
    get_docker_version()
```
- Ensures that `get_docker_version()` runs **only if the script is executed directly**.
- If the script is imported as a module in another Python program, `get_docker_version()` **won’t execute automatically**.

---

### **4. How to Run the Script**
Save the script as `docker_version.py` and execute it using:
```bash
python3 docker_version.py
```

If Docker is installed, you’ll see output like:
```bash
Docker Version: Docker version 20.10.8, build 3967b7d
```

If Docker is **not installed** or if an error occurs, it will print:
```bash
Error: Command '['docker', '--version']' returned non-zero exit status 1.
```

---

### **Summary**
- Uses `subprocess.run()` to execute `docker --version`.
- Captures and prints the **Docker version**.
- Implements **error handling** to manage command failures.
- Runs the function only when the script is executed directly.

This script is useful for quickly checking if Docker is installed and obtaining version details.

