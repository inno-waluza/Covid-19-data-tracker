from tkinter import *
from time import *
from tkinter import messagebox
from covid import Covid
from datetime import date


root = Tk()
root.title("COVID-19 DATA TRACKER")
root.geometry("900x500+300+200")
root.resizable(False,False)
window_icon = PhotoImage(file = "window_logo.png")
root.iconphoto(True,window_icon)

#get todays date
today = date.today()
date_strings = "Date"
day_String = "As of Today"

def getCovidData():
    country_name =  textfield.get()
    
    
    try:
        covid = Covid()
        covid.get_data()
        covid_data = covid.get_status_by_country_name(country_name)
        country = covid_data["country"]
        comfirmed = covid_data['confirmed']
        active = covid_data['active']
        deaths = covid_data['deaths']
        recovered = covid_data['recovered']
        
         #reference from previous code
        """
         t.config(text=(temp,"º"))
         c.config(text = ())
         w.config(text = wind)
         h.config(text = humidity)
         d.config(text = weather) 
         #p.config(text = preassure)
         v.config(text = visibility)
         """
        #Display country name and date
        t.config(text=(country_name))
        c.config(text = (today))

        #display covid 19 data
        w.config(text = comfirmed)
        h.config(text = active)
        d.config(text = deaths) 
        v.config(text = recovered)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry" +"\n Or" + "\nNo Internet Connection Available")


Search_image = PhotoImage(file="search.png")
myimage = Label(image = Search_image)
myimage.place(x=20,y=20)

textfield = Entry(root,justify = "center", width = 17, font=("poppins",25,"bold"),bg = "#404040",border = 0, fg = "white")
textfield.place(x = 50, y = 40)
textfield.focus()

Search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = Search_icon,borderwidth = 0, cursor = "hand2", bg = "#404040",command = getCovidData)
myimage_icon.place(x = 400, y = 34)

#logo
Logo_image = PhotoImage(file = "covid.png")
logo = Label(image = Logo_image)
logo.place(x = 150, y = 100) 

Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image = Frame_image)
frame_myimage.pack(padx=5, pady=5, side="bottom")

#time
name = Label(root,font = ("arial",15,"bold"))
name.place(x = 30, y =100)
clock = Label(root,font = ("Helvetica",20))
clock.place(x = 30, y = 130)

#label
label1 = Label(root,text="CONFIRMED", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label1.place(x = 120, y =400)

label2 = Label(root,text="  ACTIVE", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label2.place(x = 250 , y =400)

label3 = Label(root,text="DEATHS", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label3.place(x = 430, y =400)

label4 = Label(root,text="RECOVERED", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label4.place(x = 650, y =400)

#countryname label
t = Label(font = ("arial",40,"bold"),fg = "#000814")
t.place(x = 400,y = 150)
#date label to be displayed later
c = Label(text = "Date",font=("arial",15,"bold"),fg="#000814")
c.place(x = 400,y =250)

w = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
w.place(x =120, y = 430)
h = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
h.place(x =280, y = 430)
d = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
d.place(x =450, y = 430)
v = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
v.place(x =670, y = 430)



root.mainloop()