print("Exercise 1: Student Grades Analysis ")
print()
# 1. Calculate and print the average score for each student.

students = {
 "Alice": [85, 78, 92],
 "Bob": [79, 74, 81],
 "Charlie": [91, 82, 85],
 "David": [76, 85, 83],
 "Eve": [88, 79, 92]
}

students_score = []

for name in students:
    n = len(students[name])
    # len the number of values inside the key
    score = sum(students[name])/n
    print(f"{name}: {round(score, 1)}") # the round format the result of the number to 1 decimal place

# 2. Find and print the name of the student with the highest average score.
    students_score.append((name, round(score, 1)))

highest_score = float('-inf')  # -inf means starts with the lowest numb
lowest_score = float('inf')     # starts with the highest
top_student = ''
lowest_student = ''

for student in students_score:
    if student[1] > highest_score:  # [1] working only with the values in the tuple
        highest_score = student[1]
        top_student = student[0]  # name of student with the highest score

    if student[1] < lowest_score:  #
        lowest_score = student[1]
        lowest_student = student[0]

print(f"Highest average score is {top_student}: {round(highest_score, 1)}")

# 3. Find and print the name of the student with the lowest average score.
print(f"Lowest average score is {lowest_student}: {round(lowest_score, 1)}")

# 4. Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary.
students["Frank"] = [80, 90, 85]
print(students)

print("-"*80)
print("Exercise 2: Product Inventory Management ")
inventory = {
 "apple": (50, 0.5),
 "banana": (100, 0.2),
 "orange": (75, 0.3),
 "pear": (20, 0.4)
}

print(inventory)
print()
# 1. Print the current inventory in a user-friendly format.

print("Current Inventory:") #print the title
print("{:<20} {:<10} {:<10}".format("Item", "Quantity", "Price")) #print the space between the names n create a table
print("-" * 40) #print the under line

# print the items on it
for item, details in inventory.items(): #tuple pairs
    print("{:<20} {:<10} ${:<10.2f}".format(item, details[0], details[1])) #2f 2 decimal
print("-" * 40) #print the under line
# 2. Calculate and print the total value of the inventory
for v in inventory:
    val = inventory[v]
    total = val[0] * val[1]
    print(f"{v}: {total}")
print("-" * 40) #print the under line
# 3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
inventory['mango'] = (30, 0.6)
print(inventory)
# 4. Update the quantity of "banana" to 120 and print the updated inventory.
inventory['banana'] = (120, 0.2)
print(inventory)
# 5. Remove "pear" from the inventory and print the updated inventory.
del inventory['pear']
print(inventory)
print("-"*80)

print("Exercise 3: Employee Records ")

employees = [
 ("John Doe", "Accounting", "john.doe@example.com"),  ("Jane Smith", "Marketing", "jane.smith@example.com"),  ("Emily Davis", "HR", "emily.davis@example.com"),  ("Michael Brown", "IT", "michael.brown@example.com") ]

# 1. Print the names and departments of all employees.
for name, department, _ in employees:  # Iterando sobre a lista de tuplas
    print("{:<15} {:<15}".format(name, department))
# 2. Print the email addresses of all employees in alphabetical order by their last names.
print("-"*40)
sorted_employees = sorted(employees, key=lambda emp: emp[0].split()[-1].lower())  # sort by last name
print("Email Addresses (sorted by last names):")
for _, _, email in sorted_employees:  # Ignoring the other values
    print(email)
# 3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.
print("-"*40)
new_employee = ("David Wilson", "Sales", "david.wilson@example.com")
employees.append(new_employee)
for employee in employees:
    print(employee)
# 4. Find and print the department of "Jane Smith".
print("-"*40)
for employee in employees:
    if employee[0] == "Jane Smith":
        print(f"Name: {employee[0]}, Department: {employee[1]}, Email: {employee[2]}")
print("-"*80)

print("Exercise 4: Book Library System ")

library = {
 "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
 "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
 "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
 "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

# Printing details of all books
print("Library Books:")
print("-" * 30)  # Separator line
for isbn, details in library.items():
    title = details["title"]
    author = details["author"]
    year = details["year"]

    print(f"ISBN: {isbn}")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
    print("-" * 30)  # Separator line

# 2. Find and print the details of the book with the ISBN "978-0-14-028329-7".
isbn_to_find = "978-0-14-028329-7"
# Finding and printing the book details
if isbn_to_find in library:
    book_details = library[isbn_to_find]
    print(f"Details of the book with ISBN {isbn_to_find}:")
    print(f"Title: {book_details['title']}")
    print(f"Author: {book_details['author']}")
    print(f"Year: {book_details['year']}")
else:
    print(f"No book found with ISBN {isbn_to_find}.")

# 3. Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925.
# Adding a new book
new_isbn = "978-1-4028-9462-6"
new_book_details = { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}

# Adding the new book to the library
library[new_isbn] = new_book_details
# Printing the updated library
print("Updated Library:")
for isbn, details in library.items():
    print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Year: {details['year']}")

# 4. Update the year of "To Kill a Mockingbird" to 1961 and print the updated details.
# Title to search for
title_to_update = "To Kill a Mockingbird"

# Find the ISBN and update the year
isbn_to_update = None  # Variable to store the ISBN if found

for isbn, details in library.items():
    if details["title"] == title_to_update:
        isbn_to_update = isbn  # Store the ISBN if the title matches
        break  # Exit the loop since we found the book

# Update the year if the book was found
if isbn_to_update:
    library[isbn_to_update]["year"] = 1961

    # Printing the updated details
    updated_book = library[isbn_to_update]
    print(f"Updated details for '{title_to_update}':")
    print(f"Title: {updated_book['title']}")
    print(f"Author: {updated_book['author']}")
    print(f"Year: {updated_book['year']}")
else:
    print(f"'{title_to_update}' not found in the library.")

# 5. Remove the book with ISBN "978-0-452-28423-4" and print the updated library.
# Adding a new book
del_isbn = "978-1-4028-9462-6"
del library[del_isbn]
for isbn, details in library.items():
    print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Year: {details['year']}")
print("-"*80)

print("Exercise 5: City Population Data ")
cities = {
 "New York": 8419000,
 "Los Angeles": 3980000,
 "Chicago": 2716000,
 "Houston": 2328000,
 "Phoenix": 1690000
}

# 1. Print the population of each city in a user-friendly format.
print("{:<15} {:<15}".format("City", "Population",))
print("-" * 30) #print the under line

for p in cities:
    pop = cities[p] #
   # print(f"{p}: {pop}")
    print("{:<15} {:<15}".format(p, pop))
print("-" * 30) #print the under line

# 2. Find and print the city with the highest population.
# 3. Find and print the city with the lowest population.

highest = float('-inf')  # -inf means starts with the lowest numb
lowest = float('inf')     # starts with the highest
high_pop = ''
lowest_pop = ''

for c in cities:
    if cities[c] > highest:
        highest = cities[c]
        high_pop = c

    if cities[c] < lowest:
        lowest = cities[c]
        lowest_pop = c

print(f"Highest population {high_pop}: {highest}")
print(f"lowest population {lowest_pop}: {lowest}")

# 4. Update the population of "Phoenix" to 1700000 and print the updated data.
cities['Phoenix'] = (1700000)
print(cities)

# 5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
cities["San Francisco"] = (884000)
print(cities)
print("-"*80)

print("Exercise 6: Movie Database ")
movies = {
 "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci Fi"},
 "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
 "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
 "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
 "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}

# 1. Print the details of all movies in a user-friendly format.
print("Movies details:")
print("-" * 30)  # Separator line
for mov, details in movies.items():
    year = details["year"]
    rating = details["rating"]
    genre = details["genre"]
    print(f"{mov}: {year}")
    print(f"Genre: {genre}")
    print(f"Rating: {rating}")
    print("-" * 30)

# 2. Find and print the highest-rated movie.

highest = movies[max(movies, key=lambda v: movies[v]['rating'])]
Movie_name = (list(movies.keys())[list(movies.values()).index(highest)])
print(f"Movie with the highest rating is : {Movie_name}")


# 3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
new_mov = "The Matrix"
new_mov_details = {"year": 1999, "rating": 8.7, "genre": "Sci Fi"}

# Adding the new book to the library
movies[new_mov] = new_mov_details
# Printing the updated library
print("Updated Movies:")
for mov, details in movies.items():
    print(f"{mov}: {year}, Genre: {genre}, Rating: {rating}")

# 4. Update the rating of "Inception" to 9.0 and print the updated details.
movies["Inception"] = {"year": 2010, "rating": 9.0, "genre": "Sci Fi"}

# 5. Remove "Pulp Fiction" from the database and print the updated list.
del movies["Pulp Fiction"]

print("{:<20} {:<10} {:<10} {:<10}".format("Title", "Year", "Rating", "Genre"))
print("_" * 50)

for key, details in movies.items():
     print("{:<20} {:<10} {:<10} {:<10}".format(key, details["year"], details["rating"], details["genre"]))

print("-"*80)


print("Exercise 7: Country Capitals")

countries = {
 "USA": "Washington, D.C.",
 "Canada": "Ottawa",
 "France": "Paris",
 "Germany": "Berlin",
 "Japan": "Tokyo"
}

# 1. Print the names of all countries and their capitals.
for k,v in countries.items():
     print(k,"-", v)

# 2. Find and print the capital of Germany.
germany = countries["Germany"]

print(f"Capital of Germany: {germany}")

# 3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
countries["Australia"] = "Canberra"

# 4. Update the capital of "USA" to "New Washington" and print the updated dictionary.
countries["USA"] = "New Washington"

# 5. Remove "France" from the dictionary and print the updated dictionary.
del countries["France"]
print(countries)

print("-"*80)

print("Exercise 8: Shopping Cart")

cart = [
     {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
     {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
     {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
     {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

total_cart = 0
# 1. Print the details of all items in the cart.
for e in cart:
     print(e["item"], "u",e["quantity"], "$",e["price_per_unit"])

# 2. Calculate and print the total cost of the cart.
     value_each = e["quantity"] * e["price_per_unit"]
     total_cart += value_each
print(f"Total cost of the cart is: ${total_cart}")

# 3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

# 4. Update the quantity of "banana" to 10 and print the updated cart.
banana = cart[1]

for k,v in banana.items():
     banana["quantity"] = 10

print(cart)

# 5. Remove "pear" from the cart and print the updated cart.
cart.pop(3)
print(cart)

print("-"*80)

print("Exercise 9: Weather Data")
weather = {
     "Monday": {"temperature": 20, "humidity": 60},
     "Tuesday": {"temperature": 22, "humidity": 55},
     "Wednesday": {"temperature": 19, "humidity": 65},
     "Thursday": {"temperature": 23, "humidity": 50},
     "Friday": {"temperature": 21, "humidity": 70}
}

# 1. Print the weather details for each day.
for k,v in weather.items():
     print(k, "-", "temperature", v["temperature"], "humidity", v["humidity"])

# 2. Find and print the day with the highest temperature.

highest = weather[max(weather, key=lambda v: weather[v]['temperature'])]
highest_day = (list(weather.keys())[list(weather.values()).index(highest)])
print(f"The day with the highest temperature is : {highest_day}")

# 3. Find and print the day with the lowest humidity.
lowest = weather[min(weather, key=lambda v: weather[v]["humidity"])]
humidity_day = (list(weather.keys())[list(weather.values()).index(lowest)])
print(f"The day with the lowest humidity is : {humidity_day}")

# 4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
weather["Wednesday"] = {"temperature": 25, "humidity": 65}
print(weather)
# 5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data.
weather["Saturday"] = {"temperature": 24, "humidity": 60}
print(weather)
print("-"*80)

print("Exercise 10 Library Members ")
members = [
 {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
 {"name": "Bob", "age": 30, "books_borrowed": ["The Catche r in the Rye"]},
 {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
 {"name": "David", "age": 35, "books_borrowed": ["The Grea t Gatsby"]}
]

# 1. Print the names and ages of all members.
for a in members:
     print(a["name"], ":",a["age"])

# 2. Find and print the books borrowed by "Charlie".
for m in members:
     if "Charlie" in m["name"]:
          print("Charlie borrowed:", m["books_borrowed"])

# 3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})
print(members)

# 4. Update the age of "Bob" to 31 and print the updated list.
bob = members[1]
bob["age"] = 31
for m in members:
     print(m["name"], m["age"], "years old")

# 5. Remove "David" from the list and print the updated list.
members.pop(3)

for i in members:
     print(list(i.values()))
