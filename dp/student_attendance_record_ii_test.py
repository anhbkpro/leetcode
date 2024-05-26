from dp.student_attendance_record_ii import Solution


def test_checkRecord():
    assert Solution().checkRecord(1) == 3
    assert Solution().checkRecord(2) == 8
