import tkinter as tk
from PIL import ImageTk, Image

# AUTHOR: jtnoble

class App(tk.Frame):
    # Initialize application
    def __init__(self, parent):
        tk.Frame = tk.Frame
        self.parent = parent
        self.parent.title("Four Souls Floor Manager")
        self.parent.resizable(False, False)
        self.settings()
        self.first_Time = True
        self.screen_width = int(self.settings_width)
        self.screen_height = int(self.settings_height)
        self.background_image_setup("isaac_bg.png")
        self.title_screen()
    
    # "Title" as in main screen
    def title_screen(self):
        # Width/Height are arbitrary, made to just fit to what looks good.
        _width = int(self.screen_width / 75)
        _height = int(self.screen_height / 150)

        # Ran on initialize to create a buttons list. Must be cleared every time "title_screen" is loaded to prevent extra buttons
        if self.first_Time:
            self.buttons = []
        self.buttons.clear()
        
        # Hard Coded floors. Easily changable, didn't feel like putting these in a file
        floors = [
            "Basement/Cellar/Burning Basement", 
            "Caves/Flooded Caves/Catacombs", 
            "Downpour/Dross", 
            "Mines/Ashpit", 
            "Depths/Dank Depths/Necropolis",
            "Mausoleum/Gehenna",
            "Womb/Scarred Womb/Utero",
            "Cathedral/Sheol",
            "The Chest/Dark Room",
            "Void/Home",
            "???/Corpse"
            ]

        # Create a frame to hold all of the floors (first time only to prevent extra buttons)
        if self.first_Time:
            self.buttons_frame = tk.Frame(self.parent, bg='black', width=(self.screen_width/3), height=(self.screen_height/3))
            for floor in floors:
                self.buttons.append(tk.Button(self.buttons_frame, text=floor, wraplength=_width*15, font=("",18), bg="darkgrey", width=_width, height=_height, command=lambda floor=floor:self.nested_floors(floor)))
            self.buttons.append(tk.Button(self.buttons_frame, text="Quit", bg="darkgrey", wraplength=_width*15, font=("",18), width=_width, height=_height, command=self.parent.destroy))
            self.first_Time = False
        # Placing frame, will be forgotten later
        self.buttons_frame.place(anchor="c", relx=.5, rely=.5)
        # Placing buttons on grid, will be forgotten later
        for i in range(0, len(self.buttons)):
            self.buttons[i].grid(row=int(i/4), column=int(i%4), padx=3, pady=3)

    # Forget placement of buttons_frame, Check if floors have a "/"
    def nested_floors(self, _index):
        self.buttons_frame.place_forget()
        #print(_index)

        self.back_button = tk.Button(text="Back", bg='#696969', width=10, height=3, command=lambda: [self.title_screen(), self.change_background_image("isaac_bg"), self.back_button.destroy()])
        self.back_button.place(relx=0.95, rely=0.95, anchor="se")

        if "/" in _index:
            self.separate_n_generate(_index)
        else:
            self.change_background_image(_index)

    # Splits floors with "/" into separate elements to make buttons for individual floors
    def separate_n_generate(self, _index):
        _width = int(self.screen_width / 100)
        _height = int(self.screen_height / 200)
        nested_buttons = []
        buttons_frame = tk.Frame(self.parent, bg='black', width=(self.screen_width/3), height=(self.screen_height/3))
        subfloors = _index.split("/")
        
        self.back_button.configure(command=lambda: [self.title_screen(), buttons_frame.place_forget(), self.change_background_image("isaac_bg"), nested_buttons.clear(), self.back_button.destroy()])
        
        # New buttons/frame generator
        for subfloor in subfloors:
            nested_buttons.append(tk.Button(buttons_frame, text=subfloor, wraplength=200, font=("Arial", 20), bg="darkgrey", width=_width, height=_height, command=lambda subfloor=subfloor:[self.change_background_image(subfloor), buttons_frame.place_forget(), nested_buttons.clear()]))
        buttons_frame.place(anchor="c", relx=.5, rely=.5)
        for i in range(0, len(nested_buttons)):
            nested_buttons[i].grid(row=int(i/3), column=int(i%3), padx=3, pady=3)

    # Change background image to match background. Backgrounds have the text on them to make scaling to resolution easier.
    def change_background_image(self, img):
        img = img.lower().replace(" ","_")
        # Check for ??? as filenames cannot contain question marks
        if img == "???":
            img = "hush"
        # If for some reason a background doesn't match, this protects from erroring out.
        try:
            image = Image.open("config/images/"+img+".png")
        except:
            image = Image.open("config/images/isaac_bg.png")

        # Resizing image to fit resolution and placing image on screen
        resize_image = image.resize((self.screen_width, self.screen_height))

        self.bg_img = ImageTk.PhotoImage(resize_image)

        self.label1.configure(image=self.bg_img)

        # Close image to preserve resources
        image.close()

    # Run initially to open up background image
    def background_image_setup(self, img_link):
        image = Image.open("config/images/"+img_link)

        # Resize the image using resize() method
        resize_image = image.resize((self.screen_width, self.screen_height))
        self.bg_img = ImageTk.PhotoImage(resize_image)
        
        # create label and add resize image
        self.label1 = tk.Label(image=self.bg_img)
        self.label1.pack()
        image.close()
 
    # Read settings.txt file for specific settings
    def settings(self):
        # Failsafe to set width and height initially to desktop width and height
        self.settings_width = self.parent.winfo_screenwidth()
        self.settings_height = self.parent.winfo_screenheight()
        fullscreen = False

        # Reading Settings
        with open("config/settings.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("#"):    # Skip lines with "#"
                line = ""
            if "Fullscreen" in line:    # Check if application should be fullscreen
                if "1" in line:
                    fullscreen = True
            if not fullscreen:          # Set width/height to values in settings.txt
                if "Width" in line:
                    self.settings_width = line.strip("Width=")
                    self.settings_width = self.settings_width.strip("\n")
                if "Height" in line:
                    self.settings_height = line.strip("Height=")
                    self.settings_height = self.settings_height.strip("\n")
        
        # Settings Passthrough
        if fullscreen:
            self.parent.attributes('-fullscreen', True)
        else:
            self.parent.geometry(self.settings_width + "x" + self.settings_height)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()