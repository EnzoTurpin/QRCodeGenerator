# Générateur de QR Code

Ce script Python permet de créer un fichier image contenant un QR Code généré à partir d'une URL spécifiée par l'utilisateur.

## Dépendances

Ce script nécessite la bibliothèque `qrcode`. Vous pouvez installer cette dépendance en utilisant pip :

```bash
pip install qrcode[pil]
```

## Utilisation

1. Modifiez la variable `data` dans le script pour inclure l'URL ou les données que vous souhaitez encoder dans le QR Code.
2. Exécutez le script avec Python pour générer l'image du QR Code :

```bash
python generate_qr.py
```

Le fichier image `MyQrCode.png` sera créé dans le répertoire courant.

## Configuration

Le script est configuré avec les paramètres suivants :
- `version=1` : Cela définit la version du QR Code, avec des valeurs possibles de 1 à 40. La version 1 est la plus petite taille.
- `error_correction=qrcode.constants.ERROR_CORRECT_L` : Niveau de correction d'erreur bas, permet une correction d'environ 7% des erreurs.
- `box_size=10` : Définit la taille de chaque boîte dans le QR Code.
- `border=4` : Définit la largeur de la bordure autour du QR Code.

## Sortie

Le script sauvegardera le QR Code généré en tant que fichier `myqr.png` dans le répertoire où le script est exécuté. Un message sera également affiché dans la console pour indiquer que le QR Code a été généré avec succès.

## Licence

Ce projet est sous licence libre. Vous pouvez le redistribuer et/ou le modifier selon les termes de votre choix.
