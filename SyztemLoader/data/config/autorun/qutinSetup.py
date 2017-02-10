# SCmd
sz.SZData("clear", "SCmd", 'clearCI()')
sz.SZData("ls", "SCmd", "listDir()")
sz.SZData("output", "SCmd", "cmdInput=ast.literal_eval(sz.SZdata['cmdInput']['value'])\ndel cmdInput[0]\ncmdInput.append(' '.join(args))\nsz.SZdata['cmdInput']['value']=str(cmdInput)")

# SVars
sz.SZData("cmdInput", "SVar", '["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]')
sz.SZData("QWorking", "SVar", "Yeah! :D")