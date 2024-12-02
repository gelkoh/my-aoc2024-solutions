def read_input():
    with open("day02-input.txt") as f:
        return f.readlines()

def get_num_of_safe_reports(reports):
    num_of_safe_reports = 0

    def check_report(report, order):
        is_level_removed = False

        for idx in range(len(report) - 1):
            step_size = report[idx + 1] - report[idx]
            abs_step_size = abs(step_size)

            invalid_conditions = [
                abs_step_size == 0,
                abs_step_size < 1 or abs_step_size > 3,
                order == "asc" and step_size < 0,
                order == "desc" and step_size > 0,
            ]

            if any(invalid_conditions):
                if not is_level_removed:
                    is_level_removed = True
                    continue

                return False

        return True

    for report in reports:
        report = list(map(int, report.split()))
        order = None

        if (
            report[0] < report[1] or
            report[0] < report[2] or 
            report[1] < report[2]
        ):
            order = "asc"
        elif (
            report[0] > report[1] or
            report[0] > report[2] or
            report[1] > report[2]
        ):
            order = "desc"

        if check_report(report, order):
            num_of_safe_reports += 1

    return num_of_safe_reports

def main():
    reports = read_input()
    num_of_safe_reports = get_num_of_safe_reports(reports)

    print("Num of safe reports:", num_of_safe_reports)
    
if __name__ == "__main__":
    main()
