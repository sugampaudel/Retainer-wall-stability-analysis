# Retaining_Wall.py
# Developed by: Sugam Paudel
# Description: Retaining Wall Stability and Design Analysis Tool
# Year: 2025




from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import math
from PIL import Image, ImageTk, ImageGrab
import sys
import os
import io


base_dir = os.path.dirname(os.path.abspath(__file__))

def OK():
    global soil_layer_n
    soil_layer_n = int(soil_layer.get())
    window.destroy()
    if not soil_layer_n:
        window.quit()
    return soil_layer_n

def get_values():
    global layers
    global water_table 
    global gamma_conc
    global gamma_water
    global allowable_capacity
    global delta
    global a,b,c,d,e,f,g,l,h,q,alpha,beta

    a = float(entries['a'].get() or 0)
    b = float(entries['b'].get() or 0)
    c = float(entries['c'].get() or 0)
    d = float(entries['d'].get() or 0)
    e = float(entries['e'].get() or 0)
    f = float(entries['f'].get() or 0)
    g = float(entries['g'].get() or 0)
    q = float(entries['q'].get() or 0)
    h = float(entries['h'].get() or 0)
    
    alpha = float(entries['α'].get() or math.atan(h/(f+g))*180/math.pi)
    if f == 0:
        beta = 90
    else:
        beta  = float(entries['β'].get() or math.atan(a/f)*180/math.pi)


    if "i" in entries:
        layers[0][1] = float(entries["h"].get() or 0) + float(entries["i"].get() or 0)
    if "j" in entries:
        layers[1][1] = float(entries["j"].get() or 0)
    if "k" in entries:
        layers[2][1] = float(entries["k"].get() or 0)
    if "l" in entries:
        layers[3][1] = float(entries["l"].get() or 0)

    for i, ent in enumerate(gamma):
        value = float(ent.get() or 0)
        layers[i][0] = value

    for i, ent in enumerate(internal_friction):
        value = float(ent.get() or 0)
        layers[i][2] = value

    for i, ent in enumerate(cohesion):
        value = float(ent.get() or 0)
        layers[i][3] = value

    if water_table_value.get().lower()=="n":
        water_table = None
    else:
        try:
            water_table = float(water_table_value.get())
        except ValueError:
            water_table = None

    gamma_conc = float(gamma_conc_value.get())
    gamma_water = float(gamma_water_value.get())
    allowable_capacity = float(allowable_value.get())
    delta = float(delta_value.get() or layers[soil_layer_n-1][2])

    wall_window.destroy()
    wall_window.quit()



def rf(value,decimals=2):
    return round(float(value),decimals)



def close_application():
    report.destroy()
    report.quit()


    


window = Tk()
window.geometry("500x200")
window.title("Retainer")
window.config(bg="#334443")
label = Label(window, text = "Number of Soil Layers :", 
              font = ('Times New Roman',20),
              fg = "#FFFEFB",
              bg="#334443"
              )
label.place(x=30, y=60)
label = Label(window, text = "Queries: 079bce174.sugam@pcampus.edu.np", 
              font = ('Times New Roman',8),
              fg = "#FFFEFB",
              bg="#334443"
              )
label.place(x=280, y=180)
# label = Label(window, text = "version: 1.0.0.0", 
#               font = ('Times New Roman',8),
#               fg = "#FFFEFB",
#               bg="#334443"
#               )
# label.place(x=25, y=180)
soil_layer = Entry(justify="center", font=("Times New Roman",15) )
soil_layer.config(width=10)
soil_layer.insert(0,1)
soil_layer.place(x=300,y=65)
soil_layer.focus()
button = Button(window,text= "OK",font=("Times New Roman",15),command=OK)
window.bind("<Return>", lambda event: OK())
button.place(x=250,y=125)
window.mainloop()



wall_window = Tk()
wall_window.geometry("1400x700")
wall_window.title("Retainer")

wall_window.config(bg="#334443")
wall_window.focus_force()
wall = Canvas(wall_window,height=600,width=600,bg="#334443",highlightthickness=0,bd=0)
wall.create_line(150,400,150,450, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(150,400,200,400, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(200,400,250,150, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(250,150,300,150, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(300,150,350,400, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(350,400,500,400, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(350,400,500,400, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(500,400,500,450, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(500,450,150,450, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(500,450,150,450, width=1, fill="#FFFEFB" ) #Wall Line
wall.create_line(300,150,500,100, width=1, fill="#FFFEFB" ) #Soil Top Line
wall.create_line(500,400,500,100, width=1, fill="#8F8F8F" ) #Soil Boundary Line
wall.create_line(250,150,250,400, width=1, fill="#FFFEFB",dash=(2,1) ) #Inside Lines
wall.create_line(300,150,300,400, width=1, fill="#FFFEFB",dash=(2,1) ) #Inside Lines
wall.create_line(200,400,350,400, width=1, fill="#FFFEFB",dash=(2,1) ) #Inside Lines
wall.create_line(300,150,500,150, width=1, fill="#FFFEFB",dash=(2,1) ) #Inside Lines
wall.create_line(125,450,125,150, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(120,450,130,450, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(120,400,130,400, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(120,150,130,150, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(150,475,500,475, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(150,470,150,480, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(200,470,200,480, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(250,470,250,480, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(300,470,300,480, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(350,470,350,480, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(500,470,500,480, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(525,100,525,400, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(520,100,530,100, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(520,150,530,150, width=1, fill="#8F8F8F" ) #Dimension Line
wall.create_line(520,400,530,400, width=1, fill="#8F8F8F" ) #Dimension Line

#surcharge
wall.create_line(300,100,500,50, width=1, fill="#8F8F8F" )
for x in range(300,540,40):
    wall.create_line(x,100-(x-300)*(50/200),x,150-(x-300)*(50/200),arrow=LAST,fill="#8F8F8F")
    

a_1=500.0
a_2=250.0/soil_layer_n
a_3=(50.0/250)*a_2
a_5=350
a_6=400
a_7=a_6-250.0/soil_layer_n
a_8=150+a_2/2

for i in range (soil_layer_n):
    
    wall.create_line(a_1,150.0+a_2,300.0+a_3,150.0+a_2, width=1,fill = "#FFFEFB")
    wall.create_line(520,150.0+a_2,530,150.0+a_2, width=1,fill = "#8F8F8F")
    # wall.create_line(a_5,a_6,a_5,a_7, width=1,fill = "#FFFEFB",dash=(2,1))
    wall.create_oval(410,a_8-15,440,a_8+15,outline="#8F8F8F")
    subscript = chr(0x2080 + (i+6))  # makes subscript
    text = f"W{subscript}"
    wall.create_text(425,a_8,text=text,font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
    wall.create_text(535,a_8,text=chr(105+i),font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
    a_5=a_5-50.0/soil_layer_n
    a_6=a_6-250.0/soil_layer_n
    a_7=a_6-250.0/soil_layer_n
    a_8=a_8+250.0/soil_layer_n
    a_2 = a_2 + 250.0/soil_layer_n
    a_3 = (50.0/250)*a_2


wall.create_arc(330,380,370,420,extent = 78.69, style = "arc",outline="#FFFEFB",start = 101.31)
wall.create_arc(245,100,345,200,extent = 14.036, style = "arc",outline="#FFFEFB")

#For Texts Label
wall.create_text(115,275,text="a",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(115,425,text="b",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(175,485,text="c",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(225,485,text="d",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(275,485,text="e",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(325,485,text="f",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(425,485,text="g",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(535,125,text="h",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(400,50,text="q",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(365,142,text="α",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(320,385,text="β",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")

#For Weight Label
wall.create_oval(310,410,340,440,outline="#8F8F8F")
wall.create_oval(215,345,245,375,outline="#8F8F8F")
wall.create_oval(305,345,335,375,outline="#8F8F8F")
wall.create_oval(260,260,290,290,outline="#8F8F8F")
wall.create_oval(460,115,490,145,outline="#8F8F8F")

#For Weight Text Label
wall.create_text(230,360,text="W\u2081",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(275,275,text="W\u2082",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(320,360,text="W\u2083",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(325,425,text="W\u2084",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
wall.create_text(475,130,text="W\u2085",font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")

wall.place(x=-50,y=75)


title_label = Label(wall_window,text="Enter Values: ",font=("Times New Roman",30),bg="#334443",fg="#FFFEFB")
title_label.place(x=850,y=50)

input_frame = Frame(wall_window,bg="#334443")
input_frame.place(x=650,y=150)

variables = ['a','b','c','d','e','f','g']

entries = {}

layers = np.zeros((soil_layer_n,4))


for i, var in enumerate(variables):
    lbl=Label(input_frame,text=var+"    :",font = ("Times New Roman",12),bg="#334443",fg="#FFFEFB")
    lbl.grid(row=i,column=0,padx=10,pady=5)

    ent = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
    ent.grid(row=i, column = 1, padx=10,pady=5)
    entries[var] = ent

    globals()[var] = ent



variables_2 = ['q','α','β']


for i, var in enumerate(variables_2):
    lbl=Label(input_frame,text=var+"    :",font = ("Times New Roman",12),bg="#334443",fg="#FFFEFB")
    lbl.grid(row=i,column=2,padx=10,pady=5)

    ent = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
    ent.grid(row=i, column = 3, padx=10,pady=5)
    entries[var] = ent

    globals()[var] = ent


variables_3 = ['h','i','j','k','l']


for i, var in enumerate(variables_3[:soil_layer_n+1]):
    lbl=Label(input_frame,text=var+"    :",font = ("Times New Roman",12),bg="#334443",fg="#FFFEFB")
    lbl.grid(row=i,column=4,padx=10,pady=5)

    ent = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
    ent.grid(row=i, column = 5, padx=10,pady=5)
    entries[var] = ent

#Unit weight for concrete
lbl = Label(input_frame,text = "γc  :",font=("Times New Roman",12),bg="#334443",fg="#FFFEFB")
lbl.grid(row=3,column=2,padx=10,pady=5)
conc = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
conc.insert(0,24)
conc.grid(row=3,column=3,padx=10,pady=5)
gamma_conc_value=conc

#Unit weight for Water
lbl = Label(input_frame,text = "γw  :",font=("Times New Roman",12),bg="#334443",fg="#FFFEFB")
lbl.grid(row=4,column=2,padx=10,pady=5)
water = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
water.insert(0,10)
water.grid(row=4,column=3,padx=10,pady=5)
gamma_water_value=water

lbl = Label(input_frame,text = "𝛿  :",font=("Times New Roman",12),bg="#334443",fg="#FFFEFB")
lbl.grid(row=5,column=2,padx=10,pady=5)
delt = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
delt.grid(row=5,column=3,padx=10,pady=5)
delta_value=delt

lbl = Label(input_frame,text = "qₙₐ  :",font=("Times New Roman",12),bg="#334443",fg="#FFFEFB")
lbl.grid(row=6,column=2,padx=10,pady=5)
allowable = Entry(input_frame,font=("Times New Roman",12),width=15,justify="center")
allowable.insert(0,600)
allowable.grid(row=6,column=3,padx=10,pady=5)
allowable_value=allowable



input_frame_2 = Frame(wall_window,bg="#334443")
input_frame_2.place(x=650,y=420)
gamma = []
internal_friction = []
cohesion = []

for i in range (soil_layer_n):
    subscript = chr(0x2080 + (i+1))  # makes subscript
    text = f"γ{subscript}   :"
    lbl=Label(input_frame_2,text=text,font = ("Times New Roman",12),bg="#334443",fg="#FFFEFB")
    lbl.grid(row=i+12,column=0,padx=10,pady=5)

    ent = Entry(input_frame_2,font=("Times New Roman",12),width=15,justify="center")
    ent.grid(row=i+12, column = 1, padx=10,pady=5)
    gamma.append(ent)

for i in range (soil_layer_n):
    subscript = chr(0x2080 + (i+1))  # makes subscript
    text = f"φ{subscript}   :"
    lbl=Label(input_frame_2,text=text,font = ("Times New Roman",12),bg="#334443",fg="#FFFEFB")
    lbl.grid(row=i+12,column=2,padx=10,pady=5)

    ent = Entry(input_frame_2,font=("Times New Roman",12),width=15,justify="center")
    ent.grid(row=i+12, column = 3, padx=10,pady=5)
    internal_friction.append(ent)

for i in range (soil_layer_n):
    subscript = chr(0x2080 + (i+1))  # makes subscript
    text = f"C{subscript}   :"
    lbl=Label(input_frame_2,text=text,font = ("Times New Roman",12),bg="#334443",fg="#FFFEFB")
    lbl.grid(row=i+12,column=4,padx=10,pady=5)

    ent = Entry(input_frame_2,font=("Times New Roman",12),width=15,justify="center")
    ent.grid(row=i+12, column = 5, padx=10,pady=5)
    cohesion.append(ent)

lbl = Label(input_frame_2,text="Position of Water Table: (n if not present) :",font=("Times New Roman",12),bg="#334443",fg="#FFFEFB",justify="center")
lbl.grid(row=soil_layer_n+12,column=0,padx=10,pady=25,columnspan=3)
value = Entry(input_frame_2,font=("Times New Roman",12),width=12,justify="center")
value.grid(row=soil_layer_n+12,column=3,padx=10,pady=25)
water_table_value=value

data_entry_button = Button(wall_window,text="Generate Report",font=("Times New Roman",16),command=get_values)


data_entry_button.place(x=650,y=600)
wall_window.bind("<Return>",lambda event: get_values())

wall_window.mainloop()

report = Tk()
report.geometry("1200x750")
report.title("Retainer (Final Report)")
report.focus_force()

canvas = Canvas(report,width=1150,height=750,bg="#334443")
canvas.pack(side=LEFT,fill=BOTH,expand=True)

scrollbar = Scrollbar(report,orient="vertical",command=canvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)


scrollable_frame = Frame(canvas,bg="#334443",width=1200,height=2200)
frame_id = canvas.create_window((0,0),window = scrollable_frame,anchor="nw")

reporttext = Label(scrollable_frame,text="Report On Stability",font = ("Times New Roman",40),fg="#FFFEFB",bg="#334443",anchor="center")
reporttext.place(relx=0.5,y=30,anchor="center")
reporttext.lift()
canvas.create_window((0,0),window=scrollable_frame,anchor="nw")

def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>",update_scrollregion)

def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int(event.delta/120),"units")

canvas.bind_all("<MouseWheel>",on_mouse_wheel)



eta = rf((45+alpha/2)-layers[0][2]/2-math.asin(math.sin(math.radians(alpha))/math.sin(math.radians(layers[0][2])))*180/math.pi)
actual_angle = rf(math.asin((f+g)/(a+b))*180/math.pi)

Ka = np.zeros(soil_layer_n)
rankine = False
columb = False
if delta>0:
    delta = delta
else:
    delta = (2/3)*layers[soil_layer_n-1][2]

if q>0 or (water_table is not None and water_table>=0 and water_table<=(a+b+h)) or soil_layer_n>1 or eta < actual_angle:
    for i in range(soil_layer_n):
        Ka[i] = math.cos(math.radians(alpha))*(math.cos(math.radians(alpha))-math.sqrt(math.pow(math.cos(math.radians(alpha)),2)-math.pow(math.cos(math.radians(layers[i][2])),2)))/(math.cos(math.radians(alpha))+math.sqrt(math.pow(math.cos(math.radians(alpha)),2)-math.pow(math.cos(math.radians(layers[i][2])),2)))
        rankine = True
    if q>0 and (water_table is not None and water_table>=0 and water_table<=(a+b+h))>0 and (soil_layer_n>1) :
        lbl_text="Since there is Surcharge, presence of water table and more than one layer of soil, Apply Rankine's method."
            
    elif (water_table is not None and water_table>=0 and water_table<=(a+b+h))>0 and q>0:
        lbl_text = "Since there is Presence of Water Table and surcharge, Apply Rankine' method."
        
    elif (soil_layer_n>1) and q>0:
        lbl_text = "Since there are more than one soil layer and presence of surcharge, Apply Rankine's method"
        
    elif (soil_layer_n>1) and (water_table is not None and water_table>=0 and water_table<=(a+b+h))>0:
        lbl_text = "Since there are more than one soil layer and presence of water table, Apply Rankine's method"
        
    elif soil_layer_n>1:
        lbl_text = "Since there is more than one layer of soil, Apply Rankine's method"
        
    elif q>0:
        lbl_text = "Since there is surcharge, Apply Rankine's method"
        
    elif (water_table is not None and water_table>=0 and water_table<=(a+b+h))>0:
        lbl_text = "Since there is presence of water table, Apply Rankine's method"
        
    else:
        lbl_text = f"Angle from Heel to top of Wall = {rf(math.asin((f+g)/(a+b))*180/math.pi)}\nη = (45+α/2)-φ/2-asin(sinα/sinφ) = {rf((45+alpha/2)-layers[0][2]/2-math.asin(math.sin(math.radians(alpha))/math.sin(math.radians(layers[0][2])))*180/math.pi)}\nSince {actual_angle}>{eta} i.e. the shear zone doesnot intersect the stem. Therefore apply Rankine's method."
        
    lbl = Label(scrollable_frame,text=lbl_text,font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",anchor="center")
    lbl.place(relx=0.5,y=725,anchor="center")

            
else:
    Ka[0] = (
        math.sin(math.radians(beta + layers[0][2])) ** 2) / (
        (math.sin(math.radians(beta)) ** 2)
        * (math.sin(math.radians(beta - delta)))
        * ((1 + math.sqrt(
            (math.sin(math.radians(layers[0][2] + delta))
            * math.sin(math.radians(layers[0][2] - alpha)))
            / (math.sin(math.radians(beta - delta))
            * math.sin(math.radians(beta + alpha)))
        )) ** 2)
    )
    columb = True
    lbl_text = f"Angle from Heel to top of Wall = {rf(math.asin((f+g)/(a+b))*180/math.pi)}\nη = (45+α/2)-φ/2-asin(sinα/sinφ) = {rf((45+alpha/2)-layers[0][2]/2-math.asin(math.sin(math.radians(alpha))/math.sin(math.radians(layers[0][2])))*180/math.pi)}\nSince {actual_angle}<{eta} i.e the shear zone intersects the stem. Therefore apply Columb's method."
        
    lbl = Label(scrollable_frame,text=lbl_text,font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",anchor="center")
    lbl.place(relx=0.5,y=725,anchor="center")

diagram = Canvas(scrollable_frame,width=750,height=560,bg="#334443",highlightthickness=1,bd=0)

diagram.create_line(50,400,50,400+b*50,width=1, fill="#FFFEFB")
diagram.create_line(50+c*50,400,50+(c+d+e+f)*50,400, width=1, fill="#FFFEFB",dash=(2,1))
diagram.create_line(50+(c+d)*50,400,50+(c+d)*50,400-a*50, width=1, fill="#FFFEFB",dash=(2,1))
diagram.create_line(50+(c+d+e)*50,400,50+(c+d+e)*50,400-a*50, width=1, fill="#FFFEFB",dash=(2,1))
diagram.create_line(50+(c+d+e)*50,400-a*50,50+(c+d+e+f+g)*50,400-a*50, width=1, fill="#FFFEFB",dash=(2,1))
diagram.create_line(50+(c+d+e+f+g)*50,400-(a+h)*50,50+(c+d+e+f+g)*50,400, width=1, fill="#8F8F8F")
diagram.create_line(30,400-(a)*50,30,400, width=1, fill="#8F8F8F")
diagram.create_line(30,400+(b)*50,30,400, width=1, fill="#8F8F8F")
diagram.create_line(50,400+(b)*50+20,50+(c+d+e+f+g)*50,400+b*50+20, width=1, fill="#8F8F8F")
diagram.create_line(50+(c+d+e+f+g)*50+20,400-(a+h)*50,50+(c+d+e+f+g)*50+20,400, width=1, fill="#8F8F8F")
diagram.create_line(25,400-a*50,35,400-a*50, width=1, fill="#8F8F8F")
diagram.create_line(25,400,35,400, width=1, fill="#8F8F8F")
diagram.create_line(25,400+b*50,35,400+b*50, width=1, fill="#8F8F8F")
diagram.create_line(50,400+b*50+15,50,400+b*50+25, width=1, fill="#8F8F8F")
diagram.create_line(50+c*50,400+b*50+15,50+c*50,400+b*50+25, width=1, fill="#8F8F8F")
diagram.create_line(50+(c+d)*50,400+b*50+15,50+(c+d)*50,400+b*50+25, width=1, fill="#8F8F8F")
diagram.create_line(50+(c+d+e)*50,400+b*50+15,50+(c+d+e)*50,400+b*50+25, width=1, fill="#8F8F8F")
diagram.create_line(50+(c+d+e+f)*50,400+b*50+15,50+(c+d+e+f)*50,400+b*50+25, width=1, fill="#8F8F8F")
diagram.create_line(50+(c+d+e+f+g)*50,400+b*50+15,50+(c+d+e+f+g)*50,400+b*50+25, width=1, fill="#8F8F8F")
if d>0:
    diagram.create_text(50+(c+d*2/3)*50,400-(a/3)*50,text=f"(1)", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
if e>0:
    diagram.create_text(50+(c+d+e/2)*50,400-(a/2)*50,text=f"(2)", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
if f>0:
    diagram.create_text(50+(c+d+e+f/3)*50,400-(a/3)*50,text=f"(3)", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
if h>0:
    diagram.create_text(50+(c+d+e+(f+g)*2/3)*50,400-(a+h/3)*50,text=f"(5)", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
    diagram.create_text(50,460+(b)*50,text=f"α = {rf(alpha)}", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")

diagram.create_text(50,485+b*50,text=f"β = {rf(beta)}", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
diagram.create_text(50+(c+d+e+f+g)*25,400+(b)*25,text=f"(4)", font=("Times New Roman",12,"italic"),fill="#FFFEFB",anchor="center")
diagram.create_text(15,400-a*25,text=f"{a}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center")
diagram.create_text(15,400+b*25,text=f"{b}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center")
diagram.create_line(50,400+b*50,50+(c+d+e+f+g)*50,400+b*50,width=1, fill="#FFFEFB")
if c>0:
    diagram.create_text(50+(c)*25,400+b*50+35,text=f"{c}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center",angle=90)
if d>0:
    diagram.create_text(50+(c+d/2)*50,400+b*50+35,text=f"{d}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center",angle=90)
if e>0:
    diagram.create_text(50+(c+d+e/2)*50,400+b*50+35,text=f"{e}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center",angle=90)
if f>0:
    diagram.create_text(50+(c+d+e+f/2)*50,400+b*50+35,text=f"{f}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center",angle=90)
if g>0:
    diagram.create_text(50+(c+d+e+f+g/2)*50,400+b*50+35,text=f"{g}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center",angle=90)
if h>0:
    diagram.create_line(65+(c+d+e+f+g)*50,400-(a+h)*50,75+(c+d+e+f+g)*50,400-(a+h)*50, width=1, fill="#8F8F8F")
    diagram.create_text(85+(c+d+e+f+g)*50,400-(a+h/2)*50,text=f"{h}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center")

diagram.create_line(65+(c+d+e+f+g)*50,400-(a)*50,75+(c+d+e+f+g)*50,400-(a)*50, width=1, fill="#8F8F8F")
diagram.create_line(50+(c+d+e+f+g)*50,400+b*50,50+(c+d+e+f+g)*50,400,width=1, fill="#FFFEFB")
diagram.create_line(50+(c+d+e+f)*50,400,50+(c+d+e+f+g)*50,400,width=1, fill="#FFFEFB")
diagram.create_line(50+(c+d+e)*50,400-a*50,50+(c+d+e+f)*50,400,width=1, fill="#FFFEFB")
diagram.create_line(50+(c+d+e)*50,400-a*50,50+(c+d)*50,400-a*50,width=1, fill="#FFFEFB")
diagram.create_line(50+(c)*50,400,50+(c+d)*50,400-a*50,width=1, fill="#FFFEFB")
diagram.create_line(50+(c)*50,400,50,400,width=1, fill="#FFFEFB")
diagram.create_line(50+(c+d+e)*50,400-a*50,50+(c+d+e+f+g)*50,400-(a+h)*50,width=1, fill="#FFFEFB")

layers[0][1]=layers[0][1]-h
d1 = 50+(c+d+e)*50
d2 = 400-(a)*50
d3 = 50+(c+d+e+f+g)*50
ini = layers[0][1]
for i in range(soil_layer_n):
    d1 = 50+(c+d+e)*50+(f/a)*ini*50
    d2 = d2+layers[i][1]*50
    diagram.create_line(d1,d2,d3,d2,width =1,fill="#FFFEFB",dash=(2,1))
    diagram.create_line(65+(c+d+e+f+g)*50,d2,75+(c+d+e+f+g)*50,d2, width=1, fill="#8F8F8F")
    diagram.create_text(85+(c+d+e+f+g)*50,d2-0.5*layers[i][1]*50,text=f"{layers[i][1]}", font=("Times New Roman",10,"italic"),fill="#FFFEFB",anchor="center")
    if rankine:
        diagram.create_text((d1+d3)/2,d2-layers[i][1]*25,text=f"({i+6})", font=("Times New Roman",12,"italic"),fill="#FFFEFB")
    if i+1<soil_layer_n:
        ini=ini+layers[i+1][1]
layers[0][1]=layers[0][1]+h



#surcharge
if q>0:
    diagram.create_line(50+(c+d+e)*50,400-(a)*50-25,50+(c+d+e+f+g)*50,400-(a+h)*50-25, width=1, fill="#8F8F8F" )
    diagram.create_text(50+(c+d+e+(f+g)/2)*50,355-(a+h/2)*50,text=f"{q} KN/ m²", font=("Times New Roman",12,"italic"),fill="#FFFEFB")
    for i in range(int((50+(c+d+e+f+g)*50 - (50+(c+d+e)*50)) / 40) +1):
        diagram.create_line(x := 50+(c+d+e)*50 + i*40, y_on_line := 400-(a)*50-25 + ((400-(a+h)*50-25)-(400-(a)*50-25))/((50+(c+d+e+f+g)*50)-(50+(c+d+e)*50))*(x-(50+(c+d+e)*50)), x, y_on_line+25, arrow='last', fill="#8F8F8F", width=1)
    diagram.create_line(50+(c+d+e+f+g)*50,400-(a+h)*50-25,50+(c+d+e+f+g)*50,400-(a+h)*50,arrow='last', fill="#8F8F8F", width=1)

diagram.scale("all",0,500,1.25,1.25)
diagram.place(relx=0.5,y=400,anchor="center")



if not water_table:
    coordinates = np.zeros((2*soil_layer_n,2))
else:
    coordinates = np.zeros((2*soil_layer_n+1,2))


soil = 0
height = 0
depth = 0
r = 0
water_done = False
layers[soil_layer_n-1][1] = layers[soil_layer_n-1][1]+b
for i in range(soil_layer_n):
    for j in range (2):
        depth = depth + height
        if(water_table is not None and depth>water_table):
            pw = gamma_water*(depth-water_table)
        else:
            pw = 0
        if not water_done and (water_table is not None and depth>=water_table):
            soil_1=soil+layers[i][0]*(water_table-(depth-height))
            stress = q*Ka[i]-2*layers[i][3]*math.sqrt(Ka[i])+(soil_1)*Ka[i]
            coordinates[r] = [water_table,stress]
            r+=1
            water_done = True
        
        soil = soil+layers[i][0]*height
        stress = q*Ka[i]-2*layers[i][3]*math.sqrt(Ka[i])+(soil-pw)*Ka[i]
        coordinates[r] = [depth,stress]
        r+=1

        height = height + layers[i][1]
        
    height = 0


depth_value = coordinates[:,0]
stress_value = coordinates[:,1]

fig, ax =plt.subplots()

ax.plot(stress_value,depth_value,linestyle='-',color="#FFFEFB",label="Lateral Stress")
ax.invert_yaxis()
ax.set_xlabel("Lateral Stress(Kpa)",color="#FFFEFB",fontsize = 12)
ax.set_ylabel("Depth(m)",color="#FFFEFB", fontsize =12)
ax.set_title("Lateral Earth Pressure Diagram",color="#FFFEFB", fontsize =12)
ax.margins(x=0,y=0)
ax.grid(False)
ax.tick_params(axis="x",colors="#8F8F8F")
ax.tick_params(axis="y",colors="#8F8F8F")
ax.spines['left'].set_position(('data',0))
ax.spines['left'].set_color("#FFFEFB")
ax.spines['bottom'].set_color("#FFFEFB")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.set_facecolor("#334443")
ax.set_facecolor("#334443")

xmin,xmax = ax.get_xlim()
ax.set_xlim(left=min(0,xmin),right=xmax)

for x_1,y_1 in zip(stress_value,depth_value):
    ax.text(x_1+0.2,y_1-0.1,f"({x_1:.2f})",fontsize=8,va="center",color = "#FFFEFB")

new_depth = np.arange(0,depth,1)
new_stress=np.interp(new_depth,depth_value,stress_value)

new_depth_area = np.linspace(depth_value[0],depth_value[-1],100)
new_stress_area = np.interp(new_depth_area,depth_value,stress_value)

for x_1,y_1 in zip (new_stress,new_depth):
    ax.annotate(
        '',
        xy=(0,y_1),
        xytext=(x_1,y_1),
        arrowprops = dict(arrowstyle='->',color="#CFCFCF",lw=0.5)     
    )


if water_table is not None and water_table<depth:
    

    water_coordinates = np.zeros((2,2))

    water_coordinates[0]=[water_table,0]
    water_coordinates[1]=[depth,gamma_water*(depth-water_table)]

    water_depth_value = water_coordinates[:,0]
    water_stress_value = water_coordinates[:,1]

    fig1, ax1 =plt.subplots()

    ax1.plot(water_stress_value,water_depth_value,linestyle='-',color="#FFFEFB",label="Lateral Stress")
    ax1.invert_yaxis()
    ax1.set_xlabel("Water Pressure",color="#FFFEFB",fontsize = 12)
    ax1.set_ylabel("Depth(m)",color="#FFFEFB", fontsize =12)
    ax1.set_title("Water Pressure Diagram",color="#FFFEFB", fontsize =12)
    ax1.margins(x=0,y=0)
    ax1.grid(False)
    ax1.tick_params(axis="x",colors="#8F8F8F")
    ax1.tick_params(axis="y",colors="#8F8F8F")
    ax1.spines['left'].set_position(('data',0))
    ax1.spines['left'].set_color("#FFFEFB")
    ax1.spines['bottom'].set_color("#FFFEFB")
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    fig1.set_facecolor("#334443")
    ax1.set_facecolor("#334443")

    xmin,xmax = ax1.get_xlim()
    ax1.set_xlim(left=min(0,xmin),right=xmax)

    for x_1,y_1 in zip(water_stress_value,water_depth_value):
        ax1.text(x_1+0.2,y_1-0.1,f"({x_1:.2f})",fontsize=8,va="center",color = "#FFFEFB")

    water_depth = np.arange(water_table,depth,1)
    water_stress = np.interp(water_depth,water_depth_value,water_stress_value)

    for x_1,y_1 in zip (water_stress,water_depth):
        ax1.annotate(
            '',
            xy=(0,y_1),
            xytext=(x_1,y_1),
            arrowprops = dict(arrowstyle='->',color="#CFCFCF",lw=0.5)    
        )

    


for i in range(len(new_stress_area)-1):
    if new_stress_area[i]<=0<new_stress_area[i+1]:
        zero_depth = new_depth_area[i]-new_stress_area[i]*(new_depth_area[i+1]-new_depth_area[i])/(new_stress_area[i+1]-new_stress_area[i])
        new_depth_area = np.insert(new_depth_area,i+1,zero_depth)
        new_stress_area = np.insert(new_stress_area,i+1,0)

positive_side = new_stress_area >= 0
Force_Earth = np.trapezoid(new_stress_area[positive_side],x=new_depth_area[positive_side])
moment = np.trapezoid(new_depth_area[positive_side]*new_stress_area[positive_side],x=new_depth_area[positive_side])
centroid_earth = moment/Force_Earth if Force_Earth>0 else None

if rankine and water_table is not None:
    Force_Water = np.trapezoid(water_stress_value,water_depth_value)
    centroid_water = water_table + (depth-water_table)*(2/3)
else:
    Force_Water = 0
    centroid_water = 0

Active_Pressure = Force_Earth+Force_Water
Centroid = depth-(Force_Earth*centroid_earth + Force_Water*centroid_water)/Active_Pressure



fig.savefig(os.path.join(base_dir, "plot.png"),dpi=300,bbox_inches="tight")
if rankine and water_table is not None:
    fig1.savefig(os.path.join(base_dir,"water.png"),dpi=300,bbox_inches="tight")

plotpng = Image.open(os.path.join(base_dir,"plot.png"))
plotpng.thumbnail((550,550))
place_water_image = False
if rankine and water_table is not None:
    waterpng = Image.open(os.path.join(base_dir,"water.png"))
    waterpng.thumbnail((550,550))
    place_water_image = True

photo_plot = ImageTk.PhotoImage(plotpng)
if rankine and water_table is not None: 
    photo_water = ImageTk.PhotoImage(waterpng)


images = Canvas(scrollable_frame,width = 1150,height = 600,bg="#334443",highlightthickness=1,bd=0)

    
if not place_water_image:
    images.create_image(300,100,anchor="nw",image=photo_plot)
else:
    images.create_image(25,100,anchor="nw",image=photo_plot)


if rankine and water_table is not None:
    images.create_image(575,100,anchor="nw",image=photo_water)

images.place(relx=0.5,y=1100,anchor="center")



table =np.zeros((20,6), dtype=object)

table[0] = ('W₁',rf(0.5*a*d*gamma_conc),0,rf(c+(2/3)*d),rf((0.5*a*d*gamma_conc)*(c+(2/3)*d)),0)
table[1] = ('W₂',rf(a*e*gamma_conc),0,rf(c+d+e/2),rf((a*e*gamma_conc)*(c+d+e/2)),0)
table[2] = ('W₃',rf(0.5*a*f*gamma_conc),0,rf(c+d+e+f/3),rf((0.5*a*f*gamma_conc)*(c+d+e+f/3)),0)
table[3] = ('W₄',rf((c+d+e+f+g)*(b)*gamma_conc),0,rf((c+d+e+f+g)/2),rf(((c+d+e+f+g)*(b)*gamma_conc)*((c+d+e+f+g)/2)),0)
if h>0:
    table[4] = ('W₅',rf(0.5*(f+g)*h*layers[0][0]),0,rf((c+d+e+f+(2/3)*g)),rf((0.5*(f+g)*h*layers[0][0])*((c+d+e+f+(2/3)*g))),0)
layers[0][1] = layers[0][1] - h
layers[soil_layer_n-1][1] = layers[soil_layer_n-1][1]-b
top = f+g
dep = 0
if rankine:
    for i in range (soil_layer_n):
        dep = dep+layers[i][1]
        bottom = top -(f/a)*dep
        table[i+5] = (f'W{chr(0x2080 + (i+6))}',rf(0.5*(top+bottom)*layers[i][1]*layers[i][0]),0,rf((c+d+e+f+g-((top**2+top*bottom+bottom**2)/(3*(top+bottom))))),rf((0.5*(top+bottom)*layers[i][1]*layers[i][0])*((c+d+e+f+g-((top**2+top*bottom+bottom**2)/(3*(top+bottom)))))),0)
        top = bottom
    if q>0:
        table[soil_layer_n+5]=('Q',rf(q*(f+g)),0,rf(c+d+e+(f+g)/2),rf((q*(f+g))*(c+d+e+(f+g)/2)),0)
        table[soil_layer_n+6]=('Pᵥ',rf(Active_Pressure*math.sin(math.radians(alpha))),0,rf((c+d+e+f+g)),rf((Active_Pressure*math.sin(math.radians(alpha)))*(c+d+e+f+g)),0)
        table[soil_layer_n+7]=('Pₕ',0,rf(Active_Pressure*math.cos(math.radians(alpha))),rf(Centroid),0,rf((Active_Pressure*math.cos(math.radians(alpha)))*(Centroid)))
        Pv = rf(Active_Pressure*math.sin(math.radians(alpha)))
        Ph = rf(Active_Pressure*math.cos(math.radians(alpha)))
    
    else:
        table[soil_layer_n+5]=('Pᵥ',rf(Active_Pressure*math.sin(math.radians(alpha))),0,rf((c+d+e+f+g)),rf((Active_Pressure*math.sin(math.radians(alpha)))*(c+d+e+f+g)),0)
        table[soil_layer_n+6]=('Pₕ',0,rf(Active_Pressure*math.cos(math.radians(alpha))),rf(Centroid),0,rf((Active_Pressure*math.cos(math.radians(alpha)))*(Centroid)))
        Pv = rf(Active_Pressure*math.sin(math.radians(alpha)))
        Ph = rf(Active_Pressure*math.cos(math.radians(alpha)))

else:
    table[5]=(('Pᵥ',rf(Active_Pressure*math.sin(math.radians(alpha+90-beta+delta))),0,rf((c+d+e+f-(f/a)*(Centroid-b))),rf((Active_Pressure*math.sin(math.radians(alpha+90-beta+delta)))*(c+d+e+f-(f/a)*(Centroid-b))),0))
    table[6]=(('Pₕ',0,rf(Active_Pressure*math.cos(math.radians(alpha+90-beta+delta))),rf(Centroid),0,rf((Active_Pressure*math.cos(math.radians(alpha+90-beta+delta)))*(Centroid))))
    Pv = rf(Active_Pressure*math.sin(math.radians(alpha+90-beta+delta)))
    Ph = rf(Active_Pressure*math.cos(math.radians(alpha+90-beta+delta)))

filtered_table = table[np.any(table !=0, axis =1)]

lbl = Label(scrollable_frame,text=f"Total Pressure, Pₐ = {rf(Active_Pressure)} KN\nHorizontal Component, Pₕ  = {rf(Ph)} KN\nVertical Component, Pᵥ = {rf(Pv)} KN",font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",justify="left")
lbl.place(x=100,y=1424)
lbl = Label(scrollable_frame,text="Calculations are shown in the tabular form. The moment are taken about toe. The clockwise moments are taken as positive.",font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",justify="left")
lbl.place(x=100,y=1500)


table_format = Frame(scrollable_frame,padx=2,pady=2,bg="#FFFEFB")
table_format.place(relx=0.5,y=1680,anchor="center")

col_sum = np.sum(filtered_table,axis=0)
filtered_table = np.vstack([filtered_table,col_sum])
filtered_table[-1,0]="Sum"
filtered_table[-1][3] = "-"
filtered_table[-1][1] = rf(filtered_table[-1][1])
filtered_table[-1][2] = rf(filtered_table[-1][2])
filtered_table[-1][4] = rf(filtered_table[-1][4])
filtered_table[-1][5] = rf(filtered_table[-1][5])

heading = ['Label','Vertical (KN)','Horizontal (KN)','Lever Arm (m)','CW Mom. (KN-m)','ACW Mom. (KN-m)']
Bottom = [' ','ΣV','ΣH',' ','ΣMᵣ','ΣMₒ']
for j, value in enumerate(heading):
    label = Label(
        table_format,
        text=value,
        font=("Times New Roman", 16),
        borderwidth=1,
        width=15,
        fg="#FFFEFB",      # text color
        bg="#334443"       # background color
    )
    label.grid(row=0, column=j, padx=0, pady=0)

for i, row in enumerate(filtered_table):
    for j, value in enumerate(row):
        label = Label(
            table_format,
            text=value,
            font=("Times New Roman", 16),
            borderwidth=1,
            width=15,
            fg="#FFFEFB",      # text color
            bg="#334443"       # background color
        )
        label.grid(row=i+1, column=j, padx=1, pady=1)

for j, value in enumerate(Bottom):
    label = Label(
        table_format,
        text=value,
        font=("Times New Roman", 16),
        borderwidth=0,
        width=15,
        fg="#FFFEFB",      # text color
        bg="#334443"       # background color
    )
    label.grid(row=i+2, column=j, padx=0, pady=0)

scrollable_frame.update_idletasks()
table_height = table_format.winfo_height()

lbl = Label(scrollable_frame,text=f"Calculating FOS, \nThe factor of safety against sliding,\n\t\t\t Fₛ = tanδ * (ΣV / ΣH) = {rf(filtered_table[-1][1]*math.tan(math.radians(delta))/filtered_table[-1][2])}\nThe factor of safety against overturning,\n\t\t\tFₒ = ΣMᵣ / ΣMₒ = {rf(filtered_table[-1][4]/filtered_table[-1][5])}",font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",justify="left",anchor="w")
lbl.place(x=100,y=1680+table_height/2+15)

x_value = (filtered_table[-1][4]-filtered_table[-1][5])/filtered_table[-1][1]
eccentricity = abs((c+d+e+f+g)/2-x_value)

lbl = Label(scrollable_frame,text=f"x̄ = ΣM / ΣV = {rf(x_value)} m \n e = b/2 - x̄ ={rf(eccentricity)} m",font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",justify="left",anchor="w")
lbl.place(x=100,y=1790+table_height/2+15)

if eccentricity<(c+d+e+f+g)/6:
    pmax=rf((filtered_table[-1][1]/(c+d+e+f+g))*(1+6*eccentricity/(c+d+e+f+g)))
    text = "Since e<b/6, there is no tension"
    formula = "(ΣV / b) * (1 + 6e / b)"
else:
    pmax=rf((4/3)*(filtered_table[-1][1]/(c+d+e+f+g-2*eccentricity)))
    text = "Since e>b/6, there is tension"
    formula = "(4 / 3) * (ΣV / (b - 2e))"

lbl = Label(scrollable_frame,text=f"pₘₐₓ = {formula} = {pmax}\nThe factor of safety against bearing capacity,\n\t\t\tFᵦ = qₙₐ / pₘₐₓ = {rf(allowable_capacity/pmax)}",font = ("Times New Roman",14,"italic"),fg="#FFFEFB",bg="#334443",justify = "left")
lbl.place(x=100,y=1840+table_height/2+15)

report.protocol("WM_DELETE_WINDOW",lambda: close_application())
report.mainloop()


sys.exit()
