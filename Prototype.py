# Fichier contenant les differents prototype utillitaire au main

# -*- encoding:utf8 -*-

from tkinter import*
from sys_sgbd import *
from glob_var import *

class Windows:

    def __init__(self, master, background, image=None):

        self.bground=background
        self.image=image
        self.master=master

        self.can=Canvas(master, width=900, height=800, bg=background)
        self.bou_login=Button(self.can)

        self.type_user=Entry(self.can)
        self.type_user_new=Entry(self.can)

        self.type_mdp=Entry(self.can)
        self.type_mdp_new=Entry(self.can)

        self.bou_create_user=Button(self.can)

        self.can.pack()

    def page_star(self):
        self.can.create_text(450, 400, text='insiderDB', font='ubuntu 50')

    def menu_login(self):

       Menu(self.can, 'utilisateur', self.type_user, 'nouvel utilisateur', self.type_mdp, self.bou_login\
            ,self.bou_create_user, self.connect_db, self.create_user)

    def connect_db(self):

        Glob_connect.user=self.type_user.get()
        Glob_connect.passsword=self.type_mdp.get()
        sys_SGBD = SGBD(Glob_connect.user, Glob_connect.dbname, Glob_connect.passsword)

        if sys_SGBD.echec == 0:
            self.can.delete(ALL)
            self.connected_succed()

        else:
            self.can.create_text(470, 290, text='utilisateur ou mot de passe incorrect' \
                                , font='ubuntu 12', fill='red')

    def connected_succed(self):
        print('welcome')

    def create_user(self):

        Menu(self.can, 'utilisateur', self.type_user, 'nouvel utilisateur', self.type_mdp, self.bou_login\
            ,self.bou_create_user, self.connect_db, self.create_user)

# creation des differentes cases neccessaires à l'instanciation d'un nouvel utilisateur

        self.can.create_text(200, 450, text='Nouvel utilisateur',\
                             font='ubuntu 25', fill='blue')

        self.can.create_text(220, 500, text='Nom Utilisateur', font='ubuntu 20')

        self.type_user_new.configure(width=20)
        new_user_window_ = self.can.create_window(330, 492, anchor=NW, window=self.type_user_new)

        self.can.create_text(240, 550, text='Mot de Passe', font='ubuntu 20')
        self.type_mdp_new.configure(width=20)
        new_mdp_window = self.can.create_window(330, 543, anchor=NW, window=self.type_mdp_new)

        self.bou_create_user.configure(width=30, height=2, activebackground='blue', bg='green' \
                                       , font='ubuntu 10', command=self.connected_succed)
        boue_create_user_window = self.can.create_window(315, 580, anchor=NW, \
                                                  window=self.bou_create_user)


class Menu:
    #instanciation des different outils de gention de menu

    def __init__(self, master, user, e_user, c_user, e_mdp, bou_login, boue_c,\
                 function1, function2, clean=1):

    #instanciation
        self.boue_c, self.boue_login = boue_c, bou_login
        self.c_user, self.e_user = c_user, e_user
        self.e_mdp = e_mdp
        self.user, self.e_user = user, e_user
        self.master=master
        self.clean=clean

        self.function1, self.function2=function1, function2

        self.create_menu()

    def create_menu(self):

        self.clean=self.master.delete(ALL)
        self.master.configure(bg='dark grey')

        self.master.create_text(200, 130, text='insiderDB', font='ubuntu 40', fill='dark blue')

        self.master.create_text(250, 200, text=self.user, font='ubuntu 20')
        self.e_user.configure(width=20)
        user_window = self.master.create_window(330, 192, anchor=NW, window=self.e_user)

        self.master.create_text(240, 250, text='Mot de Passe', font='ubuntu 20')
        self.e_mdp.configure(width=20)
        mdp_window = self.master.create_window(330, 243, anchor=NW, window=self.e_mdp)

        self.bou_login = Button(self.master, text='Login', command=self.function1)
        self.bou_login.configure(width=30, height=2, activebackground='blue', bg='green'\
                                 , font='ubuntu 10')
        choix_window = self.master.create_window(315, 330, anchor=NW, window=self.bou_login)

        self.boue_c.configure(width=30, height=2, text='Create user',\
                                       activebackground='blue', bg='green' \
                                       , font='ubuntu 10', command=self.function2)
        boue_create_user = self.master.create_window(315, 380, anchor=NW, window=self.boue_c)
