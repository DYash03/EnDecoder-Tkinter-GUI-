from tkinter import *
import os.path
import random as rand
import smtplib
import base64
scr=Tk()
scr.title("Encoder-Decoder")
scr.configure(bg="#C0C0C0")
canvas = Canvas(width=1000,height=5000)
canvas.pack()
photo = PhotoImage(file='C:\\Users\\hp\\Desktop\\EnDecoder\\hacker0.png')
canvas.create_image(60,425, image=photo ,anchor=NW)
l=Label(scr,text="Enter text for Encoding or Decoding",bg="silver",fg="blue",font=('time','44','bold'))
l.place(x=262,y=0)
text=Text(scr,width=53,height=10,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
text.place(x=326,y=100)
b=Button(scr,text="ENDE-CODE",bg="red",fg="black",font=('Time','20','bold'),command=lambda:encode())
b.place(x=326,y=426)
b1=Button(scr,text="SAVE",bg="green",fg="black",font=('Time','20','bold'),command=lambda:save())
b1.place(x=1027,y=426)
ee=Entry(scr,bg="silver",fg="black",font=('Time','25','bold'))
ee.place(x=570,y=540)
b7=Button(scr,text="Email",bg="blue",fg="black",font=('Time','20','bold'),command=lambda:Mail())
b7.place(x=700,y=610)
l=Label(scr,text="E",bg="silver",fg="red",font=('time','50','bold'))
l.place(x=150,y=0)
l1=Label(scr,text="N",bg="silver",fg="red",font=('time','50','bold'))
l1.place(x=150,y=120)
l2=Label(scr,text="G",bg="silver",fg="red",font=('time','50','bold'))
l2.place(x=150,y=240)
l3=Label(scr,text="L",bg="silver",fg="red",font=('time','50','bold'))
l3.place(x=150,y=360)
l4=Label(scr,text="I",bg="silver",fg="red",font=('time','50','bold'))
l4.place(x=150,y=480)
l5=Label(scr,text="S",bg="silver",fg="red",font=('time','50','bold'))
l5.place(x=150,y=600)
l6=Label(scr,text="H",bg="silver",fg="red",font=('time','50','bold'))
l6.place(x=150,y=720)
l7=Label(scr,text="H",bg="silver",fg="green",font=('time','50','bold'))
l7.place(x=1350,y=0)
l8=Label(scr,text="A",bg="silver",fg="green",font=('time','50','bold'))
l8.place(x=1350,y=120)
l9=Label(scr,text="W",bg="silver",fg="green",font=('time','50','bold'))
l9.place(x=1350,y=240)
l10=Label(scr,text="K",bg="silver",fg="green",font=('time','50','bold'))
l10.place(x=1350,y=360)
l11=Label(scr,text="I",bg="silver",fg="green",font=('time','50','bold'))
l11.place(x=1350,y=480)
l12=Label(scr,text="N",bg="silver",fg="green",font=('time','50','bold'))
l12.place(x=1350,y=600)
l13=Label(scr,text="S",bg="silver",fg="green",font=('time','50','bold'))
l13.place(x=1350,y=720)

def Mail():
    a1=ee.get()
    content="HEY!"+"\n"+"This is Kaido. Someone has send a message for you using Incassable software. At present message is encoded in HAWKINS language. In order to decode don't use much brain just use an Incassable software. The message is : "+"\n"+e
    try:
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('sender email','password')
        mail.sendmail('sender email',a1,content)
        mail.close()
        l=Label(scr,text="SEND",bg="white",fg="red",font=('time','20','bold'))
        l.place(x=1130,y=540)
    except:
        l=Label(scr,text="FAILED",bg="white",fg="red",font=('time','20','bold'))
        l.place(x=1130,y=540)

def encode():
    scr1=Tk()
    global e
    e=""
    t=text.get(0.0,"end")
    for i in t:
        if(i=="A")|(i=="a"):
            e=e+":"
        elif(i=="B")|(i=="b"):
            e=e+" "
        elif(i=="C")|(i=="c"):
            e=e+"_"
        elif(i=="D")|(i=="d"):
            e=e+"{"
        elif(i=="E")|(i=="e"):
            e=e+")"
        elif(i=="F")|(i=="f"):
            e=e+"^"
        elif(i=="G")|(i=="g"):
            e=e+"`"
        elif(i=="H")|(i=="h"):
            e=e+"."
        elif(i=="I")|(i=="i"):
            e=e+";"
        elif(i=="J")|(i=="j"):
            e=e+"*"
        elif(i=="K")|(i=="k"):
            e=e+"}"
        elif(i=="L")|(i=="l"):
            e=e+"%"
        elif(i=="M")|(i=="m"):
            e=e+"/"
        elif(i=="N")|(i=="n"):
            e=e+"<"
        elif(i=="O")|(i=="o"):
            e=e+"8"
        elif(i=="P")|(i=="p"):
            e=e+"]"
        elif(i=="Q")|(i=="q"):
            e=e+"!"
        elif(i=="R")|(i=="r"):
            e=e+"&"
        elif(i=="S")|(i=="s"):
            e=e+"="
        elif(i=="T")|(i=="t"):
            e=e+"'"
        elif(i=="U")|(i=="u"):
            e=e+"@"
        elif(i=="V")|(i=="v"):
            e=e+"-"
        elif(i=="W")|(i=="w"):
            e=e+"|"
        elif(i=="X")|(i=="x"):
            e=e+"$"
        elif(i=="Y")|(i=="y"):
            e=e+","
        elif(i=="Z")|(i=="z"):
            e=e+"["
        elif(i=="0"):
            e=e+"5"
        elif(i=="1"):
            e=e+"+"
        elif(i=="2"):
            e=e+"#"
        elif(i=="3"):
            e=e+"3"
        elif(i=="4"):
            e=e+"~"
        elif(i=="5"):
            e=e+"0"
        elif(i=="6"):
            e=e+"("
        elif(i=="7"):
            e=e+"?"
        elif(i=="8"):
            e=e+"o"
        elif(i=="9"):
            e=e+">"
        elif(i==":"):
            e=e+"a"
        elif(i==" "):
            e=e+"b"
        elif(i=="_"):
            e=e+"c"
        elif(i=="{"):
            e=e+"d"
        elif(i==")"):
            e=e+"e"
        elif(i=="^"):
            e=e+"f"
        elif(i=="`"):
            e=e+"g"
        elif(i=="."):
            e=e+"h"
        elif(i==";"):
            e=e+"i"
        elif(i=="*"):
            e=e+"j"
        elif(i=="}"):
            e=e+"k"
        elif(i=="%"):
            e=e+"l"
        elif(i=="/"):
            e=e+"m"
        elif(i=="<"):
            e=e+"n"
        elif(i=="]"):
            e=e+"p"
        elif(i=="!"):
            e=e+"q"
        elif(i=="&"):
            e=e+"r"
        elif(i=="="):
            e=e+"s"
        elif(i=="'"):
            e=e+"t"
        elif(i=="@"):
            e=e+"u"
        elif(i=="-"):
            e=e+"v"
        elif(i=="|"):
            e=e+"w"
        elif(i=="$"):
            e=e+"x"
        elif(i==","):
            e=e+"y"
        elif(i=="["):
            e=e+"z"
        elif(i=="+"):
            e=e+"1"
        elif(i=="#"):
            e=e+"2"
        elif(i=="~"):
            e=e+"4"
        elif(i=="("):
            e=e+"6"
        elif(i=="?"):
            e=e+"7"
        elif(i==">"):
            e=e+"9"
        else:
            e=e+i
    text2=Text(scr1,width=80,height=20,wrap=WORD,font=('Time','20','bold'),selectbackground="grey")
    text2.place(x=5,y=40)
    text2.insert(0.0,e)
def save():
    a="ED"
    b=e
    for i in range(0,8):
        a=a+str(rand.randint(0,9))
    completeName = os.path.join("D:\\Ende-coder",a+".txt")
    file1 = open(completeName, "w")
    file1.write(b)
    file1.close()
    info=a+".txt"
    linfo=Label(scr,text=info,bg="silver",fg="black",font=('time','15','bold'))
    linfo.place(x=1130,y=460)
    l=Label(scr,text="SAVED",bg="silver",fg="black",font=('time','20','bold'))
    l.place(x=1130,y=426)
