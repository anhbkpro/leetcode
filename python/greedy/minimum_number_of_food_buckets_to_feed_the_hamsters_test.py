from .minimum_number_of_food_buckets_to_feed_the_hamsters import Solution


def test_minimum_buckets():
    assert Solution().minimumBuckets("H..H") == 2
    assert Solution().minimumBuckets(".H.H.") == 1
    assert Solution().minimumBuckets(".HHH.") == -1
    assert Solution().minimumBuckets("HH..") == -1
    assert Solution().minimumBuckets("..HHH..") == -1
