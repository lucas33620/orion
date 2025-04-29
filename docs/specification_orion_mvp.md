# Spécification du Besoin – Projet ORION

## 1. Informations générales

- **Nom du projet** : ORION
- **Client** : Mr Baquey (simulation)
- **Consultant en charge** : Lucas (freelance)
- **Date de rédaction** : Avril 2025
- **Version** : 1.0

---

## 2. Contexte et objectifs

Le client souhaite concevoir un **assistant IA personnel**, capable de centraliser des idées, documents, messages vocaux, puis de générer automatiquement des contenus adaptés à différents canaux (LinkedIn, email, Twitter, TikTok, etc.).

Le but est de :

- Réduire le temps passé à produire et organiser du contenu.
- Offrir un outil “tout-en-un” simple et moderne pour les indépendants.
- Intégrer de l’intelligence contextuelle et une automatisation des tâches de publication.

---

## 3. Description fonctionnelle

### 3.1 Fonctionnalités principales MVP

| Réf. | Fonctionnalité | Objectif de la fonctionnalité | Entrées (Input) | Sorties (Output) | Interactions / Dépendances | Priorité | Faisabilité immédiate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F01 | Capture d’idées | Permettre à l’utilisateur d’enregistrer une idée rapidement | Texte libre, note vocale (fichier audio) | Enregistrement dans la base, transcription IA (Whisper) | Whisper API, DB, interface utilisateur | Haute | Oui |
| F02 | Résumé IA | Résumer un texte long ou un document | PDF, URL, texte brut | Résumé structuré (bullet points, paragraphe) | GPT API, modèle `Document` | Haute | Oui (GPT ready) |
| F03 | Génération de contenu | Créer un post, tweet, email, script vidéo à partir d’une idée | ID d’idée, format cible, ton souhaité | Contenu généré (ex: texte LinkedIn, thread Twitter, etc.) | GPT API, modèle `Content`, user context | Haute | Oui |
| F04 | Planification | Permettre à l’utilisateur de planifier la diffusion du contenu | Date/heure, plateforme cible, contenu lié | Tâche planifiée (N8N trigger, API call, notification) | N8N, modèle `Schedule`, DB | Moyenne | Oui (interface simple) |
| F06 | Interface utilisateur | Affichage clair des brouillons, idées, documents, contenus générés | Aucune (juste navigation) | Dashboard responsive avec sections claires | HTMX/Tailwind, back Django REST | Haute | Oui (dès maintenant) |

---

### 3.2 Cas d’usage simplifié

- L’utilisateur saisit une idée ou une note audio → Orion la stocke
- Il peut l’enrichir ou demander une génération IA → Orion propose plusieurs formats
- Il choisit un canal de diffusion → Orion suggère le bon ton
- Il programme ou déclenche la publication → Orion passe par N8N
- Il consulte plus tard les statistiques ou reprend une idée passée

---

## 4. Contraintes techniques

- **Python** : 3.9.1
- **Django** : 3.1.7
- **Base de données** : PostgreSQL
- **Frontend** : HTMX + TailwindCSS
- **Outils IA** : OpenAI (GPT-4, Whisper), TTS
- **Automatisation** : N8N
- **Hébergement** : VPS Linux Ubuntu 22.04
- **Déploiement** : Docker + GitHub Actions
- **Authentification** : à définir (token ou session)

---

## 5. Organisation du projet

### 5.1 Déploiement Git

- `main` : version stable
- `lba_dev` : branche de développement active
- Futures branches `feature/*` prévues si besoin

### 5.2 Planning prévisionnel

| Étape | Délai estimé |
| --- | --- |
| Initialisation du projet + environnement | 2 jours |
| Mise en place des modèles & admin | 3 jours |
| Développement frontend MVP | 1 semaine |
| Intégration IA (GPT, Whisper) | 1 semaine |
| Déploiement automatisé | 2 jours |
| Livraison finale + documentation | 2 jours |

---

## 6. Livrables attendus

- Interface web fonctionnelle avec modules clés
- Code source versionné et documenté
- README avec instructions d’installation
- Scripts Docker
- Exemple de contenus générés (exportables PDF/Notion)
- Rapport final ou présentation client

---

## 7. Prolongements potentiels

- Connexion multi-utilisateur
- Système de paiement si passage en SaaS
- API publique pour intégration d’outils tiers
- Application mobile ou PWA

---

## 8. Validation

Ce document servira de base pour la réalisation du projet. Toute modification majeure devra faire l’objet d’un avenant.

---

**Rédigé par : Lucas Baquey**

Freelance – Développement Backend & IA

Avril 2025
