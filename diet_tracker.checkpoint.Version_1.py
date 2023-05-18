import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  

# Create FirstPage class
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Open image
        load = Image.open("Asset/diet_4.png")
        # # Resize image to fit the GUI page
        resized_image = load.resize((800, 500))
        photo = ImageTk.PhotoImage(resized_image)
        # Create a label
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)


        # Border 
        border = tk.LabelFrame(self, text='Welcome', bg='black', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        # Label as username
        Label_1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='black')
        Label_1.place(x=50, y=20)
        # Username textfield
        Textfield_1 = tk.Entry(border, width = 30, bd = 5)
        Textfield_1.place(x=180, y=20)
        # Label as password
        Label_2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='black')
        Label_2.place(x=50, y=80)
        # Password textfield
        Textfield_2 = tk.Entry(border, width = 30, show='*', bd = 5)
        Textfield_2.place(x=180, y=80)
        
        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        u, p =e.split(",")
                        if u.strip() == Textfield_1.get() and p.strip() == Textfield_2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
        # Log in button 
        Button_1 = tk.Button(border, text="Log in", font=("Arial", 15), command=verify)
        Button_1.place(x=320, y=115)

        # Register button    
        Button_2 = tk.Button(self, text="Register", bg = "dark orange", font=("Arial",15))
        Button_2.place(x=650, y=20)

#Create SecondPage class       
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        
        # Button to thridpage
        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)
        # Button to previous page
        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)

# Create ThirdPage class    
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='grey')
    
        # Button to homepage
        home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        home_button.place(x=650, y=450)
        # Button to previous page
        back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        back_button.place(x=100, y=450)

# Main function        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Creating a window
        window = tk.Frame(self)
        window.pack()
        # Size of window
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        # Store the frames for each page
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
        
        # Display the firstpage frame    
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        # Raises the frame to the top, making it visible in the GUI
        frame.tkraise()
        # Title
        self.title("Diet_gui")

          
app = Application()
app.maxsize(800,500)
# Run the main event loop
app.mainloop()