
#contient l'instanciation des toutes les  operation possible sur un base de données

import psycopg2

class SGBD:

    def __init__(self, user, db_name, password):

        self.connection = None
        self.requette=None

        try:
            self.conection=psycopg2.connect(user=user, dbname=db_name, password=password)

        except Exception as err:
            print('fail to connect data base:  \n'
                  'error detected: \n'
                  '{}'.format(err))
            self.echec = 1

        else:
            self.cursor =self.conection.cursor()        #create cursor
            print('connected sucessful')
            self.echec = 0

    def create_table(self, table):
        self.requette = ('CREATE TABLE {}(nom text, age INTEGER)'.format(table))
        self.cursor.execute(self.requette)


    def enregistre(self):
        choix=input("voulez vous enregistre les modification o/n: ")
        if choix=='o' or  choix=='O':
            self.conection.commit()
        else:
            self.echec=1

    def sortie(self):
        self.cursor.close()
        self.conection.close()

