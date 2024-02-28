import yfinance as yf
from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    clear_screen()

    print('Stock Portfolio Tracker')
    print('1. Add stock')
    print('2. Remove stock')
    print('3. View stock Info')
    print('4. Exit')

    choice = None
    while choice not in ['1', '2', '3', '4']:
        choice = input('Enter the choice (1/2/3/4): ')

    if choice == '1':
        add_stock()
    elif choice == '2':
        remove_stock()
    elif choice == '3':
        view_stock_info()
    else:
        exit()

def add_stock():
    clear_screen()

    stock = input('Enter stock symbol first: ')
    with open('stocks.txt', 'a') as f:
        f.write(stock + '\n')
    print(f'{stock} added')

    input('Press enter to continue')
    menu()

def remove_stock():
    clear_screen()

    with open('stocks.txt', 'r') as f:
        stocks = f.readlines()

    print('Your stocks: ')

    for stock in stocks:
        print(stock.strip())

    stock = input('Enter stock symbol first: ')
    with open('stocks.txt', 'w') as f:
        if stock + '\n' in stocks:
            stocks.remove(stock + '\n')
            for s in stocks:
                f.write(s)
        
            print(f'{stock} removed')
        else:
            print(f'{stock} not found')
            f.writelines(stocks)
    
    input('Press enter to continue')
    menu()

def view_stock_info():
    clear_screen()

    with open('stocks.txt', 'r') as f:
        stocks = f.readlines()

    print('Your stocks: ')

    for stock in stocks:
        stock = stock.strip()
        data = yf.Ticker(stock).financials
        if data.empty:
            print(f'\n----- No data found for {stock} -----\n')
            continue
        print(f'\n----- Financials for {stock} -----\n')
        print(data)
    
    input('Press enter to continue')
    menu()


menu()
