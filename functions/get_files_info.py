import os

def get_files_info(working_directory, directory="."):
    abs_wd = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(os.path.join(working_directory, directory))

    if not target_abs_path.startswith(abs_wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_abs_path):
        return f'Error: "{directory}" is not a directory'

    try:
        lines = []
        dir_list = os.listdir(target_abs_path)
        for doc in dir_list:
            filepath = target_abs_path + "/" + doc
            file_size = os.path.getsize(filepath)
            is_file = os.path.isfile(filepath)
            lines.append(f"- {doc}: file_size={file_size} bytes is_dir={not is_file}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing files: {e}"


