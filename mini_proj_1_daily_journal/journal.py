import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "journal_data")


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def get_filename(date_str):
    return os.path.join(DATA_DIR, f"{date_str}.txt")

def add_entry():
    date_str = datetime.today().strftime("%Y-%m-%d")
    print(f"Adding entry for {date_str}. Type your entry below:")
    entry = input("> ")
    with open(get_filename(date_str), "a") as f:
        f.write(f"{datetime.now().strftime('%H:%M')} - {entry}\n")
    print("Entry saved!")

def view_entries():
    date_str = input("Enter the date you want to view in a format (YYYY-MM-DD) ")
    filename = get_filename(date_str)
    if os.path.exists(filename):
        with open(filename,"r") as f:
            print(f"\n Entries for {date_str}--")
            print(f.read())

    else:
        print("No entries found for this date")

def list_dates():
    files = os.listdir(DATA_DIR)
    dates = [f.replace(".txt","") for f in files]
    print("\n Journal Dates: ")
    for date in sorted(dates):
        print(date)

def main():
    ensure_data_dir()
    while True:
        print("\n Daily Journal CLI")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. List All Entry Dates")
        print("4. Exit")
        

        choice = input("Choose an option: ")
        if choice == "1":
            add_entry()
        if choice == "2":
            view_entries()
        if choice == "3":
            list_dates()
        if choice == "4":
            print("Bubye")
            break
        else:
            print("Invalid Choice")
            

        
if __name__ == "__main__":
    main()