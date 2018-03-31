class Movie:
    "A class for handle movie objects"

    def __init__(self, title, synopsis, poster_image, trailer_youtube):
        """Constructor of movie objects

        Attributes:
            title (str): title of the movie
            synopsis (str): synopsis of the movie
            poster_image (str): url of an image related to the movie
            trailer_youtube (str):url from the trailer obtained from youtube
        """

        self.title = title
        self.movie_synopsis = synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
