from primes.prime_finder import PrimeFinder


def main():
    prime_finder = PrimeFinder()
    while True:
        user_input = input("Enter a number (or type 'quit' to exit): ")
        if user_input.strip().lower() == 'quit':
            break

        try:
            n = int(user_input)
            if prime_finder.is_prime(n):
                print(f"{n} is a prime number.")
            else:
                print(f"{n} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer or 'quit' to exit.")


if __name__ == "__main__":
    main()
