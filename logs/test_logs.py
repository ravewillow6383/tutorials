from logs import reorder_logs

def test_exists():
    assert reorder_logs

def test_vanilla():
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

    assert reorder_logs(logs) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]