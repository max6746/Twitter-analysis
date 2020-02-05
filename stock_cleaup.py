import pandas as pd
import csv

def main():
    df = pd.read_csv('tesla_stocks.csv')
    stock = []
    date = []
    for inx in df.index:
        stock.append(df['Close'][inx])
        #separate date and time
        date_str = df['Date'][inx].split()[0]

        #change date fmt
        date_sep = date_str.split('/')
        date_fmt = date_sep[1]+'-'+date_sep[0]+'-'+date_sep[2]
        date.append(date_fmt)
    #write to csv
    with open('tesla_stocks.csv', mode='w') as csv_file:
        fieldnames = ['Date', 'Close']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(date)):
            writer.writerow({'Date': date[i], 'Close': stock[i]})

if __name__ == "__main__":
    main()