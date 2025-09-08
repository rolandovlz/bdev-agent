from functions.get_file_content import get_file_content

res = get_file_content("calculator", "main.py")
print(res)
res = get_file_content("calculator", "pkg/calculator.py")
print(res)
res = get_file_content("calculator", "/bin/cat")
print(res)
res = get_file_content("calculator", "pkg/does_not_exist.py")
print(res)