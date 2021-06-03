import numpy as np
import matplotlib.pyplot as plt
import csv

x = [i for i in range(775)]
D_A = []
G_A = []
cycle_A = []
idt_A = []
D_B = []
G_B = []
cycle_B = []
idt_B = []

with open('loss_log.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')

    for row in plots:
        D_A.append(float(row[0]))
        G_A.append(float(row[1]))
        cycle_A.append(float(row[2]))
        idt_A.append(float(row[3]))
        D_B.append(float(row[4]))
        G_B.append(float(row[5]))
        cycle_B.append(float(row[6]))
        idt_B.append(float(row[7]))

#plots are too crowded together, uncomment your desired line then plot

# plt.plot(x, D_A, label = 'D_A')
# plt.plot(x, G_A, label = 'G_A')
# plt.plot(x, cycle_A, label = 'cycle_A')
# plt.plot(x, idt_A, label = 'idt_A')
# plt.plot(x, D_B, label = 'D_B')
# plt.plot(x, G_B, label = 'G_B')
# plt.plot(x, cycle_B, label = 'cycle_B')
plt.plot(x, idt_B, label = 'idt_B')

#change this line to get proper ranges based on what you're graphing
plt.yticks(np.arange(min(idt_B), max(idt_B), .05))
plt.xlabel('Iterations/Epochs')
plt.legend()
plt.show()
