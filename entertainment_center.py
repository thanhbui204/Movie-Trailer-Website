import media
import fresh_tomatoes


hunger_games = media.Movie("Hunger Games - Mockingjay - Part 2",
                            "The story continues from Part 1 with Katniss Everdeen" +  # noqa
                                "preparing to win the war against President Snow and the tyrannical Capitol.",  # noqa
                            "https://upload.wikimedia.org/wikipedia/en/9/9d/Mockingjay_Part_2_Poster.jpg",  # noqa
                            "hhttps://www.youtube.com/watch?v=n-7K_OjsDCQ")  # noqa

iron_man3 = media.Movie("Iron Man 3",
                        "Tony Stark deals with posttraumatic stress disorder caused by the events of The Avengers, while investigating a string" +  # noqa
                            "of terrorist attacks led by the mysterious Mandarin, and comes into a conflict with an old enemy: Aldrich Killian.",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=2CzoSeClcw0")

infinity_war = media.Movie("Infinity war",
                        "The Avengers and the Guardians of the Galaxy attempt to stop" +  # noqa
                            " Thanos from amassing the all-powerful Infinity Stones.",  # noqa
                        "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

mission_impossible = media.Movie("Mission: Impossible - Rogue Nation",
            "IMF agent Ethan Hunt is on the run from the CIA, following the IMF's disbandment as " +  # noqa
                "he tries to prove the existence of the Syndicate, a mysterious international terrorist consortium.",  # noqa
            "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",  # noqa
            "https://www.youtube.com/watch?v=gOW_azQbOjw")

deadpool = media.Movie("Deadpool",
            " American superhero film based on the Marvel Comics character of the same name" +  # noqa
                " In Deadpool, Wade Wilson hunts the man who gave him mutant abilities, but" +  # noqa
                "also a scarred physical appearance, as the antihero Deadpool.",  # noqa
            "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",  # noqa
            "https://www.youtube.com/watch?v=D86RtevtfrA")

the_expendables3 = media.Movie("The Expendables 3",
            "The story follows the mercenary group known as The Expendables as they come into" +  # noqa
                "conflict with ruthless arms dealer Conrad Stonebanks, the Expendables' co-founder," +  # noqa
                "who is determined to destroy the team.",
            "https://upload.wikimedia.org/wikipedia/en/5/55/Expendables_3_poster.jpg",  # noqa
            "https://www.youtube.com/watch?v=4xD0junWlFc")

movies = [deadpool, the_expendables3, mission_impossible, hunger_games, iron_man3, infinity_war]  # noqa
fresh_tomatoes.open_movies_page(movies)
