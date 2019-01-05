
from tkinter import *
from neo4j_main import maintest
from load_data import loadcsv
from tkinter.messagebox import showwarning


def callback():
    try:
        if v.get()=='请输入查询内容:':
            str = maintest(ent.get())
            if str == '':
                showwarning('警告', '错误')
            if str == '错误':
                showwarning('警告', '错误')
            inf_txt.delete(0.0, END)
            inf_txt.insert(0.0, str)
        elif v.get()=='请输入贩毒金额:':
            pass
    except:
        showwarning('警告', '错误')

def callback2():
    try:
        str = '123'
        inf_txt.delete(0.0, END)
        inf_txt.insert(0.0, str)
    except:
        showwarning('警告', '错误')

def change():
    v.set('请输入查询内容:')

def change1():
    v.set('请输入贩毒金额:')

root = Tk()
root.geometry('800x800+300+100')
root.title("审判记录查询系统")
frame =Frame(height=700,width=1300,bg='blue')
Label( text="     ").grid(row=0, column=0, sticky=W)

v=StringVar()
v.set("请输入查询内容:")
t1=Label( textvariable = v,font=("黑体",15)).grid(row = 1, column = 1, sticky = W)
Label( text="     ").grid(row=2, column=0, sticky=W)
Label( text="     ").grid(row=4, column=0, sticky=W)
Label( text="     ").grid(row=6, column=0, sticky=W)
ent = Entry(width=80,font=50)
ent.grid(row=3, column=1, sticky=W)
b1=Button(text = "确定",command = callback,font=("黑体",15)).grid(row = 5, column = 1, sticky = W)

inf_txt = Text(width=80, height=25, wrap=WORD,font=50)
inf_txt.grid(row=7, column=1)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='加载更多数据', command=loadcsv,font=50)
filemenu.add_command(label='普通查询', command= change,font=50)
filemenu.add_command(label='贩毒刑期推理', command= change1,font=50)
filemenu.add_separator()  # 添加分割线
filemenu.add_command(label='退出', command=callback,font=50)
menubar.add_cascade(label='菜单', menu=filemenu,font=("黑体",15))  # 第一级

root.config(menu=menubar)
root.iconbitmap(r'C:\Users\lenovo\Desktop\bitbug_favicon.ico')
root.mainloop()