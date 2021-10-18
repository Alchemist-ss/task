from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:Gt;St+d7SovX@localhost/mydb", echo=True)
# engine = create_engine("postgresql://alchemist:qwer1243@127.0.0.1:5432/mydb", echo=True) - для постгрес но вылетает ошибка "No module named 'psycopg2'", и причём импорт этой библиотеки невозможен....