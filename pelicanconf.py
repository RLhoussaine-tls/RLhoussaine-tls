from datetime import datetime

AUTHOR = "Romain Lhoussaine"
SITEURL = "http://localhost:8000"
SITENAME = "Romain Lhoussaine"
SITETITLE = "Romain Lhoussaine"
SITESUBTITLE = "Ingénieur en programmation scientifique et instrumentation spatiale"
SITEDESCRIPTION = "Ingénieur en programmation scientifique et instrumentation spatiale - Développement d'algorithmes de traitement d'image, pipelines scientifiques et simulateurs pour l'observation de la Terre et l'astrophysique."
SITELOGO = '/images/IDgh.jpg'
# Favicon - utiliser l'icône du site comme favicon
FAVICON = '/images/icon_website.png'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

# Utilisation du thème Flex depuis le répertoire themes local
THEME = "themes/Flex"
PATH = "content"
OUTPUT_PATH = "output"
TIMEZONE = "Europe/Paris"

DISABLE_URL_HASH = True

I18N_TEMPLATES_LANG = "fr"
DEFAULT_LANG = "fr"
OG_LOCALE = "fr_FR"
# Utiliser une locale disponible sur le système (C.utf8 est compatible UTF-8)
LOCALE = "C.utf8"

DATE_FORMATS = {
    "fr": "%d %B %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False  # Désactiver le menu principal (Home, etc.)
DISPLAY_PAGES_ON_MENU = False  # Ne pas afficher les pages dans la sidebar
HOME_HIDE_TAGS = True

# Bandeau GitHub désactivé (déjà dans les contacts)
# GITHUB_CORNER_URL = "https://github.com/RLhoussaine-tls"

SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/lhoussaineromain"),
    ("github", "https://github.com/RLhoussaine-tls"),
    ("envelope", "mailto:romain.lhoussaine@gmail.com"),
)

# Informations de contact pour la sidebar
CONTACT_EMAIL = "romain.lhoussaine@gmail.com"
CONTACT_PHONE = "0661783051"
CONTACT_LOCATION = "Toulouse, 31000"

MENUITEMS = (
    ("Expériences", "/pages/experiences.html"),
    ("Formations", "/pages/formations.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "fr_FR",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = False  # Afficher toutes les expériences sans pagination

STATIC_PATHS = ["images", "static"]

EXTRA_PATH_METADATA = {
    "static/css/custom.css": {"path": "theme/css/custom.css"},
}

# Exclure le dossier templates du scan de contenu
ARTICLE_EXCLUDES = ['templates']
PAGE_EXCLUDES = ['templates']

# Chemin vers les templates personnalisés
THEME_TEMPLATES_OVERRIDES = ['content/templates']

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Désactiver LESS pour utiliser les CSS compilés (plus stable)
USE_LESS = False

# CSS personnalisé pour changer orange -> bleu
CUSTOM_CSS = "theme/css/custom.css"

