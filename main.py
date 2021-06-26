import sys


def parse_swiftlint_line(line):
    splitted = line.split('::')
    location, description = splitted[0], splitted[1]
    location_arr = location.split(',')
    file, line, col = location_arr[0], location_arr[1], location_arr[2]
    return f"*File:* {file}\n" \
           f"*Location:* ({line.replace('line=', '')}, {col.replace('col=', '')})\n" \
           f"*Description:* {description}\n"


def get_swiftlint_result():
    path = sys.argv[1]
    swiftlint_results_file = open(path, 'r')
    lines = swiftlint_results_file.readlines()

    swiftlint_report = ""
    errors_report = "⛔️ Errors\n\n"
    warnings_report = "⚠️ Warnings\n\n"
    errors_count = 0
    warnings_count = 0

    for line in lines:
        if 'Done linting' in line:
            break

        if '::warning file=' in line:
            warnings_count += 1
            new_line = line.replace('::warning file=', '')
            warnings_report += parse_swiftlint_line(new_line)
            continue

        if '::error file=' in line:
            errors_count += 1
            new_line = line.replace('::error file=', '')
            errors_report += parse_swiftlint_line(new_line)
            continue

    if errors_count > 0:
        swiftlint_report += errors_report

    if warnings_count > 0:
        swiftlint_report += warnings_report

    if errors_count == 0 and warnings_count == 0:
        swiftlint_report = '✅ Successful! No linter warnings and errors\n'

    swiftlint_results_file.close()
    return swiftlint_report


def get_test_results():
    path = sys.argv[2]
    test_results_file = open(path, mode='r')
    test_results = test_results_file.read()
    test_results_file.close()
    return test_results


if __name__ == '__main__':
    report = f'*Author:* {sys.argv[3]}\n\n' \
             f'*Linter:*\n' \
             f'{get_swiftlint_result()}\n' \
             f'*Test results:*\n' \
             f'{get_test_results()}'

    textfile = open("./Artifacts/ReviewReport.txt", "w")
    textfile.write(report)
    textfile.close()
