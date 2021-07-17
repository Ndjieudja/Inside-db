# -*-ncoding:UTF-8 -*-

from glob_var import *
from sys_sgbd import *
from tkinter import*
from Prototype import*
import os
import  psycopg2
import sys

root=Tk()
root.title('insiderDB')
root.resizable(width=False, height=False)

appli=Windows(root, 'green')

root.after(1000, appli.page_star)
root.after(3000, appli.menu_login)

root.mainloop()
root.quit()


