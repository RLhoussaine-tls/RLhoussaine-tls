# Guide de démarrage rapide

## Installation initiale

1. **Installer les dépendances Python :**

```bash
pip install -r requirements.txt
```

2. **Vérifier que le thème Flex est accessible :**

Le thème doit être situé dans `../Flex-e63fdae267319fdfb5a0788fe2de9e75ce063569/Flex-e63fdae267319fdfb5a0788fe2de9e75ce063569`

Si le chemin est différent, modifiez la variable `THEME` dans `pelicanconf.py`.

## Génération du site

### Mode développement

```bash
# Générer le site une fois
make html

# Servir le site localement (http://localhost:8000)
make serve

# Ou régénérer automatiquement lors des modifications
make devserver
```

### Mode production

```bash
# Générer le site pour la production
make publish
```

## Déploiement sur GitHub Pages

### Méthode 1 : Via Makefile (nécessite ghp-import)

```bash
make github
```

### Méthode 2 : Via GitHub Actions (automatique)

Le workflow GitHub Actions est configuré dans `.github/workflows/pelican.yml`. Il se déclenche automatiquement lors d'un push sur `main` ou `master`.

Pour activer GitHub Pages :
1. Allez dans Settings > Pages de votre repository
2. Sélectionnez la branche `gh-pages` comme source
3. Le site sera disponible à `https://rlhoussaine-tls.github.io`

## Structure des fichiers

```
RLhoussaine-tls/
├── content/              # Contenu du site
│   ├── pages/           # Pages statiques
│   │   ├── about.md
│   │   ├── experiences.md
│   │   ├── formations.md
│   │   └── competences.md
│   └── index.md         # Page d'accueil
├── output/              # Site généré (ignoré par git)
├── pelicanconf.py       # Configuration de développement
├── publishconf.py       # Configuration de production
├── Makefile            # Commandes de build
└── requirements.txt    # Dépendances Python
```

## Personnalisation

### Modifier le contenu

Éditez les fichiers Markdown dans `content/pages/` pour modifier le contenu.

### Modifier la configuration

- `pelicanconf.py` : Configuration générale (titre, description, liens sociaux, etc.)
- `publishconf.py` : Configuration pour la production (URL du site, analytics, etc.)

### Modifier le thème

Le thème Flex peut être personnalisé en copiant les templates nécessaires dans un nouveau dossier et en modifiant `THEME` dans `pelicanconf.py`.

## Commandes utiles

```bash
# Nettoyer le dossier output
make clean

# Régénérer le site
make regenerate

# Aide
make help
```

