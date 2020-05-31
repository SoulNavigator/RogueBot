from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()
engine = engine = create_engine('sqlite:///littlebot/data.db')

class Guild(Base):
    __tablename__ = 'guilds'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lobby = Column(Integer)
    candidate = Column(Integer)
    meme = Column(Integer)
    
    def __init__(self, id:int, name:str='Test', lobby:int=-1, candidate:int=-1, meme:int=-1):
        self.id = id
        self.name = name
        self.lobby = lobby
        self.candidate = candidate
        self.meme = meme

def init():
    Base.metadata.create_all(engine)

def guild_exist(guild_id):
    Session = sessionmaker(bind=engine)
    pass

def add_guild(guild_id:int, guild_name:str):
    Session = sessionmaker(bind=engine)
    session = Session()
    entry = Guild(id=guild_id, name=guild_name)
    # pylint: disable=fixme, no-member
    try:
        session.add(entry)
        session.commit()
    except IntegrityError:
        raise Exception("Sorry, but this guild is already registered! :s")

