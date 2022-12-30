import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User(name = {self.name}, fullname = {self.fullname}, nickname={self.nickname})>"

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

#dodawanie usera do bazy
j_user = User(name="Marcin", fullname="Marcin Albiniak", nickname="al")
session.add(j_user)
session.commit()

k_user = User(name="Roman", fullname="Roman Majcher", nickname="majek")
session.add(k_user)
session.commit()

Session = sessionmaker(bind=engine)
session = Session()

for s in session.query(User).all():
    print(s.fullname)

