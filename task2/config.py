from sqlalchemy import create_engine

engine = create_engine("postgresql://alchemist:qwer1243@127.0.0.1:5432/mydb", echo=True)