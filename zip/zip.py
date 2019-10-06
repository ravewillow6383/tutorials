#Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

# Zipping numbers and letters

def zip_lists(lst1, lst2):

    zipped = zip(lst1, lst2)

    return list(zipped)

