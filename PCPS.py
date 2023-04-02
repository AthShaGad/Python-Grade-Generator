from tkinter import *

from PIL import ImageTk, Image
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
root.title("Welcome")

bg="C:\\Users\\ShaileshGadad\\Desktop\\PYTHON PROJECT 1 SEM\\PYTHON PROJECT\\gui 3.jpeg"
mage=Image.open(bg)
mage=mage.resize((900,800), Image.ANTIALIAS)
mage=ImageTk.PhotoImage(mage)
l=Label(root, image=mage)
l.pack()



def createNewWindow():
        newWindow=Toplevel( height=500,width=100)
        newWindow.title("Student Window")
        bg="C:\\Users\\ShaileshGadad\\Desktop\\PYTHON PROJECT 1 SEM\\PYTHON PROJECT\\gui 1.jpg"
        mage=Image.open(bg)
        mage=mage.resize((500,500),Image.ANTIALIAS)
        mage=ImageTk.PhotoImage(mage)
        newWindow=Label(newWindow, image=mage)
        newWindow.pack()
        labelExample =Label(newWindow, text = " If you want to know your GPA",font='Times 15 italic',bg='pink').pack()
        Button(newWindow, text='Click Me', bg='light blue',command=rt6).pack(pady=30)
        Label(newWindow, text='If you want to know the Minimum Marks to be scored to obtain your desired GPA', font='Times 15 italic',bg='pink').pack(pady=30)
        Button(newWindow, text='Click Me', bg='light blue',command=rt5).pack(pady=30)
       

        labelExample.pack()
        
        
        newWindow.mainloop()
        

def createWindow():
        Window=Toplevel(height=500,width=100)
        Window.title("Teacher Window")
        bg="C:\\Users\\ShaileshGadad\\Desktop\\PYTHON PROJECT 1 SEM\\PYTHON PROJECT\\gui 5.jpg"
        mage=Image.open(bg)
        mage=mage.resize((500,500),Image.ANTIALIAS)
        mage=ImageTk.PhotoImage(mage)
        Window=Label(Window, image=mage)
        Window.pack()
        Label(Window, text=" If you want to calculate GPA from an excel sheet",font='Times 15 italic', bg='dark blue',fg='white').pack()
        Button(Window, text='Click Me', bg='light blue',command=f4).pack(pady=30)
        Label(Window, text='If you want to calculate the GPA manually', font='Times 15 italic' ,bg='dark blue',fg='white').pack(pady=30)
        Button(Window, text='Click Me', bg='light blue',command=f2).pack(pady=30)
        Window.mainloop()


        

def f2():
    rt2=Tk()
    rt2.title("GPA Calculation Manually")
    isa_1= Entry(rt2,width=50)
    isa_1.insert(0,"Enter student marks in ISA-1")
    isa_1.pack()
    isa_2=Entry(rt2,width=50)
    isa_2.insert(0,"Enter student marks in ISA-2")
    isa_2.pack()
    ESA=Entry(rt2,width=50)
    ESA.insert(0,"Enter student marks in ESA")
    ESA.pack()
    Assignments=Entry(rt2,width=50)
    Assignments.insert(0,"Enter student in Assignments")
    Assignments.pack()
    

    def fn():
        a=isa_1.get()
        if a.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        isa1_marks=float(a)
        
        b=isa_2.get()
        if b.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        isa2_marks=float(b)
        
        c=ESA.get()
        if c.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        ESA_marks=float(c)
        d=Assignments.get()
        if d.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        Assignment_marks=float(d)
        
        if isa1_marks>60:
            messagebox.showwarning("Warning","Invalid Input")
        elif isa2_marks>45:
            messagebox.showwarning("Warning","Invalid Input")
        elif ESA_marks>100:
            messagebox.showwarning("Warning","Invalid Input")
        elif Assignment_marks>15:
            messagebox.showwarning("Warning","Invalid Input")
        else:
            
            x=((isa1_marks/60)*21)+((isa2_marks/45)*14)+((ESA_marks/100)*50)+((Assignment_marks/15)*15)
            if x>90:
                msg=Label(rt2,text="Student will get a 10 GPA and S Grade").pack()
            elif 90>x>80:
                msg=Label(rt2,text="Student will get a 9 GPA and A Grade").pack()
            elif 80>x>70:
                msg=Label(rt2,text="Student will get a 8 GPA and B Grade").pack()
            elif 70>x>60:
                msg=Label(rt2,text="Student will get a 7 GPA and C Grade").pack()
            elif 60>x>50:
                msg=Label(rt2,text="Student will get a 6 GPA and D Grade").pack()
            elif 50>x>40:
                msg=Label(rt2,text="Student will get a 5 GPA and E Grade").pack()
            elif 40>x>30:
                msg=Label(rt2,text="Student will get a 4 GPA and E- Grade").pack()
            elif x<30:
                msg=Label(rt2, text="Student Fails").pack()
        
    
    bt1=Button(rt2,text="Click Me",command=fn).pack()
    rt2.mainloop()


    
def f4():
    rt4=Tk()
    rt4.title("Excel sheet import")
    

    def getExcel ():
        
        global df
    
        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel (import_file_path)
        root.destroy()
        createWindow.destroy()
        

    
    browseButton_Excel =Button(rt4,text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold')).pack()
    
    Label(rt4,text="Please close this window after choosing file to obtain new window displaying required output.").pack()

    rt4.mainloop()
    percentage=[]
    for i in range(len(df["SRN"])):
        x=(((df['ISA-1'][i])/60)*21)+(((df['ISA-2'][i])/45)*14)+(((df['Assignments'][i])/15)*15)+(((df['ESA'][i])/100)*50)
        percentage.append(x)
    df["Percentage"]=percentage 
    l=[]
    for i in df["Percentage"]:
        if i>=90:
            l.append(10)
        elif 80<=i<90:
            l.append(9)
        elif 70<=i<80:
            l.append(8)
        elif 60<=i<70:
            l.append(7)
        elif 50<=i<60:
            l.append(6)
        elif 40<=i<50:
            l.append(5)
        elif 30<=i<40:
            l.append(4)
        elif i<30:
            l.append("Fail")
    df["GPA"]=l
    l1=[]
    for i in df["Percentage"]:
        if i>=90:
            l1.append('S')
        elif 80<=i<90:
            l1.append('A')
        elif 70<=i<80:
            l1.append('B')
        elif 60<=i<70:
            l1.append('C')
        elif 50<=i<60:
            l1.append('D')
        elif 40<=i<50:
            l1.append('E')
        elif 30<=i<40:
            l1.append('E-')
        elif i<30:
            l1.append("Fail")
    df["Grade"]=l1
    
    
    root1 = Tk() 

    t1 = Text(root1) 
    t1.pack() 
    t1.insert(END,df)

    mainloop() 
   


def rt5():
    root=Tk()
    root.title("Minimum Marks desired GPA")
    Label(root,text="Minimum marks required to pass in ISA-1 is 18").pack()
    Label(root,text="Minimum marks required to pass in ISA-2 is 14").pack()
    Label(root,text="Minimum marks required to pass in ESA is 30").pack()
    Label(root,text="Minimum marks required to pass in Assignments is 5").pack()
    Label(root,text="Negative output indicates that you have already scored more than required to obtain your desired gpa").pack()
    e=Entry(root,width=50)
    e.insert(0,"Enter Desired GPA in a subject (E.g.: 10, 9,..)")
    e.pack()
    isa1=Entry(root,width=50)
    isa1.insert(0,"Enter marks in ISA-1")
    isa1.pack()
    isa2=Entry(root,width=50)
    isa2.insert(0,"Enter marks in ISA-2 (If not conducted enter 0)")
    isa2.pack()
    esa=Entry(root,width=50)
    esa.insert(0,"Enter marks in ESA (If not conducted enter 0)")
    esa.pack()
    assg=Entry(root,width=50)
    assg.insert(0,"Enter marks in Assignments (If not known enter 0)")
    assg.pack()

    def f():
        a=e.get()
        if a.isdigit()==True:
            pass
        
        else:
            messagebox.showwarning("Warning","Invalid Input")
        ex=int(a)
        b=isa1.get()
        if b.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        isa1x=int(b)
        c=isa2.get()
        if c.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        isa2x=int(c)
        d=esa.get()
        if d.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        esax=int(d)
        f=assg.get()
        if f.isdigit()==True:
            pass
        else:
            messagebox.showwarning("Warning","Invalid Input")
        assgx=int(f)
        if ex>10:
            Label(root,text="At least one of your inputs is wrong. Please check and try again.").pack()

        elif isa1x>60:
            Label(root,text="At least one of your inputs is wrong. Please check and try again.").pack()
        
        elif isa2x>45:
            Label(root,text="At least one of your inputs is wrong. Please check and try again.").pack()
        elif esax>100:
            Label(root,text="At least one of your inputs is wrong. Please check and try again.").pack()
        elif assgx>15:
            Label(root,text="At least one of your inputs is wrong. Please check and try again.").pack()
        else:
            total=isa1x+isa2x+esax+assgx
            if ex==10:
                a=0.9*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            elif ex==9:
                a=0.8*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            elif ex==8:
                a=0.7*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            elif ex==7:
                a=0.6*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            elif ex==6:
                a=0.5*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            elif ex==5:
                a=0.4*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            elif ex==4:
                a=0.3*220-total
                Label(root,text="You need to score "+str(a)+" marks more in rest of the tests put together").pack()
            
        
    bt=Button(root, text="Calculate",command=f).pack()
    root.mainloop()
    


def rt6():
    df=pd.read_excel(r"C:\Users\ShaileshGadad\Desktop\PYTHON PROJECT 1 SEM\PYTHON PROJECT\Experimental.xlsx")

    percentage_math=[]
    for i in range(len(df["SRN"])):
            x1=(((df['ISA1 Math'][i])/60)*21)+(((df['ISA2 Math'][i])/45)*14)+(((df['Assignments Math'][i])/15)*15)+(((df['ESA Math'][i])/100)*50)
            percentage_math.append(x1)
    df["Percentage Math"]=percentage_math
    l1=[]
    for i in df["Percentage Math"]:
            if i>=90:
                l1.append(10)
            elif 80<=i<90:
                l1.append(9)
            elif 70<=i<80:
                l1.append(8)
            elif 60<=i<70:
                l1.append(7)
            elif 50<=i<60:
                l1.append(6)
            elif 40<=i<50:
                l1.append(5)
            elif 30<=i<40:
                l1.append(4)
            elif i<30:
                l1.append("Fail")
    df["GPA Math"]=l1

    percentage_PCPS=[]
    for i in range(len(df["SRN"])):
            x2=(((df['ISA1 PCPS'][i])/60)*21)+(((df['ISA2 PCPS'][i])/45)*14)+(((df['Assignments PCPS'][i])/15)*15)+(((df['ESA PCPS'][i])/100)*50)
            percentage_PCPS.append(x2)
    df["Percentage PCPS"]=percentage_PCPS 
    l2=[]
    for i in df["Percentage PCPS"]:
            if i>=90:
                l2.append(10)
            elif 80<=i<90:
                l2.append(9)
            elif 70<=i<80:
                l2.append(8)
            elif 60<=i<70:
                l2.append(7)
            elif 50<=i<60:
                l2.append(6)
            elif 40<=i<50:
                l2.append(5)
            elif 30<=i<40:
                l2.append(4)
            elif i<30:
                l2.append("Fail")
    df["GPA PCPS"]=l2

    percentage_Civil=[]
    for i in range(len(df["SRN"])):
            x3=(((df['ISA1 Civil'][i])/60)*21)+(((df['ISA2 Civil'][i])/45)*14)+(((df['Assignments Civil'][i])/15)*15)+(((df['ESA Civil'][i])/100)*50)
            percentage_Civil.append(x3)
    df["Percentage Civil"]=percentage_Civil 
    l3=[]
    for i in df["Percentage Civil"]:
            if i>=90:
                l3.append(10)
            elif 80<=i<90:
                l3.append(9)
            elif 70<=i<80:
                l3.append(8)
            elif 60<=i<70:
                l3.append(7)
            elif 50<=i<60:
                l3.append(6)
            elif 40<=i<50:
                l3.append(5)
            elif 30<=i<40:
                l3.append(4)
            elif i<30:
                l3.append("Fail")
    df["GPA Civil"]=l3

    percentage_Chemistry=[]
    for i in range(len(df["SRN"])):
            x4=(((df['ISA1 Chemistry'][i])/60)*21)+(((df['ISA2 Chemistry'][i])/45)*14)+(((df['Assignments Chemistry'][i])/15)*15)+(((df['ESA Chemistry'][i])/100)*50)
            percentage_Chemistry.append(x4)
    df["Percentage Chemistry"]=percentage_Chemistry 
    l4=[]
    for i in df["Percentage Chemistry"]:
            if i>=90:
                l4.append(10)
            elif 80<=i<90:
                l4.append(9)
            elif 70<=i<80:
                l4.append(8)
            elif 60<=i<70:
                l4.append(7)
            elif 50<=i<60:
                l4.append(6)
            elif 40<=i<50:
                l4.append(5)
            elif 30<=i<40:
                l4.append(4)
            elif i<30:
                l4.append("Fail")
    df["GPA Chemistry"]=l4

    percentage_Electronics=[]
    for i in range(len(df["SRN"])):
            x5=(((df['ISA1 Electronics'][i])/60)*21)+(((df['ISA2 Electronics'][i])/45)*14)+(((df['Assignments Electronics'][i])/15)*15)+(((df['ESA Electronics'][i])/100)*50)
            percentage_Electronics.append(x5)
    df["Percentage Electronics"]=percentage_Electronics
    l5=[]
    for i in df["Percentage Electronics"]:
            if i>=90:
                l5.append(10)
            elif 80<=i<90:
                l5.append(9)
            elif 70<=i<80:
                l5.append(8)
            elif 60<=i<70:
                l5.append(7)
            elif 50<=i<60:
                l5.append(6)
            elif 40<=i<50:
                l5.append(5)
            elif 30<=i<40:
                l5.append(4)
            elif i<30:
                l5.append("Fail")
    df["GPA Electronics"]=l5

    l_GPA=[]
    for i in range(len(df["SRN"])):
        x=(df["GPA Math"][i]+df["GPA PCPS"][i]+df["GPA Civil"][i]+df["GPA Electronics"][i]+df["GPA Chemistry"][i])/5
        l_GPA.append(x)
    df["SGPA"]=l_GPA

    root=Tk()
    root.title("Student SRN GPA")
    root.geometry("200x200")
    e=Entry(root)
    e.insert(0,"Enter your SRN")
    e.pack()
    listxyz=[]
    for i in df["SRN"]:
        listxyz.append(i)


    def f():
        a=e.get()
        #a=str(a)
        a=a.upper()
    
        if a not in listxyz:
            #msg=Label(root,text="SRN Not found").pack()  
            messagebox.showwarning("Warning","Invalid SRN")
        else:
            for i in range(len(df["SRN"])):
                if a==df["SRN"][i]:
                    message=Label(root, text="Your SGPA is "+str(df["SGPA"][i])).pack()
                    
                else:
                    continue
                
    Button(root,text="Click Here",command=f).pack()
    root.mainloop()

    

Label(root, text='Hello User', font='Times 20 bold',bg='lightsteelblue').place(x=550,y=100)
Label(root, text='Welcome to the Student Grade Generator Software', font='Times 20 bold',bg='lightsteelblue').place(x=340,y=140)
Label(root, text='If you are a student', font='Times 15 italic', bg='light green').place(x=540,y=200)
Button(root, text='Click Me', font='Times 15 italic',bg='yellow',command=createNewWindow).place(x=560,y=230)
Label(root, text='If you are a teacher', font='Times 15 italic',bg='light green').place(x=540,y=290)
Button(root, text='Click Me', font='Times 15 italic' , bg='green', command=createWindow).place(x=560,y=320)

root.mainloop()
