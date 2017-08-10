import media
import fresh_tomatoes

toy_stroy = media.Moive("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_stroy.storyline)


avatar = media.Moive("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_stroy, avatar]
#fresh_tomatoes.open_movies_page(movies)
print(media.Moive.VALID_RATINGS)
print(media.Moive.__doc__)
print(media.Moive.__name__)
print(media.Moive.__module__)