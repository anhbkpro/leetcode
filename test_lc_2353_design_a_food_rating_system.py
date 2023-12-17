from lc_2353_design_a_food_rating_system import FoodRatings
food_ratings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])

def test_food_ratings():
    assert food_ratings.highestRated("korean") is "kimchi"
    assert food_ratings.highestRated("japanese") is "ramen"
    assert food_ratings.highestRated("greek") is "moussaka"
    food_ratings.changeRating("bulgogi", 10)
    assert food_ratings.highestRated("korean") is "bulgogi"
