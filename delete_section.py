
import os

file_path = r"e:\WebsiteProject(2026)\Vardan\index.html"
start_line = 885
end_line = 2475

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# lines are 0-indexed, so start_line 885 is index 884
# end_line 2475 is index 2474.
# We want to remove from index 884 up to index 2474 inclusive.
# So slice from 0 to 884, and then from 2475 to end.

new_lines = lines[:start_line-1] + lines[end_line:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully deleted lines.")
