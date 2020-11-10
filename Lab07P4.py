def main():
    num_labs = int(input("Enter number of labs: "))
    lab_scores = []
    for i in range(num_labs):
        lab_score = float(input("Enter lab score: "))
        lab_scores.append(lab_score)
    print(lab_scores)
    num_tests = int(input("Enter number of tests: "))
    test_scores = []
    for i in range(num_tests):
        test_score = float(input("Enter test score: "))
        test_scores.append(test_score)
    print(test_scores)
    print("The default weights for course grade are 50% labs and 50% tests.")
    weight_choice = input("Enter C to change the weights or D to use default weights: ")
    weight_choice.upper()
    while True:
        if weight_choice != "C":
            grade_calculator(lab_scores, test_scores)
            break

        elif weight_choice == "C":
            lab_weight = float(input("Enter lab weight percentage (without % sign): "))
            lab_weight = lab_weight/100
            test_weight = float(input("Enter test weight percentage (without the % sign): "))
            test_weight = test_weight/100
            grade_calculator(lab_scores, test_scores, lab_weight, test_weight)
            break


def grade_calculator(lab, test, lab_weight=.50, test_weight=.50):
    lab_average = (sum(lab) / len(lab))
    print("Lab score average: %.2f" % lab_average)
    test_average = (sum(test) / len(test))
    print("Test score average: %.2f" % test_average)
    course_grade = (lab_average * lab_weight) + (test_average * test_weight)
    print("Course grade: %.2f" % course_grade)


main()
