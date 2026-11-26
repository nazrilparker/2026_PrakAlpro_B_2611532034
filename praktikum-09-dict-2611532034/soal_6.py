
schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a.
busiest_day = ""
most_courses = 0

for day, courses in schedule.items():
    if len(courses) > most_courses:
        most_courses = len(courses)
        busiest_day = day

print(f"Busiest day: {busiest_day} ({most_courses} courses)")

# 6b.
course = input("Enter course name: ")
count = 0

for day, courses in schedule.items():
    if course in courses:
        count += 1

print(f"{course}: {count} days")
