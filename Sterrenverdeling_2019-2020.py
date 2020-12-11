"""
Dit is een analyse die de verdeling van het aantal sterratings voor de maanden mei tot en met november 2019 en 2020 telt 
"""
df_2019.describe()
df_2020.describe()

# Verdeling bekijken voor het jaar 2019
df_2019['sterren'].value_counts()

# Een list maken van de verdeling hierboven, de labels en waarden voor 2019 worden weergegeven in een piechart
import numpy as np
import matplotlib.pyplot as plt

sterrendata_2019 = [401,66,33,125,484]
sterrenlabels = [1,2,3,4,5]
plt.pie(sterrendata_2019,labels=sterrenlabels,autopct='%1.1f%%')
plt.title('Aantal sterren 2019')
plt.show()
plt.savefig('Aantal sterren 2019')

# Verdeling bekijken voor het jaar 2020  
df_2020['sterren'].value_counts()


# Een list maken van de verdeling hierboven, de labels en waarden voor 2020 worden weergegeven in een piechart
import numpy as np
import matplotlib.pyplot as plt

sterrendata_2020 = [447,74,29,68,384]
plt.pie(sterrendata_2020,labels=sterrenlabels,autopct='%1.1f%%')
plt.title('Aantal sterren 2020')
plt.show()
plt.close()
plt.savefig('Aantal sterren 2020')
import numpy as np
import matplotlib.pyplot as plt

# Het maken van een barchart van bovenstaande lists voor 2019 en 2020

gemiddelde_sterren_2019 = df_2019['sterren'].mean()
gemiddelde_sterren_2020 = df_2020['sterren'].mean()

bars = ['Gemiddelde sterren 2019', 'Gemiddelde sterren  2020']
plt.bar(bars, [gemiddelde_sterren_2019, gemiddelde_sterren_2020])
plt.xticks()
plt.show()
plt.savefig('barchartsgemiddelden')

