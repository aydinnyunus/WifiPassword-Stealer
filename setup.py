from cx_Freeze import setup, Executable

file = open("main.py","a",encoding="utf-8")
r1 = random.randint(-100000, 100000) 
file.write("\nvar = " + r1)
file.write("\nprint(var)\n")
file.close()

base = None    

executables = [Executable("main.py", base=base)]

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

