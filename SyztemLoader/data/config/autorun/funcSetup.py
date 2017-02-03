# Setups all basic varaibles etc.
# If you want use commands with arguments simply put args[int] in place.
import time
# SCmd
sz.SZData("print", "SCmd", "print( ast.literal_eval( ' '.join(args[0:]) ) )")
sz.SZData("getSZdata", "SCmd", "print(sz.SZdata)")
sz.SZData("termColor", "SCmd", "os.system('color {}'.format(args[0]))")
sz.SZData("terminate", "SCmd", "exit()")
sz.SZData("python", "SCmd", "ISC.python(args[0])")
sz.SZData("cd", "SCmd", "os.chdir(args[0])")
sz.SZData("clear", "SCmd", "os.system('cls')")