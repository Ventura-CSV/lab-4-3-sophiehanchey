def main():
    ##################################################
    # Comlete your code here
    ##################################################

    sum = 0
    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input())
        sum += numbers[i]
        # print (numbers[i], end=' ')
    print(f'Total is {sum}')

    pass


if __name__ == '__main__':
    main()
