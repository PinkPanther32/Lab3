import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])
    
def test_bubble_sort_case3():
    result = 1
    input_arr = [64, 34, 25, 12, 22, 11, 90,12,34,23,27]
    test_arr = [11, 12, 12, 22, 23, 25, 27, 34, 34, 64, 90]
    
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    
    assert result == test_arr
    
def test_bubble_sort_case4():
    result = 0
    input_arr = []
    test_arr = []
    
    result = Lab3.bubble_sort(input_arr, test_arr)
    
    assert result == test_arr
    
def test_bubble_sort_case5():
    result = 2
    input_arr = ["John"]
    test_arr = ["John"]
    
    result = Lab3.bubble_sort(input_arr, test_arr)
    
    assert result == test_arr