#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
and prints the new state's id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username, password, database = sys.argv[1:4]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
