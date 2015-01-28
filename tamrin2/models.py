__author__ = 'ParsData'

import  peewee


myDB = peewee.MySQLDatabase("new",host="localhost",port=3306,user="root",passwd="")

class MYSQLModel(peewee.Model):
    class Meta:
        database = myDB


class NewPost(MYSQLModel):
    id = peewee.primarykeyField()
    title = peewee.charField()
    author = peewee.charField()
    date = peewee.charField()
    text = peewee.charField()
    image = peewee.charField()

myDB.connect()

if __name__ == '__main__':

    myDB.creat_tables([NewPost])
