import os


def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 16005 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'test1234')
    user, db_name = 'covidscreener', 'covidscreener'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
