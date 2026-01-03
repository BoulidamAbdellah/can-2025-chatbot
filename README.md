# 🏆 CAN 2025 Chatbot

Un chatbot intelligent basé sur RAG (Retrieval-Augmented Generation) pour répondre aux questions sur la Coupe d'Afrique des Nations 2025.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture](#-architecture)
- [Structure du projet](#-structure-du-projet)
- [Technologies utilisées](#-technologies-utilisées)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Utilisation](#-utilisation)
- [API Endpoints](#-api-endpoints)
- [Sources de données](#-sources-de-données)
- [Licence](#-licence)

## 📖 À propos

Ce projet est un chatbot intelligent spécialisé dans la Coupe d'Afrique des Nations 2025 (CAN 2025) qui se déroule au Maroc. Le chatbot utilise la technologie RAG (Retrieval-Augmented Generation) combinée avec le modèle Gemini de Google pour fournir des réponses précises et contextualisées sur :

- Les équipes participantes
- Les joueurs et leurs statistiques
- Les matchs et résultats
- Les stades et villes hôtes
- L'historique des équipes nationales

## ✨ Fonctionnalités

- 🤖 **Chatbot intelligent** : Répond aux questions en français et en anglais
- 🔍 **Recherche sémantique** : Utilise FAISS pour une recherche vectorielle efficace
- 📊 **Base de connaissances riche** : Données sur les 24 équipes qualifiées
- ⚡ **API REST** : Interface Flask pour l'intégration facile
- 🔄 **Réponses contextuelles** : Utilise le contexte pour des réponses précises

## 🏗 Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Utilisateur   │────▶│   API Flask     │────▶│  RAG Service    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                              ┌─────────────────────────┼─────────────────────────┐
                              ▼                         ▼                         ▼
                    ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
                    │  FAISS Vector   │     │   HuggingFace   │     │  Gemini LLM     │
                    │     Store       │     │   Embeddings    │     │    (Google)     │
                    └─────────────────┘     └─────────────────┘     └─────────────────┘
```

## 📁 Structure du projet

```
can-2025-chatbot/
├── can-chatbot-back/           # Backend Flask
│   ├── app.py                  # Application principale Flask
│   ├── ragService.py           # Service RAG avec LangChain
│   └── faiss_index_can/        # Index FAISS pré-calculé
│
├── can-chatbot-front/          # Frontend (à développer)
│
├── corpus_txt/                 # Corpus de texte pour le RAG
│   ├── matchs/                 # Données des matchs
│   ├── players/                # Fiches des joueurs par équipe
│   ├── stade/                  # Informations sur les stades
│   ├── team/                   # Données des équipes
│   ├── stades.txt              # Résumé des stades
│   └── teams_data.txt          # Résumé des équipes
│
├── documents/                  # Documents JSON source
│   ├── matchs/                 # Matchs en format JSON
│   ├── players/                # Joueurs par équipe en JSON
│   ├── stades.json             # Données des stades
│   └── teams_data.json         # Données des équipes
│
├── document_construction.ipynb # Notebook Jupyter pour la construction des données
├── .gitignore                  # Fichiers ignorés par Git
└── README.md                   # Ce fichier
```

## 🛠 Technologies utilisées

### Backend
- **Python 3.10+** - Langage de programmation
- **Flask** - Framework web
- **LangChain** - Framework pour applications LLM
- **FAISS** - Bibliothèque de recherche vectorielle
- **HuggingFace Transformers** - Modèle d'embeddings (all-MiniLM-L6-v2)
- **Google Generative AI** - Modèle Gemini pour la génération de texte

### Data Processing
- **BeautifulSoup4** - Web scraping
- **Wikipedia API** - Extraction de données Wikipedia
- **Pandas** - Manipulation de données

## 🚀 Installation

### Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)
- Une clé API Google Gemini

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/BoulidamAbdellah/can-2025-chatbot.git
   cd can-2025-chatbot
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   # ou
   .\venv\Scripts\activate   # Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install flask langchain langchain-community langchain-google-genai langchain-huggingface faiss-cpu python-dotenv
   ```

4. **Configurer les variables d'environnement**
   ```bash
   cd can-chatbot-back
   touch .env  # Créer le fichier .env
   ```

5. **Configurer la clé API Google**
   Éditer le fichier `.env` et ajouter votre clé API :
   ```
   GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE
   ```

## ⚙️ Configuration

### Variables d'environnement

| Variable | Description | Obligatoire |
|----------|-------------|-------------|
| `GOOGLE_API_KEY` | Clé API Google Gemini | ✅ Oui |

### Obtenir une clé API Google Gemini

1. Rendez-vous sur [Google AI Studio](https://aistudio.google.com/)
2. Connectez-vous avec votre compte Google
3. Cliquez sur "Get API key"
4. Créez une nouvelle clé ou utilisez une existante
5. Copiez la clé dans votre fichier `.env`

## 🎮 Utilisation

### Démarrer le serveur

```bash
cd can-chatbot-back
python app.py
```

Le serveur démarre sur `http://localhost:5555`

### Exemple d'utilisation avec curl

```bash
# Vérifier l'état du serveur
curl http://localhost:5555/api/health

# Poser une question
curl -X POST http://localhost:5555/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quels sont les joueurs de l'équipe du Maroc?"}'
```

### Exemple avec Python

```python
import requests

response = requests.post(
    "http://localhost:5555/api/chat",
    json={"message": "Qui a marqué lors du match Maroc vs DR Congo?"}
)
print(response.json()["response"])
```

## 🌐 API Endpoints

### `GET /`
Page d'accueil de l'API.

**Réponse :**
```json
{
  "message": "🏆 Chatbot CAN 2025 API",
  "version": "1.0.0",
  "status": "✅ En ligne",
  "endpoints": {
    "home": "GET /",
    "health": "GET /api/health",
    "chat": "POST /api/chat"
  }
}
```

### `GET /api/health`
Vérifier l'état du serveur.

**Réponse :**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-03T12:00:00",
  "chatbot_loaded": true
}
```

### `POST /api/chat`
Envoyer une question au chatbot.

**Requête :**
```json
{
  "message": "Votre question ici"
}
```

**Réponse :**
```json
{
  "response": "Réponse du chatbot",
  "timestamp": "2025-01-03T12:00:00",
  "status": "success"
}
```

## 📊 Sources de données

Les données utilisées par le chatbot proviennent de :

- **Wikipedia** - Informations sur les équipes, joueurs et stades
- **Données officielles CAN 2025** - Calendrier des matchs et résultats

### Équipes participantes (24 équipes)

| Groupe A | Groupe B | Groupe C | Groupe D |
|----------|----------|----------|----------|
| Maroc | Égypte | Nigeria | Tunisie |
| Mali | Afrique du Sud | Algérie | Angola |
| Zambie | Côte d'Ivoire | Cameroun | RD Congo |
| Comores | Gabon | Zimbabwe | Tanzanie |

| Groupe E | Groupe F |
|----------|----------|
| Sénégal | Burkina Faso |
| Guinée Équatoriale | Soudan |
| Bénin | Mozambique |
| Botswana | Ouganda |

## 🔧 Reconstruction de la base de données

Si vous souhaitez reconstruire la base de données vectorielle :

1. **Exécuter le notebook Jupyter**
   ```bash
   jupyter notebook document_construction.ipynb
   ```

2. **Suivre les étapes du notebook pour :**
   - Extraire les données des équipes
   - Récupérer les informations des joueurs
   - Collecter les données des matchs et stades
   - Générer le corpus de texte
   - Créer l'index FAISS

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

**Boulidam Abdellah**

- GitHub: [@BoulidamAbdellah](https://github.com/BoulidamAbdellah)

---

⭐ N'hésitez pas à mettre une étoile si ce projet vous a été utile !
