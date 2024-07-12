from matplotlib import pyplot as plt
import pandas as pd
import csv
from datetime import datetime
from entry_data import get_date, get_amount, get_category, get_description

class CSV:    
    CSV_FILE = 'finance.csv'
    COL = ['date', 'amount', 'category', 'description']
    FORMAT = '%d-%m-%Y'

    @classmethod
    def init(cls):
        """Initializes the CSV file if it doesn't exist."""
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['date', 'amount', 'category', 'description'])
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def entry(cls, date, amount, category, description):
        """Adds a new entry to the CSV file."""
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }

        with open(cls.CSV_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.COL)
            writer.writerow(new_entry)
        print('The entry has been added successfully!')

    @classmethod
    def transactions(cls, start_date, end_date):
        """Displays the transactions between the given dates."""

        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('No transactions have been found in the given date range.')
        else:
            print(
                f"Transactions between {start_date.strftime(CSV.FORMAT)} and {end_date.strftime(CSV.FORMAT)}"
                )
            print(filtered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.FORMAT)})
                )
            
            total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
            total_expenses = filtered_df[filtered_df['category'] == 'Expense']['amount'].sum()
            print('\nSummary of transactions:')
            print(f'The total income is: {total_income:.2f}')
            print(f'The total expenses is: {total_expenses:.2f}')
            print(f'The balance is: {(total_income - total_expenses):.2f}')
        return filtered_df
    


def add():
    """Adds a new entry to the CSV file."""
    CSV.init()
    date = get_date('Enter the date (DD-MM-YYYY): ')
    amount = get_amount('Enter the amount')
    category = get_category('Enter the category: ')
    description = get_description('Enter the description: ')
    CSV.entry(date, amount, category, description)

def transactions_chart(df):
    """Displays a chart of the income and expenses through time."""
    df.set_index('date', inplace=True)

    df_income = df[df['category'] == 'Income'].resample('D').sum().reindex(df.index, fill_value=0)
    df_expense = df[df['category'] == 'Expense'].resample('D').sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 6))
    plt.plot(df_income.index, df_income['amount'], label='Income', color='green')
    plt.plot(df_expense.index, df_expense['amount'], label='Expense', color='red')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Chart of Income and Expense through time')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """Displays the main menu."""
    while True:
        print('\n1. Add an entry')
        print('2. View transactions')
        print('3. View transactions chart')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            add()
        elif choice == '2':
            start_date = get_date('Enter the start date (DD-MM-YYYY): ')
            end_date = get_date('Enter the end date (DD-MM-YYYY): ')
            CSV.transactions(start_date, end_date)
        elif choice == '3':
            start_date = get_date('Enter the start date (DD-MM-YYYY): ')
            end_date = get_date('Enter the end date (DD-MM-YYYY): ')
            df = CSV.transactions(start_date, end_date)
            transactions_chart(df)
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again. Enter a number between 1 and 4.')
            
if __name__ == '__main__':
    main()
