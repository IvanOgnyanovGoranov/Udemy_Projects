import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Create dataframe
color_counts = data['Primary Fur Color'].value_counts().to_dict()

new_dict = {'Fur color': [], 'Count': []}

for key, value in color_counts.items():
    if key == 'Cinnamon':
        new_dict['Fur color'] += ['Red']
    else:
        new_dict['Fur color'] += [key]
    new_dict['Count'] += [value]

squirrel_count = pandas.DataFrame(new_dict)

squirrel_count.to_csv("squirrel_count.csv")