import webbrowser
class Movie():
    ''' This class provides a way to store movie information '''
    VALID_RATINGS = ["PG", "U", "R", "PG-13"]
    
    def __init__(self, name, desc, trailer, poster):
        self.title = name
        self.storyline = desc
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
