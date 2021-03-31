
users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

def find_person_by_name(list, person_name):
    for person in list:
        if person["first_name"] == person_name:
            return person
    
    return "Not found"

print(find_person_by_name(users, "Margaret"))
print(find_person_by_name(users, "Bill"))
print(find_person_by_name(users, "Kieran"))