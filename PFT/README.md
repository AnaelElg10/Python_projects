# Finance Tracker

## Introduction
Finance Tracker is a Python application designed to help users manage their personal finances. It allows users to add, view, and analyze their income and expenses over time through a simple command-line interface. The data is stored in a CSV file, making it easy to maintain and access.

## Installation
To get started with Finance Tracker, follow these steps:

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip install matplotlib pandas` in your terminal.

## Usage
To use Finance Tracker, navigate to the project directory in your terminal and run:

```sh
python main.py
```

Follow the on-screen prompts to add transactions, view transactions, or generate charts.

## Scripts

### entry_data.py

This script contains functions to get user input for date, amount, category, and description.

### main.py

This script contains the main logic for the application, including initializing the CSV file, adding entries, viewing transactions, and generating charts.

## Functions

### entry_data.py

- `get_date(prompt, allow_default=False)`: Prompts the user to enter a date.
- `get_amount(prompt)`: Prompts the user to enter an amount.
- `get_category(prompt)`: Prompts the user to enter a category (income or expense).
- `get_description(prompt)`: Prompts the user to enter a description.

### main.py

- `CSV`: A class for handling CSV file operations.
  - `init()`: Initializes the CSV file.
  - `entry(date, amount, category, description)`: Adds a new entry to the CSV file.
  - `transactions(start_date, end_date)`: Retrieves transactions within a specified date range.
- `add()`: Adds a new entry by prompting the user for details.
- `transactions_chart(df)`: Generates a chart for income and expenses.
- `main()`: The main function that handles user choices.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```