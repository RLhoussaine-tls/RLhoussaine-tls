#!/bin/bash
# Script pour activer l'environnement virtuel et utiliser Pelican

# Activer l'environnement virtuel
source .venv/bin/activate

# Exécuter la commande passée en argument
"$@"

