
tk = rint = btnN = None
initial, count = 1, 0
Exit = BOLD = None

def get_pkgs():
    global tk
    global rint
    global Exit
    global BOLD
    from sys import exit as Exit
    import tkinter as tk
    from tkinter.font import BOLD
    from random import randint as rint

def txtF(txt):
    return f"\n\n\t {txt} \t\n\n"

def add_text(win, user_text, fsize = 20):
    lbl = tk.Label(win, text = user_text)
    lbl.config(font = ("Courier", fsize, BOLD))
    lbl.pack()

def get_pose(pos):
    global btnN
    global initial
    global rint
    rpos =  (
        (249, 250), (83, 150), (332, 348), 
        (168, 255), (32, 323), (318, 156), 
        (211, 102), (12, 9), (5, 234), (97, 250)
            )
    if ".!button2" == str(pos.widget):
        nx, ny = rpos[rint(0, 9)]
        btnN.place(x = nx, y = ny)



def add_btns(win):
    global btnN
    h, w = 2, 3
    
    btnY = tk.Button(win, text = "YES", font=(BOLD), command= lambda : add_text(win, "I knew it!", fsize = 30))
    btnY.config(bg = "#87fa61", height = h, width = w)
    btnN = tk.Button(win, text = "NO", font = (BOLD))
    btnN.config(bg = "#fa6c61", height = h, width = w)
    
    btnY.place(x = 97, y = 250) #lower : 90, upper : 350
    win.bind('<Motion>', get_pose)
    if initial == 1:
        btnN.place(x = 249, y = 250)


def quit(trash):
    global Exit
    Exit()

def run_program():
    global count
    ws = 400
    if initial == 1:
        count += 2
    py = 100 + count*10
    px = py+10
    txt = "Are you STUPID?"
    window = tk.Tk()
    window.title(" WeLcOmE ")

    window.geometry(f"{ws}x{ws}+{px}+{py}")
    window.minsize(ws, ws)
    window.maxsize(ws, ws)

    user_text = txtF(txt)
   
    add_text(window, user_text)
    add_btns(window)

    window.protocol("WM_DELETE_WINDOW", run_program)
    window.bind("<Alt_L>", quit)
    window.mainloop()


def main():
    get_pkgs()
    run_program()


if __name__ == "__main__":   
    main()