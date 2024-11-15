import pandas as pd
import matplotlib.pyplot as plt

#Find the frequency and their percentage of entity names and saves them as png file

df = pd.read_csv('./student_resource 3/dataset/train.csv') #Change the file path

entity_counts = df['entity_name'].value_counts()

print(entity_counts)
plt.figure(figsize=(10, 6))
entity_counts.plot(kind='bar', color='skyblue')


plt.title('Frequency of Unique Entity Names')
plt.xlabel('Entity Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.savefig('entity_name_frequency.png')


entity_percentages = df['entity_name'].value_counts(normalize=True) * 100

print(entity_percentages)


plt.figure(figsize=(10, 6))
entity_percentages.plot(kind='bar', color='skyblue')


plt.title('Percentage of Unique Entity Names')
plt.xlabel('Entity Name')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.savefig('entity_name_percentage.png')
