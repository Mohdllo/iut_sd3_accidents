import pandas as pd
import os

carac  = pd.read_csv('data/carac.csv', sep=';')
lieux  = pd.read_csv('data/lieux.csv', sep=';', low_memory=False)
veh = pd.read_csv('data/veh.csv', sep=';')
vict = pd.read_csv('data/vict.csv', sep=';')

victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
victime = victime.merge(accident,on='Num_Acc')

merged_data = victime

output_dir = 'step1'
os.makedirs(output_dir, exist_ok=True)

# Exporter le DataFrame résultant vers un fichier CSV
output_path = os.path.join(output_dir, 'merged_data.csv')
merged_data.to_csv(output_path, index=False)

# Ajouter et valider les modifications dans Git
os.system(f'git add {output_path}')
os.system('git commit -m "Ajouter merged_data.csv"')

# Pousser les modifications vers le référentiel distant
os.system('git push origin DEV')
…
