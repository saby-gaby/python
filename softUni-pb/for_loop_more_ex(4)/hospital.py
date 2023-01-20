days = int(input())

doctors = 7
treated = 0
redirected = 0

for day in range(1, days + 1):
    if day % 3 == 0 and redirected > treated:
        doctors += 1

    patients = int(input())

    if patients > doctors:
        treated += doctors
        redirected += patients - doctors
    else:
        treated += patients


print(f'Treated patients: {treated}.')
print(f'Untreated patients: {redirected}.')
