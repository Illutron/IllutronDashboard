# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b-6!khjsadlgfiiawer3bv%4kcv-^h1tag6e_!2_iw'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test.db',                      # Or path to database file if using sqlite3.
    }
}