# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
data=pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
alignment=data['Alignment'].value_counts()
plt.pie(alignment,autopct='%.2f')


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]

sc_covariance=sc_df.cov().iloc[0,1]

sc_strength=data['Strength'].std()
print(sc_strength)
sc_combat=data['Combat'].std()
print(sc_combat)
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

#######################################################
ic_df=data[['Intelligence','Combat']]
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=data['Intelligence'].std()
print(ic_intelligence)
ic_combat=data['Combat'].std()
print(ic_combat)
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
total_high=data['Total'].quantile(0.99)
super_best=data.loc[data['Total']>total_high]
super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ax_1=data.boxplot(column='Intelligence',by='Intelligence')
ax_2=data.boxplot(column='Speed',by='Speed')
ax_3=data.boxplot(column='Power',by='Power')


