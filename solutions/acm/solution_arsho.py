"""
Title     : ACM Contest Scoring
Source    : 2015 ICPC Mid-Central Regional
URL       : https://open.kattis.com/problems/acm
Author    : arsho
Created   : 04 January 2022
"""
table = {}
total_penalty = 0
total_solve = 0
while True:
    line = input()
    if line == "-1":
        print(total_solve, total_penalty)
        break
    else:
        submission_time, problem, verdict = line.split(" ")
        submission_time = int(submission_time)
        if problem not in table:
            if verdict == "right":
                total_solve += 1
                table[problem] = {
                    "solved": True,
                    "penalty": submission_time
                }
                total_penalty += submission_time
            else:
                table[problem] = {
                    "solved": False,
                    "penalty": 20
                }
        else:
            penalty = table[problem]["penalty"]
            if verdict == "right":
                if not table[problem]["solved"]:
                    total_solve += 1
                    table[problem] = {
                        "solved": True,
                        "penalty": penalty + submission_time
                    }
                    total_penalty += penalty + submission_time
            else:
                table[problem] = {
                    "solved": False,
                    "penalty": penalty + 20
                }
