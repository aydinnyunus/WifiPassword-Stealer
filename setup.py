from cx_Freeze import setup, Executable

base = None    

executables = [Executable("temp.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Wifi",
    options = options,
    version = "1.0.0",
    description = 'Wifi Password',
    executables = executables
)
