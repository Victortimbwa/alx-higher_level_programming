#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username, password, database, search_name = sys.argv[1:5]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == search_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
