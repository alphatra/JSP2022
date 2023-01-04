import random


def generate_pesel():

  pesel = [str(random.randint(0, 9)) for _ in range(9)]

  check_digit = (1 * int(pesel[0]) + 3 * int(pesel[1]) + 7 * int(pesel[2]) +
                 9 * int(pesel[3]) + 1 * int(pesel[4]) + 3 * int(pesel[5]) +
                 7 * int(pesel[6]) + 9 * int(pesel[7]) + 1 * int(pesel[8])) % 10


  return ''.join(pesel + [str(check_digit)])

with open('PESEL.txt', 'w') as f:
  for _ in range(10):
    f.write(generate_pesel() + '\n')

