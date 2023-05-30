#file_transfer 
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("Data Share")
root.geometry("450x560+500+200")
root.configure(bg='#f4fdfe')
root.resizable(False,False)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        file = filedialog.askopenfile(initialdir=os.getcwd(),title='select image file', filetype=(('Text File','*.txt'),('All Files','*.*')))
        return file.name

    def sender():
        filename = select_file()
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('Searching for incoming connections...')
        conn, addr = s.accept()
        print(f"Incoming connection from {addr}")
        with open(filename, 'rb') as file:
            file_data = file.read(1024)
            while file_data:
                conn.send(file_data)
                file_data = file.read(1024)
        print("File has been sent...")

    #icon
    image_icon1 = PhotoImage(file="Image/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="Image/sender.png")
    Label(window, image=Sbackground).place(x=-2,y=0)

    Mbackground = PhotoImage(file="Image/id.png")
    Label(window, image=Mbackground, bg="#f4fdfe").place(x=100,y=260)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white', fg='black').place(x=140,y=290)

    select_button = Button(window, text="+ Select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file)
    select_button.place(x=160, y=150)

    send_button = Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg='#000', fg="#fff", command=sender)
    send_button.place(x=300, y=150)

    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID = SenderId.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        with open(filename1, 'wb') as file:
            while True:
                file_data = s.recv(1024)
                if not file_data:
                    break
                file.write(file_data)
        print("File has been received")

    #icon
    image_icon1 = PhotoImage(file="Image/receive.png")
    main.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file="Image/receiver.png")
    Label(main, image=Hbackground).place(x=-2,y=0)

    logo = PhotoImage(file="Image/receiver.png")
    Label(main, image=logo, bg="#f4fdfe").place(x=100,y=250)

    Label(main, text="Receive", font=('arial',20), bg="#f4fdfe").place(x=100,y=250)

    Label(main, text="Receive", font=('arial',20), bg="#f4fdfe").place(x=100,y=280)

    Label(main, text="Input sender id", font=('arial',10,'bold'), bg="#f4fdfe").place(x=20,y=340)

    SenderId = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderId.place(x=20,y=370)
    SenderId.focus()
    Label(main, text="filename for incoming file", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    imageicon=PhotoImage(file="Image/arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)

    main.mainloop()

#icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)


#send image
send_image=PhotoImage(file="Image/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)

#receive image
receive_image=PhotoImage(file="Image/receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)


#label
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)


#background
background=PhotoImage(file="Image/background.png")
Label(root,image=background).place(x=-2,y=323)

root.mainloop()

