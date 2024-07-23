from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    main = Column(String)
    temp = Column(Float)
    feels_like = Column(Float)
    dt = Column(DateTime)

engine = create_engine('sqlite:///weather.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
