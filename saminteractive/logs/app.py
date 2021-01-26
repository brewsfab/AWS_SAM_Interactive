from saminteractive.utils import utils 

import sys
import tomlkit
import subprocess


template_file = sys.argv[1]
tomlfile = sys.argv[2]

def get_stack_name(tomlfile, environ="default"):
    #TODO check if the file exists and so on

    with open(tomlfile,"r") as f:
        tomlcontent = f.read()

    toml_to_dict = tomlkit.parse(tomlcontent)
    parameters = toml_to_dict[environ]['deploy']['parameters']
    
    return parameters['stack_name'] 


functions = utils.get_template_function_resource_ids(template_file)
stack_name = get_stack_name(tomlfile) 


print(functions)
print(stack_name)

# Test with the first found function 0
subprocess.run(['sam','logs','-n', functions[1], '--stack-name', stack_name])