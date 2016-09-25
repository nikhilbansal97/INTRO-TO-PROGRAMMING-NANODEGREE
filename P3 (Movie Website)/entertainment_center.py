#Project : Movie Trailer Webpage

#On executing this code fresh_tomatoes.html file is created and you can open it to open your Movie Trailer Webpage

import media
#This importes the media.py file stored in the same folder. This is done so that the variable used in media.py file can also be used here.

import fresh_tomatoes
#This importes the fresh_tomatoes.py file stored in the same folder as this file.

maze_runner = media.Movie("Maze Runner Scorch Trials","2015 . Science Fiction/Thriller",
                          "http://www.impawards.com/2015/posters/maze_runner_the_scorch_trials.jpg",
                          "https://www.youtube.com/watch?v=EKawDPkcYdY")
#media.Movie depicts that in media.py file Movie class is accessed and is given the input the list in the brackets.

doctor_strange = media.Movie("Doctor Strange","2016 . Fantasy/Science Fiction",
                             "http://orig05.deviantart.net/394a/f/2016/103/2/9/doctor_strange_poster__by_sajalhasan-d9yv1ui.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")
#doctor_strange movie object is created and is given the values such as title,release year, poster src and trailer url
miracles_from_heaven = media.Movie("Miracles From Heaven","2016 . Drama/Biography",
                                   "http://www.impawards.com/2016/posters/miracles_from_heaven.jpg",
                                   "https://www.youtube.com/watch?v=CldGTG6iVrU")
#miracles_from_heaven movie object is created and is given the values such as title,release year, poster src and trailer url
now_you_see_me = media.Movie("Now You See Me","2013 . Crime/Caper Story"
                             ,"https://images-na.ssl-images-amazon.com/images/M/MV5BMTY0NDY3MDMxN15BMl5BanBnXkFtZTcwOTM5NzMzOQ@@._V1_SX640_SY720_.jpg",
                             "https://www.youtube.com/watch?v=KzJNYYkkhzc")
#now_you_see_me movie object is created and is given the values such as title,release year, poster src and trailer url
kung_fu_panda3 = media.Movie("Kung Fu Panda 3","2016 . Action/Adventure",
                             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd0kB6hFjkiIPKHkU4qgZfaPtNeFGH2rTUXX4cUpY8twUhKfCX",
                             "https://www.youtube.com/watch?v=fGPPfZIvtCw")
#kung_fu_panda3 movie object is created and is given the values such as title,release year, poster src and trailer url
fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                               "2016 . Fantasy/Action","https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                               "https://www.youtube.com/watch?v=flypX4XT3qE")
#fantastic_beasts movie object is created and is given the values such as title,release year, poster src and trailer url

movies = [fantastic_beasts,kung_fu_panda3,maze_runner,doctor_strange,miracles_from_heaven,now_you_see_me]
#An array of all the movie objects is ceated.
fresh_tomatoes.open_movies_page(movies)
#The array created is passed into open_movies_page function in fresh_tomatoes.py file.


