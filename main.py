from typing import List, Dict, Optional
import os.path
import datetime


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}

    # checking if the file exist or not
    if not os.path.isfile(fileName):
        print(f"The file '{fileName}' could not be found.")
        exit()

    # opening file
    with open(fileName, 'r') as files:
        try:
            # traversing single line
            for line in files:
                # spliting data
                field = line.strip().split(",")

                # Checking number of field
                if len(field) != 8:
                    print(f"Invalid number of fields {len(field)} in line: {line}")
                    continue

                # Check the format of the patient ID
                try:
                    patient_id = int(field[0])
                except ValueError:
                    print(f"Invalid patient ID in line: {line}")
                    continue

                # Check the format of the other data values
                try:
                    date = field[1]
                    temp = float(field[2])
                    hr = int(field[3])
                    rr = int(field[4])
                    systolic = int(field[5])
                    diastolic = int(field[6])
                    oxsat = int(field[7])
                    #implementing condtion to find the invalid data
                    if temp < 35 or temp > 42:
                        print(f"Invalid temperature value ({temp}) in line: {line}")
                        continue
                    if hr < 30 or hr > 180:
                        print(f"Invalid heart rate value ({hr}) in line: {line}")
                        continue
                    if rr < 5 or rr > 40:
                        print(f"Invalid respiratory rate value ({rr}) in line: {line}")
                        continue
                    if systolic < 70 or systolic > 200:
                        print(f"Invalid systolic blood pressure value ({systolic}) in line: {line}")
                        continue
                    if diastolic < 40 or diastolic > 120:
                        print(f"Invalid diastolic blood pressure value ({diastolic}) in line: {line}")
                        continue
                    if oxsat < 70 or oxsat > 100:
                        print(f"Invalid oxygen saturation value ({oxsat}) in line: {line}")
                        continue
                    # adding data to dict
                    if patient_id in patients:
                        datatoappent = [date, temp, hr, rr, systolic, diastolic, oxsat]
                        patients[patient_id].append(datatoappent)
                    else:
                        datatoappent = [date, temp, hr, rr, systolic, diastolic, oxsat]
                        patients[patient_id] = [datatoappent[0:]]



                except ValueError:
                    print(f"Invalid data type in line: {line}")
                    continue

        except:
            print("An unexpected error occurred while reading the file.")

    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################

    if patientId == 0:
        #dispalying all data from the dic
        for id in patients:
            patient_data = patients[id]
            print(f"Patient ID: {id}")
            for visit in patient_data:
                print(f"Visit date: {visit[0]}")
                print(f"Temperature: {visit[1]}C")
                print(f"Heart rate: {visit[2]}bpm")
                print(f"Respiratory rate: {visit[3]}bpm")
                print(f"Systolic blood pressure: {visit[4]}mmHg")
                print(f"Diastolic blood pressure: {visit[5]}mmHg")
                print(f"Oxygen saturation: {visit[6]}%")
                print(" ")
            print("")
    else:
        #displaying specific data from the dict
        if patientId not in patients:
            print("No data found for patient id: ", patientId)
            return
    
        patient_data = patients[patientId]
        print(f"Patient ID: {patientId}")
        for visit in patient_data:
            print(f"Visit date: {visit[0]}")
            print(f"Temperature: {visit[1]}C")
            print(f"Heart rate: {visit[2]}bpm")
            print(f"Respiratory rate: {visit[3]}bpm")
            print(f"Systolic blood pressure: {visit[4]}mmHg")
            print(f"Diastolic blood pressure: {visit[5]}mmHg")
            print(f"Oxygen saturation: {visit[6]}%")
            print(" ")
        print("")

    return


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################

    if type(patients)!=dict:
        print("Error: 'patients' should be a dictionary.")
        return
    # initilizing all values with 0 so that we can take avg
    tempsum = 0.0
    hrsum = 0
    rrsum = 0
    sys = 0
    dia = 0
    oxs = 0
    length = 0
    try:
        patientId = int(patientId)
    except:
        print("Patient id is not an integer")
        return

    if patientId == 0:
        print(f"\nVital Signs for All Patients ")
        for id in patients:
            patient_data = patients[id]
            if len(patient_data) == 0:
                print("No data found for patient id: ", id)
                continue
            for visit in patient_data:
                # adding all values with their previous values
                tempsum += visit[1]
                hrsum += visit[2]
                rrsum += visit[3]
                sys += visit[4]
                dia += visit[5]
                oxs += visit[6]
                length += 1

        print("Average temperature:", "%.2f" % (tempsum / length), "C")
        print("Average heart rate:","%.2f" % (hrsum / length),"bpm")
        print("Average respiratory rate: ","%.2f" %(rrsum / length),"bpm")
        print("Average systolic blood pressure:", "%.2f" %(sys / length),"mmHg")
        print("Average diastolic blood pressure:","%.2f" % (dia / length),"mmHg")
        print("Average oxygen saturation:", "%.2f" %(oxs / length),"mmHg")
        print(" ")
    else:
        if patientId not in patients:
            print("No data found for patient id: ", patientId)
            return

        patient_data = patients[patientId]
        for visit in patient_data:
            #adding all values with their previous values
            tempsum += visit[1]
            hrsum += visit[2]
            rrsum += visit[3]
            sys += visit[4]
            dia += visit[5]
            oxs += visit[6]
            length += 1

        print(f"\nVital Signs for patients id: ",patientId)
        print("Average temperature:", "%.2f" % (tempsum / length), "C")
        print("Average heart rate:","%.2f" % (hrsum / length),"bpm")
        print("Average respiratory rate: ","%.2f" %(rrsum / length),"bpm")
        print("Average systolic blood pressure:", "%.2f" %(sys / length),"mmHg")
        print("Average diastolic blood pressure:","%.2f" % (dia / length),"mmHg")
        print("Average oxygen saturation:", "%.2f" %(oxs / length),"mmHg")
        print(" ")


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
    try:


        # Checking if date format is valid
        date_str = date
        try:
            date23 = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
            return

        # Checking if date is valid
        try:
            datetime.date(date23.year, date23.month, date23.day)
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            return

        # Checking temperature
        temperature = float(temp)
        if temperature < 35.0 or temperature > 42.0:
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return

        # Checking heart rate
        heart_rate = int(hr)
        if heart_rate < 30 or heart_rate > 180:
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
            return

        # Checking respiratory rate
        respiratory_rate = int(rr)
        if respiratory_rate < 5 or respiratory_rate > 40:
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return

        # Checking systolic blood pressure
        systolic_bp = int(sbp)
        if systolic_bp < 70 or systolic_bp > 200:
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return

        # Checking diastolic blood pressure
        diastolic_bp = int(dbp)
        if diastolic_bp < 40 or diastolic_bp > 120:
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
            return

        # Checking oxygen saturation level
        oxygen_saturation = int(spo2)
        if oxygen_saturation < 70 or oxygen_saturation > 100:
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return

        # Add data to patient's record

        # Checking if patient_id exists in patients
        if patientId not in patients:
            patients[patientId] = []
            return
        datatoappent = [date, temp, hr, rr, sbp, dbp, spo2]
        patients[patientId].append(datatoappent)

        with open(fileName, 'a') as file:
            file.write(f'\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}')

    except Exception:
        print("An unexpected error occurred while adding new data.")


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits12 = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    if not bool(patients):
        print("The dictionary is empty.")
        return  visits12
    #starting a loop that will run if year and month are none
    if month==None and year==None:
        #taking values from dictionary
        for patient_id, visits in patients.items():
            for visit in visits:
                try:
                    data = [visit[0], float(visit[1]), int(visit[2]), int(visit[3]), int(visit[4]), int(visit[5]),
                            int(visit[6])]
                    dataadd = (patient_id, data)
                    #appending value in list
                    visits12.append(dataadd)
                except ValueError:
                    print("Value Error")
                    continue

        return visits12

    # starting a loop that will run if year and month are none
    if month==None:
        # taking values from dictionary
        for patient_id, visits in patients.items():
            for visit in visits:
                try:
                    visityear, visitmonth, visitdate = str(visit[0]).split('-')
                    # checking if the year from user and dict matches
                    if year != int(visityear):
                        continue
                    data = [visit[0], float(visit[1]), int(visit[2]), int(visit[3]), int(visit[4]), int(visit[5]),
                            int(visit[6])]
                    # appending value in list
                    dataadd = (patient_id, data)
                    visits12.append(dataadd)
                except ValueError:
                    print("Value Error")
                    continue

        return visits12


    if month<0 or month>12:
        return visits12


    if year==None:
        for patient_id, visits in patients.items():
            for visit in visits:
                try:
                    #separating the date
                    visityear, visitmonth, visitdate = str(visit[0]).split('-')
                    #checking if the month from user and dict matches
                    if month != int(visitmonth):
                        continue
                    data = [visit[0], float(visit[1]), int(visit[2]), int(visit[3]), int(visit[4]), int(visit[5]),
                            int(visit[6])]
                    dataadd = (patient_id, data)
                    visits12.append(dataadd)
                except ValueError:
                    print("Value Error")
                    continue

        return visits12

    for patient_id, visits in patients.items():
        for visit in visits:
            try:
                #separting the date
                visityear, visitmonth,visitdate  = str(visit[0]).split('-')
                #checking if the year and month matches
                if year != int(visityear):
                    continue
                if month != int(visitmonth):
                    continue
                data=[visit[0],float(visit[1]),int(visit[2]),int(visit[3]),int(visit[4]),int(visit[5]),int(visit[6])]
                dataadd=(patient_id,data)
                visits12.append(dataadd)
            except ValueError:
                print("Value Error")
                continue

    return visits12


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    con=False
    for patientid,visits in patients.items():
        for vist in visits:
            #saving values
            hr=vist[2]
            sys=vist[4]
            dia=vist[5]
            oxs=vist[6]
            #setting condition for follow ups
            if hr<60 or hr>100:
                con=True
            if sys>140:
                con=True
            if dia>90:
                con=True
            if oxs<90:
                con=True

        if con:
            followup_patients.append(patientid)
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################
    #checking if the ide exist or not
    if patientId not in patients:
        patients[patientId] = []
        print(f"No data found for patient with ID {patientId}")
        return

    writedict={}
    #starting loop to delete a given id values
    for patientid,visits in patients.items():
        #deleting specific id values
        if patientid==patientId:
            print(f'Data for patient {patientId} has been deleted.')
            continue
        #traversing in values of the dict
        for visit in visits:
            #add data to new dict so that we can write that dict in the file
            if patientid in writedict:
                datatoappent = [visit[0], visit[1], visit[2], visit[3], visit[4], visit[5], visit[6]]
                writedict[patientid].append(datatoappent)
            else:
                datatoappent = [visit[0], visit[1], visit[2], visit[3], visit[4], visit[5], visit[6]]
                writedict[patientid] = [datatoappent[0:]]
    with open(filename, 'w') as file:
        for patientID, visits in writedict.items():
            for visit in visits:
                    file.write(f'\n{patientID},{visit[0]},{visit[1]},{visit[2]},{visit[3]},{visit[4]},{visit[5]},{visit[6]}')



###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter tempe rature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
            patients = readPatientsFromFile('patients.txt')
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
