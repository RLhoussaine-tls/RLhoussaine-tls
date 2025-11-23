#!/bin/bash
# Script pour arrêter le serveur Pelican

echo "Arrêt du serveur Pelican..."
pkill -f "pelican.*RLhoussaine-tls" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Serveur arrêté avec succès"
else
    echo "Aucun serveur Pelican en cours d'exécution"
fi

