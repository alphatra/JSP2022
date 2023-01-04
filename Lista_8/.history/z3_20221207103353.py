import random

# Function to generate a random PESEL number
def generate_pesel():
  # Randomly generate the first 9 digits of the PESEL number
  pesel = [str(random.randint(0, 9)) for _ in range(9)]

  # Calculate the check digit using the algorithm specified in the PESEL
  # standard (https://en.wikipedia.org/wiki/PESEL#Structure)
  check_digit = (1 * int(pesel[0]) + 3 * int(pesel[1]) + 7 * int(pesel[2]) +
                 9 * int(pesel[3]) + 1 * int(pesel[4]) + 3 * int(pesel[5]) +
                 7 * int(pesel[6]) + 9 * int(pesel[7]) + 1 * int(pesel[8])) % 10

  # Append the check digit to the PESEL number and return the full string
  return ''.join(pesel + [str(check_digit)])

# Generate 10 random PESEL numbers and write them to the PESEL.txt file
with open('PESEL.txt', 'w') as f:
  for _ in range(10):
    f.write(generate_pesel() + '\n')
