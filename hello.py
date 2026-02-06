def greet(name):
    print(f"Hello, {name}!")


def count_to(n):
    for i in range(1, n + 1):
        print(i)


print("What do you want to do? (1) Get greeted (2) Count numbers (3) Quit")
choice = input("> ")

if choice == "1":
    name = input("What is your name? ")
    greet(name)
elif choice == "2":
    n = int(input("Count to what number? "))
    count_to(n)
elif choice == "3":
    print("Goodbye!")
