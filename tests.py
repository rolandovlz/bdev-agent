from functions.run_python_file import run_python_file 

res = run_python_file("calculator", "main.py")
print(res)
res = run_python_file("calculator", "main.py", ["3 + 5"])
print(res)
res = run_python_file("calculator", "tests.py")
print(res)
res = run_python_file("calculator", "../main.py")
print(res)
res = run_python_file("calculator", "nonexistent.py")
print(res)