import time

def issue_ticket(tix):
    passenger_name = input("Please enter the passenger's name: ").strip().title()
    if not passenger_name:
        print("Passenger name cannot be empty.")
        return
    if passenger_name in tix:
        print(f"Ticket for {passenger_name} already exists.")
        return

    time.sleep(0.5)
    print(f"""Welcome {passenger_name}! Please Select your ticket type:
    1. Single Journey
    2. Stored Value Card""")
    time.sleep(0.5)
    ticket_type = input("Enter ticket type (1 or 2): ").strip()
    if ticket_type not in ['1', '2']:
        print("Invalid ticket type selected.")
        return

    time.sleep(0.5)
    print("""Now please select your destination:
    1. [RL15] Solis
    2. [RL14] Caloocan
    3. [RL13] Valenzuela
    4. [RL12] Meycauayan
    5. [RL11] Marilao
    6. [RL10] Bocaue
    7. [RL09] Balagtas
    8. [RL08] Guiguinto
    9. [RL07] Malolos
    10. [RL06] Calumpit
    11. [RL05] Apalit
    12. [RL04] San Fernando
    13. [RL03] Angeles
    14. [RL02] Clark
    15. [RL01] Clark International Airport""")

    time.sleep(0.5)
    destination = input("Enter destination number (1-15): ").strip()
    if destination not in [str(i) for i in range(1, 16)]:
        print("Invalid destination selected.")
        return
    
    time.sleep(0.5)
    print("""Please select your desired train service: 
    1. Commuter
    2. Commuter Express
    3. Airport Limited-Express""")

    time.sleep(0.5)
    service_type = input("Enter service type (1, 2, or 3): ").strip()
    if service_type not in ['1', '2', '3']:
        print("Invalid service type selected.")
        return
    
    tix[passenger_name] = {
        "passenger_name": passenger_name,
        "ticket_type": "Single Journey" if ticket_type == '1' else "Stored Value Card",
        "destination": "Solis" if destination == '1' else
                      "Caloocan" if destination == '2' else
                      "Valenzuela" if destination == '3' else
                      "Meycauayan" if destination == '4' else
                      "Marilao" if destination == '5' else
                      "Bocaue" if destination == '6' else
                      "Balagtas" if destination == '7' else
                      "Guiguinto" if destination == '8' else
                      "Malolos" if destination == '9' else
                      "Calumpit" if destination == '10' else
                      "Apalit" if destination == '11' else
                      "San Fernando" if destination == '12' else
                      "Angeles" if destination == '13' else
                      "Clark" if destination == '14' else
                      "Clark International Airport" if destination == '15' else None,
        "service_type": "Commuter" if service_type == '1' else
                        "Commuter Express" if service_type == '2' else
                        "Airport Limited-Express" if service_type == '3' else None
    }
    time.sleep(0.5)
    print(f"Ticket issued successfully! | Passenger: {passenger_name} | Ticket Type: {tix[passenger_name]['ticket_type']} | Destination: {tix[passenger_name]['destination']} | Service Type: {tix[passenger_name]['service_type']}")
    time.sleep(0.5)
    
def find_tickets(tix):
    passenger_name = input("Please enter the passenger's name to find their ticket: ").strip().title()
    if not passenger_name:
        print("Passenger name cannot be empty.")
        return
    if passenger_name in tix:
        ticket_info = tix[passenger_name]
        time.sleep(0.5)
        print(f"Ticket found! | Passenger: {ticket_info['passenger_name']} | Ticket Type: {ticket_info['ticket_type']} | Destination: {ticket_info['destination']} | Service Type: {ticket_info['service_type']}")
    else:
        print(f"No ticket found for {passenger_name}.")

def edit_ticket(tix):
    passenger_name = input("Please enter the passenger's name to edit their ticket: ").strip().title()
    if not passenger_name:
        print("Passenger name cannot be empty.")
        return
    if passenger_name in tix:
        print(f"Editing ticket for {passenger_name}. Current details: {tix[passenger_name]}")
        revise_ticket = input("Do you want to revise the ticket? (Y/N): ").strip().lower()
        if revise_ticket == 'y':
            del tix[passenger_name]
            print("Please fill up the new ticket details.")
            issue_ticket(tix)  
    else:
        print(f"No ticket found for {passenger_name}.")

def train_info():
    commuter_info = ("Stops at all stations", "Travel time: Slow-Moderate", "Cheapest Fare")
    commuter_express_info = ("Stops at selected stations", "Travel time: Moderate-Fast", "Moderate Fare")
    airport_limited_express_info = ("Direct service to the airport", "Travel time: Fast", "Expensive Fare")
    print("Welcome to the train service information page! Here are the details of our train services:")
    time.sleep(1)
    print(f"1. Commuter: {commuter_info[0]}, {commuter_info[1]}, {commuter_info[2]}")
    time.sleep(1)
    print(f"2. Commuter Express: {commuter_express_info[0]}, {commuter_express_info[1]}, {commuter_express_info[2]}")
    time.sleep(1)
    print(f"3. Airport Limited-Express: {airport_limited_express_info[0]}, {airport_limited_express_info[1]}, {airport_limited_express_info[2]}")
    time.sleep(1)

def main():
    tix = {}
    while True:
        print("Initializing the ticket machine...")
        time.sleep(1.5)
        print(""""========YUAN'S NSCR(NORTHBOUND) TICKET MACHINE SIMULATOR=========
        Welcome to Tutuban Station!

        Dear Customer, please select an option:
        1. Issue Ticket
        2. Find Ticket
        3. Edit Ticket
        4. Train Information
        5. Exit""")
        choice = input("Please select an option (1-5): ").strip()
        try:
            if choice == '1':
                issue_ticket(tix)
            if choice == '2':
                find_tickets(tix)
            if choice == '3':
                edit_ticket(tix)
            if choice == '4':
                train_info()
            if choice == '5':
                print("Enjoy your journey!")
                time.sleep(0.5)
                print("Exiting the program...")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

main()