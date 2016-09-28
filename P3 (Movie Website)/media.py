#Project : Movie Website
#File : media.py

#In this file Movie class is created and a function __init__ is called
#Double underscore before and after init function is used to signify that that
#init is reserved and is a predefined method.

import webbrowser
#The webbrowser module provides a high-level interface to allow displaying Web-based documents to users.
class Movie():
    """ This class provides a way to store movie related iniformation """
    #This class calls the __init__ function which takes movie_title,poster_image,_trailer_youtube,_image_alt as input.
    
    def __init__(self,movie_title,movie_genre,poster_image,trailer_youtube,image_alt):
        #self refers to the newly created object. In other class methods, it refers to the instance whose method was called.
        #Here self will refer to the new movie object created in the entertainment_center.py file.
        
        self.title = movie_title
        #self.title stores the title of the movie
        self.genre = movie_genre
        #self.genre stores the genre of the movie
        self.poster_image_url = poster_image
        #self.poster stores the source of the poster for movie
        self.trailer_youtube_url = trailer_youtube
        #self.trailer stores the url of the trailer of the movie
        self.alt = image_alt
        #self.alt is used to store the alternate image to the poster of the image. 

    def show_trailer(self):
        webbrowser.open(self.trailer_image_url)
        #This command is used to open a web page of url mentioned in brackets in the same tab 
            
