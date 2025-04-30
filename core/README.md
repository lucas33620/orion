# 🧩 App Django : core

## 🎯 Rôle
Cette app contient les **éléments fondamentaux** du projet Orion :
- Les modèles principaux (`Idea`, `Document`, `Content`, `Schedule`)
- Les vues de base liées au dashboard et aux interactions utilisateur
- La logique de génération IA (à terme via `services/` ou `utils/`)

---

## 📦 Contenu
- `models.py` : structure des données principales
- `views.py` : vues HTMX (dashboard, ajout, affichage de contenu)
- `admin.py` : configuration de l’interface d’administration Django
- `services/` : logique IA (GPT, Whisper) [à venir]
- `api/` : future API REST si besoin d’exposer l’app via JSON

---

## 🔗 Dépendances
- OpenAI (GPT, Whisper) [à venir]
- TailwindCSS pour styliser les templates
- N8N (connecté à `Schedule`) pour les automatisations

---

## 🧱 Exemple d’usage
```python
idea = Idea.objects.create(title="Nouvelle idée", content="Créer une app IA pour générer des posts LinkedIn.")
