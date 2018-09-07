s_cadou = 'N-r90-f100-l90-f50-l90-f100-l90-f50-l90-f50-l90-f100-l90-f50-b100-l90-f50-r90-f100-r90-f50-r90-f100-r90-f50-l45-f20-l45-f10-l45-f5-l45-f7-l45-f5-l45-f26-r135-f17-r45-f9-r45-f5-r45-f5-r45-f5-r45-f22-U-f150-D'
s_cadouri = 'N-r90-f100-l90-f50-l90-f100-l90-f50-l90-f50-l90-f100-l90-f50-b100-l90-f50-r90-f100-r90-f50-r90-f100-r90-f50-l45-f20-l45-f10-l45-f5-l45-f7-l45-f5-l45-f26-r135-f17-r45-f9-r45-f5-r45-f5-r45-f5-r45-f22-U-f150-D-r90-f100-l90-f50-l90-f100-l90-f50-l90-f50-l90-f100-l90-f50-b100-l90-f50-r90-f100-r90-f50-r90-f100-r90-f50-l45-f20-l45-f10-l45-f5-l45-f7-l45-f5-l45-f26-r135-f17-r45-f9-r45-f5-r45-f5-r45-f5-r45-f22-U-f150-D-r90-f100-l90-f50-l90-f100-l90-f50-l90-f50-l90-f100-l90-f50-b100-l90-f50-r90-f100-r90-f50-r90-f100-r90-f50-l45-f20-l45-f10-l45-f5-l45-f7-l45-f5-l45-f26-r135-f17-r45-f9-r45-f5-r45-f5-r45-f5-r45-f22-U-f150-D-r90-f100-l90-f50-l90-f100-l90-f50-l90-f50-l90-f100-l90-f50-b100-l90-f50-r90-f100-r90-f50-r90-f100-r90-f50-l45-f20-l45-f10-l45-f5-l45-f7-l45-f5-l45-f26-r135-f17-r45-f9-r45-f5-r45-f5-r45-f5-r45-f22-U-f150-D'
ins = '''Enter a program for the turtle machine
eg f100-r45-f100-r45-f100-f45-f100
N = New file
F100 = forward 100
B50 = backwards 100
R50 = Right turn 50 deg
L45 = Left turn 40 deg'''
from turtle import *
def tc(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        left(val)
    elif do == 'L':
        right(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Error')

def artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command,':',cmd_type,num)
        tc(cmd_type,num)

def cadou():
    cadou_list = s_cadou.split('-')
    for cammand in cadou_list:
        cadou_len = len(cammand)
        if cadou_len == 0:
            continue
        cammand_type = cammand[0]
        ind = 0
        if cadou_len > 1:
            nam_string = cammand[1:]
            ind = int(nam_string)
        tc(cammand_type,ind)

def cadouri():
    cadou_list = s_cadouri.split('-')
    for cammand in cadou_list:
        cadou_len = len(cammand)
        if cadou_len == 0:
            continue
        cammand_type = cammand[0]
        ind = 0
        if cadou_len > 1:
            nam_string = cammand[1:]
            ind = int(nam_string)
        tc(cammand_type,ind)
    

while True:
    from turtle import getscreen
    screen = getscreen()
    program = screen.textinput('Masina de desenat', ins)
    print(program)
    if program == 'cadouri':
        cadouri()
    elif program == 'cadou':
        cadou()
    elif program == None or program.upper() == 'END':
        break
    import pyperclip
    pyperclip.copy(program)
    artist(program)

