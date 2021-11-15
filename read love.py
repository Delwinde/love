from tkinter import *
def app():
	boy = bname.get()
	girl=gname.get()
	k =[]
	l = []
#print("ENTER THE NAME OF THE BOY")
#n = input()
#print("ENTER THE NAME OF THE GIRL")
#m = input()
	for i in boy:
		if i not in girl:
			l.append(i)
		
	for j in girl:
		if j not in boy:
			k.append(j)
	a=len(k) + len(l)

	if a== 1 or a== 7 or a==13:
		message.set("are friends")
	elif a == 2 or a==8 or a ==14:
		message.set("are Lovers")
	elif a == 3 or a ==9 or a ==15:
		message.set("are Afection")
	elif a== 4 or a == 10 or a ==16:
		message.set("Marriage")
	elif a == 5 or a ==11 or a ==17:
		message.set("are Enemies")
	elif a == 6 or a==12 or a==18:
		message.set("Hiding Secret")
	else:
		message.set("No relationship")
		
root=Tk()
global message
global bname
global gname
	
	
message = StringVar()
bname=StringVar()
gname=StringVar()
Label(root,width="300", text="Please enter details below", bg="orange",fg="white").pack()
Label(root, text="").pack()
Label(root, text="Enter Boy name * ").pack()
Entry(root, textvariable=bname).pack()
Label(root, text="Enter Girl name* ").pack()
Entry(root, textvariable=gname).pack()
Label(root, text="",textvariable=message).pack()
Button(root, text="Check", width=10, height=1, bg="orange",command=app).pack()
root.mainloop()
#calling function L
#tes()