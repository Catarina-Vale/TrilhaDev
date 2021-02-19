import urllib

from sqlalchemy import create_engine


from sqlalchemy.ext.declarative import declarative_base


server = 'alexandre-server.database.windows.net'
database = 'oiojoio'
username = 'cloudadmin'
password =  'D0ffy123'
driver = '{ODBC Driver 17 for SQL Server}'


odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)


engine = create_engine(connect_str, echo=True)

Base = declarative_base()
    

