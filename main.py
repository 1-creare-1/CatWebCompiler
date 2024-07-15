import json
from catweb_compiler import compile

# Example Program
code = '''
log("Program Start!");
play(1835895687);
hide("[");
wait(3);
show("[");
log("Delayed print!");
error("heres an error");
'''

# code = '''
# log("Start");
# wait(1);
# configure("Background Color", "[", "#ff0000");
# wait(1);
# configure("Background Color", "[", "#0000ff");
# wait(1);
# configure("Background Color", "[", "#ff0000");
# wait(1);
# configure("Background Color", "[", "#0000ff");
# wait(1);

# configure("Background Color", "[", "#c8c8c8");
# '''
# Compile the program
compiled = compile(code)

# Output to json file
with open('compiled_code.json', 'w', encoding='utf-8') as f:
    json.dump(compiled, f, ensure_ascii=False, indent=4)