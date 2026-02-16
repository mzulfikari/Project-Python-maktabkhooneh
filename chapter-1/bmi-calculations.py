# global variable and imports 

 
# getting user inputs as height and weight 
def get_user_inputs():
    weight =  float(input(" enter you weight (kg): "))
    height =  float(input(" enter you height (m): "))
    return weight,height

# calculate nmi 
def calculate_bmi(weight,height):
    return weight // (height**2)

# get the bmi result 
def get_bmi_result(bmi):
    print(f"bmi: {bmi}/n result:")
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi <25:
        print("Normal")
    elif 25 <= bmi <30:
        print("Over Weight")
    elif 30 <= bmi < 35:
        print("Obese")
    else:
        print("EXtremely Obese")
        
# crate main function to run 
def main():
    weight,height = get_user_inputs()
    bmi = calculate_bmi(weight,height)
    get_bmi_result(bmi)
    
if __name__ == "__main__":
    main()