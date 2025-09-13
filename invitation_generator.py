import os
os.system("cls" if os.name == "nt" else "clear")

RECIPIENTS_FILE = "Names/invited_names.txt"
TEMPLATE_FILE = "Input/Letters/starting_letter.txt"

def read_template():
    with open(TEMPLATE_FILE, "r") as file:
        return file.read()
    

def read_names():
    with open(RECIPIENTS_FILE, "r", encoding="utf-8") as file:
        names = file.read().splitlines()
        return list(dict.fromkeys([name.strip() for name in names if name.strip()]))

    
template = read_template()
guests = read_names()

def generate_invitations():
    for guest_name in guests:
        new_letter = template.replace("{name}", guest_name).replace("{signature}", "[Muhamad Ammar Team]")
        output_file = f"Output/Ready_to_send/letter_for_{guest_name.lower()}.txt"
        with open (output_file, "w") as file:
            file.write(new_letter)
        print(f"Generated invitation for {guest_name}")

        
generate_invitations()

