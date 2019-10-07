#8
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("400x400")

l = tk.Label(window,text = '',bg = 'yellow')
l.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(window,te)

window.mainloop()


"""
#7
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry("400x400")

canvas = tk.Canvas(window,bg = 'blue',height = 100,width = 200,).pack()
image_file = tk.PhotoImage(file='D:\图片\家人图片\黄燕涛图片\1.jpg')
image = canvas.create_image(0,0,anchor = 'nw',image = image_file)
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill = 'red')
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start = 0,extent = 180)
rect = canvas.create_rectangle(100,20,120,40)
def moveit():
    canvas.move(rect,0,2)

button = tk.Button(window,text = 'move',command = moveit).pack()
window.mainloop()
"""


"""
#6
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("400x400")

l = tk.Label(window,bg = 'yellow',width = 20,text = 'empty')
l.pack()

def print_selection():
    if(var1.get() == 1) & (var2.get() == 0):
        l.config(text = 'I love only Python')
    elif(var1.get() == 0) & (var2.get() == 1):
        l.config(text = 'I love only C++')
    elif(var1.get() == 0) & (var2.get() == 0):
        l.config(text = 'I do not love the two language')
    else:
        l.config(text = 'I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window,text = 'Python',variable = var1,onvalue = 1, offvalue = 0,command = print_selection)
c2 = tk.Checkbutton(window,text = 'C++',variable = var2,onvalue = 1, offvalue = 0,command = print_selection)
c1.pack()
c2.pack()

window.mainloop()
"""

"""
#5
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("400x400")

lable = tk.Label(window,bg = 'yellow',width = 20,text = 'empty')
lable.pack()

def print_selection(v):
    lable.config(text = 'you have selected ' + v)
s = tk.Scale(window,label = 'try me',from_ = 5,to = 11,orient = tk.HORIZONTAL,length = 200,showvalue = 1,tickinterval = 1,resolution = 0.01,command = print_selection)
s.pack()

window.mainloop()
"""

"""
#4
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("500x500")

var = tk.StringVar()
l = tk.Label(window,bg = "yellow",width = 25,text = 'empty')
l.pack()

def print_selection():
    l.config(text = 'you have selected ' + var.get())

r1 = tk.Radiobutton(window,text = 'Option A',variable = var,value='A',command = print_selection)
r1.pack()

r2 = tk.Radiobutton(window,text = 'Option B',variable = var,value='B',command = print_selection)
r2.pack()

r3 = tk.Radiobutton(window,text = 'Option C',variable = var,value='C',command = print_selection)
r3.pack()

window.mainloop()
"""

"""
#3
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x300")

var1 = tk.StringVar()
lable = tk.Label(window,bg = "yellow",width = 4,textvariable =var1)
lable.pack()

def print_selection():
    value = lb.get(lb.curselection())#光标选定的那个
    var1.set(value)

button = tk.Button(window,text = 'point selection',width = 12, height = 2,command = print_selection)
button.pack()

var2 = tk.StringVar()
var2 = set((11,22,33,44))
lb = tk.Listbox(window,listvariable = var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert("end",item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

window.mainloop()
"""


"""
#2
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("300x300")
e = tk.Entry(window,show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert(1.1,var)

button1 = tk.Button(window,text = "insert point",width = 12,height = 2,command = insert_point)
button1.pack()
button2 = tk.Button(window,text = "insert end",command = insert_end)
button2.pack()

t = tk.Text(window,height = 2)
t.pack()
window.mainloop()
"""
"""
#1
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('500x300')

var = tk.StringVar()

l = tk.Label(window,textvariable = var,bg = "green",font = ("Arial",12),width = 12,height = 2)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me!")
    else:
        var.set("")
        on_hit = False

button = tk.Button(window,text = "hit me!",width = 12,height = 2,command = hit_me)
button.pack()
window.mainloop()

"""
