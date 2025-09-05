DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projeto_integrador',          # O nome do banco de dados que você criou
        'USER': 'projeto_integrador_user',        # O usuário que você criou
        'PASSWORD': 'projeto_integrador_user', # A senha que você definiu
        'HOST': 'localhost',             # Ou o endereço do seu servidor de BD (ex: 127.0.0.1)
        'PORT': '3306',                  # A porta padrão do MySQL
    }
}
