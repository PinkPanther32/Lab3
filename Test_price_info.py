import price_info

def test_total_cost_shopping():
    expected_total_cost = 46.75
    
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            total_cost += quantity_list[key] * price_list[key]

    assert total_cost == expected_total_cost, f"Expected total cost: {expected_total_cost}, Actual total cost: {total_cost}"

    
def test_cost_of_fruits():
    fruit = 'apple'
    quantity = 10
    expected_total_cost_of_fruits = 12
    
    cost = 0
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    assert expected_total_cost_of_fruits == cost, f"Expected total cost: {expected_total_cost_of_fruits}, Actual total cost: {cost}"


# Sample data
price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}
quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}



