import os
from google.genai import types

def write_file(working_directory, file_path, content):

    try:
        bootdev_llm_dir = os.path.join(working_directory, file_path)
        abs_bootdev_llm_dir = os.path.abspath(bootdev_llm_dir)

        if not abs_bootdev_llm_dir.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        parent_dir = os.path.dirname(abs_bootdev_llm_dir)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with open(abs_bootdev_llm_dir, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)