from tkinter import*
import qrcode

w= Tk()
w.title("QRCODE GENERATOR")
w.geometry("1000x550")
w.config(background="#316381")
w.resizable(False,False)
Img_logo = PhotoImage(file="barcode-gc570d519b_640.png")
w.iconphoto(False,Img_logo)
def generate_qrcode():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("qrcodes/"+ str(name)+ ".png")

    global Img
    Img = PhotoImage(file = "qrcodes/"+ str(name)+ ".png")
    Img_view.config(image=Img)

Img_view = Label(w,bg = "#316381")
Img_view.pack(padx=50,pady=10,side=RIGHT)

Label(w,text="Qr-code Title",fg="white",background="#316381",font=15).place(x=50,y=170)

title = Entry(w,width=13,font = "arial 15")
title.place(x=50,y=200)

entry = Entry(w,width=28,font="arial 15")
entry.place(x=50,y=250)

Button(w,text="Genereate QrCode",width=20,height=2, bg='#89AFC7', fg = "white",command= generate_qrcode).place(x=50,y=300)


w.mainloop()
