import employee_info

def test_get_employees_by_age_range():
    expected_result = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result = employee_info.get_employees_by_age_range(22, 31)
    
    assert(expected_result == result)
    

def test_calculate_average_salary():
    expected_result = 60166.666666666664
    result = employee_info.calculate_average_salary()
    
    assert(expected_result == result)


def  test_get_employees_by_dep():
    expected_result =[
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    
    result = employee_info.get_employees_by_dept("Engineering")
    
    assert(expected_result == result)