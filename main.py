from employees import gen_employees_csv

# Store the user's options in a dictionary
options = {
    1: 'Generate random data for employees.'
}


def main():
    
    try:
        # Prompt the user to enter how many records worth of data they want to generate
        user_num = int(input("Please enter an integer (no commas) for how many records of test data you want to generate: "))
        gen_employees_csv(user_num)
        print(f'{user_num} record(s) successfully generated. Check the "data" directory for an "employees.csv" file ')
    except ValueError:
        print("Please enter an integer. Program terminated.")


main()