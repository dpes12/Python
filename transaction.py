#Transaction Recording Program
import datetime
import csv
    
ans = None
#initialising loop for transaction
while ans != 'y':

    with open('Transaction_Recording.csv' , 'a' , newline = '' ) as trecording:
        twriter = csv.writer(trecording)

        #prompt user for data to write into the file
        from_name = input('Transaction From: ')
        to_name = input('Transaction To: ')
        amt = input('Amount: ')
        try:
            amt = int(amt)
            if amt <=0:
                print("Invalid input, Enter positive numbers")
                continue
        except ValueError:
            print("Invalid input, Enter numbers")
            continue
        timestamp = datetime.datetime.now()
        #writing to transaction recording file
        twriter.writerow([ from_name , to_name , str(amt) , str(timestamp)])
        trecording.close()

        ans = input('Do you want to quit? y/n: ')
        if ans == ('y'):
                print('Goodbye')

print('Transaction is saved in Transaction_Recording.csv file')
