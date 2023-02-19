SECRET_KEY = {
    'secret'    :'django-insecure-eli!26m=wo0*oid4#jmm=o-(4@#^ik3!-f&6u2lq=y_64psg3i',
    'algorithm' :'HS256'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset'     : 'utf8mb4',
            'use_unicode' : True,
        },
    }
}
