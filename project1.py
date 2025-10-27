def countAvg(scores, avg):
    if avg >= 85:
        print("Excellent")
    elif avg >= 70:
        print("Good")
    else:
        print("Needs Improvement")

score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))

scores = [score1, score2, score3]

avg = sum(scores) / len(scores)

print(f"Average score: {avg:.2f}")
countAvg(scores, avg)