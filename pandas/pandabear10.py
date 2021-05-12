#!/usr/bin/python3

import pandas as pd
import argparse

def main(args):
    excel_file = 'movies.xls'
    movies = pd.read_excel(excel_file)
    print(movies.head())
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    print(movies_sheet1.head())
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    print(movies_sheet3.head())
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
    print(movies.shape)

    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)
    if args.year:
        subset = sorted_by_gross[sorted_by_gross['Year']==args.year]
        print(subset)
 

def parze():
    parser = argparse.ArgumentParser(description="Sort by Year")
    parser.add_argument("-y", "--year", type=int, help="Please enter Year")
    return parser.parse_args()

if __name__ == "__main__":
    args = parze()
    main(args)

