from logs import reorder_logs

def test_exists():
    assert reorder_logs

def test_vanilla():
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

    assert reorder_logs(logs) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

def test_for_same_word_at_1():
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

    assert reorder_logs(logs) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

def test_empty_list():
    logs = []

    assert reorder_logs(logs) == []