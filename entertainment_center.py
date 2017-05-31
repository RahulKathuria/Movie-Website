import fresh_tomatoes
import media

thirteen_reasons = media.Movie("13 Reasons Why",
                         "Follows teenager Clay Jensen, in his quest to uncover the story behind his classmate and crush, Hannah, and her decision to end her life.",
                         "https://2.bp.blogspot.com/-zGJ8q3MjZ6o/WIj19lZ7HrI/AAAAAAAAQd4/QugAgRS0p5EVq-BVZtXh8us6lyu_jvG7gCLcB/s1600/13ReasonsWhy%2B%255Bwww.imagesplitter.net%255D.jpeg",
                         "https://www.youtube.com/watch?v=JebwYGn5Z3E")

flash = media.Movie("The Flash",
                    "The Flash (Barry Allen) is a fictional superhero appearing in American comic books published by DC Comics. ... Barry Allen is a reinvention of a previous character called The Flash that had appeared in 1940s comic books as the character Jay Garrick. His power consists mainly of superhuman speed.",
                    "http://img09.deviantart.net/4653/i/2015/161/2/5/the_flash___fan_made_poster_by_eduardohurtado-d8w70f6.png",
                    "https://www.youtube.com/watch?v=Yj0l7iGKh8g")

iron_man = media.Movie("Iron Man",
            "A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.",
            "http://i.ebayimg.com/00/s/NTAwWDMzOQ==/z/k1IAAOxycD9TVkwT/$_35.JPG?set_id=2",
            "https://www.youtube.com/watch?v=8hYlB38asDY")

pirates = media.Movie("Pirates of the caribbean",
                      "Capt. Jack Sparrow (Johnny Depp) arrives at Port Royal in the Caribbean without a ship or crew. His timing is inopportune, however, because later that evening the town is besieged by a pirate ship. The pirates kidnap the governor's daughter, Elizabeth (Keira Knightley), who's in possession of a valuable coin that is linked to a curse that has transformed the pirates into the undead. A gallant blacksmith (Orlando Bloom) in love with Elizabeth allies with Sparrow in pursuit of the pirates.",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQySvhDSAcIekqATXtaZfWgm_ZDzXYr9gyl3PCATN-3gyLDWal0",
                      "https://www.youtube.com/watch?v=lsJ58L3u8qw")
logan = media.Movie("Logan",
                    "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border. His plan to hide from the outside world gets upended when he meets a young mutant (Dafne Keen) who is very much like him. Logan must now protect the girl and battle the dark forces that want to capture her.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")
justice_league = media.Movie("Justice League",
                             "Fueled by his restored faith in humanity and inspired by Superman's (Henry Cavill) selfless act, Bruce Wayne (Ben Affleck) enlists newfound ally Diana Prince to face an even greater threat. Together, Batman and Wonder Woman work quickly to recruit a team to stand against this newly awakened enemy. Despite the formation of an unprecedented league of heroes -- Batman, Wonder Woman, Aquaman, Cyborg and the Flash -- it may be too late to save the planet from an assault of catastrophic proportions.",
                             "http://t2.gstatic.com/images?q=tbn:ANd9GcQl4jDmsaajCfFvMRLWm7-3-lsXaJ4jc5BsJcpNZi1FypJUFuwE",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")
movies = [thirteen_reasons, flash, iron_man, pirates, logan, justice_league]
fresh_tomatoes.open_movies_page(movies)

