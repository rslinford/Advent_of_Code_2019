
filename = 'Day_01_data.txt'


def calculate_fuel_for_fuel(fuel):
    fuel_for_fuel = fuel // 3 - 2
    if fuel_for_fuel <= 0:
        return fuel
    return calculate_fuel_for_fuel(fuel )


with open(filename, 'r') as f:
    fuel_required_total = 0
    for line in f:
        mass = int(line.strip())
        fuel_required = mass // 3 - 2
        fuel_for_fuel = fuel_required // 3 - 2
        while fuel_for_fuel > 0:
            fuel_required += fuel_for_fuel
            fuel_for_fuel = fuel_for_fuel // 3 -2
        fuel_required_total += fuel_required
    print(f'Total fuel required: {fuel_required_total}')