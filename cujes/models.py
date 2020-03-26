from cujes import db
from enum import Enum, auto
from slugify import slugify
from datetime import datetime


# association table which models a many-to-many relationship between
# artists and seasons
seasons_artists = db.Table(
    'seasonsArtists',
    db.Column('season_id', db.Integer, db.ForeignKey('seasons.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True)
)


class SeasonStatus(Enum):
    """
    This class is an enumeration of possible statuses of each season
    """

    upcoming = auto()
    applications_open = auto()
    applications_closed = auto()
    in_progress = auto()
    finished = auto()


class ApplicationStatus(Enum):
    """
    This class is an enumeration of possible statuses of each artist application
    """

    received = auto()
    approved = auto()
    declined = auto()


class Season(db.Model):
    """
    This class models the season instances, to be used with SQLAlchemy, which
    will map the class to an SQL table.
    """

    __tablename__ = "seasons"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(64), unique=True, nullable=False)
    slug = db.Column(db.String(64), unique=True)
    status = db.Column(db.Enum(SeasonStatus), nullable=False)
    # note: "artists" is the name of the Postgres table, not the Python class
    winner_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=True)
    participants = db.relationship("Artist",
                                   secondary=seasons_artists,
                                   lazy='subquery',
                                   backref=db.backref('seasons', lazy=True))

    def __init__(self, *args, **kwargs):
        """
        Override the default constructor to autopopulate the slug field
        """
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('year', ''))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """
        Override the default string representation method
        """
        return '<Season: {}; Status: {}>'.format(self.year, self.status)


class Artist(db.Model):
    """
    This class models the artist instances, to be used with SQLAlchemy, which
    will map the class to an SQL table.
    """

    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), unique=True, nullable=False)
    slug = db.Column(db.String(127), unique=True)
    town = db.Column(db.String(127), unique=True, nullable=False)
    form_year = db.Column(db.DateTime, nullable=False)
    bio = db.Column(db.Text, nullable=False)

    # path storage needs to be changed once the form is implemented
    demo_path = db.Column(db.String(255))
    image_path = db.Column(db.String(255))

    # note: "Season" is the name of the Python class, not the Postgres table
    won_seasons = db.relationship("Season", backref="winner", lazy="dynamic")
    applications = db.relationship("Application", backref="artist", lazy="dynamic")

    def __init__(self, *args, **kwargs):
        """
        Override the default constructor to autopopulate the slug field
        """
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """
        Override the default string representation method
        """
        return '<Artist: {}>'.format(self.name)


class Post(db.Model):
    """
    This class models the news post instances, to be used with SQLAlchemy, which
    will map the class to an SQL table.
    """

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    slug = db.Column(db.String(255), unique=True)
    abstract = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    # path storage needs to be changed after admin page is done
    image_path = db.Column(db.String(255))
    author = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Override the default constructor to autopopulate the slug field
        """
        if 'slug' not in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        if 'date' not in kwargs:
            kwargs['date'] = datetime.today()
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """
        Override the default string representation method
        """
        return '<Post: {}>'.format(self.title)


class Application(db.Model):
    """
    This class models the artists' application instances, to be used with SQLAlchemy, which
    will map the class to an SQL table.
    """

    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    status = db.Column(db.Enum(ApplicationStatus), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Override the default constructor to autopopulate several fields
        """
        kwargs['slug'] = slugify(kwargs.get('title', ''))
        kwargs['date'] = datetime.today()
        kwargs['status'] = ApplicationStatus.received
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """
        Override the default string representation method
        """
        return '<Application - ArtistID: {}; E-mail: {}>'.format(self.artist_id, self.email)
