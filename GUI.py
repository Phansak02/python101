from tkinter import *  # Tkinter คือ เป็นเครื่องที่ใช้สำหรับสร้าง GUI
                       # * คือการ import library ทั้งหมด   
from tkinter import ttk, messagebox

GUI = Tk ()
GUI.title ('โปรแกรมลงข้อมูลน้ำหนัก')  #ชื่อโปรแกรม
GUI.geometry ('500x500') # ปรับขนาดหน้าจอ

def Show():
    messagebox.showinfo ('show Box','ยินดีตอนรับ')

B1 = ttk.Button (GUI,text= 'กดปุ่มนี้',command=Show)  # Button สร้างปุ่มกด
B1.pack (ipadx=40 ,ipady=40,pady=50) #แปะปุ่มไว้กับโปรแกรมหลัก+ขนาดของปุ่ม
# ipad...x , y ปรับขนาดของปุ่มในแนวแกน x y , pad...x  y ปรับระยะห่างที่อยู่ภายนอก

GUI.mainlook()
