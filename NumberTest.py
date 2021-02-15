#Name: Dipesh Gautam




choice = None
while choice != ('n'):
    
    try:

        number =int(input('Please enter a number: '))

    except ValueError:
        print('Invalid input, Try again using numbers')
        continue

    is_prime = True
    for factor in range(2, number):

        if number % factor ==0:
            is_prime = False
            break
    if is_prime ==True:
        print('prime number')

    else:
        print('not prime number')


    if number == 0:
        print( 'zero')
    elif number > 0:
         print ('positive')
    else:
         print ('negative')

    if number%2 == 0:
        print('even')

    else:
        print( 'odd')

    import random
    count = 0
    num = random.randint(0, 4)
    if num == 0:
        try:
            
            second_number = int(input('Please Enter a number that is prime: '))

        except ValueError:
            print('Invalid input, Try again using number')
            continue

        is_prime = True
        for factor in range(2, second_number):

            if second_number % factor ==0:
                is_prime = False
                break
        if is_prime ==True:
            print('Correct',second_number,'is a prime number')

        else:
            print('Sorry',second_number,'is not prime number')

    elif num == 1:

        try:
            second_number = int(input('Please Enter a number that is not prime: '))
        except ValueError:
            print('Invalid Input, Try again using number')
            continue

        is_prime = True
        for factor in range(2, second_number):

            if second_number % factor ==0:
                is_prime = False
                break
        if is_prime ==True:
            print('sorry',second_number ,'is   a prime number')

        else:
            print('Correct',second_number,'is not a prime number')

    elif num ==2:
        try:
            
            second_number = int(input('Please Enter a mumber that is even: '))

        except ValueError:
                print('Invalid Input, Try again using numbers')
                continue

        if second_number%2 == 0:
            print(' Correct',second_number,'is even')

        else:
            print('Sorry',second_number,'is not even')

    elif num == 3:
        try:

            second_number = int(input('Please Enter a number that is positive, negative or zero: '))
        except ValueError:
            print('Invalid input, Try again using numbers')
            continue
        if second_number>0:
            print('Correct',second_number,'is positive')

        elif second_number<0:
            print('Correct',second_number,'is negative')

        elif second_number==0:
            print('Correct,The number is zero')

        else:
            print('Sorry, invalid choice')

    elif num ==4:
        try:
            second_number = int(input('Please enter a number that is odd: '))
        except ValueError:
            print('Invalid input, Try again using numbers')
            continue
        if second_number %2 ==0:
            print('Sorry', second_number,'is not odd')

        else:
            print('Correct' ,second_number, 'is odd')
            
    
    choice = input('Do you wish to try again (y/n)')
        
    if choice == ('n'):
        print('Goodbye')
    

        
        



    


        
        
    
