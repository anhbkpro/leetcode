from lc_735_asteroid_collision import asteroid_collision


def test_asteroid_collision():
    assert asteroid_collision(asteroids=[5, 10, -5]) == [5, 10]
    assert asteroid_collision(asteroids=[8, -8]) == []
    assert asteroid_collision(asteroids=[10, 2, -5]) == [10]
