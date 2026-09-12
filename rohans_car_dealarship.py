import random

print('Welcome to Rohan\'s Car Dealership.')
print('We have a huge inventory of cars.')
print('Please indicate your preference of specs.')
print()

def append_s(name):
    return name + 's'

# Define the car features
specs = ['Brand', 'Model', 'Engine', 'Fuel', 'Transmission', 'Drive', 'Color', 'Price']
specs_new = list(map(append_s, specs))
master_dict = dict.fromkeys(specs_new)

# Available options for each specification
master_dict['Brands'] = ['Toyota', 'Honda', 'Ford', 'BMW', 'Tesla']
master_dict['Models'] = ['Sedan', 'SUV', 'Truck', 'Coupe', 'Hatchback']
master_dict['Engines'] = ['2.0L 4-Cyl', '3.5L V6', 'Electric Motor', 'Twin-Turbo V8']
master_dict['Fuels'] = ['Gasoline', 'Diesel', 'Electric', 'Hybrid']
master_dict['Transmissions'] = ['Automatic', 'Manual', 'CVT']
master_dict['Drives'] = ['FWD', 'RWD', 'AWD', '4WD']
master_dict['Colors'] = ['Black', 'White', 'Silver', 'Red', 'Blue']
master_dict['Prices'] = ['USD 25000', 'USD 35000', 'USD 45000', 'USD 60000']

# Create a simulated inventory of 60 random cars
cars_list = []
for n_cars in range(60):
    new_car = dict.fromkeys(specs)
    for kk in new_car:
        new_car[kk] = random.choice(master_dict[kk+'s'])
    cars_list.append(new_car)

# Seek user preference and explicitly list options
user_choice = dict.fromkeys(specs)
for kk in specs:
    options_str = ", ".join(map(str, master_dict[kk+'s']))
    print(f"\nAvailable options for {kk}: [ {options_str} ]")
    user_choice[kk] = input(f'Enter preferred {kk} (or "none" for no preference):\n').strip()

# Create the evaluation query
query = ''
for kk in user_choice:
    if user_choice[kk].lower() == 'none' or user_choice[kk] == '':
        pass
    else:
        # Match case-insensitively or exact match
        query = query + 'car[' + '\'' + kk + '\'].lower() == ' + '\'' + user_choice[kk].lower() + '\' and '

if query != '':
    query = query[0:-5:1]  # Strip trailing ' and '
    selected = [car for car in cars_list if eval(query)]
else:
    selected = [car for car in cars_list]

# Display the final matching cars
print('\n' + '='*50)
print(f"{len(selected)} cars met your preference.")
print('='*50)

if len(selected) > 0:
    # Print header row using character length formatting
    for kk in specs:
        print(kk, end='')
        characters = len(kk)
        print((16 - characters) * ' ', end='')
    print()
    print('-' * 125)
    
    # Print car details matching character length structural guidelines
    for car in selected:
        for kk in specs:
            val_str = str(car[kk])
            print(val_str, end='')
            characters = len(val_str)
            print((16 - characters) * ' ', end='')
        print()
else:
    print("No cars found matching those exact options. Try running again with fewer restrictions!")

