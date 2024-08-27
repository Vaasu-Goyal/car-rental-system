from datetime import datetime
import threading

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock
        self.rental_basis = 0
        self.rental_time = 0
        self.rented_cars = 0
        self.lock = threading.Lock()  # Lock for thread safety

    def display_stock(self):
        """Display the number of available cars"""
        print(f"Available cars: {self.stock}")
        return self.stock

    def rent_car_on_hourly_basis(self, n):
        """Rent cars on an hourly basis"""
        with self.lock:
            if n <= 0:
                print("Number of cars should be positive!")
                return None
            elif n > self.stock:
                print(f"Sorry! We have currently {self.stock} cars available to rent.")
                return None
            else:
                self.rental_basis = 1  # Hourly rental
                self.rental_time = datetime.now()
                self.stock -= n
                self.rented_cars = n
                print(f"You have rented {n} car(s) on an hourly basis at {self.rental_time.hour} hours.")
                return self.rental_time

    def rent_car_on_daily_basis(self, n):
        """Rent cars on a daily basis"""
        with self.lock:
            if n <= 0:
                print("Number of cars should be positive!")
                return None
            elif n > self.stock:
                print(f"Sorry! We have currently {self.stock} cars available to rent.")
                return None
            else:
                self.rental_basis = 2  # Daily rental
                self.rental_time = datetime.now()
                self.stock -= n
                self.rented_cars = n
                print(f"You have rented {n} car(s) on a daily basis at {self.rental_time.hour} hours.")
                return self.rental_time

    def rent_car_on_weekly_basis(self, n):
        """Rent cars on a weekly basis"""
        with self.lock:
            if n <= 0:
                print("Number of cars should be positive!")
                return None
            elif n > self.stock:
                print(f"Sorry! We have currently {self.stock} cars available to rent.")
                return None
            else:
                self.rental_basis = 3  # Weekly rental
                self.rental_time = datetime.now()
                self.stock -= n
                self.rented_cars = n
                print(f"You have rented {n} car(s) on a weekly basis at {self.rental_time.hour} hours.")
                return self.rental_time

    def return_car(self):
        """Return a rented car and calculate the bill"""
        with self.lock:
            if self.rental_basis and self.rental_time and self.rented_cars:
                now = datetime.now()
                rental_period = now - self.rental_time
                bill = 0

                if self.rental_basis == 1:  # Hourly rental
                    bill = rental_period.seconds / 3600 * 5 * self.rented_cars
                elif self.rental_basis == 2:  # Daily rental
                    bill = rental_period.days * 20 * self.rented_cars
                elif self.rental_basis == 3:  # Weekly rental
                    bill = (rental_period.days // 7) * 60 * self.rented_cars

                print(f"Thanks for returning your car(s).")
                print(f"That would be ${bill:.2f}")
                self.stock += self.rented_cars  # Return cars to stock
                self.rental_basis, self.rental_time, self.rented_cars = 0, 0, 0
                return bill
            else:
                print("You did not rent a car.")
                return None


class Customer:
    def __init__(self):
        self.cars = 0

    def request_car(self):
        """Request a car to rent"""
        cars = int(input("How many cars would you like to rent? "))
        self.cars = cars
        return self.cars

    def return_car(self):
        """Return a rented car"""
        if self.cars:
            return self.cars
        else:
            return 0


def main():
    rental = CarRental(10)  # Initialize with 10 cars in stock
    customer = Customer()

    while True:
        print("""
        ====== Car Rental Shop =======
        1. Display available cars
        2. Request a car on hourly basis $5/hour
        3. Request a car on daily basis $20/day
        4. Request a car on weekly basis $60/week
        5. Return a car
        6. Exit
        """)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            rental.display_stock()

        elif choice == 2:
            customer.request_car()
            rental.rent_car_on_hourly_basis(customer.cars)

        elif choice == 3:
            customer.request_car()
            rental.rent_car_on_daily_basis(customer.cars)

        elif choice == 4:
            customer.request_car()
            rental.rent_car_on_weekly_basis(customer.cars)

        elif choice == 5:
            rental.return_car()

        elif choice == 6:
            print("Thank you for using our service.")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
