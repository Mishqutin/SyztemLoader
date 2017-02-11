# SCmd
sz.SZData("clear", "SCmd", 'clearCI()')
sz.SZData("ls", "SCmd", "listDir()")
sz.SZData("exec", "SCmd", "try:\n   exec(' '.join(args), globals())\nexcept:\n  appendCI('Failed to execute')")
sz.SZData("output", "SCmd", "appendCI(' '.join(args))")
sz.SZData("scrollUp", "SCmd", "scrollUp()")
sz.SZData("scrollDown", "SCmd", "scrollDown()")
sz.SZData("note", "SCmd", "editSidebar(args[0], ' '.join(args[1:]))")
# SVars
sz.SZData("cmdInput", "SVar", '["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]')
sz.SZData("QWorking", "SVar", "Yeah! :D")
sz.SZData("currentPageScroll", 'SVar', '[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21]')
sz.SZData("sidebarContent", "SVar", '["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]')
