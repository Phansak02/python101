from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk ()
GUI.title ('โปรแกรมจัดการ layout')
GUI.geometry ('500x500')

#Label (GUI, text='ผลดี').pack()  # .pack ทำให้ข้อความอยู่ตรงกลางของ GUI
# ใช้ Layout แสดงข้อความ

L1 = Label (GUI, text='ผลดี 1')
L1.pack() # .pack ()  คือ เรียงจากบนลงล่าง

L2 = Label (GUI, text='ผลดี 2')
L2.place (x=0,y=0)    # .place คือ การคอนโทรลต่ำแหน่ง ใช่พิกัด x'y

F1 = LabelFrame (GUI, text='grid color') # Frame คือการใส่กรอบเส้น
F1.place(x=50,y=50)    # .place คือ คอนโทรลตำแหน่ง Frame

L3 = Label (F1, text='ผลดี 3',bg='red')  # bg คือ การใส่สีพื้นหลัง
L3.grid (row=0, column=0)  #  .grid คือ การคอนโทรลตำแหน่ง ใช้ row, column ในการคอนโทรล

L4 = Label (F1, text= 'ผลดี 4',bg='green')
L4.grid (row=0, column=1)

L5 = Label (F1, text='ผลดี 5' ,bg='orange')
L5.grid (row=1, column=0)

L6 = Label (F1, text='ผลดี 6' ,bg='blue' ,fg='red')   # fg คือ การใส่สีตัวหนังสือ
L6.grid (row=2, column=2)

GUI.mainloop ()

