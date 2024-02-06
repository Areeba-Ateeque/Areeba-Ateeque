# variable expressions 
#1:building fitness 
daily_step=5000
distance_walked=2.5
calories=250
#calculate average steps 
average_step_per_week=(daily_step*7)/7
# calculate total_distance
total_distance_covered_in_month=distance_walked*30
#result 
print("average_step_per_week:", average_step_per_week)
print("total_distance_covered_in_month:",total_distance_covered_in_month)
# 2.shopping list 
item_name = ["shirt", "jacket", "jeans", "scarf"]
price = [2.5, 2.3, 5.2, 8.0]
quantity = [2, 4, 3, 2]
budget = 2.0

# Calculate the total_cost
total_cost = sum(quantity * price for quantity, price in zip(quantity, price))

# Budget check
if total_cost <= budget:
    print("You have enough budget.")
else:
    print("Review your shopping list.")
#3.Recipt calculator 
num_servings = int(input("Enter number of serving"))

ingredients = ["meat", "oil", "rice", "water", "yogurt", "masaly"]

amounts = [ 1 , 2 , 4 , 6 , 1 , 3 ]

adjusted_quantities = [amount * num_servings for amount in amounts]

print (adjusted_quantities)
#4
# Movie Recommendation System
# User preferences
user_genre = input("Enter your preferred movie genre: ")
user_rating = float(input("Enter your preferred movie rating (0.0 to 10.0): "))
user_release_year = int(input("Enter your preferred movie release year: "))

# Sample movie data
movies = [
    {"title": "Movie1", "genre": "Action", "rating": 8.5, "release_year": 2020},
    {"title": "Movie2", "genre": "Comedy", "rating": 7.2, "release_year": 2019},
    {"title": "Movie3", "genre": "Drama", "rating": 9.0, "release_year": 2023},
]

# Recommend movies based on user preferences
recommended_movies = []
for movie in movies:
    if (
        user_genre.lower() == movie["genre"].lower()
        and user_rating <= movie["rating"]
        and user_release_year == movie["release_year"]
    ):
        recommended_movies.append(movie["title"])

# Display recommendations
if recommended_movies:
    print("Recommended movies:")
    for title in recommended_movies:
        print(f"- {title}")
else:
    print("No movies match your preferences. Try adjusting your criteria.")
#5.
# Time Management Tools
taska_name = "assignment"
task1_duration = 2.5  # in hours

taskb_name = "presentation"
task2_duration = 1.5  # in hours

taskc_name = "shopping"
task3_duration = 1.0  # in hour 
# Calculate total time spent on each task
total_task1_time = task1_duration
total_task2_time = task2_duration
total_task3_time = task3_duration

# Calculate overall total time
total_time = total_task1_time + total_task2_time + total_task3_time
#result 
print(f"Total time spent on {taska_name}: {total_task1_time} hours")
print(f"Total time spent on {taskb_name}: {total_task2_time} hours")
print(f"Total time spent on {taskc_name}: {total_task3_time} hours")

print(f"\nOverall total time spent: {total_time:.2f} hours")