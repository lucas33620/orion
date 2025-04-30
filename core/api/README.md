# core/api/

Ce dossier contient les vues API (REST ou HTMX) du projet Orion.

Chaque fichier correspond à un ensemble de endpoints liés à une ressource :
- `idea_api.py` : Endpoints liés aux idées
- `content_api.py` : Endpoints liés à la génération de contenu

Les vues ici peuvent renvoyer du JSON, du HTML (via HTMX), ou déclencher des services.
