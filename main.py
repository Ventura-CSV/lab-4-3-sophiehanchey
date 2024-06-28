def main():
    
    total = 0
    i = 0
    
    # while loop 
    while i<5: 
        new_num = int(input('Please enter a number: '))
        total += new_num
        
        i += 1
        
    print(f'Your total is: {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
