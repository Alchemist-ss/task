from sqlalchemy import Table, Column, Integer, String, MetaData, DECIMAL, Boolean, Date
from config import engine
from main import read_csv

# Метаданные - это информаци о данных в БД. 
meta = MetaData()

# nullable - это команда для того чтобы обязательное имя было заполнено
# Создание таблицы о информации людей
info_tb = Table('info_tb', meta,
        Column('ID', Integer, primary_key=True),
        Column('Year_Birthh', Integer),
        Column('Education', String(250)),
        Column('Marital_Status', String(250)),
        Column('Income', DECIMAL),
        Column('Kidhome', Boolean),
        Column('Teenhome', Boolean),
        Column('Dt_Customer', Date),
        Column('Recency', Integer),
        Column('Complain', Boolean),
        Column('Z_CostContact', Integer),
        Column('Z_Revenue', Integer),
        Column('Response', Integer),
# Продукты
        Column('MntWines', DECIMAL),
        Column('MntFruits', DECIMAL),
        Column('MntMeatProducts', DECIMAL),
        Column('MntFishProducts', DECIMAL),
        Column('MntSweetProducts', DECIMAL),
        Column('MntGoldProds', DECIMAL),
# Продажи-Продвижение
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

# Подключаем к БД и вносим данные
meta.create_all(engine)
conn = engine.connect()

# Чтение CSV файлика

# для вывода столбцов
#csv_columns = read_csv.columns.values
#kk = info_tb.insert().values(Year_Birthh = csv_columns[1])
#print()