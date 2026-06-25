from colorama import Fore, Style, init
import re

init(autoreset=True)

def analyze_code(file_path):
with open(file_path, "r", encoding="utf-8") as f:
code = f.read()

```
lines = code.splitlines()

total_lines = len(lines)
blank_lines = sum(1 for line in lines if line.strip() == "")
comment_lines = sum(1 for line in lines if line.strip().startswith("#"))
todo_count = code.count("TODO")

function_count = len(re.findall(r"^\s*def\s+", code, re.MULTILINE))
class_count = len(re.findall(r"^\s*class\s+", code, re.MULTILINE))

print(Fore.CYAN + "\n========== AI CODE REVIEW ==========\n")

print(Fore.GREEN + f"Total Lines      : {total_lines}")
print(Fore.GREEN + f"Functions        : {function_count}")
print(Fore.GREEN + f"Classes          : {class_count}")
print(Fore.GREEN + f"Comments         : {comment_lines}")
print(Fore.GREEN + f"Blank Lines      : {blank_lines}")
print(Fore.GREEN + f"TODOs            : {todo_count}")

print(Fore.YELLOW + "\nSuggestions\n")

if blank_lines > total_lines * 0.3:
    print("- Large number of blank lines.")

if comment_lines < max(1, total_lines * 0.05):
    print("- Add more comments to improve readability.")

if function_count == 0:
    print("- No functions detected.")

if class_count == 0:
    print("- No classes detected.")

if todo_count > 0:
    print("- Resolve pending TODO comments.")

if function_count > 0 and comment_lines >= max(1, total_lines * 0.05):
    print("- Code structure looks good.")

print(Fore.CYAN + "\n========== REVIEW COMPLETE ==========\n")
```

if **name** == "**main**":
file_name = input("Enter Python file name: ")
analyze_code(file_name)
