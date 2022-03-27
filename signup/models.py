from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, id, nickname, password=None):
        if not id:
            raise ValueError("Users must have an ID")
        user = self.model(
            id=id,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, nickname, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(id, nickname, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=255)
    nickname = models.CharField(
        max_length=50,
        unique=True,
    )
    age = models.PositiveIntegerField
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['nickname',] 

    def __str__(self):
        return self.id

    class Meta:
        db_table = "user"
