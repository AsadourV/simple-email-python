import smtplib
import ssl
from tkinter import *

window = Tk()
lbl = Label(window, text="Please fill in all fields !", font=("Arial Bold", 35))
e = Entry(window, width=40)
passentry = Entry(window, show="*", width=40)
receiverentry = Entry(window, width=40)
smtpserverentry = Entry(window, width=40)
messageentry = Entry(window, width=40)
portentry = Entry(window, width=40)


def send(password, smtp_server, receiver_email, message, sender_email, port):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        print(server.sendmail(sender_email, receiver_email, message))


def createpanel():
    window.title("Email sender program")
    window.geometry('850x600')

    window.grid(lbl.grid(column=0, row=0))
    # ////////////////////////////////////////////////////////////////
    user = Label(window, text="Your email", font=("Arial Bold", 20))
    window.grid(user.grid(column=0, row=3))

    e.grid(row=3, column=1, padx=90, pady=30, ipady=7)
    # ////////////////////////////////////////////////////////////////

    passw = Label(window, text="Password", font=("Arial Bold", 20))
    window.grid(passw.grid(column=0, row=4))

    passentry.grid(row=4, column=1, padx=90, pady=30, ipady=7)

    recemail = Label(window, text="Receiver email", font=("Arial Bold", 20))
    window.grid(recemail.grid(column=0, row=5))
    receiverentry.grid(row=5, column=1, padx=90, pady=30, ipady=7)

    smtpserver = Label(window, text="SMTP Server", font=("Arial Bold", 20))
    window.grid(smtpserver.grid(column=0, row=6))
    smtpserverentry.grid(row=6, column=1, padx=90, pady=30, ipady=7)

    portlab = Label(window, text="Port", font=("Arial Bold", 20))
    window.grid(portlab.grid(column=3, row=6))
    portentry.grid(row=6, column=4, padx=90, pady=30, ipady=7)

    message = Label(window, text="Message!", font=("Arial Bold", 20))
    window.grid(message.grid(column=1, row=7))
    messageentry.grid(row=8, column=1, padx=90, pady=30, ipady=50)

    login = Button(window, text="Send", command=clicked)
    login.grid(column=1, row=9)

    window.grid(user.grid(column=0, row=3))
    window.mainloop()


def clicked():

    # password, smtp_server, receiver_email, message, sender_email, port

    send(passentry.get(), smtpserverentry.get(), receiverentry.get(), messageentry.get(), e.get(), int(portentry.get()))


if __name__ == "__main__":
    createpanel()
