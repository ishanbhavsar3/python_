print("Welcome to automatic booking software developed by Ishan Bhavsar.")
name = input("What is your name? ")
age = input("What is your age(In numbers only.) ")
gender = input("What is your gender?(Male/Female) ").upper()
marriage_check = input("Are you married?(Yes or No Only)").upper()


if int(age) < 18:
    print("""Please contact a guardian.
    You are a minor and hence you cannot book by yourselves.""")
    guardian_name = input("What is your name?(To be filled by GUARDIAN ONLY.) ")
    guardian_age = input("What is your age?(In numbers only.) ")
    guardian_gender = input("What is your gender(Male/Female)").upper()
    marriage_check = input("Are you married?(Yes or No Only)").upper()
    if int(guardian_age) >= 18:
        if guardian_gender == "MALE":
            if marriage_check == "YES":
                print(f"Mr.{guardian_name},Your booking has been done.Thank You for using our software.")
            elif marriage_check == "NO":
                print(f"Master.{guardian_name},Your booking has been done.Thank You for using our software.")
            else:
                print(f"{guardian_name},Your booking has been done.Thank You for using our software.")
        elif guardian_gender == "FEMALE":
            if marriage_check == "YES":
                print(f"Mrs.{guardian_name},Your booking has been done.Thank You for using our software.")
            elif marriage_check == "NO":
                print(f"Miss.{guardian_name},Your booking has been done.Thank You for using our software.")
            else:
                print(f"{guardian_name},Your booking has been done.Thank You for using our software.")
        else:
            print("""Please put in a suitable gender.
                     People with genders other than MALE and FEMALE are not allowed at our place.""")

    else:
        print("Please bring a major (18+) guardian to get the booking done.")
        closure_asking = "If you wish to quit,simply press the red cross on the top right."
        print(closure_asking)
if gender == "MALE":
    if marriage_check == "YES":
        print(f"Mr.{name},Your booking has been done.Thank You for using our software.")
    elif marriage_check == "NO":
        print(f"Master.{name},Your booking has been done.Thank You for using our software.")
elif gender == "FEMALE":
    if marriage_check == "YES":
        print(f"Mrs.{name},Your booking has been done.Thank You for using our software.")
    elif marriage_check == "NO":
        print(f"Miss.{name},Your booking has been done.Thank You for using our software.")
else:
    print("""Please put in a suitable gender.
                     People with genders other than MALE and FEMALE are not allowed at our place.""")


the_god = input("What is your name?")
if the_god == "Ishan":
    print("Welcome master.")
else:
    print(f"{the_god} you are not my master")





