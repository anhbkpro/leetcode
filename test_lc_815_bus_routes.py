from lc_815_bus_routes import Solution


def test_num_buses_to_destination():
    assert Solution.numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6) == 2
    assert Solution.numBusesToDestination(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15,
                                          target=12) == -1
