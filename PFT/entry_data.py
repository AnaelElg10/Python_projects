from datetime import datetime

format_date = '%d-%m-%Y'
CATEG = {'I': 'Income', 'E': 'Expense'}

def get_date(prompt, allow_default=False):

    while True:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(format_date)
        
        try:
            valid_date = datetime.strptime(date_str, format_date)
            return valid_date.strftime(format_date)
        except ValueError:
            print('The date is invalid. Please enter a valid date in the format DD-MM-YYYY')

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt + ': '))
            if amount <= 0:
                print('The amount is invalid. It must be greater than 0.')
            else:
                return amount
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

def get_category(prompt):
    category = input("Enter the category: 'I' for income or 'E' for expense ").capitalize()
    if category not in CATEG:
        print('Invalid category. Please enter either "I" for Income or "E" for Expense.')
        return get_category()
    return CATEG[category]


def get_description(prompt):
    description = input("Enter the description: ")
    return description