def main():
    val = int(input('enter an integer:'))    
    print("")
    print("Binary:", bin(val))
    print("Hexadecimal:", hex(val))
    print("Octal:", oct(val))

main()

#run scanner again
while True:
    again = input("Would you like to convert another number? (y/n): ")
    if again not in ('y', 'n'):
        print("Not a valid input.")
        break
    if again == 'y':
        main()
    else:
        print("Goodbye ")
        break

