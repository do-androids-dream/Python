from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=21, default=None)
    first_name = models.CharField(max_length=21, blank=True, null=True, validators=[MaxLengthValidator(21)])
    middle_name = models.CharField(max_length=21, blank=True, null=True, validators=[MaxLengthValidator(21)])
    last_name = models.CharField(max_length=21, blank=True, null=True, validators=[MaxLengthValidator(21)])
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return (
            f"'id': {self.id}, "
            f"'first_name': '{self.first_name}', "
            f"'middle_name': '{self.middle_name}', "
            f"'last_name': '{self.last_name}', "
            f"'email': '{self.email}', "
            f"'created_at': {int(self.created_at.timestamp())}, "
            f"'updated_at': {int(self.updated_at.timestamp())}, "
            f"'role': {self.role}, "
            f"'is_active': {self.is_active}"
        )

    def __repr__(self):
        return f"CustomUser(id={self.id})"

    @staticmethod
    def get_by_id(user_id):
        try:
            return CustomUser.objects.get(id=user_id, is_active=True)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def get_by_email(email):
        try:
            return CustomUser.objects.get(email=email, is_active=True)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            user.delete()
            return True
        except CustomUser.DoesNotExist:
            return False

    @staticmethod
    def create(email, password, first_name=None, middle_name=None, last_name=None):
        try:
            validate_email(email)
        except ValidationError:
            return None

        existing_user = CustomUser.objects.filter(email=email).first()
        if existing_user:
            return None

        if first_name and len(first_name) > 20:
            return None

        if middle_name and len(middle_name) > 20:
            return None

        if last_name and len(last_name) > 20:
            return None

        user = CustomUser(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return user

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': int(self.created_at.timestamp()),
            'updated_at': int(self.updated_at.timestamp()),
            'role': self.role,
            'is_active': self.is_active,
        }

    def update(self, first_name=None, last_name=None, middle_name=None, password=None, role=None, is_active=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if password is not None:
            self.set_password(password)
        if role is not None:
            self.role = role
        if is_active is not None:
            self.is_active = is_active
        self.save()

    @staticmethod
    def get_all():
        return CustomUser.objects.all()

    def get_role_name(self):
        return self.get_role_display()
