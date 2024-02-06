#Bonus chalange :
#Create your own real-life example problems related to your hobbies, interests, or daily routines. Think creatively and apply your understanding of variables, operators, and expressions to solve at least 3 practical problems
# Attendance records for each student daily routine:
student1_attendance = 4
student2_attendance = 5
student3_attendance = 3
student4_attendance = 5
student5_attendance = 2

# Total possible attendances per student
max_attendance = 5
# Calculate total attendance for the class
total_attendance = (
    student1_attendance + student2_attendance +
    student3_attendance + student4_attendance +
    student5_attendance
)
# Calculate average attendance percentage
average_percentage = (total_attendance / (max_attendance * 5)) * 100

print(f"The average attendance percentage for the class is {average_percentage:.2f}%.")

# problem no 2:  hobbies novel read 
# Daily  Novel pages read
monday_pages = 25
tuesday_pages = 30
wednesday_pages = 40

# Weekly goal
weekly_goal = 50

# Calculate total pages read so far
total_pages_read = monday_pages + tuesday_pages + wednesday_pages

# Calculate remaining pages needed to reach the weekly goal
remaining_pages = max(0, weekly_goal - total_pages_read)

print(f"You need to read {remaining_pages} more pages to reach your weekly goal.")


# Bonus chalange:3 interest Gardening problem 
flower_cost = 5
num_flowers = 10
soil_cost = 15
# Calculate total cost for flowers
flower_total_cost = flower_cost * num_flowers
# Calculate total cost including soil
total_cost = flower_total_cost + soil_cost
print(f"You will spend $ {total_cost} in total for the flowers and soil.")
