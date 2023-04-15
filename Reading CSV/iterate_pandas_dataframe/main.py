import pandas
def main():
    student_dict = {
        "student": ["Usman", "James", "John"],
        "score": [12, 53, 77]
    }
    student_data_frame = pandas.DataFrame(student_dict)

    # Loop through rows of students
    for (index, row) in student_data_frame.iterrows():
        # Get the score for a specific student
        if row.student == "Usman":
            print(row.score)


if __name__ == '__main__':
    main()