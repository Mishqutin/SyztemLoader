ISC.do("cls")
ISC.do("title Qutin")
sz.SZData("cmdInput", "SVar", '["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]')
print("""

#PBFSEP V0.1.0`


                          SBPQ OS
(Early shit/Wczesne gowno)""")
time.sleep(1)
while True:
    ISC.do("cls")
    cmdInput = ast.literal_eval(sz.SZdata["cmdInput"]["value"])
    print("""\
{}
--------------------------------------------------------------------|Qutin
{: <68}|v0
{: <68}|
{: <68}|PreInDev
{: <68}|
{: <68}|LOL
{: <68}|---------
{: <68}|Nothing
{: <68}|  to
{: <68}|display.
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
{: <68}|
--------------------------------------------------------------------^---------""".format( os.getcwd()+" "*(68-len( os.getcwd() ))+"|==", cmdInput[0], cmdInput[1], cmdInput[2], cmdInput[3], cmdInput[4], cmdInput[5], cmdInput[6], cmdInput[7], cmdInput[8], cmdInput[9], cmdInput[10], cmdInput[11], cmdInput[12], cmdInput[13], cmdInput[14], cmdInput[15], cmdInput[16], cmdInput[17], cmdInput[18], cmdInput[19], cmdInput[20]))
    x = input()
    if x:
        ISC.do("output {}".format(x))
        ISC.do(x)
