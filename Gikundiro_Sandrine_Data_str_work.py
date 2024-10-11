from collections import deque

bus_routes = ["KAMONYI", "MUHANGA", "KIGALI",]

undo_stack = []

purchase_queue = deque()

def display_routes():
    print("Available bus routes:")
    for i, route in enumerate(bus_routes):
        print(f"{i+1}. {route}")


def book_ticket(user):
    display_routes()
    choice = int(input("Select a route to book a ticket (1-4): "))
    if 1 <= choice <= len(bus_routes):
        route = bus_routes[choice - 1]
        undo_stack.append((user, route))
        print(f"{user} booked a ticket for {route}.")
    else:
        print("Invalid route selection.")
def undo_booking():
    if undo_stack:
        last_booking = undo_stack.pop()
        print(f"Booking undone: {last_booking[0]} for {last_booking[1]}")
    else:
        print("No bookings to undo.")


def add_to_queue(user):
    purchase_queue.append(user)
    print(f"{user} added to the purchase queue.")


def process_queue():
    if purchase_queue:
        user = purchase_queue.popleft()
        print(f"Processing ticket purchase for {user}.")
        book_ticket(user)
    else:
        print("No users in the queue.")

def main():
    while True:
        print("\n1. Display Routes\n2. Book Ticket\n3. Undo Last Booking\n4. Add User to Purchase Queue\n5. Process Purchase Queue\n6. Exit")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            display_routes()
        elif choice == 2:
            user = input("Enter your name: ")
            book_ticket(user)
        elif choice == 3:
            undo_booking()
        elif choice == 4:
            user = input("Enter your name to join the queue: ")
            add_to_queue(user)
        elif choice == 5:
            process_queue()
        elif choice == 6:
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
