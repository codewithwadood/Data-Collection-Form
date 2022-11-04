import csv
from os import spawnve
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def save_i():
    try:
        if name.get()=='':
          messagebox.showwarning('Warning', 'Invalid Name')
        else:
          name_info = name.get()
        try:
            age_info = int(age.get())  
        except:
            messagebox.showwarning('Warning', 'Invalid Age')
        try:
          if len(mobile_number.get())==11 :
            mobile_number_info = int(mobile_number.get()[1:])
          else:
            messagebox.showwarning('Warning', 'Invalid Mobile Number')
        except:
            messagebox.showwarning('Warning', 'Invalid Mobile Number')
        if address.get()=='':
          
            messagebox.showwarning('Warning', 'Invalid Address')
        else:
          address_info = address.get()
        if v.get()==0:
          messagebox.showwarning('Warning', 'Invalid Gender')
        else:

          a = v.get()
          if a== 1:
              gender1= 'Male'
          elif a== 2:
              gender1 ='Female'  

        age_info = str(age_info)
        mobile_number_info = str(mobile_number_info)
        print(name_info, 'saved successfully')
        with open('Wadood Academy Data Collection Form.csv','a',newline='') as wf:
            with open('Wadood Academy Data Collection Form.csv','r',) as rf:
                form=csv.DictWriter(wf,fieldnames=['Name','Age','Mobile number','Gender','Address'])
                if form.fieldnames in  csv.reader(rf):
                    pass
                else:
                    form.writeheader()
                rf.close()
                
                formdict={
                        'Name':name_info.title(),
                        'Age':age_info,
                        'Mobile number':mobile_number_info,
                        'Gender':gender1,
                        'Address':address_info.title()
                    }
                already=False
                with open('Wadood Academy Data Collection Form.csv','r',) as rf1:
                    print(1)
                    for data in  csv.DictReader(rf1):
                        if data==formdict:
                            already=True
                            break
                if already==False:
                    form.writerow(formdict)  
                    name_entry.delete(0, END)
                    age_entry.delete(0, END)
                    mobile_number_entry.delete(0, END)
                    address_entry.delete(0, END)
                    print(formdict)
                    messagebox.showinfo('Congratulate','%s Form Saved Successfully'%name_info)
                elif already==True:
                    messagebox.showwarning('Warning', 'Already exite')      
    except Exception as e:
        print(e)

def about_us():
    messagebox.showinfo('About us', 'Company Name :\n\n\tFsd Software\n\nProgram Writer:\n\n\tAbdul wadood\n')

#def Open_f():
#    file1 = filedialog.askopenfilename()
#    file2 = open(file1,'r')
#    print(file2.read())
screen = Tk() 
screen.geometry('340x345')
screen.title('Data Collection Form')
screen.resizable(0,0)

heading1 = Label(text = 'Data Collection Form ', bg = 'white', fg = 'black', width = '500', height = '2',font = ('Helvetica', 13, 'bold') ).pack()
heading2 = Label(text = 'POWERED BY  \n  Fsd software ',fg = 'black', width = '15', height = '2').place(x = 210, y = 308)

name_text = Label(text = 'Name :',).place(x = 25, y = 50)
age_text = Label(text = 'Age :',).place(x = 25, y = 80)
mobile_number_text = Label(text = 'Mobile No :',).place(x = 25, y = 110)
address_text = Label(text = 'Address :',).place(x = 25, y = 140)
gender_text = Label(text = 'Gender :').place(x =25, y= 170)


name = StringVar()
age = StringVar()
mobile_number = StringVar()
address = StringVar()

name_entry = Entry(textvariable = name, width = 35)
age_entry = Entry(textvariable = age,  width = 35)
mobile_number_entry = Entry(textvariable = mobile_number,  width = 31)
address_entry = Entry(textvariable = address,  width = 35)

name_entry.place(x = 110, y = 50)
age_entry.place(x = 110, y = 80)
mobile_number_entry.place(x = 135, y = 110)
address_entry.place(x = 110, y = 140)

v = IntVar()
Radiobutton(screen, text="Male", variable=v ,value=1).place(x = 115 ,y= 166)
Radiobutton(screen, text="Female", variable=v, value=2).place(x = 170 ,y= 166)

save = Button(text = 'Save Form', width= 10, height = 1, activebackground = 'grey',activeforeground = 'white' ,command = save_i ).place(x = 116, y = 230)
About_us= Button(text = 'About us', width= 10, height = 1,activebackground = 'grey',activeforeground = 'white',command = about_us       ).place(x = 15 ,y = 308)      

#open_f= Button(text = 'Open Form', width= 10, height = 1,activebackground = 'grey',activeforeground = 'white',command = Open_f      )          
#open_f.place(x = 116 ,y = 260)

screen.mainloop()
