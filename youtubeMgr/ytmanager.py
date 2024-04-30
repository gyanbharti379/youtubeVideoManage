import tkinter
import tkinter.ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import json

class YtManager:

    dot = "."*10
    dot1 = "."*15
    welcome = f"{dot}Welcome to the python Youtube Manager Program{dot1}\n" + f"\n{dot1}select the choice and get the result{dot1}\n\n"

    def __init__(self):
        self.videos = self.loadData()
        self.itemList = []
        self.pre_len, self.after_len = 1.0, 1.0
        self.item, self.name,self.time = "","",""
        self.num = 1

# ---------------------Area for creating window ---------------------------Start -------------------------

        self.master = tkinter.Tk()
        self.master.title("Python Youtube Manage App")
        self.master.geometry("1100x750+150+10")
        self.master.resizable(False,False)
        self.choice = tkinter.StringVar()

# ---------------------Area for creating window ---------------------------END -------------------------

# -------------Area to add widget in window ------------------------------Start ------------------------

# ------------Left Frame -------------------------------------------------START-----------------------------

        self.left_frame = tkinter.Frame(self.master, bg="#ff8a35", width=330, height=750)
        self.left_frame.place(x=0,y=0)

        self.Title_Label = tkinter.Label(self.left_frame, text="Youtube manager",bg="#ff8a35", fg="#a8fff8",
                                         font=("book old style",25,"bold"))
        self.Title_Label.place(x=20, y=10)

        self.img = Image.open("images/ytimage.jpg").resize((280,280),Image.BOX)
        self.photo_img = ImageTk.PhotoImage(self.img)

        self.Image_Label = tkinter.Label(self.left_frame, image=self.photo_img)
        self.Image_Label.place(x=20, y=60)

        self.Des_Label = tkinter.Label(self.left_frame, text="*"*55, bg="#ff8a35",font=("book old style",10))
        self.Des_Label.place(x=20, y=355)

# -----------Choices for user -----------------------------------------------START -----------------------

        self.heading_Label = tkinter.Label(self.left_frame, text="Welcome user choice below", bg="#ff8a35",   fg="#8b2543",
                                           font=("book old style",18))
        self.heading_Label.place(x=10, y=420)

        self.radio_btn1 = tkinter.Radiobutton(self.left_frame,text="List all Youtube Videos", variable = self.choice,
                                           bg="#ff8a35",font=("book old style", 10), value="1")
        self.choice.set("1")
        self.radio_btn1.place(x=20, y=460)
        self.radio_btn2 = tkinter.Radiobutton(self.left_frame,text="Add a Youtube Videos", variable = self.choice,
                                              bg="#ff8a35",font=("book old style", 10), value="2")
        self.radio_btn2.place(x=20, y=490)
        self.radio_btn3 = tkinter.Radiobutton(self.left_frame,text="Update a Youtube Videos", variable = self.choice,
                                              bg="#ff8a35",font=("book old style", 10), value="3")
        self.radio_btn3.place(x=20, y=520)
        self.radio_btn4 = tkinter.Radiobutton(self.left_frame,text="Delete a Youtube Videos", variable = self.choice,
                                              bg="#ff8a35", font=("book old style", 10), value="4")
        self.radio_btn4.place(x=20, y=550)

        self.btn_img = Image.open("icons/save1.png").resize((20, 20), Image.BOX)
        self.photo_btn_img = ImageTk.PhotoImage(self.btn_img)

        self.submit_btn = tkinter.Button(self.left_frame, text="Submit Choice",width=180,image=self.photo_btn_img,compound=tkinter.LEFT,
                                         bg="#ff8a35",font=("book old style", 10), command=self.get_choice)
        self.submit_btn.place(x=20, y=580)

# -----------Choices for user -----------------------------------------------END ----------------------------

# ------------Left Frame ------------------------------------------------END---------------------------------

# ------------Right Frame -----------------------------------------------START-------------------------------

        self.right_frame = tkinter.Frame(self.master, bg="#ffba87", width=770, height=750)
        self.right_frame.place(x=330,y=0)

        self.Text_Area = tkinter.Text(self.right_frame,width=93, height=45)
        self.Text_Area.insert(tkinter.END,self.welcome)
        self.Text_Area.place(x=10, y=10)

# ------------Right Frame ----------------------------------------------------END--------------------------

# -------------Area to add widget in window ----------------------------------END ------------------------

        self.master.mainloop()

# ------------All other functions ---------------------------------------------Start ---------------------

    def get_choice(self):

        match self.choice.get():
                case "1":
                    self.listOfVideos(self.videos)
                case "2":
                    self.listOfVideos(self.videos)
                    self.getName("\nEnter Video Name: ")

                case "3":
                    self.listOfVideos(self.videos)
                    self.getNum("\nEnter the video number to update: ")


                case "4":
                    self.listOfVideos(self.videos)
                    self.getNum("\nEnter the video number to be deleted: ")

    def getName(self,data):
        self.pre_len = float(self.Text_Area.index(tkinter.END))
        self.Text_Area.insert(tkinter.END, data)
        self.after_len = self.pre_len + 0.18
        self.Text_Area.focus_set()
        self.Text_Area.bind("<Return>", self.onEnterName)

    def getNum(self,data):

        self.pre_len = float(self.Text_Area.index(tkinter.END))
        self.Text_Area.insert(tkinter.END, data)
        if self.choice.get() == "3":
            self.after_len = self.pre_len + 0.34

        elif self.choice.get() == "4":
            self.after_len = self.pre_len + 0.37

        self.Text_Area.focus_set()
        self.Text_Area.bind("<Return>", self.onEnterNum)

    def onEnterName(self,event):

        self.name = self.Text_Area.get(self.after_len, tkinter.END).strip()
        self.pre_len = float(self.Text_Area.index(tkinter.END))
        self.Text_Area.insert(tkinter.END, "\nEnter Time Duration of Video: ")
        self.after_len = self.pre_len + 0.31
        self.Text_Area.focus_set()
        self.time = self.Text_Area.bind("<Return>", self.onEnterTime)

    def onEnterNum(self,event):
        try:
            self.num = int(self.Text_Area.get(self.after_len, tkinter.END).strip())

            if self.choice.get() == "3":
                self.getName("\nEnter Video Name: ")

            if self.choice.get() == "4":
                self.deleteVideo(self.videos)


        except Exception:
            tkinter.messagebox.showerror("Error","Number not getting it ")

    def onEnterTime(self, event):
        self.time = self.Text_Area.get(self.after_len, tkinter.END).strip()


        if self.choice.get() == "2":
            self.addVideo(self.videos)

        elif self.choice.get() == "3":
            self.updateVideo(self.videos)

        elif self.choice.get() == "4":
            self.deleteVideo(self.videos)

    def successfulMessage(self):
        dot = "*"*80
        dash = "-"*30
        self.Text_Area.insert(tkinter.END, f"\n\n{dot}\n\n{dash}Successful{dash}\n\n{dot}")

    def loadData(self):
            try:
                with open('youtube.txt', 'r') as file:
                        return json.load(file)
            except FileNotFoundError:
                    return []

    def saveDataHelper(self,videos):
            with open('youtube.txt', 'w') as file:
                json.dump(videos, file)

    def listOfVideos(self,videos):

        self.Text_Area.delete(1.0, tkinter.END)
        self.itemList.clear()
        self.itemList.append("*"*80)

        for index, video in enumerate(videos, start=1):
            self.itemList.append(f"\n  {index}. Video Name: {video['name']}, Duration: {video['time']}\n")

        self.itemList.append("*" * 80)

        for item in self.itemList:
            self.Text_Area.insert(tkinter.END,item)

    def addVideo(self,videos):
            videos.append({'name': self.name, 'time': self.time})
            self.saveDataHelper(videos)
            self.successfulMessage()

    def updateVideo(self,videos):

            if 1 <= self.num <= len(videos):

                    videos[self.num - 1] = {'name': self.name, 'time': self.time}
                    self.saveDataHelper(videos)
                    self.successfulMessage()
            else:
                tkinter.messagebox.showerror("Error","Invalid index selected")

    def deleteVideo(self,videos):

            if 1 <= self.num <= len(videos):
                del videos[self.num - 1]
                self.saveDataHelper(videos)
                self.successfulMessage()


if __name__ == "__main__":
    YtManager()
