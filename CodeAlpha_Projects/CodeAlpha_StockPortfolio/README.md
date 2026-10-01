CodeAlpha Stock Portfolio Tracker

1. Project Overview

The Stock Portfolio Tracker is a Python-based console application that helps users keep track of their stock investments.

The program allows users to add stocks, enter quantities, view their portfolio, calculate the value of each holding, calculate the total investment, remove stocks, and save the portfolio information to a text file.

The project uses predefined stock prices as required by the CodeAlpha task.

2. Key Features

- Add stocks to the portfolio
- Enter the quantity of each stock
- Calculate the value of each stock holding
- Combine quantities when the same stock is added again
- View the complete portfolio
- Calculate total portfolio investment
- Remove stocks from the portfolio
- Save portfolio information to a text file
- Validate user input
- Simple menu-based interaction

3. Python Concepts Used

- Dictionaries
- Lists
- Variables
- Conditional statements
- Loops
- Functions
- User input
- Arithmetic operations
- File handling
- Input validation

4. Project Structure

->
CodeAlpha_StockPortfolio
├── stock_portfolio.py
└── README.md


5. How to Run

1. Open the project folder in VS Code.
2. Open (stock_portfolio.py).
3. Run the program using Python.


-> python stock_portfolio.py


6. How the Program Works

The program provides a menu with different options.

1. Add Stock  
   The user selects a stock and enters the quantity. The program calculates the investment value using the predefined stock price.

2. View Portfolio  
   The program displays the stocks currently stored in the portfolio along with their quantities, prices, and total values.

3. Remove Stock  
   The user can remove a stock from the portfolio.

4. Save Portfolio  
   The portfolio details can be saved to a text file for later reference.

5. Exit  
   The program closes when the user chooses the exit option.

7. Design Approach

The project uses a dictionary to store stock prices and another data structure to maintain the user's portfolio.

A menu-driven design was used so that users can perform different portfolio operations without restarting the program.

Input validation is included to prevent invalid stock names and quantities from causing errors.

8. What I Learned

Through this project, I practiced working with dictionaries, loops, conditional statements, functions, user input, arithmetic calculations, input validation, and file handling in Python.

I also learned how different Python concepts can be combined to build a small practical application.

9. Future Improvements

Possible future improvements include:

- Connecting the application to live stock market data
- Adding profit and loss calculations
- Supporting more companies
- Adding CSV export
- Adding portfolio performance tracking

10. Internship Context

This project was developed as part of the CodeAlpha Python Programming Internship.

The project follows the requirements of the Stock Portfolio Tracker task, which focuses on user input, predefined stock prices, investment calculations, and optional file handling.

11. Author

Chaitanya Deshaboina 