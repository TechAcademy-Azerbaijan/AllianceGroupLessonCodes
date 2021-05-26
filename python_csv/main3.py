import csv


with open('students.csv', 'w') as g:
    headers = ['name', 'surname']
    writer = csv.DictWriter(g, headers, delimiter=';')
    writer.writeheader()
    writer.writerow({
        'name': 'Kamal',
        'surname': 'Abdullayev'
    })
    writer.writerow({
        'name': 'Nermin',
        'surname': 'Shivexanova'
    })
    writer.writerow({
        'name': 'Subhan',
        'surname': 'Rzayev'
    })
