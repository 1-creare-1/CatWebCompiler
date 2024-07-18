import json
import os
from catweb_compiler import compile

# Example Program
# code = '''
# log("Program Start!");
# play(1835895687);
# hide(78);
# wait(3);
# show(78);
# log("Delayed print!");
# error("heres an error");
# '''

# Example program that breaks the filter :(
# code = '''
# log("Start");
# wait(1);
# configure("Background Color", 116, "#ff0000");
# wait(1);
# configure("Background Color", 116, "#0000ff");
# wait(1);
# configure("Background Color", 116, "#ff0000");
# wait(1);
# configure("Background Color", 116, "#0000ff");
# wait(1);

# configure("Background Color", 116, "#c8c8c8");
# '''

# Example program for loops
# code = '''
# log("Code starting");
# loop {
#     log("inner");
#     loop(2) {
#         log("hi");
#     }
#     wait(1);
# }
# '''

# Example program for variables
code = '''
// Define two variables
a = 5;
b = 10;
// Add A to B and assign to C
c = a + b;
// Divide C by 2 and assign to D
d = c / 2;
// Print outputs of C and D
log("{c}");
log("{d}");
'''

# Compile the program
compiled = compile(code)

# Output to json file
out_dir = os.path.dirname(os.path.realpath(__file__))
out_file = f'{out_dir}\compiled_code.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(compiled, f, ensure_ascii=False, indent=4)
print(f"Saved compiled json to {out_file}")