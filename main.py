import tkinter as tk
from pymem import *
from pymem.process import *
import time
import threading
from tkinter import IntVar
from tkinter import ttk

class MemoryEditorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("1v1.LOL Cheat")
        self.root.geometry("500x400")
        self.root.configure(bg='#000000') 

        self.style = ttk.Style()
        self.style.configure('TCheckbutton', background='#000000', foreground='green', font=('Arial', 12, 'bold'))
        self.style.configure('TButton', background='#555555', foreground='black', font=('Arial', 14, 'bold'))
        self.style.configure('TLabel', background='#333333', font=('Arial', 18, 'bold'))

        self.check_var1 = IntVar()
        self.check_var2 = IntVar()
        self.check_var3 = IntVar()
        self.check_var4 = IntVar()
        self.check_var5 = IntVar()

        self.editing_status = False

        self.pm = Pymem('1v1_LOL.exe') 
        self.monos = module_from_name(self.pm.process_handle, 'mono-2.0-bdwgc.dll').lpBaseOfDll
        self.gamemodu = module_from_name(self.pm.process_handle, 'UnityPlayer.dll').lpBaseOfDll
        self.offsets = [0x2A8, 0x80, 0x10, 0x58, 0x60, 0x50, 0x2C0]  
        self.offsets2 = [0x2A8, 0x88, 0x10, 0x68, 0x60, 0x88, 0xC0] 
        self.offsets3 = [0x2A8, 0x80, 0x10, 0x58, 0x20, 0x78, 0xC0]  
        self.offsets4 = [0x128, 0x48, 0x60, 0x48, 0x10, 0x90]
        self.offsets5 = [0x38, 0x1D0, 0x20, 0x90, 0x70, 0x68, 0xC4]

        self.create_gui()


    def create_gui(self):
        title_label = tk.Label(self.root, text="1V1.LOL Cheat (Made By TheCuteOwl)", font=('Arial', 18, 'bold'), bg='#000000', fg='white')                                                                                                                                    # The Cuteowl
        title_label.pack(pady=10)

        self.checkbox1 = ttk.Checkbutton(self.root, text="Infinite Ammo", variable=self.check_var1, style='TCheckbutton')
        self.checkbox2 = ttk.Checkbutton(self.root, text="Infinite Health", variable=self.check_var2, style='TCheckbutton')
        self.checkbox3 = ttk.Checkbutton(self.root, text="Infinite Build", variable=self.check_var3, style='TCheckbutton')
        self.checkbox4 = ttk.Checkbutton(self.root, text="Infinite Money", variable=self.check_var4, style='TCheckbutton')
        self.checkbox5 = ttk.Checkbutton(self.root, text="Infinite Shield (Glitched)", variable=self.check_var5, style='TCheckbutton')

        self.checkbox1.pack(pady=5)
        self.checkbox2.pack(pady=5)
        self.checkbox3.pack(pady=5)
        self.checkbox4.pack(pady=5)
        self.checkbox5.pack(pady=5)

        self.start_button = ttk.Button(self.root, text="Toggle Editing", command=self.toggle_editing, style='TButton')
        self.start_button.pack(pady=20)

        self.editing_label = ttk.Label(self.root, text="Not Started", style='TLabel', foreground='red', background='#000000')
        self.editing_label.pack(pady=10)

        self.check_var1.set(False)
        self.check_var2.set(False)
        self.check_var3.set(False)
        self.check_var4.set(False)
        self.check_var5.set(False)

        self.check_game_status()

        self.root.mainloop()

    def toggle_editing(self):
        self.editing_status = not self.editing_status
        if self.editing_status:
            self.editing_label.config(text="Started", foreground='green', background='#000000')
        else:
            self.editing_label.config(text="Stopped", foreground='red', background='#000000')

        if self.check_var1.get() or self.check_var2.get() or self.check_var3.get() or self.check_var4.get() or self.check_var5.get():
            thread = threading.Thread(target=self.start_editing)
            thread.start()

    def start_editing(self):
        while any([self.check_var1.get(), self.check_var2.get(), self.check_var3.get(), self.check_var4.get(), self.check_var5.get()]):
            if not self.editing_status:
                break
            try:
                while any([self.check_var1.get(), self.check_var2.get(), self.check_var3.get(), self.check_var4.get(), self.check_var5.get()]):
                    if not self.editing_status:
                        break
                    if self.check_var1.get():
                        self.pm.write_int(self.mono(self.monos, self.offsets), 300)

                    if self.check_var2.get():
                        self.pm.write_int(self.mono(self.monos, self.offsets2), 300)

                    if self.check_var3.get():
                        self.pm.write_int(self.mono(self.monos, self.offsets3), 100)

                    if self.check_var4.get():
                        self.pm.write_int(self.unityplayer(self.gamemodu, self.offsets4), 100000)

                    if self.check_var5.get():
                        self.pm.write_int(self.mono(self.monos, self.offsets5), 150)

                    time.sleep(0.001)
            except Exception as e:
                print(e)

    def unityplayer(self, base, offsets):
        addr = self.pm.read_longlong(base + 0x01B22730)
        for offset in offsets:
            addr = self.pm.read_longlong(addr + offset)
        return addr + offsets[-1]

    def mono(self, base, offsets):
        addr = self.pm.read_longlong(base + 0x0072A1D8)
        for offset in offsets:
            addr = self.pm.read_longlong(addr + offset)
        return addr + offsets[-1]

    def check_game_status(self):
        while True:
            try:
                self.pm = Pymem('1v1_LOL.exe')  
                self.editing_label.config(text="Game detected", foreground='green', background='#000000')
                self.checkbox1.pack()
                self.checkbox2.pack()
                self.checkbox3.pack()
                self.checkbox4.pack()
                self.checkbox5.pack()
                self.start_button.pack()
                break
            except:
                self.checkbox1.pack_forget()
                self.checkbox2.pack_forget()
                self.checkbox3.pack_forget()
                self.checkbox4.pack_forget()
                self.checkbox5.pack_forget()
                self.start_button.pack_forget()
                self.editing_label.config(text="Waiting for the game to launch", foreground='red', background='#000000')
                self.show_restart_message()
                
    def show_restart_message(self):
        restart_message = 'Start the game and click on "ok"'
        tk.messagebox.showinfo("Game Status", restart_message)


if __name__ == '__main__':
    MemoryEditorGUI()
