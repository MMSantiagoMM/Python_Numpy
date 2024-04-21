import numpy as np;


l1 = np.arange(20,71)
print(l1[l1%2!=0])

l2 = np.random.uniform(low=20,high=50, size=20)
print(l2)

l3 = np.array(l2[l2 > 35])
print(l3)

animals = ["perro","gato","leon","tigre","ave","zancudo","oso","jirafa","elefante"]

l4 = np.array([animal for animal in animals if len(animal) < 4])
print(l4)


l5 = np.random.randint(1,9, size=(4,4))
print(l5);
print(l5.sum(axis=0))



indexes = [2,4,6,9,11]

specific_elements = l2[indexes]

print(specific_elements)

people = np.array([
        ['Roberto','casado','masculino'],
        ['Sheila','soltero','femenino'],
        ['Bruno','soltero','masculino'],
        ['Rita','casado','femenino'],
        ['Carlos','casado','masculino'],
        ['Mariana','soltero','femenino'],
        ['Eugenia','casado','femenino'],
        ['Gladis','soltero','femenino'],
        ['Daniel','soltero','masculino'],
        ['Gregorio','casado','masculino']
        ])

gender_column = people[:,2]

print(people[people[:,2]=='femenino'])



