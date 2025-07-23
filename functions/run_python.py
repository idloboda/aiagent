import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path):
    try:
        bootdev_llm_file = os.path.join(working_directory, file_path)
        abs_bootdev_llm_file = os.path.abspath(bootdev_llm_file)

        if not abs_bootdev_llm_file.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_bootdev_llm_file):
            return f'Error: File "{file_path}" not found.'
        
        if not abs_bootdev_llm_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        result = subprocess.run(['python', abs_bootdev_llm_file], timeout=30, capture_output=True)

        stdout = f'STDOUT:{result.stdout}'
        stderr = f'STDERR:{result.stderr}'
        returncode = result.returncode

        if result.returncode != 0:
            return f'Process exited with code {returncode}'
        elif not stdout:
            return "No output produced."
        else:   
            return f'{stdout}\n{stderr}'
    


    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory.",
            ),
        },
    ),
)



