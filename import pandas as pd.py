import pandas as pd 
import matplotlib.pyplot as plt 

plt.style.use('bmh')
fd = pd.read_csv("C:/Users/keert/Downloads/onlinefoods.csv")

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(fd['Educational Qualifications'], fd['Age'])
plt.xlabel('Educational Qualifications', fontsize=18)
plt.ylabel('Age', fontsize=15)
plt.title('Age Distribution by Educational Qualifications')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 8))
plt.pie(fd['Age'], labels=fd['Educational Qualifications'], autopct='%0.1f%%', shadow=True, explode=[0.05] * len(fd))
plt.title('Age Distribution by Educational Qualifications')
plt.axis('equal')  
plt.tight_layout()
plt.show()
