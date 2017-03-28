# SCmds
sz.SZData("clear", "SCmd", 'clearCI()')
sz.SZData("ls", "SCmd", "listDir()")
sz.SZData("exec", "SCmd", "try:\n   exec(' '.join(args), globals())\nexcept:\n  appendCI('Failed to execute')")
sz.SZData("output", "SCmd", "output(' '.join(args))")
sz.SZData("scrollUp", "SCmd", "scrollUp()")
sz.SZData("scrollDown", "SCmd", "scrollDown()")
sz.SZData("side", "SCmd", "editSidebar(args[0], ' '.join(args[1:]))")
sz.SZData("mode", "SCmd", "sz.SZdata['termMode']['value'] = args[0]")
sz.SZData("cat", "SCmd", "showFile(args[0])")
sz.SZData("sleep", "SCmd", "time.sleep(float(args[0]))")
sz.SZData("alias", "SCmd", 'sz.SZData(args[1], "SCmd", sz.SZdata[args[0]]["value"])')
sz.SZData("sz", "SCmd", "ISC.exeSzFull(args[0])")
sz.SZData("start", "SCmd", "os.system('start {}'.format(' '.join(args)))")
sz.SZData("setting", "SCmd", "defSet(args[0], args[1])")

# Long SCmds
sz.SZData("help", "SCmd", '''\
appendCI("This is the list of commands:")
appendCI("Syntax: <cmd> 0 1 - 0 and 1 represents argumets.")
appendCI("clear - Clears output screen.")
appendCI("output 0 - Prints string to output screen.")
appendCI("title 0 - Sets window\'s title.")
appendCI("set 0 1 - Defines a new SVar: 0 - name, 1 - value.")
appendCI("termColor 0 - Like color in Winshit cmd.")
appendCI("terminate - Exit.")
appendCI("ls - List files in current directory.")
appendCI("cd 0 - Change directory.")
appendCI("cat 0 - Shows file content.")
appendCI("exec 0 - Execute Python things idk how I could explain this.")
appendCI("alias 0 1 - 0:Command 1:Alias name.")
appendCI("sleep 0 - Wait secs.")
appendCI("mode 0 - Change mode. Try mode scroll.")
appendCI("----")
appendCI("Enter SVar name to get it\'s value.")
appendCI("Enter SVar name and any value to change it\'s value.")
appendCI("You can also eval expressions just by typing them.")
''')

# SVars
sz.SZData("cmdInput", "SVar", '["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]')
sz.SZData("QWorking", "SVar", "Yeah! :D")
sz.SZData("currentPageScroll", 'SVar', '[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21]')
sz.SZData("sidebarContent", "SVar", '["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]')
sz.SZData("termMode", "SVar", 'console')
sz.SZData("echo", "SVar", 1)
sz.SZData("prompt", "SVar", "> ")