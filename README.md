# Orion 🚀

Agent IA personnel de productivité et de diffusion multi-plateformes.

---

## 📖 Objectif
Créer un assistant intelligent capable de :
- Centraliser idées, documents, liens, messages vocaux
- Générer des contenus adaptés (posts LinkedIn, threads Twitter, emails, scripts vidéo)
- Automatiser la planification et la publication avec N8N
- Suivre les performances de diffusion

---

## 🛠️ Stack technique
- **Backend** : Django 3.1.7 + Django REST API
- **Base de données** : PostgreSQL
- **Frontend** : Tailwind CSS + HTMX
- **IA** : OpenAI GPT, Whisper, Text-to-Speech
- **Automatisation** : N8N
- **Déploiement** : Docker + GitHub Actions + VPS Linux Ubuntu 22.04

---

## 🚀 Instructions d'installation rapide

```bash
# Clone du projet
git clone git@github.com:lucas33620/orion.git
cd orion

# Création et activation d'un environnement virtuel
python3.9 -m venv venv
source venv/bin/activate

# Installation de Django
pip install django==3.1.7

# Démarrage du serveur local
python manage.py runserver
