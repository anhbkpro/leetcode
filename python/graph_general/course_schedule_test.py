import pytest

from .course_schedule import Solution


@pytest.fixture
def solution():
    return Solution()


def test_no_prerequisites(solution):
    assert solution.canFinish(1, []) == True
    assert solution.canFinish(5, []) == True


def test_single_course(solution):
    assert solution.canFinish(1, []) == True


def test_two_courses_no_cycle(solution):
    prerequisites = [[1, 0]]  # course 1 depends on course 0
    assert solution.canFinish(2, prerequisites) == True


def test_two_courses_with_cycle(solution):
    prerequisites = [[1, 0], [0, 1]]  # courses depend on each other
    assert solution.canFinish(2, prerequisites) == False


def test_multiple_independent_courses(solution):
    prerequisites = [[1, 0], [3, 2]]  # two independent pairs
    assert solution.canFinish(4, prerequisites) == True


def test_multiple_dependent_courses(solution):
    prerequisites = [[1, 0], [2, 1], [3, 2]]  # linear dependency
    assert solution.canFinish(4, prerequisites) == True


def test_complex_dependencies(solution):
    prerequisites = [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2],
    ]  # multiple courses depend on same prerequisite
    assert solution.canFinish(4, prerequisites) == True


def test_complex_cycle(solution):
    prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]  # cycle through multiple courses
    assert solution.canFinish(4, prerequisites) == False


def test_self_dependent_course(solution):
    prerequisites = [[0, 0]]  # course depends on itself
    assert solution.canFinish(1, prerequisites) == False


def test_multiple_prerequisites_for_course(solution):
    prerequisites = [[3, 0], [3, 1], [3, 2]]  # one course has multiple prerequisites
    assert solution.canFinish(4, prerequisites) == True


def test_disconnected_cycles(solution):
    prerequisites = [[0, 1], [1, 0], [2, 3], [3, 2]]  # cycle 1  # cycle 2
    assert solution.canFinish(4, prerequisites) == False


def test_large_course_numbers(solution):
    prerequisites = [[1, 999], [2, 998], [3, 997]]  # using large course numbers
    assert solution.canFinish(1000, prerequisites) == True


def test_all_courses_connected(solution):
    prerequisites = [
        [1, 0],
        [2, 1],
        [3, 2],
        [4, 3],
        [5, 4],
    ]  # each course depends on previous
    assert solution.canFinish(6, prerequisites) == True
