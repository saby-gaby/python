submissions = {}
results = {}
submission = input().split('-')

while len(submission) > 1:

    if len(submission) == 3:
        username, language, points = submission[0], submission[1], int(submission[2])
        if username not in results.keys():
            results[username] = 0
        if results[username] < points:
            results[username] = points
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
    elif len(submission) == 2:
        username = submission[0]
        del results[username]

    submission = input().split('-')

print('Results:')
for username, points in results.items():
    print(f'{username} | {points}')
print('Submissions:')
for language, points in submissions.items():
    print(f'{language} - {points}')


# tests
# Peter-Java-84
# George-C#-84
# George-C#-70
# Katy-C#-94
# exam finished

# Peter-Java-91
# George-C#-84
# Katy-Java-90
# Katy-C#-50
# Katy-banned
# exam finished