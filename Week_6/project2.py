def computer_science():
    jamb = int(input("What is your JAMB score\n"))
    credit = input("Do you have at least 5 credits in your 5 key subject\n")
    interview = input("Did you pass the interview\n")
    if jamb >= 250 and credit == "yes" and interview == "yes":
        print("You have been admitted into the computer science department")
    else:
        print("Unfortunately, you were not admitted into the computer science department")
    return

    

def mass_communication():
    jamb = int(input("What is your JAMB score\n"))
    credit = input("Do you have at least 5 credits in your 5 key subject\n")
    interview = input("Did you pass the interview\n")
    if jamb >= 230 and credit == "yes" and interview == "yes":
        print("You have been admitted into the mass communication department")
    else:
        print("Unfortunately, you were not admitted into the mass communication department")
    return


name = input("Input your candidate name ")
Admission = input("If you are applied for computer science input computer scince and if you applied for mass communication input mass communication\n")
if Admission == "computer science":
    computer_science()
elif Admission == "mass communication":
    mass_communication()
else:
    print("Enter computer science or mass communication")
    
Admitted = []
noAdmitted = []

if computer_science() == "You have been admitted into the computer science department":
    Admitted.append(name)
else:
    noAdmitted.append(name)

if mass_communication() == "You have been admitted into the mass communication department":
    Admitted.append(name)
else:
    noAdmitted.append(name)

print(Admitted)
print(noAdmitted)