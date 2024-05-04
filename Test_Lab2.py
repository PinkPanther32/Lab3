import Lab2 

print("Test_Lab2")

def test_find_min_max():
    # Define test inputs
    num1, num2, num3, num4 = 3, 67, 32, 14
    
    # Call the function being tested
    min_num, max_num = Lab2.find_min_max(num1, num2, num3, num4)
    
    # Print the results
    print("Minimum number is:", min_num)
    print("Maximum number is:", max_num)
    
    # Assert the results
    assert min_num == min(num1, num2, num3, num4)
    assert max_num == max(num1, num2, num3, num4)


def test_calc_average():
    # Define test inputs
    num1, num2, num3, num4 = 3, 67, 32, 14
    
    # Call the function being tested
    average = Lab2.calc_average(num1, num2, num3, num4)
    
    # Print the result
    print("The average =", average)
    
    # Assert the result
    assert average == (num1 + num2 + num3 + num4) / 4
    
    


def test_calc_median_temperature():
    # Define test inputs
    num1, num2, num3, num4 = 3, 67, 32, 14
    
    # Call the function being tested
    median = Lab2.calc_median_temperature([num1, num2, num3, num4])
    
    # Print the result
    print("Median temperature:", median)
    
    # Calculate the expected median manually
    sorted_temperatures = sorted([num1, num2, num3, num4])
    n = len(sorted_temperatures)
    if n % 2 == 0:
        expected_median = (sorted_temperatures[n//2 - 1] + sorted_temperatures[n//2]) / 2
    else:
        expected_median = sorted_temperatures[n//2]

    # Assert the result
    assert median == expected_median