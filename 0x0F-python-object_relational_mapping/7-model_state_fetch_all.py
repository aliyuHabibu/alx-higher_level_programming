#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}", pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for no, name in session.query(State.id, State.name).order_by(State.id):
        print(f"{no}: {name}")
