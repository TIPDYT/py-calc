from tkinter import *
import ply.lex as lex
import ply.yacc as yacc
from math import log, e, pi, cos, sin, tan, acos, asin, atan, sqrt
tokens = ['FLOAT', 'INT', 'DIV', 'ADD', 'SUB', 'MUL', 'LP', 'RP', 'LSQU', 'RSQU', 'UP', 'SQRT', 'FUNC', 'MOD']
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LP = r'\('
t_RP = r'\)'
t_LSQU = r'\['
t_RSQU = r'\]'
t_UP = r'\^'
t_SQRT = r'√'
t_MOD = r'%'
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_FUNC(t):
    r'[a-zA-Z_][a-zA-Z]*'
    t.value = str(t.value)
    return t
def t_newline(t):
    r'\n+'
    pass
def p_expression_add(p):
    'expression : expression ADD term'
    p[0] = p[1] + p[3]
def p_expression_sub(p):
    'expression : expression SUB term'
    p[0] = p[1] - p[3]
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
def p_term_mul(p):
    'term : term MUL factor'
    p[0] = p[1] * p[3]
def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]
def p_term_modulo(p):
    'term : term MOD factor'
    p[0] = p[1] % p[3]
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
def p_factor_int(p):
    'factor : INT'
    p[0] = p[1]
def p_factor_float(p):
    'factor : FLOAT'
    p[0] = p[1]
def p_factor_expression(p):
    'factor : LP expression RP'
    p[0] = p[2]
def p_factor_expression_br(p):
    'factor : LSQU expression RSQU'
    p[0] = p[2]
def p_factor_power(p):
    'factor : factor UP factor'
    p[0] = p[1] ** p[3]
def p_factor_sqrt(p):
    'factor : SQRT factor'
    p[0] = sqrt(p[2])
def p_factor_function(p):
    'factor : function'
    p[0] = p[1]
def p_function(p):
    'function : FUNC LP factor RP'
    if p[1] == 'sin':
        p[0] = sin(p[3])
    elif p[1] == 'cos':
        p[0] = cos(p[3])
    elif p[1] == 'tan':
        p[0] = tan(p[3])
    elif p[1] == 'asin':
        p[0] = asin(p[3])
    elif p[1] == 'acos':
        p[0] = acos(p[3])
    elif p[1] == 'atan':
        p[0] = atan(p[3])
    elif p[1] == 'log':
        p[0] = log(p[3])
    elif p[1] == 'ln':
        p[0] = log(p[3]) / log(e)
t_ignore = ' \t'
lexer = lex.lex()
parser = yacc.yacc()
def dnum(num):
    global txt
    txt.insert(INSERT, str(num))
def equal():
    pass
def solve():
    global txt
    equ = txt.get()
    txt.delete(0, len(txt.get()))
    txt.insert(INSERT, parser.parse(equ))
gui = Tk()
gui.title("Calculator")
gui.geometry("310x250")
result = ""
txt = Entry(gui, width=48)
button1 = Button(gui, text='1', command= lambda: dnum(1), height=1, width=7)
button2 = Button(gui, text='2', command= lambda: dnum(2), height=1, width=7)
button3 = Button(gui, text='3', command= lambda: dnum(3), height=1, width=7)
button4 = Button(gui, text='4', command= lambda: dnum(4), height=1, width=7)
button5 = Button(gui, text='5', command= lambda: dnum(5), height=1, width=7)
button6 = Button(gui, text='6', command= lambda: dnum(6), height=1, width=7)
button7 = Button(gui, text='7', command= lambda: dnum(7), height=1, width=7)
button8 = Button(gui, text='8', command= lambda: dnum(8), height=1, width=7)
button9 = Button(gui, text='9', command= lambda: dnum(9), height=1, width=7)
button0 = Button(gui, text='0', command= lambda: dnum(0), height=1, width=7)
add = Button(gui, text='+', command=lambda: dnum('+'), height=1, width=7)
sub = Button(gui, text='-', command=lambda: dnum('-'), height=1, width=7)
mul = Button(gui, text='*', command=lambda: dnum('*'), height=1, width=7)
div = Button(gui, text='/', command=lambda: dnum('/'), height=1, width=7)
eq = Button(gui, text='=', command=solve, height=1, width=7)
lparen = Button(gui, text='(', command=lambda: dnum('('), height=1, width=7)
rparen = Button(gui, text=')', command=lambda: dnum(')'), height=1, width=7)
lsqu = Button(gui, text='[', command= lambda: dnum('['), height=1, width=7)
rsqu = Button(gui, text=']', command= lambda: dnum(']'), height=1, width=7)
p = Button(gui, text='π', command= lambda: dnum(str(pi)), height=1, width=7)
ee = Button(gui, text='e', command= lambda: dnum(str(e)), height=1, width=7)
sqr = Button(gui, text='sqrt', command= lambda: dnum(str('√')), height=1, width=7)
mo = Button(gui, text='mod', command= lambda: dnum(str('%')), height=1, width=7)
c = Button(gui, text='cos', command= lambda: dnum(str('cos(')), height=1, width=7)
s = Button(gui, text='sin', command= lambda: dnum(str('sin(')), height=1, width=7)
t = Button(gui, text='tan', command= lambda: dnum(str('tan(')), height=1, width=7)
ac = Button(gui, text='acos', command= lambda: dnum(str('acos(')), height=1, width=7)
asss = Button(gui, text='asin', command= lambda: dnum(str('asin(')), height=1, width=7)
at = Button(gui, text='atan', command= lambda: dnum(str('atan(')), height=1, width=7)
lo = Button(gui, text='log', command= lambda: dnum(str('log(')), height=1, width=7)
ln = Button(gui, text='ln', command= lambda: dnum(str('ln(')), height=1, width=7)
po = Button(gui, text='^', command= lambda: dnum(str('^')), height=1, width=7)
def cc():
    global txt
    text = txt.get()[:-1]
    txt.delete(0, len(txt.get()))
    txt.insert(INSERT, text)
ccc = Button(gui, text='C', command=cc, height=1, width=7)
def clear():
    global txt
    txt.delete(0, len(txt.get()))
cls = Button(gui, text='Clear', command=clear, height=1, width=7)
txt.place(x=10, y=3)
button1.place(x=10, y= 30)
button2.place(x=70, y= 30)
button3.place(x=130, y= 30)
button4.place(x=190, y= 30)
button5.place(x=10, y= 60)
button6.place(x=70, y= 60)
button7.place(x=130, y= 60)
button8.place(x=190, y= 60)
button9.place(x=10, y= 90)
button0.place(x=70, y= 90)
add.place(x=130, y=90)
sub.place(x=190, y=90)
mul.place(x=10, y=120)
div.place(x=70, y=120)
eq.place(x=130, y=120)
cls.place(x=190, y=120)
lparen.place(x=10, y=150)
rparen.place(x=70, y=150)
lsqu.place(x=130, y=150)
rsqu.place(x=190, y=150)
p.place(x=10, y=180)
ee.place(x=70, y=180)
sqr.place(x=130, y=180)
mo.place(x=190, y=180)
s.place(x=250, y=30)
c.place(x=250, y=60)
t.place(x=250, y=90)
asss.place(x=250, y=120)
ac.place(x=250, y=150)
at.place(x=250, y=180)
lo.place(x=10, y=210)
ln.place(x=130, y=210)
po.place(x=190, y=210)
ccc.place(x=70, y=210)
gui.mainloop()