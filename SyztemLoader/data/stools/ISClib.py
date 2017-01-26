import os
import sys
import ast

class ISC:
    
    def do(cmd):
        p = cmd.split()
        if p[0] in sz.SZdata:
            if sz.SZdata[p[0]]["type"]=="SCmd":
                sz.SCmdv2(p[0], ast.literal_eval(p[1:]))