import fresh_tomatoes

from Movie import Movie

thenumber = Movie("The Number 23",
                  "A story of a man who has a problem with the number 23",
                  "https://upload.wikimedia.org/wikipedia/en/c/cc/Number23.jpg",
                  "https://www.youtube.com/watch?v=4ElUBr6-GLU")

dragon = Movie("Crunching Tiger Hidden Dragon",
                "The film is set in the Qing Dynasty during the 43rd year of the reign of the Qianlong Emperor",
                "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",
                "https://www.youtube.com/watch?v=WdhvxJZDqzU")

avatar = Movie("Avatar",
               "A marine in a alien planet",
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

revolver = Movie("Revolver",
                  "Dorothy Macha is a gang boss involved in illegal gambling all over the city.",
                  "http://ecx.images-amazon.com/images/I/51FHH9YR1DL.jpg",
                  "https://www.youtube.com/watch?v=M9JAYfZOHms")

insidious = Movie("Insidious",
                  "A married couple, their sons Dalton and Foster, and infant daughter Cali have recently moved into a new home.",
                  "https://upload.wikimedia.org/wikipedia/en/2/2d/Insidious_poster.jpg",
                  "https://www.youtube.com/watch?v=zuZnRUcoWos")

cyborg = Movie("Cyborg She",
                "iro Kitamura is spending his 20th birthday alone.",
                "https://upload.wikimedia.org/wikipedia/en/b/b1/Cyborg_She.jpg",
                "https://www.youtube.com/watch?v=iAkzga9mA6k")

imcyborg = Movie("Im a cyborg, but that is ok",
                  "The film takes place mostly in a mental institution filled with an eclectic menagerie of patients",
                  "http://www.marthagarzon.com/contemporary_art/wp-content/gallery/cyborg/im_a_cyborg_but_thats_ok.jpg",
                  "https://www.youtube.com/watch?v=1KaOLDZe2GI")


movies = [thenumber, revolver, avatar,
          insidious, cyborg, imcyborg, dragon]

fresh_tomatoes.open_movies_page(movies)
