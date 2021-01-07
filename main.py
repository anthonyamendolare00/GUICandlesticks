# This program is a simple GUI with a chat box
from tkinter import * # interface library

window = Tk() # main window

window.title('Interactive Candlesticks') # title of application

window.geometry('800x800') # dimensions

menu = Menu(window) # file menu bar
menu.add_command(label='New File') # add New File to menu bar
menu.add_command(label='Open') # add Open to menu bar
menu.add_command(label='Save As...') # add Save As to menu bar
menu.add_command(label='Save') # add Save to menu bar
menu.add_command(label='Exit') # add Exit to menu bar

main = Menu(window) # main menu bar
main.add_cascade(label='File', menu=menu) # file label and file commands
window.config(menu=main) # config the main menu

chat = Text(window, bd=1, bg='black', width=50, height=8) # add the chat window
chat.place(x=675, y=675, height=300, width=300) # place the chat window

message = Text(window, bg='white', width=30, height=4) # add the message window
message.place(x=700, y=700, height=200, width=300) # place the message window
# add button to chat window
button = Button(window, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 12))
button.place(x=750, y=750, height=50, width=50) # place the button window

scrollbar = Scrollbar(window, command=chat.yview()) # add scroll bar
scrollbar.place(x=690, y=700, height=375) # place the scroll bar

window.mainloop() # loop