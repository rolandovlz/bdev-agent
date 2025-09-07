from functions.get_files_info import get_files_info

res = get_files_info("calculator", ".")
print(res)
res = get_files_info("calculator", "pkg")
print(res)
res = get_files_info("calculator", "/bin")
print(res)
res = get_files_info("calculator", "../")
print(res)