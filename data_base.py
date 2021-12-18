import datetime

from peewee import *

mysql_db = MySQLDatabase()

class Users(Model):
    user_id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    is_online = BooleanField(default=False)
    sid = CharField(default=None)
    last_login = DateTimeField(default=None)

    class Meta:
        database = mysql_db  # This model uses the "mysql.db" database.


class Groups(Model):
    group_id = AutoField()
    group_name = CharField(unique=True)
    created_by = ForeignKeyField(Users, backref='users')
    created_at = DateTimeField()
    is_active = BooleanField()
    last_activity = DateTimeField(default=None)

    class Meta:
        database = mysql_db  # This model uses the "mysql.db" database.


class Membership(Model):
    member_id = AutoField()
    user_id = ForeignKeyField(Users, backref='users')
    group_id = ForeignKeyField(Groups, backref='groups')
    create_at = DateTimeField(default=datetime.datetime.now())
    is_active = BooleanField(default=True)
    last_active = DateTimeField(default=None)
    is_watch = BooleanField(default=False)
    last_watch = DateTimeField(default=None)

    class Meta:
        database = mysql_db  # This model uses the "mysql.db" database.


class Message(Model):
    message_id = AutoField()
    creator_id = ForeignKeyField(Users, backref='users')
    group_id = ForeignKeyField(Groups, backref='groups')
    message_body = CharField()
    created_at = DateTimeField(default=datetime.datetime.now())
    is_read = BooleanField(default=False)

    class Meta:
        database = mysql_db  # This model uses the "mysql.db" database.


if __name__ == '__main__':
    query = Membership.select(Membership.member_id).where(
       (Membership.user_id == Users.select(Users.user_id).where(Users.username == "roei")) & (
               Membership.group_id == Groups.select(Groups.group_id).where(Groups.group_name == "test2")))
    for i in query:
        print(i)

