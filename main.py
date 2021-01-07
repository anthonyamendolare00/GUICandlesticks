# This program is a simple GUI with a chat box
from tkinter import * # interface library

root = Tk() # main window

root.title('Interactive Candlesticks') # title of application

root.geometry('800x800') # dimensions

file_menu = Menu(root) # file menu bar
file_menu.add_command(label='New File') # add New File to menu bar
file_menu.add_command(label='Open') # add Open to menu bar
file_menu.add_command(label='Save As...') # add Save As to menu bar
file_menu.add_command(label='Save') # add Save to menu bar
file_menu.add_command(label='Exit') # add Exit to menu bar

main_menu = Menu(root) # main menu bar
main_menu.add_cascade(label='File', menu=file_menu) # file label and file commands
root.config(menu=main_menu) # config the main menu

chatWindow = Text(root, bd=1, bg='black', width=50, height=8) # add the chat window
chatWindow.place(x=675, y=675, height=300, width=300) # place the chat window

messageWindow = Text(root, bg='white', width=30, height=4) # add the message window
messageWindow.place(x=700, y=700, height=200, width=300) # place the message window
# add button to chat window
Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 12))
Button.place(x=750, y=750, height=50, width=50) # place the button window

scrollbar = Scrollbar(root, command=chatWindow.yview()) # add scroll bar
scrollbar.place(x=690, y=700, height=375) # place the scroll bar

root.mainloop() # loop 