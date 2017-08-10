import webbrowser

class Moive():
    """ This class provides a way to store moive related infomation """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, moive_title, moive_storyline, poster_image, trailer_youtube):
        self.title = moive_title
        self.storyline = moive_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)