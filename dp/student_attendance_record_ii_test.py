from dp.student_attendance_record_ii import Solution


def test_check_record():
    assert Solution().checkRecord(1) == 3
    assert Solution().checkRecord(2) == 8
