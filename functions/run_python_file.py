import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_wd = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"): 
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = [sys.executable, target_file]
        if args:
            commands.extend(args)
        completed_process = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_wd
        )
        output = []
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")

        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")

        return "\n".join(output) if output else "No output produced." 
    except Exception as e:
        return f"Error: executing Python file: {e}"