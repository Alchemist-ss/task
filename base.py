from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, DECIMAL, Boolean, Date, ForeignKey


# Метаданные - это информаци о данных в БД.
meta = MetaData()

# Создание таблицы "Люди"
People = Table('People', meta,
        Column('ID_people', Integer, primary_key=True),
        Column('Year_Birth', Integer),
        Column('Education', String(250), nullable=False), # nullable - это команда для того чтобы обязательное имя было заполнено
        Column('Marital_Status', String(250), nullable=False),
        Column('Income', DECIMAL),
        Column('Kidhome', Boolean),
        Column('Teenhome', Boolean),
        Column('Dt_Customer', Date),
        Column('Recency', Integer),
        Column('Complain', Boolean),
        Column('Z_CostContact', Integer),
        Column('Z_Revenue', Integer),
        Column('Response', Integer)
)

# Создание таблицы "Продуты"
Products = Table('Products', meta,
        Column('ID_products', Integer, primary_key=True),
        Column('MntWines', DECIMAL),
        Column('MntFruits', DECIMAL),
        Column('MntMeatProducts', DECIMAL),
        Column('MntFishProducts', DECIMAL),
        Column('MntSweetProducts', DECIMAL),
        Column('MntGoldProds', DECIMAL)
)
# Создание таблицы "Продажи-Продвижение"
Promotion = Table('Promotion', meta,
        Column('ID_promotion', Integer, primary_key=True),
        Column('NumDealsPurchases', Integer),
        Column('NumWebPurchases', Integer),
        Column('NumCatalogPurchases', Integer),
        Column('NumStorePurchases', Integer),
        Column('NumWebVisitsMonth', Integer),
        Column('AcceptedCmp3', Integer),
        Column('AcceptedCmp4', Integer),
        Column('AcceptedCmp5', Integer),
        Column('AcceptedCmp1', Integer),
        Column('AcceptedCmp2', Integer)
)

#Подключаем к БД и вносим данные
engine = create_engine("mysql+mysqlconnector://root:Gt;St+d7SovX@localhost/mysql", echo=True)
meta.create_all(engine)

conn = engine.connect()

#kk = People.insert().values(Year_Birth=1996)
#conn.execute(kk)

