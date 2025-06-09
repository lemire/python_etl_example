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

## Références

- Lemire et al., [La science des données: Théorie et applications avec R et Python](https://www.amazon.ca/science-données-Théorie-applications-Python/dp/B0D53QXGKM)
- Robert Godin et Daniel Lemire, [Programmation avec Python: des jeux au Web](https://www.amazon.ca/Programmation-avec-Python-jeux-Web/dp/B0CVX9296P)
