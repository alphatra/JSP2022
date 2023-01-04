import math

# Function to calculate the area of a circle with a given radius and unit
def calculate_area(radius, unit):
  # Convert the radius to meters
  if unit == 'cm':
    radius = radius / 100
  elif unit == 'mm':
    radius = radius / 1000

  # Calculate the area of the circle and return the result in square meters
  return math.pi * radius ** 2

# Get the radius and unit from the user
radius = float(input('Enter the radius of the circle: '))
unit = input('Enter the unit of the radius (m, cm, mm): ')

# Calculate and print the area of the circle
area = calculate_area(radius, unit)
print(f'The area of the circle is {area:.3f} square meters.')
