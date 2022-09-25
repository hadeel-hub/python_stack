

x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print(f"x was orginally [ [5,2,3], [10,8,9] ]  and is now {x}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(f"{students[0]}")


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(f"{sports_directory['soccer']}")

z = [{'x': 10, 'y': 20}] 
z[0]['y'] = 30
print(f"{z}") 

def  iterateDictionary(some_list):
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    for student in students(len(students)):
        print(f"{students["first_name"]["last_name"]}")


