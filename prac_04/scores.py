"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice.
Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""




def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")

    scores_data = scores_file.readlines()
    print(scores_data)

    subjects = scores_data[0].strip().split(",")

    student_score_values = []
    # Appends each students' subject score_value
    for student_scores in scores_data[1:]:
        score_strings = student_scores.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        student_score_values.append(score_numbers)

        # FOr subjects[i], append score_num[i];

    scores_file.close()

    subject_dict = {}
    for i in range(len(subjects)):
        subject_dict[subjects[i]] = []  # Create subject key
        subject_scores = []
        print(subjects[i], "Scores:")

        for j, score_list in enumerate(student_score_values):
            subject_dict[subjects[i]].append(score_list[i])
            subject_scores.append(score_list[i])
            print(score_list[i], end=' ')

        print("\nMax: ", max(subject_scores),
              "\nMin: ", min(subject_scores),
              "\nAvg: ", sum(subject_scores)/len(subject_scores))
        print()

    print(subject_dict)

    # TODO: pretty print table from data


main()
