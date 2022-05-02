import tkinter as tk
from tkinter import PhotoImage, ttk
from PIL import ImageTk, Image


class App(tk.Frame):
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
    

    def title_screen(self):
        _width = int(self.screen_width / 100)
        _height = int(self.screen_height / 200)
        if self.first_Time:
            self.buttons = []
        self.buttons.clear()
        floors = ["Basement", "Catacombs", "Mines", "Sheol/Cathedral", "Depths", "The Chest", "The Womb", "Downpour"]

        if self.first_Time:
            self.buttons_frame = tk.Frame(self.parent, bg='black', width=(self.screen_width/3), height=(self.screen_height/3))
            for floor in floors:
                self.buttons.append(tk.Button(self.buttons_frame, text=floor, font=("Arial", 20), bg="darkgrey", width=_width, height=_height, command=lambda floor=floor:self.floor_rules(floor)))
            self.buttons.append(tk.Button(self.buttons_frame, text="Quit", font=("Arial", 20), bg="darkgrey", width=_width, height=_height, command=self.parent.destroy))
            self.first_Time = False
        self.buttons_frame.place(anchor="c", relx=.5, rely=.5)
        for i in range(0, len(self.buttons)):
            self.buttons[i].grid(row=int(i/3), column=int(i%3), padx=3, pady=3)
            self.buttons[i].configure()

    def floor_rules(self, _index):
        self.buttons_frame.place_forget()
        print(_index)

        back_button = tk.Button(text="Back", bg='#696969', width=10, height=3, command=lambda: [self.title_screen(), self.change_background_image("isaac_bg"), back_button.destroy()])
        back_button.place(relx=0.95, rely=0.95, anchor="se")

        if _index == "Basement":
            self.basement_choices()
        elif _index == "Sheol/Cathedral":
            self.cathedral_choices()
        else:
            self.change_background_image(_index)
        

    def cathedral_choices(self):
        _width = int(self.screen_width / 100)
        _height = int(self.screen_height / 200)
        buttons_cathedral = []
        buttons_frame = tk.Frame(self.parent, bg='black', width=(self.screen_width/3), height=(self.screen_height/3))
        sheol_cathedral = ["Sheol", "Cathedral"]
        
        back_button = tk.Button(text="Back", bg='#696969', width=10, height=3, command=lambda: [self.title_screen(), buttons_frame.place_forget(), self.change_background_image("isaac_bg"), buttons_cathedral.clear(), back_button.destroy()])
        back_button.place(relx=0.95, rely=0.95, anchor="se")
        
        for subfloor in sheol_cathedral:
            buttons_cathedral.append(tk.Button(buttons_frame, text=subfloor, wraplength=200, font=("Arial", 20), bg="darkgrey", width=_width, height=_height, command=lambda subfloor=subfloor:[self.change_background_image(subfloor), buttons_frame.place_forget(), buttons_cathedral.clear(), back_button.destroy()]))
        buttons_frame.place(anchor="c", relx=.5, rely=.5)
        for i in range(0, len(buttons_cathedral)):
            buttons_cathedral[i].grid(row=int(i/3), column=int(i%3), padx=3, pady=3)

    def basement_choices(self):
        _width = int(self.screen_width / 100)
        _height = int(self.screen_height / 200)
        buttons_basement = []
        buttons_frame = tk.Frame(self.parent, bg='black', width=(self.screen_width/3), height=(self.screen_height/3))
        basement_subfloors = ["Basement", "Flooded Basement", "Burning Basement"]
        
        back_button = tk.Button(text="Back", bg='#696969', width=10, height=3, command=lambda: [self.title_screen(), buttons_frame.place_forget(), buttons_basement.clear(), self.change_background_image("isaac_bg"), back_button.destroy()])
        back_button.place(relx=0.95, rely=0.95, anchor="se")
        
        for subfloor in basement_subfloors:
            buttons_basement.append(tk.Button(buttons_frame, text=subfloor, wraplength=200, font=("Arial", 20), bg="darkgrey", width=_width, height=_height, command=lambda subfloor=subfloor:[self.change_background_image(subfloor), buttons_frame.place_forget(), buttons_basement.clear(), back_button.destroy()]))
        buttons_frame.place(anchor="c", relx=.5, rely=.5)
        for i in range(0, len(buttons_basement)):
            buttons_basement[i].grid(row=int(i/3), column=int(i%3), padx=3, pady=3)


    def change_background_image(self, img):
        print("CHANGING")
        img = img.lower().replace(" ","_")
        print(img)

        image = Image.open("config/images/"+img+".png")
        resize_image = image.resize((self.screen_width, self.screen_height))

        self.bg_img = ImageTk.PhotoImage(resize_image)

        self.label1.configure(image=self.bg_img)

        image.close()

    def background_image_setup(self, img_link):
        image = Image.open("config/images/"+img_link)

        # Resize the image using resize() method
        resize_image = image.resize((self.screen_width, self.screen_height))
        self.bg_img = ImageTk.PhotoImage(resize_image)
        
        # create label and add resize image
        self.label1 = tk.Label(image=self.bg_img)
        self.label1.pack()
        image.close()
 

    def settings(self):
        self.settings_width = self.parent.winfo_screenwidth()
        self.settings_height = self.parent.winfo_screenheight()
        fullscreen = False

        # Reading Settings
        with open("config/settings.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                line = ""
            if "Fullscreen" in line:
                if "1" in line:
                    fullscreen = True
            if not fullscreen:
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