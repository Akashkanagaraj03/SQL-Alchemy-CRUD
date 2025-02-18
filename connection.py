from sqlalchemy import create_engine

user = "postgres"
password = "1243"
server = "localhost"
port = "5432"
database = "task2"

engine = create_engine(f'postgresql://{user}:{password}@{server}:{port}/{database}', echo=True)

try:
    with engine.connect() as connection:
        print("Connected")
except Exception as e:
    print(f"Error: {e}")