
from tkinter import *
from backend import Database

database=Database('libros.db')

def get_selected_row(event): #get selected row
    global selected_tuple
    index=list1.curselection()[0] #gets index
    selected_tuple=list1.get(index) #gets tuple
    e1.delete(0,END) #clears entries
    e1.insert(END,selected_tuple[1]) #inserts tuple
    e2.delete(0,END) #clears entries ...
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])    
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
   

def view_command():
    list1.delete(0,END) #clears list
    for row in database.view():
        list1.insert(END,row)  # END means at the end of list
        

def search_command():
    list1.delete(0,END)
    for row in database.search(titulo_text.get(),autor_text.get(),year_text.get(),isbn_text.get()): #search function
        list1.insert(END,row)
        
def add_command():
    database.insert(titulo_text.get(),autor_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(titulo_text.get(),autor_text.get(),year_text.get(),isbn_text.get()))  
    
def delete_command():
    database.delete(selected_tuple[0])
    
def update_command():
    database.update(selected_tuple[0],titulo_text.get(),autor_text.get(),year_text.get(),isbn_text.get())

window=Tk()
window.wm_title("Librería")

# labels
l1=Label(window,text="Titulo")
l1.grid(row=0,column=0)

l2=Label(window,text="Autor")
l2.grid(row=0,column=2)

l3=Label(window,text="Año")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

# texts
titulo_text=StringVar()
e1=Entry(window,textvariable=titulo_text)
e1.grid(row=0,column=1)

autor_text=StringVar()
e2=Entry(window,textvariable=autor_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#list
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

#buttons
b1=Button(window,text="Ver todo",width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Buscar",width=12, command=search_command) 
b2.grid(row=3,column=3)

b3=Button(window,text="Anadir",width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Actualizar",width=12 , command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Borrar",width=12 , command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Cerrar",width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()