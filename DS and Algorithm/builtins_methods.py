import types
import builtins
for name, obj in vars(builtins).items():
    print(f'{name} : {obj} \n')