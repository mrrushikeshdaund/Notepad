from tkinter import *

base = Tk()
base.title("NotePad")
base.geometry("500x600")




mb = Menu(base)
m1 = Menu(mb,tearoff=0)
m1.add_command(label="New",accelerator="Ctrl+N")
m1.add_command(label="New Window",accelerator="Ctrl+Shift+N")
m1.add_command(label="Open",accelerator="Ctrl+O")
m1.add_command(label="Save",accelerator="Ctrl+S")
m1.add_command(label="Save As",accelerator="Ctrl+Shift+N")
m1.add_separator()
m1.add_command(label="Page Setup...")
m1.add_command(label="Print...",accelerator="Ctrl+P")
m1.add_separator()
m1.add_command(label="Exit")

m2 = Menu(base,tearoff=0)
m2.add_command(label="Undo",accelerator="Ctrl+Z")
m2.add_separator()
m2.add_command(label="Cut",accelerator="Ctrl+X")
m2.add_command(label="Copy",accelerator="Ctrl+C")
m2.add_command(label="Paste",accelerator="Ctrl+V")
m2.add_command(label="Delete",accelerator="Del")
m2.add_separator()
m2.add_command(label="Search with Bing...",accelerator="Ctrl+E")
m2.add_command(label="Find...",accelerator="Ctrl+F")
m2.add_command(label="Find Next",accelerator="F3")
m2.add_command(label="Find Previous",accelerator="Shift+F3")
m2.add_command(label="Replace...",accelerator="Ctrl+H")
m2.add_command(label="Go To...",accelerator="Ctrl+G")
m2.add_separator()
m2.add_command(label="Select All",accelerator="Ctrl+A")
m2.add_command(label="Time/Date",accelerator="F5")

m3 = Menu(base,tearoff=0)
m3.add_command(label="Word Wrap")
m3.add_command(label="Font...")

m6 = Menu(mb,tearoff=0)
m6.add_command(label="Zoom In", accelerator="Ctrl+plus")
m6.add_command(label="Zoom Out", accelerator="Ctrl+Minus")
m6.add_command(label="Restore Default Zoom", accelerator="Ctrl+O")

m4 = Menu(base,tearoff=0)
m4.add_cascade(label="Zoom",underline=0,menu=m6)
m4.add_checkbutton(label="Status Bar")

m5 = Menu(base,tearoff=0)
m5.add_command(label="View Help")
m5.add_command(label="Send Feedback")
m5.add_separator()
m5.add_command(label="About Notepad")

mb.add_cascade(label="File",menu=m1)
mb.add_cascade(label="Edit",menu=m2)
mb.add_cascade(label="Format",menu=m3)
mb.add_cascade(label="View",menu=m4)
mb.add_cascade(label="Help",menu=m5)

t1 = Text(base,width=1000,height=500)
t1.place(x=1,y=1)

base.configure(menu=mb)
base.mainloop()