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
    # Special roles IDs
    member = Column(Integer)
    guest = Column(Integer)
    meme = Column(Integer)
    
    def __init__(self, id:int, name:str='Test', lobby:int=-1, member:int=-1, guest:int=-1, meme:int=-1):
        self.id = id
        self.name = name
        self.lobby = lobby
        self.member = member
        self.guest = guest
        self.meme = meme

def init():
    Base.metadata.create_all(engine)

# Рефакторинг этого говна

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


def set_member(guild_id:int, role_id:int):
    Session = sessionmaker(bind=engine)
    session = Session()
    # pylint: disable=fixme, no-member
    try:
        current_guild = session.query(Guild).get(guild_id)
        current_guild.member = role_id
        session.add(current_guild)
        session.commit()
    except:
        Exception("Couldn't set this role as a member")


def get_member(guild_id:int):
    Session = sessionmaker(bind=engine)
    session = Session()
    # pylint: disable=fixme, no-member
    try:
        current_guild = session.query(Guild).get(guild_id)
        session.commit()
        return current_guild.member
    except:
        Exception("Member role doesn't exist yet")


def remove_guild(guild_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    # pylint: disable=fixme, no-member
    current_guild = session.query(Guild).get(guild_id)
    session.delete(current_guild)
    session.commit()


def add_lobby(guild_id:int, channel_id:int):
    Session = sessionmaker(bind=engine)
    session = Session()
    # pylint: disable=fixme, no-member
    try:
        current_guild = session.query(Guild).get(guild_id)
        current_guild.lobby = channel_id
        session.add(current_guild)
        session.commit()
    except:
        Exception("This guild probably doesn't exist")
