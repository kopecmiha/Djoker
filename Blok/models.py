from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    email = models.TextField(default=None)
    password = models.TextField(default=None)


    def create(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.save()

    def __repr__(self):
        return str({"id": self.id,
                    "username": self.username,
                    "email": self.email,
                    "password": self.password})