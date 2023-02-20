from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk ()
GUI.title ('โปรแกรมจัดการ layout')
GUI.geometry ('500,500')

L1 = Label (GUI,text='กรอกข้อมูลน้ำหนัก' ,font=('Angsana New', 25))
L1.pack()

v_kilo = StringVar()  # ตัวแปรพิเศษเอาไว้เก็บค่า

E1 = ttk.Entry (GUI, textvariable= v_kilo, width=10, justify='right', font=('impact',30))
# สร้างช่องกรอกข้อมูล โดยใช้ Entry ปรับขนาดของช่อง โดยใช้ width1 = 1 ตัวอักษร, justify คือการปรับตัวหนังสือให้อยู่ด้านขวา, font คือ ปรับฟอนท์
# ลิงค์ stringvar กับ entry โดยการใช้ textvariable
E1.pack (pady=20)

def Calc (event=None):
    print ('กำลังคำนวณ...รอสักครู่')
    kilo = float (v_kilo.get ()) # .get () ดึงข้อมูลจากตัวแปรที่เปลี่ยนเป็น stringVar
    print (kilo * 10)
    calc_result = kilo *299
    messagebox.showinfo ('ราคาทั้งหมด','ทั้งหมด: {:,.2f} บาท  (โลละ 1 บาท)'.format (Calc_result))

B1 = ttk.Button (GUI, text='คำนวณ', command=Calc)
B1.pack (ipadx=40,ipady=40)

E1.bind ('<Return>',Calc)  # ต้องใส่คำว่า event=None ในฟังก์ชันด้วย

GUI.mainloop ()
