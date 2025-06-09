# Exemple de projet ETL en Python

Ce projet illustre un pipeline ETL (Extraction, Transformation, Chargement) simple en Python. Il lit des fichiers texte contenant des informations sur des produits, leurs prix et leurs ventes, puis génère des rapports au format XML.

## Prérequis

Avant de procéder, assurez-vous d'installer Python 3.7 ou une version ultérieure sur votre machine.

- **Pour Windows** :
  1. Téléchargez l'installateur depuis https://www.python.org/downloads/windows/
  2. Lancez l'installateur et cochez l'option "Add Python to PATH" avant de cliquer sur "Install Now".
  3. Ouvrez l'invite de commandes :
     - Cliquez sur le menu Démarrer (icône Windows en bas à gauche), tapez "Invite de commandes" ou "cmd", puis cliquez sur l'application correspondante.
  4. Vérifiez l'installation en tapant :
     ```
     python --version
     ```
     ou
     ```
     python3 --version
     ```

- **Pour macOS** :
  1. Ouvrez le Terminal.
  2. Installez Homebrew si ce n'est pas déjà fait :
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
  3. Installez Python 3 avec Homebrew :
     ```
     brew install python
     ```
  4. Vérifiez l'installation :
     ```
     python3 --version
     ```

Le nom de l'interpréteur Python sur votre système peut être `python` ou `python3` selon votre système. Nous allons supposer qu'il s'agit de `python3`.

Pour installer les librairies nécessaires dans un environnement virtuel (recommandé) :

1. Créez un environnement virtuel dans le dossier du projet :
   ```
   python3 -m venv venv
   ```
2. Activez l'environnement virtuel :
   - **Sur macOS et Linux** :
     ```
     source venv/bin/activate
     ```
   - **Sur Windows** :
     ```
     venv\Scripts\activate
     ```
3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

Lorsque vous avez terminé, vous pouvez désactiver l'environnement virtuel avec :
```
deactivate
```

## Obtention des fichiers du projet

Pour obtenir les fichiers du projet, vous pouvez télécharger une archive ZIP depuis GitHub :

1. Rendez-vous sur la page du projet : https://github.com/lemire/python_etl_example
2. Cliquez sur le bouton vert « Code » puis sur « Download ZIP ».
3. Décompressez l’archive téléchargée sur votre ordinateur.
4. Ouvrez le dossier extrait dans votre terminal ou explorateur de fichiers pour suivre les instructions d’installation ci-dessus.

## Utilisation

Placez-vous dans le dossier où se trouvent les fichiers `txt_nom.txt`, `txt_prix.txt`, `txt_ventes.txt` puis tapez :

```
python3 solution.py
```

Et voilà!

## Fichiers d'entrée
- `txt_nom.txt` : noms des produits (un par ligne)
- `txt_prix.txt` : prix des produits (un par ligne, même ordre)
- `txt_ventes.txt` : ventes par produit (un par ligne, même ordre)

## Fichiers de sortie
- `ventes_par_produit.xml` : rapport des ventes par produit
- `ventes_par_categorie.xml` : rapport des ventes par catégorie (si applicable)

## Exemple de résultat
Après exécution, vous obtiendrez des fichiers XML contenant les rapports structurés. Vous pouvez les ouvrir avec un éditeur de texte ou un navigateur pour visualiser les résultats.

## Structure du code
- `solution.py` : script principal qui orchestre l'ETL
- `requirements.txt` : dépendances Python nécessaires

## Auteur
Projet exemple par [Votre Nom].

Avant de procéder, assurez-vous d'installer Python 3.7 ou une version ultérieure sur votre machine.

- **Pour Windows** :
  1. Téléchargez l'installateur depuis https://www.python.org/downloads/windows/
  2. Lancez l'installateur et cochez l'option "Add Python to PATH" avant de cliquer sur "Install Now".
  3. Ouvrez l'invite de commandes :
     - Cliquez sur le menu Démarrer (icône Windows en bas à gauche), tapez "Invite de commandes" ou "cmd", puis cliquez sur l'application correspondante.
  4. Vérifiez l'installation en tapant :
     ```
     python --version
     ```
     ou
     ```
     python3 --version
     ```

- **Pour macOS** :
  1. Ouvrez le Terminal.
  2. Installez Homebrew si ce n'est pas déjà fait :
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
  3. Installez Python 3 avec Homebrew :
     ```
     brew install python
     ```
  4. Vérifiez l'installation :
     ```
     python3 --version
     ```

Le nom de l'interpréteur Python sur votre système peut être `python` ou `python3` selon votre système. Nous allons supposer qu'il s'agit de `python3`.

Pour installer les librairies nécessaires dans un environnement virtuel (recommandé) :

1. Créez un environnement virtuel dans le dossier du projet :
   ```
   python3 -m venv venv
   ```
2. Activez l'environnement virtuel :
   - **Sur macOS et Linux** :
     ```
     source venv/bin/activate
     ```
   - **Sur Windows** :
     ```
     venv\Scripts\activate
     ```
3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

Lorsque vous avez terminé, vous pouvez désactiver l'environnement virtuel avec :
```
deactivate
```

## Obtention des fichiers du projet

Pour obtenir les fichiers du projet, vous pouvez télécharger une archive ZIP depuis GitHub :

1. Rendez-vous sur la page du projet : https://github.com/lemire/python_etl_example
2. Cliquez sur le bouton vert « Code » puis sur « Download ZIP ».
3. Décompressez l’archive téléchargée sur votre ordinateur.
4. Ouvrez le dossier extrait dans votre terminal ou explorateur de fichiers pour suivre les instructions d’installation ci-dessus.

## Utilisation

Placez-vous dans le dossier où se trouvent les fichiers `txt_nom.txt`, `txt_prix.txt`, `txt_ventes.txt` puis tapez :

```
python3 solution.py
```

Et voilà!

## Fichiers d'entrée
- `txt_nom.txt` : noms des produits (un par ligne)
- `txt_prix.txt` : prix des produits (un par ligne, même ordre)
- `txt_ventes.txt` : ventes par produit (un par ligne, même ordre)

## Fichiers de sortie
- `ventes_par_produit.xml` : rapport des ventes par produit
- `ventes_par_categorie.xml` : rapport des ventes par catégorie (si applicable)

## Exemple de résultat
Après exécution, vous obtiendrez des fichiers XML contenant les rapports structurés. Vous pouvez les ouvrir avec un éditeur de texte ou un navigateur pour visualiser les résultats.

## Structure du code
- `solution.py` : script principal qui orchestre l'ETL
- `requirements.txt` : dépendances Python nécessaires


## Explication du code

Ce code Python charge des données à partir de fichiers CSV, les fusionne, effectue des calculs et génère deux fichiers XML pour représenter les ventes par produit et par catégorie. Voici une explication détaillée.

### 1. Importation des bibliothèques
```python
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
```
- `pandas` : pour manipuler les données sous forme de DataFrame.
- `xml.etree.ElementTree` : pour créer et manipuler des structures XML.
- `minidom` : pour formater le XML de manière lisible.
- `os` : pour gérer les chemins de fichiers et les opérations sur le système de fichiers.

### 2. Définition de la fonction `load_file`
```python
def load_file(filename, folder_path='.'):
    file_path = os.path.join(folder_path, filename)
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} n'a pas été trouvé dans {folder_path}")
        return None
```
- Cette fonction charge un fichier CSV à partir d’un chemin spécifié.
- `os.path.join` construit le chemin complet du fichier.
- Si le fichier n’est pas trouvé, elle affiche un message d’erreur et retourne `None`.

### 3. Chargement des fichiers
```python
folder_path = '.'
prices = load_file('txt_prix.txt', folder_path)
sales = load_file('txt_ventes.txt', folder_path)
categories = load_file('txt_nom.txt', folder_path)
```
- Trois fichiers CSV (`txt_prix.txt`, `txt_ventes.txt`, `txt_nom.txt`) sont chargés depuis le dossier courant (`.`).
- Chaque fichier est supposé contenir deux colonnes (ex. : produit et prix pour `txt_prix.txt`).

### 4. Renommage des colonnes
```python
if prices is not None and prices.shape[1] == 2:
    prices.columns = ['Produit', 'Prix']
if sales is not None and sales.shape[1] == 2:
    sales.columns = ['Produit', 'Ventes']
if categories is not None and categories.shape[1] == 2:
    categories.columns = ['Produit', 'Categorie']
```
- Si un fichier est chargé correctement et contient deux colonnes, celles-ci sont renommées pour plus de clarté : `Produit` et `Prix`, `Ventes` ou `Categorie`.

### 5. Gestion des fichiers manquants
```python
if any(df is None for df in [prices, sales, categories]):
    folder_path = input("Veuillez entrer le chemin du dossier contenant les fichiers txt_prix.txt, txt_ventes.txt et txt_nom.txt : ")
    prices = load_file('txt_prix.txt', folder_path)
    sales = load_file('txt_ventes.txt', folder_path)
    categories = load_file('txt_nom.txt', folder_path)
    
    if any(df is None for df in [prices, sales, categories]):
        print("Erreur : Impossible de charger tous les fichiers. Vérifiez les noms et chemins des fichiers.")
        exit(1)
```
- Si un fichier est manquant (`None`), l’utilisateur est invité à entrer un nouveau chemin de dossier.
- Les fichiers sont rechargés avec ce nouveau chemin.
- Si un fichier reste introuvable, le programme affiche une erreur et s’arrête.

### 6. Fusion des DataFrames
```python
merged_df = prices.merge(sales, on='Produit').merge(categories, on='Produit')
```
- Les trois DataFrames (`prices`, `sales`, `categories`) sont fusionnés sur la colonne `Produit` à l’aide de `merge`.
- Le DataFrame résultant (`merged_df`) contient les colonnes : `Produit`, `Prix`, `Ventes`, `Categorie`.

### 7. Calcul du total des ventes
```python
merged_df['Total_Ventes'] = merged_df['Prix'] * merged_df['Ventes']
```
- Une nouvelle colonne `Total_Ventes` est ajoutée, calculée comme le produit de `Prix` et `Ventes` pour chaque produit.

### 8. Création du premier fichier XML (ventes par produit)
```python
root_products = ET.Element('Produits')
for _, row in merged_df.iterrows():
    product = ET.SubElement(root_products, 'Produit')
    ET.SubElement(product, 'Nom').text = row['Produit']
    ET.SubElement(product, 'Prix').text = str(row['Prix'])
    ET.SubElement(product, 'Ventes').text = str(row['Ventes'])
    ET.SubElement(product, 'Categorie').text = row['Categorie']
    ET.SubElement(product, 'TotalVentes').text = str(round(row['Total_Ventes'], 2))
```
- Une structure XML est créée avec un élément racine `<Produits>`.
- Pour chaque ligne du DataFrame, un élément `<Produit>` est ajouté avec des sous-éléments : `Nom`, `Prix`, `Ventes`, `Categorie`, `TotalVentes`.
- Les valeurs numériques sont converties en chaînes et `TotalVentes` est arrondi à deux décimales.

### 9. Enregistrement du premier fichier XML
```python
xmlstr_products = minidom.parseString(ET.tostring(root_products)).toprettyxml(indent="  ")
output_products_path = os.path.abspath('ventes_par_produit.xml')
with open(output_products_path, 'w', encoding='utf-8') as f:
    f.write(xmlstr_products)
print(f"Fichier XML 'ventes_par_produit.xml' enregistré à : {output_products_path}")
```
- La structure XML est formatée avec `minidom` pour être lisible (indentation).
- Le fichier est enregistré sous `ventes_par_produit.xml` dans le dossier courant.
- Le chemin absolu du fichier est affiché.

### 10. Regroupement par catégorie
```python
category_sales = merged_df.groupby('Categorie')['Total_Ventes'].sum().reset_index()
```
- Les ventes totales sont agrégées par catégorie à l’aide de `groupby`.
- La somme de `Total_Ventes` est calculée pour chaque catégorie, et le résultat est converti en DataFrame avec `reset_index`.

### 11. Création du second fichier XML (ventes par catégorie)
```python
root_categories = ET.Element('Categories')
for _, row in category_sales.iterrows():
    category = ET.SubElement(root_categories, 'Categorie')
    ET.SubElement(category, 'Nom').text = row['Categorie']
    ET.SubElement(category, 'TotalVentes').text = str(round(row['Total_Ventes'], 2))
```
- Une structure XML est créée avec un élément racine `<Categories>`.
- Pour chaque catégorie, un élément `<Categorie>` est ajouté avec les sous-éléments `Nom` et `TotalVentes`.

### 12. Enregistrement du second fichier XML
```python
xmlstr_categories = minidom.parseString(ET.tostring(root_categories)).toprettyxml(indent="  ")
output_categories_path = os.path.abspath('ventes_par_categorie.xml')
with open(output_categories_path, 'w', encoding='utf-8') as f:
    f.write(xmlstr_categories)
print(f"Fichier XML 'ventes_par_categorie.xml' enregistré à : {output_categories_path}")
```
- La structure XML est formatée et enregistrée sous `ventes_par_categorie.xml`.
- Le chemin absolu du fichier est affiché.

### Résumé
Ce code charge trois fichiers CSV contenant des informations sur les prix, les ventes et les catégories des produits. Il fusionne ces données, calcule le total des ventes par produit, et génère deux fichiers XML : un pour les détails par produit et un pour les ventes agrégées par catégorie. Il inclut une gestion des erreurs pour les fichiers manquants et produit des fichiers XML bien formatés avec des valeurs arrondies.

## Références

- Lemire et al., [La science des données: Théorie et applications avec R et Python](https://www.amazon.ca/science-données-Théorie-applications-Python/dp/B0D53QXGKM)
- Robert Godin et Daniel Lemire, [Programmation avec Python: des jeux au Web](https://www.amazon.ca/Programmation-avec-Python-jeux-Web/dp/B0CVX9296P)
