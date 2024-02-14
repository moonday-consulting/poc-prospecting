
## README.md pour votre application Flask de visualisation de données CSV

### Introduction

Ce projet est une application web Flask qui permet de visualiser des données provenant de différents fichiers CSV. L'application lit les fichiers CSV, analyse les données et les affiche sur une page web. Elle est conçue pour filtrer et montrer des informations spécifiques, telles que le nombre de lignes totales, le nombre de lignes par pays (Suisse et France), ainsi que les lignes correspondant à certains critères (par exemple, des réponses GPT positives).

### Configuration et installation

Pour exécuter cette application, vous aurez besoin de Python et de Flask installés sur votre machine. Voici les étapes à suivre :

1. Installez Python sur votre machine si ce n'est pas déjà fait. Vous pouvez le télécharger à partir du [site officiel de Python](https://www.python.org/downloads/).

2. Installez Flask en utilisant pip, le gestionnaire de paquets pour Python. Ouvrez un terminal ou une invite de commande et exécutez la commande suivante :
   ```
   pip install Flask
   ```

3. Clonez ce dépôt ou téléchargez les fichiers de l'application sur votre machine.

4. Placez vos fichiers CSV dans le dossier `data` de votre application. Assurez-vous que les noms de fichiers correspondent à ceux attendus par l'application (`api_data_fusion_moonday.csv`, `api_data_fusion_enedis.csv`, etc.).

### Exécution de l'application

Pour lancer l'application, naviguez dans le répertoire contenant votre application Flask et exécutez le fichier Python principal. Utilisez la commande suivante dans votre terminal :

```
python app.py
```

Cela démarrera le serveur de développement Flask et rendra votre application accessible localement. Vous pouvez accéder à l'application en ouvrant votre navigateur et en naviguant vers `http://127.0.0.1:5000/`.

### Utilisation de l'application

Une fois l'application lancée et le navigateur ouvert à l'adresse indiquée, vous verrez une page affichant les données analysées à partir des fichiers CSV. L'interface web montre :

- Le nombre total de lignes lues dans les fichiers.
- Le nombre total de lignes correspondant aux pays "SUISSE" et "FRANCE".
- Une liste détaillée pour chaque fichier CSV, montrant les lignes qui répondent aux critères spécifiés (par exemple, `gpt_responses` égal à "true").

Chaque liste est accompagnée du nombre de lignes affichées et d'un tableau contenant les détails spécifiques à ces lignes, tels que l'ID, le pays, la description, et un lien vers un PDF complet si disponible.

### Personnalisation

Vous pouvez personnaliser l'application en modifiant le code source pour ajouter de nouveaux fichiers CSV, ajuster les critères de filtrage ou modifier le design de la page web. Assurez-vous de mettre à jour les dictionnaires `displayed_rows`, `data_by_file`, et `file_labels` en conséquence si vous ajoutez ou modifiez des fichiers CSV.

### Conclusion

Cette application Flask simple est un excellent point de départ pour explorer le traitement et la visualisation de données CSV avec Python. N'hésitez pas à l'adapter et à l'étendre en fonction de vos besoins spécifiques.

---

N'oubliez pas de vérifier les dépendances et de les maintenir à jour pour assurer la sécurité et la performance de votre application.
