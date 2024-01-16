#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Float
from models.amenity import Amenity
from models.review import Review
from os import getenv




amenity_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan',
                               passive_deletes=True)
    
    amenities = relationship('Amenity', backref='place_amenities',
                                 cascade='all, delete',
                                 secondary="place_amenity",
                                 viewonly=False,
                                 passive_deletes=True)
    
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            reviewslist = []
            for r in list(models.storage.all(Review).values()):
                if r.place_id == self.id:
                    reviewslist.append(r)
            return reviewslist

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenityslist = []
            for a in list(models.storage.all(Amenity).values()):
                if a.id in self.amenity_ids:
                    amenityslist.append(a)
            return amenityslist

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
