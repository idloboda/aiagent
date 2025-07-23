from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

# print("Result for current directory:")
# get_files_info("calculator", ".")

# print("\nResult for 'pkg' directory:")
# get_files_info("calculator", "pkg")

# print("\nResult for '/bin' directory:")
# get_files_info("calculator", "/bin")

# print("\nResult for '../' directory:")
# get_files_info("calculator", "../")

# print("\nResult for lorem ipsum:")
# print(get_file_content("calculator", "lorem.txt"))
# print(len(get_file_content("calculator", "lorem.txt")))

# print("\nResult for main.py:")
# print(get_file_content("calculator", "main.py"))

# print("\nResult for pkg/calculator.py:")
# print(get_file_content("calculator", "pkg/calculator.py"))

# print("\nResult for /bin/cat:")
# print(get_file_content("calculator", "/bin/cat"))
    
# print(1)
# print( write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(2)
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(3)
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(1)
print(run_python_file("calculator", "main.py"))
print(2)
print(run_python_file("calculator", "tests.py"))
print(3)
print(run_python_file("calculator", "../main.py"))
print(4)
print(run_python_file("calculator", "nonexistent.py"))
