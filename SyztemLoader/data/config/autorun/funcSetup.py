# Setups all basic varaibles etc.
# If you want use commands with arguments simply put args[int] in place.

# SCmd
sz.SZData("print", "SCmd", "print(args[0])")
sz.SZData("getSZdata", "SCmd", "print(sz.SZdata)")
sz.SZData("termColor", "SCmd", "os.system('color {}{}'.format(args[0], args[1]))")
sz.SZData("terminate", "SCmd", "exit()")
sz.SZData("python", "SCmd", "ISC.python(args[0])")
sz.SZData("cd", "SCmd", "os.chdir(args[0])")