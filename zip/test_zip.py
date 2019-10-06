from zip import zip_lists


#Test an easy base case
def test_vanilla():
    numb = [1, 2, 3]

    letters = ['a', 'b', 'c', 'd']

    assert zip_lists(numb, letters) == [(1, 'a'), (2, 'b'), (3, 'c')]


# Test passing in one empty list

#Since the second list is empty, zip() outputs an empty list. There are still 3 unmatched elements from the numb list. These are all ignored by zip() since there are noelements from the letters list to complete the pairs.

def test_single():
    numb = [1, 2, 3]
    letters = []

    assert zip_lists(numb, letters) == []