import random

# Variables
max_capacity = 650
ticket_price = 15.00
tickets_sold = 0
total_revenue = 0.0

print(f"--- Nightclub Manager Initialized ---")
print(f"Max Capacity: {max_capacity}")

# Main Program Loop
while True:
    # Calculate available spots
    available_capacity = max_capacity - tickets_sold
    print(f"\nCapacity Status: {tickets_sold} sold, {available_capacity} remaining.")

    # Get user action
    action = input("Enter 'sell' to sell a ticket, or 'exit' to quit: ").strip().lower()

    if action == 'sell':
        # 3. Core Logic: Check Capacity
        if tickets_sold < max_capacity:
            tickets_sold += 1
            total_revenue += ticket_price
            print(f"TICKET SOLD! Total revenue so far: ${total_revenue:.2f}")
        else:
            print("CAPACITY FULL! Cannot sell any more tickets.")

    elif action == 'exit':
        print("\n--- Program Exiting ---")
        print(f"Final Tickets Sold: {tickets_sold}")
        print(f"Final Revenue: ${total_revenue:.2f}")
        break  # Exits the while loop

    else:
        print("Invalid command. Please enter 'sell' or 'exit'.")