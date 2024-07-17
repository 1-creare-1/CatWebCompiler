import json
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
a = 5;
b = 10;
c = a + b;
d = c / 2;
log("{c}");
log("{d}");
'''

# Compile the program
compiled = compile(code)

# Output to json file
with open('compiled_code.json', 'w', encoding='utf-8') as f:
    json.dump(compiled, f, ensure_ascii=False, indent=4)