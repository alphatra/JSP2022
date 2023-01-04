import math

def licz_pole(radius, unit):
  if unit == 'cm':
    radius = radius / 100
  elif unit == 'mm':
    radius = radius / 1000

  return math.pi * radius ** 2

radius = float(input('Podaj promień koła: '))
unit = input('podaj jednostkę promienia koła (m, cm, mm): ')

area = licz_pole(radius, unit)
print(f'Pole koła wynosi {area:.3f} square meters.')
