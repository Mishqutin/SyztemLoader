# Setups all basic varaibles etc.
# If you want use commands with arguments simply put args[int] in place.

# SCmd
sz.SZData("print", "SCmd", "print( ast.literal_eval( ' '.join(args[0:]) ) )")
sz.SZData("getSZdata", "SCmd", "print(sz.SZdata)")
sz.SZData("termColor", "SCmd", "os.system('color {}'.format(args[0]))")
sz.SZData("terminate", "SCmd", "exit()")
sz.SZData("python", "SCmd", "ISC.python(args[0])")
sz.SZData("cd", "SCmd", "try:\n    os.chdir(' '.join(args))\nexcept:\n    appendCI('Directory does not exist.')")
sz.SZData("cls", "SCmd", "os.system('cls')")
sz.SZData("listdir", "SCmd", "print(os.listdir())")
sz.SZData("dir", "SCmd", "print(os.getcwd())")
sz.SZData("show", "SCmd", "sz.showFile(' '.join(args))")
sz.SZData("title", "SCmd", "os.system('title {}'.format(' '.join(args)))")
sz.SZData("dcl", "SCmd", "sz.SZData(args[0], 'SVar', None)")
sz.SZData("edit", "SCmd", "os.system('start notepad.exe {}'.format(args[0]))")
sz.SZData("restart", "SCmd", "programRestart()")
sz.SZData("getKey", "SCmd", "getKey(args[0])")
sz.SZData("input", "SCmd", "inputString(args[0])")
sz.SZData("if", "SCmd", "doIf(args[0].replace(':', '', 1), ' '.join(args[1:]))")
sz.SZData("pause", "SCmd", "trash = os.system('pause >> nul')")

# SVars
sz.SZData("test", "SVar", "spam eggs")
