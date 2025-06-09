import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

# Fonction pour charger un fichier avec gestion des erreurs
def load_file(filename, folder_path='.'):
    file_path = os.path.join(folder_path, filename)
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} n'a pas été trouvé dans {folder_path}")
        return None

# Vérifier si les fichiers existent dans le dossier courant
folder_path = '.'
prices = load_file('txt_prix.txt', folder_path)
sales = load_file('txt_ventes.txt', folder_path)
categories = load_file('txt_nom.txt', folder_path)

# Si un fichier est manquant, demander un nouveau chemin à l'utilisateur
if any(df is None for df in [prices, sales, categories]):
    folder_path = input("Veuillez entrer le chemin du dossier contenant les fichiers txt_prix.txt, txt_ventes.txt et txt_nom.txt : ")
    prices = load_file('txt_prix.txt', folder_path)
    sales = load_file('txt_ventes.txt', folder_path)
    categories = load_file('txt_nom.txt', folder_path)
    
    # Vérifier si tous les fichiers ont été chargés
    if any(df is None for df in [prices, sales, categories]):
        print("Erreur : Impossible de charger tous les fichiers. Vérifiez les noms et chemins des fichiers.")
        exit(1)

# Jointure des trois DataFrames sur le champ 'Produit'
merged_df = prices.merge(sales, on='Produit').merge(categories, on='Produit')

# Calcul du total des ventes par produit (Prix * Ventes)
merged_df['Total_Ventes'] = merged_df['Prix'] * merged_df['Ventes']

# Création du premier fichier XML pour les ventes par produit
root_products = ET.Element('Produits')
for _, row in merged_df.iterrows():
    product = ET.SubElement(root_products, 'Produit')
    ET.SubElement(product, 'Nom').text = row['Produit']
    ET.SubElement(product, 'Prix').text = str(row['Prix'])
    ET.SubElement(product, 'Ventes').text = str(row['Ventes'])
    ET.SubElement(product, 'Categorie').text = row['Categorie']
    ET.SubElement(product, 'TotalVentes').text = str(round(row['Total_Ventes'], 2))

# Conversion en chaîne XML formatée et enregistrement
xmlstr_products = minidom.parseString(ET.tostring(root_products)).toprettyxml(indent="  ")
output_products_path = os.path.abspath('ventes_par_produit.xml')
with open(output_products_path, 'w', encoding='utf-8') as f:
    f.write(xmlstr_products)
print(f"Fichier XML 'ventes_par_produit.xml' enregistré à : {output_products_path}")

# Regroupement par catégorie et calcul du total des ventes
category_sales = merged_df.groupby('Categorie')['Total_Ventes'].sum().reset_index()

# Création du second fichier XML pour les ventes par catégorie
root_categories = ET.Element('Categories')
for _, row in category_sales.iterrows():
    category = ET.SubElement(root_categories, 'Categorie')
    ET.SubElement(category, 'Nom').text = row['Categorie']
    ET.SubElement(category, 'TotalVentes').text = str(round(row['Total_Ventes'], 2))

# Conversion en chaîne XML formatée et enregistrement
xmlstr_categories = minidom.parseString(ET.tostring(root_categories)).toprettyxml(indent="  ")
output_categories_path = os.path.abspath('ventes_par_categorie.xml')
with open(output_categories_path, 'w', encoding='utf-8') as f:
    f.write(xmlstr_categories)
print(f"Fichier XML 'ventes_par_categorie.xml' enregistré à : {output_categories_path}")