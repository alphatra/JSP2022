import numpy
import matplotlib.pyplot as plt

values = [16.26, 12.21, 16.36, 12.91, 5.73, 4.64, 2.87, 1.39, 1.04]
names = ('C', 'Java', 'Python', 'C++', 'C#', 'Visual Basic', 'JavaScript', 'PHP', 'R')
y_pos = numpy.arange(len(values))

plt.figure(figsize=(10, 5))

plt.bar(y_pos, values, color='#348989')

plt.xticks(y_pos, names)

plt.xlabel('Język pogramowania', fontsize=12, color='#323232')
plt.ylabel('Popularność [%]', fontsize=12, color='#323232')
plt.title('Popularność języków programowania w styczniu 2022', fontsize=13, color='#323232')

x = 0
for i in values:
    plt.text(x - 0.25, i + 0.1, str(i)+'%')
    x+=1

plt.show();