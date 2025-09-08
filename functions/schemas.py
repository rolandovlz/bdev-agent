
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
        "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
        "file_path": types.Schema(
            type=types.Type.STRING,
            description="The file path, relative to the working directory.",
        ),
        "content": types.Schema(
            type=types.Type.STRING,
            description="The content to write on the file"
        )
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
        "file_path": types.Schema(
            type=types.Type.STRING,
            description="The file path to the python script, relative to the working directory.",
        ),
        "args": types.Schema(
          type=types.Type.ARRAY,
          items=types.Schema(
            type=types.Type.STRING,
            description="Optional arguments to pass to the python file"
          ),
          description="Optional arguments to pass to the python file"
        )
        
        },
    ),
)