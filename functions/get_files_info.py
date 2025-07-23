import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = ''

    try:
        bootdev_llm_dir = os.path.join(working_directory, directory)
        abs_bootdev_llm_dir = os.path.abspath(bootdev_llm_dir)

        if not abs_bootdev_llm_dir.startswith(os.path.abspath(working_directory)):
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_bootdev_llm_dir):
            print(f'Error: "{directory}" is not a directory')
            return f'Error: "{directory}" is not a directory'
        
        file_info_list = []
        for file in os.listdir(abs_bootdev_llm_dir):
            file_size = os.path.getsize(os.path.join(abs_bootdev_llm_dir, file))
            is_dir = os.path.isdir(os.path.join(abs_bootdev_llm_dir, file))
            print(f'- {file}: file_size:{file_size} bytes, is_dir={is_dir}')
            file_info_list.append(f'- {file}: file_size:{file_size} bytes, is_dir={is_dir}')
        
        return '\n'.join(file_info_list)
    
    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

