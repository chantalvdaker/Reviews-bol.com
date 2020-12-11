""" De verdeling van keywords in de reviews van Bol.com weergegeven in een barchart voor zowel het jaar 2019 als het jaar 2020
"""

# Bar chart 2019 maken
labels_2019 = ['reviews met bezorg', 'reviews met product', 'reviews met service', 'reviews met levering']
aantallen_2019 = [143, 134, 352, 182]

# Importeren van libraries matplotlib and numpy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Opmaak barchart
y_pos = np.arange(len(labels_2019))
plt.bar(y_pos, aantallen_2019, align='center', alpha=0.5)

plt.xticks(y_pos, labels_2019, rotation=60)
plt.ylabel('Aantal Reviews')
plt.title('Onderwerpen reviews Bol.com 20')
plt.show()
plt.savefig('img2.jpg', dpi=500)

# Bar chart voor 2020 maken
labels_2020 = ['reviews met bezorg', 'reviews met product', 'reviews met service', 'reviews met levering']
aantallen_2020 = [111, 140, 340, 142]

# Importeren van libraries matplotlib and numpy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Opmaak barchart 
y_pos = np.arange(len(labels_2020))
plt.bar(y_pos, aantallen_2020, align='center', alpha=0.5)

plt.xticks(y_pos, labels_2020, rotation=60)
plt.ylabel('Aantal Reviews')
plt.title('Onderwerpen reviews Bol.com 2020')
plt.show()
plt.savefig('img2.jpg', dpi=500)

