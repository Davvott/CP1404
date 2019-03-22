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

# TODO: Print the list of (10) scores per subject with the maximum per subject

# TODO: Print minimum and average for each subject, pretty print


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")

    scores_data = scores_file.readlines()
    print(scores_data)

    subjects = scores_data[0].strip().split(",")

    score_values = []
    # Appends each students' subject score_value
    for student_scores in scores_data[1:]:
        score_strings = student_scores.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)

    scores_file.close()

    # Prints students subject score_values
    for i in range(len(subjects)):

        print(subjects[i], "Scores:")

        for score in score_values[i]:
            print(score)

        print("Max:", max(score_values[i]))
        print()


main()
