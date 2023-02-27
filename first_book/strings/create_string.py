a="hello"
b="hi"

print("hello \n\tWorld", " => new line and tab")

s='''Hello, 
****World!****'''
print(s)

s=str(b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82','utf-8')
print(s)

def func1():
    """This is documentation string"""
    pass

print(func1.__doc__)

print("""
Usage: program -if <input file> [-of <output file>]

-if: specifies the name of the input file
-of: specifies the name of the output file. If a file is not specified, it is used standart output

""")