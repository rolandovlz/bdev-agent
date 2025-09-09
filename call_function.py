from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.schemas import *

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    args = function_call_part.args
    res = None
    match (function_call_part.name):
        case "get_files_info":
            res = get_files_info("./calculator", **args)
        case "get_file_content":
            res = get_file_content("./calculator", **args)
        case "write_file":
            res = write_file("./calculator", **args)
        case "run_python_file":
            res = run_python_file("./calculator", **args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"}
                    )
                ]
            )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": res}
            )
        ]
    )

