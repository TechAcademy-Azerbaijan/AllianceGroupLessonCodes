import csv

with open('names.csv', 'r') as f:
    lines = csv.DictReader(f, ['first_name', 'last_name'])
    
    with open('new_names.csv', 'w',) as g:
        fieldnames = ['first_name', 'last_name',]
        writer = csv.DictWriter(g, fieldnames=fieldnames)

        for line in lines:
            # print(line)
            writer.writerow({
                    'first_name': line['first_name'],
                    'last_name': line['last_name']
                }
            )
