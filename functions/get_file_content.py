import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):

    try:
        file_path = file_path or ""
        bootdev_llm_file = os.path.join(working_directory, file_path)
        abs_bootdev_llm_file = os.path.abspath(bootdev_llm_file)

        if not abs_bootdev_llm_file.startswith(os.path.abspath(working_directory)):
            print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_bootdev_llm_file):
            print(f'abs_bootdev_llm_file: {abs_bootdev_llm_file}')
            print(f'working_directory: {os.path.abspath(working_directory)}')
            print(f'Error: File not found or is not a regular file: "{file_path}"')
            return f'Error: File not found or is not a regular file: "{file_path}"'
        

        with open(abs_bootdev_llm_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        return file_content_string + f' [...File "{file_path}" truncated at 10000 characters]'
        

    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to get the content of, relative to the working directory. The function will search recursively through all subdirectories to find it.",
            ),
        },
    ),
)

