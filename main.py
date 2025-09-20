def gps_tracker():
    # Starting position
    x, y = 0, 0
    print(f"Starting at position: ({x}, {y})")

    while True:
        command = input("Enter direction (N/S/E/W) or STOP to end: ").strip().lower()

        if command in ['n', 'north']:
            y += 1
        elif command in ['s', 'south']:
            y -= 1
        elif command in ['e', 'east']:
            x += 1
        elif command in ['w', 'west']:
            x -= 1
        elif command == "stop":
            break
        else:
            print("Invalid input! Please enter N, S, E, W, or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    # Final output
    print(f"\nSession ended. Final position: ({x}, {y})")
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")

# Run the program
gps_tracker()
