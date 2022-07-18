MAJOR_SUBJECT_MARKS = 100;
MINOR_SUBJECT_MARKS = 50;
TOTAL_MARKS = 400;

obtained_marks = 0

def getMarks(subject, max_marks):
    global obtained_marks
    
    while True:
        try:
            numbers = int(input(subject + "'s marks: "))

            if (numbers<=max_marks and numbers>0):
                obtained_marks += numbers
                return numbers;

            print("Invalid marks 0-100.")
        except ValueError:
            print("Only number allowed.")

print("\n")

physics = getMarks('Physic', MAJOR_SUBJECT_MARKS);
chemistry = getMarks('Chemistry', MAJOR_SUBJECT_MARKS);
maths = getMarks('Mathematics', MAJOR_SUBJECT_MARKS);
english = getMarks('English', MINOR_SUBJECT_MARKS);
arabic = getMarks('Arabic', MINOR_SUBJECT_MARKS);

print("\n************* Student Marksheet *************\n")
print("Physics\t\t\t  : " + str(physics))
print("Chemistry\t\t  : " + str(chemistry))
print("Mathematics\t\t  : " + str(maths))
print("English\t\t\t  : " + str(english))
print("Arabic\t\t\t  : " + str(arabic))

print("\n\nTotal Marks Obtained      :", obtained_marks, "out of", TOTAL_MARKS, sep=' ')
print("Total Percentage Obtained :", round((obtained_marks*100)/TOTAL_MARKS, 2), "%", sep=' ', end='\n\n')