from fastapi import FastAPI

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy import select, create_engine
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base, Session, relationship

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/jojo")
async def jojo():
    return {"Jojo": "NO"}

@app.get('/db-setup')
async def db_setup():
    metadata = MetaData()
    # engine = create_engine('mysql:///some.db', echo=True)
    engine = create_engine('mysql+mysqldb://rip_user:rip_pass@mysql-service/rip_db', echo=True)

    Base = declarative_base()


    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True, autoincrement=True)
        username = Column(String(50), nullable=False)
        fullname = Column(String(255))
        addresses = relationship('Address', back_populates='user')


    class Address(Base):
        __tablename__ = 'addresses'
        address_id = Column(Integer, primary_key=True, autoincrement=True)
        address = Column(String(128), nullable=False)
        zip = Column(String(16))
        state = Column(String(2))
        user_id = Column(Integer, ForeignKey('users.id'))
        user = relationship("User", back_populates="addresses")

    with engine.begin() as connection:
        Base.metadata.create_all(connection)
