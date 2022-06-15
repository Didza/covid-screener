import os


def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 54041 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'test1234')
    user, db_name = 'covid_screener', 'covid_screener'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"