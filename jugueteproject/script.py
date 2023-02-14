from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


file = 'categorias.txt'

engine = create_engine('sqlite:///db.sqlite3', echo=True)
session = Session(engine)

with Session(engine) as session:
    stmt = select(worker).all()
    rows = session.execute(stmt)
    print(rows)
    
#with open(file, 'r') as f:
#    line = f.readlines()


#print(line)



