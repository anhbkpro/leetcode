from .course_schedule_ii import Solution
import pytest


def is_valid_order(order, prerequisites):
    """Helper function to verify if the course order is valid"""
    if not order:
        return False
    position = {course: i for i, course in enumerate(order)}
    for course, prereq in prerequisites:
        if course in position and prereq in position:
            if position[course] <= position[prereq]:
                return False
    return True


@pytest.fixture
def solution():
    return Solution()


def test_no_prerequisites(solution):
    order = solution.findOrder(1, [])
    assert order == [0]

    order = solution.findOrder(3, [])
    assert set(order) == {0, 1, 2}  # any order is valid


def test_single_course(solution):
    order = solution.findOrder(1, [])
    assert order == [0]


def test_two_courses_no_cycle(solution):
    prerequisites = [[1, 0]]  # course 1 depends on course 0
    order = solution.findOrder(2, prerequisites)
    assert order == [0, 1]


def test_two_courses_with_cycle(solution):
    prerequisites = [[1, 0], [0, 1]]  # courses depend on each other
    order = solution.findOrder(2, prerequisites)
    assert order == []


def test_multiple_independent_courses(solution):
    prerequisites = [[1, 0], [3, 2]]  # two independent pairs
    order = solution.findOrder(4, prerequisites)
    assert is_valid_order(order, prerequisites)
    assert set(order) == {0, 1, 2, 3}


def test_multiple_dependent_courses(solution):
    prerequisites = [[1, 0], [2, 1], [3, 2]]  # linear dependency
    order = solution.findOrder(4, prerequisites)
    assert order == [0, 1, 2, 3]


def test_complex_dependencies(solution):
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = solution.findOrder(4, prerequisites)
    assert is_valid_order(order, prerequisites)
    assert set(order) == {0, 1, 2, 3}


def test_complex_cycle(solution):
    prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]
    order = solution.findOrder(4, prerequisites)
    assert order == []


def test_self_dependent_course(solution):
    prerequisites = [[0, 0]]  # course depends on itself
    order = solution.findOrder(1, prerequisites)
    assert order == []


def test_multiple_valid_orders(solution):
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = solution.findOrder(4, prerequisites)
    assert is_valid_order(order, prerequisites)
    assert len(order) == 4
    assert set(order) == {0, 1, 2, 3}


def test_disconnected_components(solution):
    prerequisites = [[1, 0], [3, 2]]  # two separate components
    order = solution.findOrder(4, prerequisites)
    assert is_valid_order(order, prerequisites)
    assert set(order) == {0, 1, 2, 3}


def test_multiple_prerequisites_for_course(solution):
    prerequisites = [[3, 0], [3, 1], [3, 2]]
    order = solution.findOrder(4, prerequisites)
    assert is_valid_order(order, prerequisites)
    assert set(order) == {0, 1, 2, 3}
    # Course 3 should be last
    assert order[-1] == 3


def test_large_course_numbers(solution):
    prerequisites = [[999, 998], [998, 997]]
    order = solution.findOrder(1000, prerequisites)
    assert is_valid_order(order, prerequisites)
    assert len(order) == 1000


def test_all_courses_connected(solution):
    prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3]]
    order = solution.findOrder(5, prerequisites)
    assert order == [0, 1, 2, 3, 4]
