from lc_1146_snapshot_array import SnapshotArray
obj = SnapshotArray(length=3)


def test_snap():
    obj.set(index=0, val=5)
    obj.snap()
    obj.set(index=0, val=6)
    assert obj.get(index=0, snap_id=0) == 5
    assert obj.get(index=0, snap_id=1) == 6
    assert obj.get(index=0, snap_id=2) == 6

