import csv

with open('names.csv', 'r') as f:
    lines = csv.reader(f)
    with open('new_names.csv', 'w') as g:
        writer = csv.writer(g, delimiter='\t')

        # for line in lines:
        writer.writerows([['Idris','Murad'], ['Kamal', 'Sebuhi']])

