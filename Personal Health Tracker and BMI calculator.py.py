print("Welcome to the Personal Health Tracker and BMI Calculator\n")
print("------------------------------------------------")
print("BMI Classification")
print("------------------------------------------------")
print("Underweight: BMI < 18.5")
print("Normal weight: 18.5 <= BMI < 24.9")
print("Overweight: 25 <= BMI < 29.9")
print("Obese: BMI >= 30")
print("------------------------------------------------")
class BMI:
    def __init__(self, record_id, height, weight, born_date, act_description):
        self.record_id = record_id
        self.height = height
        self.weight = weight
        self.born_date = born_date
        self.act_desc = act_description

    def display(self):
        print(f"Record ID: {self.record_id}, Height: {self.height}m, Weight: {self.weight}kg, Born Date: {self.born_date}, Activity Description: {self.act_desc}")

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi
    
    def health_advice(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            health_status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            health_status = "Normal weight"
        elif 25 <= bmi < 29.9:
            health_status = "Overweight"
        else:
            health_status = "Obese"
        print(f"BMI: {bmi: .2f} ({health_status})")
        return bmi
    
records = []
is_on = True
while is_on:
    choice = int(input("1. Add a new health record\n2. View all health records\n3. Update a health record\n4. Delete a health record\n5. Calculate BMI and get health advice\n6. Analyze health trends\n7. Exit\nEnter your choice: "))
    if choice == 1:
        record_id = int(input("Enter Record ID: "))
        born_date = input("Enter Date (DD/MM/YYYY): ")
        new_weight = float(input("Enter Weight (kg): "))
        new_height = float(input("Enter Height (m): "))
        aci_description = input("Enter the Activity Description: ")
        new_record = BMI(record_id, new_height, new_weight, born_date, aci_description)
        records.append(new_record)
        print("Record added successfully!")
        confirmation = input("\nDo you want to continue? (y/n): \n")
        if confirmation == "y":
            pass

        elif confirmation == "n":
            print("\n")
            break

        else:
            print("\nINVALID CONFIRMATION!\n")
    
    elif choice == 2:
        if records:
            for record in records:
                record.display()
        else:
            print("No records found.")
        print("Health records shown successfully!")

    elif choice == 3:
        record_id_to_update = int(input("Enter the ID you want to Update: "))
        isRecordFounded = False
        for record in records:
            if record.record_id == record_id_to_update:
                isRecordFounded = True
        if isRecordFounded == True:
            print("Health record is founded...")
            print("Press1 for update Date (DD/MM/YYYY)")
            print("Press2 for update Weight (kg)")
            print("Press3 for update Height (m)")
            print("Press4 for update Activity Description")
            option = int(input("Choose what do you want to update?"))

            if option == 1:
                record.date = input("Enter the updated Date (DD/MM/YYYY): ")
            if option == 2:
                record.weight = float(input("Enter the updated Weight (kg): "))
            if option == 3:
                record.height = float(input("Enter the updated Height (m): "))
            elif option == 4:
                record.act_desc = input("Enter the updated Activity Description: ")
            else:
                print("INVALID OPTION!")
            print("Health record has been updated successfully !")

    elif choice == 4:
        record_id_to_delete = int(input("Enter the ID you want to Delete: "))
        isRecordFounded = False
        for record in records:
            if record.record_id == record_id_to_delete:
                isRecordFounded = True
                records.remove(record)
                print("Health record is deleted....")
            else:
                print("Health record not found....")
    
    elif choice == 5:
        record_id = int(input("Enter ID: "))
        foundRecord = None
        for record in records:
            if record.record_id == record_id:
                foundRecord = record
                break
        
        if foundRecord:
            foundRecord.health_advice()
        else:
            print("Health record not found.....")

    elif choice == 6:
        allBMIs = []
        allWeights = []
        for record in records:
            bmi = record.calculate_bmi()
            weight = record.weight
            allWeights.append(weight)
            allBMIs.append(bmi)
            if allBMIs:
                highest_bmi = max(allBMIs)
                average_weight = sum(allWeights)/len(allWeights)

                print(f"Highest BMI: {highest_bmi: .2f}")
                print(f"Average Weighest: {average_weight: .2f} kg")    
    
    elif choice == 7:
        print("\nThankyou for using the Personal Health Tracker and BMI Calculator.. GOODBYE!\n")
        is_on = False

    else:
        print("\nINVALID CHOICE! Please enter the correct choice!\n")
        is_on = False