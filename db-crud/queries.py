from models.actor import Actor
from models.base import Session, engine, Base
from models.contact_details import ContactDetails
from models.movie import Movie
from models.stuntman import Stuntman
from datetime import date

session = Session()

# Get all movies from DB
# movies = session.query(Movie).all()

# Get recent movies after 01-01-2015
#movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1))

# Get movies that Dwayne Johnson acted in
# movies = session.query(Movie).join(Actor, Movie.actors).filter(Actor.name == "Dwayne Johnson")
#
# print('\n ### All movies that were returned by DB:')
# for movie in movies:
#     print(movie.title, movie.release_date)

# Get actors with house in Glendale
actors = session.query(Actor).join(ContactDetails).filter(ContactDetails.address.contains("Glendale"))
for actor in actors:
    print(actor.name)

session.close()

