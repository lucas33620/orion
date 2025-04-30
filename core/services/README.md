# core/services/

Ce dossier regroupe la logique métier du projet Orion.

Chaque fichier implémente une action indépendante :
- `content_generator.py` : génération de contenus via OpenAI GPT
- `summarizer.py` : résumé de textes ou documents

Ces services peuvent être appelés par des vues, des APIs, ou des tâches asynchrones.
