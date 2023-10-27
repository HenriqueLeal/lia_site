from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    #inserir todos os campos que são obrigatórios nos parametros
    def create_user(self, email, username, password=None): 
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email = self.normalize_email(email), #deixar o email em lowercase, puxa de BaseUserManager
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    '''
    esses campos abaixo são pre-definidos pelo django, não é possível mudar o nome das variáveis, quando o django consumir esse arquivo irá procurar por eles.
    USERNAME_FIELD é a variavel que o django olha para ver quando campo o usuário irá logar no sistema
    '''
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ] #campo que serão requisitados

    objects = MyAccountManager()

    def __str__(self):
        return self.email #essa é a informação que vai printar na tela
    
    def has_perm(self, perm, ojb=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
