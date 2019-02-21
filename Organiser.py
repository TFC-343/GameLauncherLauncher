# James Packham(TFC343)
# Game Launcher Launcher & Game launcher Organiser

import os
import tkinter


global file
f = open('Launchers.txt', 'r')
file = f.readlines()
f.close()
for loop in range(0, len(file)):
    file[loop] = file[loop][0:-1]
    file[loop] = file[loop].split(' | ')
    print(file)


launcher_array = []
for x in range(0, len(file)):
    launcher_array.append(file[x][1])

launcher_array_info = []
for x in range(0, len(file)):
    launcher_array_info.append(file[x][0])


def options():
    pass


def open_launcher(h):
    print(h)
    print(launcher_array_info)
    os.startfile(launcher_array_info[h])


def button():
    print(file)
    for i in range(0, int(len(file))):
        tkinter.Button(master=main, text=file[i][1],
                       command=lambda i=i: open_launcher(launcher_array.index(file[i][1])),
                       bg="#0000ff", fg="White").pack(pady=10, padx=5)


main = tkinter.Tk()

tkinter.Label(main, text='Please Pick An Option', bg="#000000", fg='#ffffff').pack(pady=10, padx=25)

main.configure(background="#000000")
main.geometry()

button()

tkinter.Button(master=main, text='OPTIONS', command=options, bg="#00ff00", fg="#000000").pack(pady=10, padx=15)

tkinter.Button(master=main, text='QUIT', command=quit, bg="#ff0000", fg="White").pack(pady=10, padx=15)

tkinter.mainloop()
