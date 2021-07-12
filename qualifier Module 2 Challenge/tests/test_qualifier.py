# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters from filters folder.  These are files in the filters folder
# Requesting fucntions from these files in filters folder
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
def test_save_csv(bank_data):
    fileio.save_csv(Path('./data/output/qualifying_loans.csv'), bank_data)

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

#not using debt, income, and home_value in test.csv - test program
def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

  
    #saving the test csv data, and calling each function one by one
    bank_data = credit_score.filter_credit_score(current_credit_score, bank_data)
    bank_data = debt_to_income.filter_debt_to_income(monthly_debt_ratio, bank_data)
    bank_data = loan_to_value.filter_loan_to_value(loan_to_value_ratio, bank_data)
    bank_data = max_loan_size.filter_max_loan_size(loan, bank_data)
    #fileio.save_csv(Path('./data/output/qualifying_loans.csv'), bank_data)
    #calling bank data to test the filters and saving this to a csv file
    test_save_csv(bank_data)