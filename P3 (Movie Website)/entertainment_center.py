#Project : Movie Trailer Webpage
#This file includes the data of all the movies.
#After adding the movies a list of all the movies is created and freshmovies.py file is opened and this list is given as input to the file.
#On executing this code fresh_tomatoes.html file is created and you can open it to open your Movie Trailer Webpage

import media
#This importes the media.py file stored in the same folder. This is done so that the variable used in media.py file can also be used here.

import fresh_tomatoes
#This importes the fresh_tomatoes.py file stored in the same folder as this file.

maze_runner = media.Movie("Maze Runner Scorch Trials","2015 . Science Fiction/Thriller",
                          "http://www.impawards.com/2015/posters/maze_runner_the_scorch_trials.jpg",
                          "https://www.youtube.com/watch?v=EKawDPkcYdY","Maze Runner Poster")
#media.Movie depicts that in media.py file Movie class is accessed and is given the input the list in the brackets.

doctor_strange = media.Movie("Doctor Strange","2016 . Fantasy/Science Fiction",
                             "http://orig05.deviantart.net/394a/f/2016/103/2/9/doctor_strange_poster__by_sajalhasan-d9yv1ui.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM","Doctor Strange Poster")
#doctor_strange movie object is created and is given the values such as title,release year, poster src and trailer url
miracles_from_heaven = media.Movie("Miracles From Heaven","2016 . Drama/Biography",
                                   "http://www.impawards.com/2016/posters/miracles_from_heaven.jpg",
                                   "https://www.youtube.com/watch?v=CldGTG6iVrU","Miracles From Heaven Poster")
#miracles_from_heaven movie object is created and is given the values such as title,release year, poster src and trailer url
now_you_see_me = media.Movie("Now You See Me","2013 . Crime/Caper Story"
                             ,"https://images-na.ssl-images-amazon.com/images/M/MV5BMTY0NDY3MDMxN15BMl5BanBnXkFtZTcwOTM5NzMzOQ@@._V1_SX640_SY720_.jpg",
                             "https://www.youtube.com/watch?v=KzJNYYkkhzc","Now You See Me Poster")
#now_you_see_me movie object is created and is given the values such as title,release year, poster src and trailer url
kung_fu_panda3 = media.Movie("Kung Fu Panda 3","2016 . Action/Adventure",
                             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd0kB6hFjkiIPKHkU4qgZfaPtNeFGH2rTUXX4cUpY8twUhKfCX",
                             "https://www.youtube.com/watch?v=fGPPfZIvtCw","Kung Fu Panda 3 Poster")
#kung_fu_panda3 movie object is created and is given the values such as title,release year, poster src and trailer url
fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them",
                               "2016 . Fantasy/Action","https://upload.wikimedia.org/wikipedia/en/5/5e/Fantastic_Beasts_and_Where_to_Find_Them_poster.png",
                               "https://www.youtube.com/watch?v=flypX4XT3qE","Fantastic Beasts Poster")
#fantastic_beasts movie object is created and is given the values such as title,release year, poster src and trailer url
avatar = media.Movie("Avatar","2009 . Fantasy/Science Fiction",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY","Avatar poster")
#avatar movie object is created and is given the values such as title,release year, poster src and trailer url

pink = media.Movie("Pink","2016 . Drama / Thriller",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Pinkmovieposter.jpg/220px-Pinkmovieposter.jpg",
                   "https://www.youtube.com/watch?v=AL2TShb6fFs","Pink Poster")
#pink movie object is created and is given the values such as title,release year, poster src and trailer url


harry_potter = media.Movie("Harry Potter and The Deathly Hallows Part 2","2011 . Fantasy/Drama",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg/220px-Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
                            "https://www.youtube.com/watch?v=mObK5XD8udk","Harry Potter Poster")

#harry_potter movie object is created and is given the values such as title,release year, poster src and trailer url

jump_street = media.Movie("22 Jump Street","2014 . Action/Comedy",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/1d/22_Jump_Street_Poster.png/220px-22_Jump_Street_Poster.png",
                             "https://www.youtube.com/watch?v=v9S_dYuq0vE","Jump Street Poster")
#jump_street movie object is created and is given the values such as title,release year, poster src and trailer url

frozen = media.Movie("Frozen","2013 . Fantasy/Comedy music",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc","Frozen Poster")
#frozen movie object is created and is given the values such as title,release year, poster src and trailer url

dragon = media.Movie("How To Train Your Dragon 2","2014 . Fantasy/Action",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/How_to_Train_Your_Dragon_2_poster.jpg/220px-How_to_Train_Your_Dragon_2_poster.jpg",
                     "https://www.youtube.com/watch?v=68AqHwgk2s8","How To Train Your Dragon 2")
#dragon movie object is created and is given the values such as title,release year, poster src and trailer url

movies = [pink,jump_street,harry_potter,fantastic_beasts,dragon,kung_fu_panda3,frozen,avatar,maze_runner,doctor_strange,miracles_from_heaven,now_you_see_me]
#An list of all the movie objects is ceated.
fresh_tomatoes.open_movies_page(movies)
#The list created is passed into open_movies_page function in fresh_tomatoes.py file.


