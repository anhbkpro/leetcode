from lc_332_reconstruct_itinerary import Solution

solution = Solution()


def test_find_itinerary():
    assert solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) \
           == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) \
           == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
