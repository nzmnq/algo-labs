from red_black_priority_queue import RedBlackPriorityQueue
import os

class clear_screen:
    def __init__(self):
        pass
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

class BoardingGate:
    def __init__(self):
        self.queue = RedBlackPriorityQueue()
        self.passenger_count = 0 
        self.deleted_count = 0
        self.waiting_list = [] 

        self.priority_map = {
            "VIP": 100,
            "Special Needs": 80,
            "Business": 60,
            "Economy": 20
        }

    def register_passenger(self, name, status):
        if status not in self.priority_map:
            print(f"Error: Unknown status")
            return

        priority = self.priority_map[status]
        passenger_info = f'{name} [{status}]'
        
        self.waiting_list.append(passenger_info) 
        self.queue.insert(passenger_info, priority)
        
        self.passenger_count += 1  
        print(f"[*] {name} successfully registered as {status}.")

    def start_boarding(self):
        print("\n BOARDING STARTED! ")
        
        count = 0
        while True:
            passenger_data = self.queue.pop() 
            
            if passenger_data is None:
                break
            self.passenger_count -= 1 
            self.deleted_count += 1
            count += 1
            print(f"{count}. Passenger {passenger_data[0]} is called for boarding!")
            
        if count == 0:
            print("Queue is empty. No one to board.")
        else:
            self.waiting_list.clear()
        
        print("Boarding completed!\n")

    def show_waiting_list(self):
        if self.waiting_list:
            print(f"Passengers waiting in queue: {self.waiting_list}")
        else:
            print("The waiting queue is currently empty.")
    
    def show_passenger_count(self):
        print(f"Total boarded (deleted from queue): {self.deleted_count}")
        return self.deleted_count
    
def main():
    gate = BoardingGate()    
    clear_terminal = clear_screen()
    clear_terminal.clear()
    print("System for Managing Boarding Gate")

    status_menu = {
        '1': 'VIP',
        '2': 'Special Needs',
        '3': 'Business',
        '4': 'Economy'
    }
    
    while True:
        print("\nAvailable Actions:")
        print("1 - Register Passenger")
        print("2 - Start Boarding")
        print("3 - Show Waiting Passengers")
        print("0 - Exit Program")
        
        choice = input("Choose an action: ")
        
        if choice == '1':
            name = input("Enter passenger name: ")
            clear_terminal.clear()
            print("\nChoose passenger status:")
            print("[1] - VIP")
            print("[2] - Special Needs")
            print("[3] - Business")
            print("[4] - Economy")
            
            status_choice = input("Enter status number (1-4): ")
            clear_terminal.clear()
            
            if status_choice in status_menu:
                status_word = status_menu[status_choice]
                gate.register_passenger(name, status_word)
            else:
                print("[-] Error: Invalid status number. Registration cancelled.")
            
        elif choice == '2':
            clear_terminal.clear()
            gate.start_boarding()
            gate.show_passenger_count()
        
        elif choice == '3':
            clear_terminal.clear()
            gate.show_waiting_list()

        elif choice == '0':
            clear_terminal.clear()
            print("Program execution completed.")
            break
        else:
            clear_terminal.clear()
            print("Unknown command. Please try again.")

if __name__ == '__main__':
    main()