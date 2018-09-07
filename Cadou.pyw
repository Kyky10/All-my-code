s_cadou = 'N-r90-f100-l90-f50-l90-f100-l90-f50-l90-f50-l90-f100-l90-f50-b100-l90-f50-r90-f100-r90-f50-r90-f100-r90-f50-l45-f20-l45-f10-l45-f5-l45-f7-l45-f5-l45-f26-r135-f17-r45-f9-r45-f5-r45-f5-r45-f5-r45-f22-U-f150-l90-f200-r90-D-f50-r90-f20-u-f35-d-r65-f50-l130-f50-b25-r66-b22-u-f80-r85-b25-d-f50-l160-f50-r160-f50-l160-f50-r74-u-f20-r90-f33-d-f25-b50-l90-f25-r90-f50-l90-u-f20-l90-d-f50-r90-f25-u-f15-r90-d-f50-r90-f10-b20-r180-u-f20-l90-d-f50-r90-u-f50-d-r60-f50-l120-f50-b25-l120-f30-u-l180-f60-l90-f30-d-r180-f50-l160-f65-r160-f50-u-l90-f30-l90-d-f50'
from turtle import *
from tkinter import *
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

windows = Tk()
btn = Button(windows,width = 25,height=3, text = 'Cadou!', command = cadou)
btn.pack()

