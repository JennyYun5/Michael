import string

from sqlalchemy import Column, Integer, Sequence, String, create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

Base = declarative_base()

fields = string.digits
random_nbr = ''.join(random.sample(fields, 2))
print(random_nbr)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(String(20))

class Random_table(Base):
    __tablename__ = 'random_code'
    id = Column(Integer, Sequence('id'), primary_key=True)
    code = Column(String(200))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
metadata = MetaData(engine)
Base.metadata.drop_all(engine)


user_table = Table('user', metadata,
                Column('id', Integer, primary_key=True),
                Column('name',String(20))
                   )

user_table = Table('random_code', metadata,
        Column('id', Integer,primary_key=True),
        Column('code', String(200))
        )

metadata.create_all()


DBsession = sessionmaker(bind=engine)
# add data in DB
session = DBsession()
new_user = User(id=random_nbr, name='The fist record')
session.add(new_user)
session.commit()

# quary data in DB
quary_u1 = session.query(User).filter(User.id == random_nbr).one()
print(quary_u1.id, quary_u1.name, type(quary_u1))
session.close()


#Michael02

fields = string.ascii_letters + string.digits


def get_random_sample():
    a = ''.join(random.sample(fields, 5))
    return a


def get_nbr1(randomCount, nbr=1):
    count = 0
    for i in range(randomCount):
        count += 1
        a = '-'.join([get_random_sample() for j in range(nbr)])
        print(count)
        yield a, count

if __name__ == '__main__':
    for i in get_nbr1(200, 5):
        print(i)
        new_code = Random_table(id=i[1], code=i[0])
        session.add(new_code)
        session.commit()
        session.close()





