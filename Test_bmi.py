import LAB2.bmi as bmi

def test_bmi_normal_weight(weight=57, height=1.73):
    # Calculate BMI using the formula
    bmi_test = weight / (height * height)
    
    # Define the test range for normal weight
    normal_weight_range = (18.5, 25.0)
    
    # Check if the calculated BMI falls within the normal weight range
    test = bmi_test >= normal_weight_range[0] and bmi_test <= normal_weight_range[1]
    
    # Assert that the calculated BMI falls within the normal weight range
    assert test, f"BMI is not within the normal weight range. BMI calculated: {bmi_test}"
    
    
def test_bmi_under_weight(weight=45, height=1.9):
    # Calculate BMI using the formula
    bmi_test = weight / (height * height)
    
    # Define the threshold for underweight classification
    underweight_threshold = 18.5
    
    # Check if the calculated BMI falls within the underweight range
    is_underweight = bmi_test < underweight_threshold
    
    # Assert that the calculated BMI indicates underweight classification
    assert is_underweight, f"BMI: {bmi_test} does not indicate underweight."
    

def test_bmi_over_weight(weight=80, height=1.5):
  
    # Calculate BMI using the formula
    bmi_test = weight / (height * height)

     # Define overweight range
    over_weight_bmi_range = 25
    
   # Check if the calculated BMI falls within the overweight range
    test = bmi_test >= over_weight_bmi_range
    
    # Assert that the calculated BMI falls within the overweight range
    assert test, f"BMI is not within the overweight range. BMI calculated: {bmi_test}"

