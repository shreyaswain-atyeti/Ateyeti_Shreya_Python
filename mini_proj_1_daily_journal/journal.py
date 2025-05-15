import os
from datetime import datetime

DATA_DIR = "journal_data"

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

def main():
    ensure_data_dir()
    while True:
        print("\n Daily Journal CLI")
        print("1. Add Entry")
        

        choice = input("Choose an option: ")
        if choice == "1":
            add_entry()
        
if __name__ == "__main__":
    main()