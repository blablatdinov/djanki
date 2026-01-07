REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Snippets API',
    'DESCRIPTION': 'Test description',
    'VERSION': 'v1',
    'SERVE_INCLUDE_SCHEMA': False,
    'TOS': 'https://www.google.com/policies/terms/',
    'CONTACT': {'email': 'contact@snippets.local'},
    'LICENSE': {'name': 'BSD License'},
}
