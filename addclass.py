#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 02, 2020 11:38:31 PM CST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import addclass_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    addclass_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    addclass_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("564x348+707+158")
        top.minsize(152, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("按行添加课程信息")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.319, rely=0.078, height=56, width=95)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Microsoft YaHei UI} -size 10 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''课程号''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.532, rely=0.259,height=41, relwidth=0.291)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.319, rely=0.244, height=56, width=95)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Microsoft YaHei UI} -size 10 -weight bold")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''课程名称''')

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.532, rely=0.431,height=41, relwidth=0.291)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.319, rely=0.69, height=40, width=116)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=addclass_support.addgrade)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Microsoft YaHei UI} -size 10 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''添加''')

        self.Button1_9 = tk.Button(top)
        self.Button1_9.place(relx=0.638, rely=0.69, height=40, width=116)
        self.Button1_9.configure(activebackground="#ececec")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#d9d9d9")
        self.Button1_9.configure(command=addclass_support.comeback)
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(font="-family {Microsoft YaHei UI} -size 10 -weight bold")
        self.Button1_9.configure(foreground="#000000")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''返回''')

        self.Label1_5 = tk.Label(top)
        self.Label1_5.place(relx=0.319, rely=0.42, height=56, width=95)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#d9d9d9")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font="-family {Microsoft YaHei UI} -size 10 -weight bold")
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''学分''')

        self.Entry1_6 = tk.Entry(top)
        self.Entry1_6.place(relx=0.532, rely=0.086,height=41, relwidth=0.291)
        self.Entry1_6.configure(background="white")
        self.Entry1_6.configure(disabledforeground="#a3a3a3")
        self.Entry1_6.configure(font="TkFixedFont")
        self.Entry1_6.configure(foreground="#000000")
        self.Entry1_6.configure(highlightbackground="#d9d9d9")
        self.Entry1_6.configure(highlightcolor="black")
        self.Entry1_6.configure(insertbackground="black")
        self.Entry1_6.configure(selectbackground="#c4c4c4")
        self.Entry1_6.configure(selectforeground="black")

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Microsoft YaHei UI} -size 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





