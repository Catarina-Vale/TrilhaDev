from Engine_to_azure import Base

from sqlalchemy import Column, Integer, String

class Repository(Base):
    __tablename__ = 'Repositories'
    username = Column(String(50))
    reponame = Column(String(50))

    def __init__(self, username, reponame):
        self.username = username
        self.reponame = reponame
