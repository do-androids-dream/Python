from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20, default="")
    surname = models.CharField(max_length=20, default="")
    patronymic = models.CharField(max_length=20, default="")

    def __str__(self):
        return f"'id': {self.id}, 'name': '{self.name}', 'surname': '{self.surname}', 'patronymic': '{self.patronymic}'"

    def __repr__(self):
        return f"Author(id={self.id})"

    @staticmethod
    def get_by_id(author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(author_id):
        try:
            author = Author.objects.get(id=author_id)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        if len(name) > 20 or len(surname) > 20:
            return None

        try:
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author
        except ValueError:
            return None

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }

    def update(self, name=None, surname=None, patronymic=None):
        if name:
            self.name = name
        if surname:
            self.surname = surname
        if patronymic:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        return Author.objects.all()
