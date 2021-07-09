# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

#fp - filepath, shorthand for file path user provides customer 
# w = write file f = object that has all the properties, 
# shorthand, stores results of open FP command variable
#return function nothing to return, just want to add return statement so Python is happy
def save_csv(fp, qualifying_loans):
    with open (fp, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"])
        for loan in qualifying_loans:
            writer.writerow(loan)
    return