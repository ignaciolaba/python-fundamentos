#1

#1.1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
#1.2

estudiantes[1]['last_name'] = 'Bryant'
print(estudiantes)

#1.3

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

#1.4

z[0]['y'] = 30
print(z)

#2

from tkinter import N


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for i in range(0, len(some_list), 1):
        print('first_name' + ' - ' +some_list[i]['first_name'])
        print('last_name' + ' - ' +some_list[i]['last_name'])






iterateDictionary(estudiantes) 



#3

def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list), 1):
        print(some_list[i][key_name])


iterateDictionary2('last_name', estudiantes)
iterateDictionary2('first_name', estudiantes)

#4

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict.keys():
        print(len(some_dict[i]), end = ' ')
        print(i)
        for h in range(0, len(some_dict[i]), 1):
            print(some_dict[i][h])

            


printInfo(dojo)

