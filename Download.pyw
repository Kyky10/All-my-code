import urllib.request, os, sys
from tkinter import Label, Text, Button, END, Tk

def save_file(f):
    i = 0
    f = f.split('/')
    for i in range(len(f)):
        my_list.append(f[i])
    url_name = my_list[-1]

    print('from: ', f)
    print()
    print('file-name:', url_name)
    print()
    url_name = path + '\\' + url_name
    try:
        label.config(text = 'downloading...')
        urllib.request.urlretrieve (s_text.get('1.0', END + "-1c"), ''.join(url_name))
        print('Download complete!')
        label.config(text = 'Download complete!')
    except Exception as err:
        label.config(text = err)

path = 'C:\\Users\\Ruslan\\Downloads'
win = Tk()
win.title = 'Download'
my_list = []
err = ''
    
label = Label(win, text = err)
s_label = Label(win, text = 'Download site:')
s_text = Text(win, width = 50, height = 1)
btn = Button(win, text = 'Download', command = lambda:[save_file(str(s_text.get('1.0', END + "-1c")))])
exit_btn = Button(win, text = 'Exit', command = lambda:[exit()])
label.pack()
s_label.pack()
s_text.pack()
btn.pack()
exit_btn.pack()

win.mainloop()

