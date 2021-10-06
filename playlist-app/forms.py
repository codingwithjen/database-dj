"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional, Length, NumberRange


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[InputRequired()],)
    description = TextAreaField("Playlist Description", validators=[Optional(), Length(min=0, max=20)],)


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Title", validators=[InputRequired()],)
    artist = StringField("Artist", validators=[InputRequired()],)


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
