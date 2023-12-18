import sys

def factorize(n):
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor = factorize_number(number)
            for factor in factor:
                print(f"{number}={factor[0]}*{factor[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

