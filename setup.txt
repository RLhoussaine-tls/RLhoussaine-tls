# Site web personnel - Romain Lhoussaine

Site web personnel généré avec [Pelican](https://getpelican.com/) et le thème [Flex](https://github.com/alexandrevicenzi/Flex).

## Installation

1. Créer et activer l'environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

**Note:** Vous devez activer l'environnement virtuel avant d'utiliser `make` :

```bash
source .venv/bin/activate
```

3. Générer le site :

```bash
make html
```

4. Servir le site localement :

```bash
make serve
```

Le site sera accessible sur http://localhost:8000

**Note:** Si le port 8000 est déjà utilisé, vous pouvez :
- Arrêter le serveur précédent : `./stop-server.sh` ou `pkill -f "pelican.*RLhoussaine-tls"`
- Utiliser un autre port : `make serve PORT=8001`

## Développement

Pour régénérer automatiquement le site lors des modifications :

```bash
make devserver
```

## Publication

Pour générer le site en mode production :

```bash
make publish
```

Pour publier sur GitHub Pages :

```bash
make github
```

## Structure

- `content/` - Contenu du site (pages, articles)
- `output/` - Site généré (ignoré par git)
- `pelicanconf.py` - Configuration de développement
- `publishconf.py` - Configuration de production

## Thème

Le thème Flex est utilisé depuis le repository [pelican-themes](https://github.com/getpelican/pelican-themes) :
- Le thème est situé dans `../pelican-themes/Flex`
- Pour mettre à jour le thème : `cd ../pelican-themes && git submodule update --remote Flex`

