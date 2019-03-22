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
from pprint import pprint


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")

    student_score_values = []
    # Appends each students' subject score_value
    for student_scores in scores_data[1:]:
        score_strings = student_scores.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        student_score_values.append(score_numbers)

    scores_file.close()

    subject_dict = arrange_scores_by_subject(student_score_values, subjects)

    display_score_table(subject_dict)
    display_simple_min_max_avg(subject_dict)
    # basic_print_scores(student_score_values, subject_dict)


def display_score_table(subject_dict):
    """Prints table from dict values with dict keys as headers"""
    subjects = [key for key in subject_dict.keys()]

    for key in subject_dict.keys():
        print("{:>10}".format(key), end='')
    print()
    for i in range(len(subject_dict[subjects[0]])):
        for j in range(len(subjects)):
            print("{:>10}".format(subject_dict[subjects[j]][i]), end='')
        print()


def display_simple_min_max_avg(subject_dict):
    """Print Min Max Avg from dict of scores"""
    subjects = [key for key in subject_dict.keys()]
    print("\nMax", end='')
    for i in range(len(subjects)):
        print("{:>7}   ".format(max(subject_dict[subjects[i]])), end='')

    print("\nMin", end='')
    for i in range(len(subjects)):
        print("{:>7}   ".format(min(subject_dict[subjects[i]])), end='')

    print("\nAvg", end='')
    for i in range(len(subjects)):
        print("{:>7}   ".format(sum(subject_dict[subjects[i]]) /
              len(subject_dict[subjects[i]])), end='')


def basic_print_scores(student_score_values, subject_dict):
    for i, key in enumerate(subject_dict.keys()):
        print(key, "Scores:")

        for score_list in student_score_values:
            print(score_list[i], end=' ')

        print("\nMax: ", max(subject_dict[key]),
              "\nMin: ", min(subject_dict[key]),
              "\nAvg: ", sum(subject_dict[key]) / len(subject_dict[key]))
        print()


def arrange_scores_by_subject(student_score_values, subjects):
    """Return list of scores as dict{subject:score_list}"""
    subject_dict = {}
    for i in range(len(subjects)):
        subject_dict[subjects[i]] = []
        for score_list in student_score_values:
            subject_dict[subjects[i]].append(score_list[i])
    return subject_dict


main()
