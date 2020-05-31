import json
from os.path import isfile
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

datafile = 'littlebot\data2.json'

Base = declarative_base()

class Guild(Base):

    __tablename__ = 'honhon'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lobby = Column(Integer)
    candidate = Column(Integer)
    meme = Column(Integer)


# Переписать
def init():
    engine = create_engine('sqlite:///littlebot/data.db')
    Base.metadata.create_all(engine)


    if(isfile(datafile)):
        pass
    else:
        data = {
            "guilds" : []
        }
        with open(datafile, 'w') as file:
            json.dump(data, file)

init()

def guild_exists(guild_id) -> bool:
    with open(datafile, 'r') as file:
        json_file = json.load(file)
        guilds = json_file['guilds']
        for guild in guilds:
            if(guild['guild'] == guild_id):
                print("Such guild exist")
                return True
        return False

def add_guild(guild_id):
    if not guild_exists(guild_id):
        with open(datafile, 'r') as file:
            json_file = json.load(file)

        data = {'guild' : guild_id, 'lobby' : -1, 'candidate_role' : -1, 'meme_role' : -1}
        json_file['guilds'].append(data)    

        with open(datafile, 'w') as file:
           json.dump(json_file, file)

def set_channel(guild_id, channel_id):
    if guild_exists(guild_id):
        with open(datafile, 'r') as file:
            json_file = json.load(file)
        
        for guild in json_file['guilds']:
            if guild['guild'] == guild_id:
                guild['lobby'] = channel_id
                print(guild)
        
        with open(datafile, 'w') as file:
            json.dump(json_file, file)


def set_candidate_role(guild_id, role_id):
    if guild_exists(guild_id):
        with open(datafile, 'r') as file:
            json_file = json.load(file)
        
        for guild in json_file['guilds']:
            if guild['guild'] == guild_id:
                guild['candidate_role'] = role_id
        
        with open(datafile, 'w') as file:
            json.dump(json_file, file)

def set_meme_role(guild_id, role_id):
    if guild_exists(guild_id):
        with open(datafile, 'r') as file:
            json_file = json.load(file)
        
        for guild in json_file['guilds']:
            if guild['guild'] == guild_id:
                guild['meme_role'] = role_id
        
        with open(datafile, 'w') as file:
            json.dump(json_file, file)