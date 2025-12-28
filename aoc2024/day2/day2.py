def isSafeLevel(report):
    if len(report) == 1:
        return True

    if report[0] == report[1]:
        return False

    isAsc = report[0] < report[1]

    if isAsc:
        for i in range(len(report) - 1):
            if report[i] >= report[i + 1] or report[i] + 3 < report[i + 1]:
                return False
    else:
        for i in range(len(report) - 1):
            if report[i] <= report[i + 1] or report[i] - 3 > report[i + 1]:
                return False

    return True



def isSafeLevelT(report):
    isSafe = isSafeLevel(report)
    if isSafe:    
        return True

    res = []
    for i in range(len(report)):
        r = report[:i] + report[i + 1:]
        res.append(isSafeLevel(r))

    return any(res)



with open('day2.txt', "r") as file:
    totalSafe = 0
    totalSafeWithTolerance = 0
    for report in file:
        report = report.split(" ")

        report = [int(level) for level in report]

        if isSafeLevel(report):
            totalSafe += 1

        if isSafeLevelT(report):
            totalSafeWithTolerance += 1
        
    print(totalSafe)
    print(totalSafeWithTolerance)
        