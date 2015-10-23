import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg");

movies = [toy_story]
#fresh_tomatoes.open_movies_page(movies)
#toy_story.show_trailer()

print (media.Movie.__name__)
