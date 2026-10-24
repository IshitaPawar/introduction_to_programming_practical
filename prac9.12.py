def input_marks(number_of_subjects):
    marks = []
    for subject in range(number_of_subjects):
        mark = float(input(f"Enter marks for subject {subject + 1}: "))
        marks.append(mark)
    return marks

def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def main():
    marks = input_marks(5)
    total, percentage = calculate_result(marks)
    grade = assign_grade(percentage)

    print("Total marks:", total)
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)

main()
