import sys

def add_numbers(a, b):
    return a + b

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <num1> <num2>")
        sys.exit(1)
    
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    result = add_numbers(num1, num2)
    print("The sum of", num1, "and", num2, "is:", result)

if __name__ == '__main__':
    main()