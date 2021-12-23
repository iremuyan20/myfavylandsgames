import sqlite3

con = sqlite3.connect("MyFavYlandsGames.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS games (GameName TEXT,Stars INT,GameCreator TEXT,Downloads INT,Updated TEXT)")
    con.commit()
    
GameContent = [
    ('SNOWY SURVIVAL',4,'iremxx',1038,'06/05/2021'),
    ('SAYLOR',4,'MYRIK',48917,'15/12/2019'),
    ('CITY SHOOTOUT - WINTER',4,'NaruTheHuman',131633,'18/12/2019'),
    ('YLANDS EXPLORATION DEMO',4,'MajorGeneral',79256,'28/03/2020'),
    ('YLAND CITY',4,'Paranoid',8087,'02/01/2018'),
    ('FEAST',4,'Ocnog',5268,'06/11/2020'),
    ('GATECRASH ALPHA 5 BIG MAP',5,'Bartsmps',2640,'01/08/2021')
    
]

cursor.executemany('INSERT INTO games(GameName,Stars,GameCreator,Downloads,Updated) VALUES (?,?,?,?,?)',GameContent)
con.commit()
cursor.execute(''' SELECT * FROM games''')


create_table()
con.close()