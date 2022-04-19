import tkinter as tk

# Create tkinter window
root = tk.Tk()
root.title('Useless Program')



# Grabs seconds from text file
with open('time_log.txt','r+') as tlog:
    seconds = int(tlog.read())

# Runs on window close. Writes new time to text file
def on_closing():
    global seconds
    with open('time_log.txt','w') as tlog:
        tlog.write(str(seconds))
    root.destroy()

# Updates timer every second.
def track():
    global seconds
    seconds += 1
    string = f'{seconds} seconds'
    timer.config(text = string)
    timer.after(1000, track)
    

# Creates label for display
timer = tk.Label(root, bg = 'white', fg = 'black', font = ('Arial',35))
timer.pack(anchor = 'center')


track()

# Calls on_closing when you close window
root.protocol('WM_DELETE_WINDOW', on_closing)

root.mainloop()