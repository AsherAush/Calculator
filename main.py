from Rectangle import Rectangle
from Square import Square
from Triangular import Triangle
from Circle import Circle
from Hexagon import Hexagon

def main():
    print("Welcome to the Area and Perimeter Calculator!")
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle (right-angled)")
    print("4. Circle")
    print("5. Hexagon")

    choice = input("Enter the number of your choice: ")

    try:
        if choice == "1":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            shape = Rectangle(width, height)

        elif choice == "2":
            side = float(input("Enter the side length: "))
            shape = Square(side)

        elif choice == "3":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            shape = Triangle(base, height)

        elif choice == "4":
            radius = float(input("Enter the radius: "))
            shape = Circle(radius)

        elif choice == "5":
            side = float(input("Enter the side length: "))
            shape = Hexagon(side)

        else:
            print("Invalid choice.")
            return

        print(f"\nYou chose: {shape}")
        print(f"Area: {shape.get_area()}")
        print(f"Perimeter: {shape.get_perimeter()}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
