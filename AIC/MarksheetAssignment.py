MAJOR_SUBJECT_MARKS = 100;
MINOR_SUBJECT_MARKS = 50;
TOTAL_MARKS = 450;


# Enter Physics marks
while True:
    try:
        physics = int(input("Physics marks: "))

        if (physics<=MAJOR_SUBJECT_MARKS and physics>0):
            break

        print("Invalid marks 0-100.")
    except ValueError:
        print("Only number allowed.")

# Enter Chemistry marks
while True:
    try:
        chemistry = int(input("Chemistry marks: "))

        if (chemistry<=MAJOR_SUBJECT_MARKS and chemistry>0):
            break
        
        print("Invalid marks 0-100.")
    except ValueError:
        print("Only number allowed.")
        continue

# Enter Mathematics marks
while True:
    try:
        maths = int(input("Mathematics marks: "))

        if (maths<=MAJOR_SUBJECT_MARKS and maths>0):
            break
        
        print("Invalid marks 0-100.")
    except ValueError:
        print("Only number allowed.")

# Enter English marks
while True:
    try:
        english = int(input("English marks: "))

        if (english<=MAJOR_SUBJECT_MARKS and english>0):
            break
        
        print("Invalid marks 0-100.")
    except ValueError:
        print("Only number allowed.")
        continue

# Enter Arabic marks
while True:
    try:
        arabic = int(input("Arabic marks: "))

        if (arabic<=MINOR_SUBJECT_MARKS and arabic>0):
            break
        
        print("Invalid marks 0-50.")
    except ValueError:
        print("Only number allowed.")

print("\n************* Student Marksheet *************\n")
print("Physics\t\t\t  : " + str(physics))
print("Chemistry\t\t  : " + str(chemistry))
print("Mathematics\t\t  : " + str(maths))
print("English\t\t\t  : " + str(english))
print("Arabic\t\t\t  : " + str(arabic))

obtained_marks = physics + chemistry + maths + english + arabic
print("\n\nTotal Marks Obtained      :", obtained_marks, "out of", TOTAL_MARKS, sep=' ')
print("Total Percentage Obtained :", round((obtained_marks*100)/TOTAL_MARKS, 2), "%", sep=' ', end='\n\n')