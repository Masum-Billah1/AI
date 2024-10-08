import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# Data for accuracies
data = {
    'Original Data': [
        f'{NMNT_accuracy*100: .2f}%',
        f'{NMAT_accuracy*100: .2f}%'
    ],
    'Augmented Data': [
        f'{AMNT_accuracy*100: .2f}%',
        f'{AMAT_accuracy*100: .2f}%'
    ]
}

# Create DataFrame for the table
df = pd.DataFrame(data, index=['Model', 'Augmented Model'])
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# Convert accuracies into float for plotting
original_accuracies = [NMNT_accuracy, NMAT_accuracy]
augmented_accuracies = [AMNT_accuracy, AMAT_accuracy]

# Plotting the accuracies
labels = ['NMNT Model', 'NMAT Model']
x = range(len(labels))

plt.figure(figsize=(8,6))
plt.bar(x, original_accuracies, width=0.4, label='Original Data', align='center')
plt.bar([i + 0.4 for i in x], augmented_accuracies, width=0.4, label='Augmented Data', align='center')

plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Comparison of Model Accuracies')
plt.xticks([i + 0.2 for i in x], labels)
plt.legend()

# Show the plot
plt.show()
