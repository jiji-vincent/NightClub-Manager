# Variables
max_capacity = 650
ticket_price = 15.00


# --- Functions Section ---

def display_status(tickets_sold):
    """Calculates and prints the current capacity status."""
    available_capacity = max_capacity - tickets_sold
    print(f"\n--- Capacity Status ---")
    print(f"Tickets Sold: {tickets_sold}")
    print(f"Remaining Spots: {available_capacity}")
    print("-" * 25)


def sell_ticket(tickets_sold, total_revenue):
    """Checks capacity, sells a ticket, and returns updated counts."""
    # Note: Accesses max_capacity and ticket_price globally (for simplicity now)

    if tickets_sold < max_capacity:
        tickets_sold += 1
        total_revenue += ticket_price
        print(f"SUCCESS! Ticket sold. New revenue: ${total_revenue:.2f}")
    else:
        print("CAPACITY FULL! Cannot sell any more tickets.")

    # Crucial step: return the updated variables
    return tickets_sold, total_revenue


def calculate_totals(tickets_sold, total_revenue):
    """Prints the final summary upon exiting."""
    print("\n--- Program Exiting: Final Summary ---")
    print(f"Total Tickets Sold: {tickets_sold}")
    print(f"Total Revenue: ${total_revenue:.2f}")
    print("-" * 35)


# --- Main Program ---

tickets_sold = 0
total_revenue = 0.0

print(f"Welcome to the Nightclub Manager. Max Capacity: {max_capacity}")

while True:
    # 1. Display status using the function
    display_status(tickets_sold)

    action = input("Enter 'sell' to sell a ticket, or 'exit' to quit: ").strip().lower()

    if action == 'sell':
        # 2. Call the sell_ticket function and update the main variables
        tickets_sold, total_revenue = sell_ticket(tickets_sold, total_revenue)

    elif action == 'exit':
        # 3. Calculate and display totals using the function
        calculate_totals(tickets_sold, total_revenue)
        break

    else:
        print("Invalid command. Please enter 'sell' or 'exit'.")