# 🎨 CAN 2025 Chatbot - Frontend

Interface utilisateur Angular pour le chatbot de la Coupe d'Afrique des Nations 2025.

![Angular](https://img.shields.io/badge/Angular-19.2+-dd0031.svg)
![TypeScript](https://img.shields.io/badge/TypeScript-5.7+-3178c6.svg)
![RxJS](https://img.shields.io/badge/RxJS-7.8+-b7178c.svg)

## 📋 Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Démarrage](#-démarrage)
- [Structure du projet](#-structure-du-projet)
- [Composants](#-composants)
- [Services](#-services)
- [Personnalisation](#-personnalisation)
- [Tests](#-tests)
- [Build et déploiement](#-build-et-déploiement)

## 📖 À propos

Cette application frontend Angular fournit une interface de chat intuitive et responsive pour interagir avec le chatbot CAN 2025. Elle se connecte à l'API backend Flask pour récupérer des réponses intelligentes basées sur RAG (Retrieval-Augmented Generation).

### Aperçu de l'interface

L'interface comprend :
- 🎯 **Header** avec le titre et le thème CAN 2025 Maroc
- 💬 **Zone de messages** avec distinction visuelle entre les messages utilisateur et bot
- ⌨️ **Zone de saisie** avec bouton d'envoi et indicateur de chargement
- 🎨 **Design moderne** aux couleurs du Maroc (rouge et vert)

## ✨ Fonctionnalités

- 💬 **Chat en temps réel** : Communication instantanée avec le chatbot
- 🔄 **Indicateur de chargement** : Animation pendant l'attente de la réponse
- 📱 **Design responsive** : Adapté aux mobiles, tablettes et desktop
- 🎨 **Interface moderne** : Animations fluides et effets visuels
- ⌨️ **Raccourci clavier** : Envoi du message avec la touche Entrée
- 🔙 **Fallback local** : Réponses de secours si l'API est indisponible
- 📜 **Défilement automatique** : Vers le dernier message reçu

## 🔧 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Node.js** version 18.19 ou supérieure
- **npm** version 9 ou supérieure
- **Angular CLI** version 19.2 ou supérieure

```bash
# Vérifier les versions installées
node --version
npm --version
ng version
```

## 🚀 Installation

1. **Naviguer vers le dossier frontend**
   ```bash
   cd can-chatbot-front
   ```

2. **Installer les dépendances**
   ```bash
   npm install
   ```

## ⚙️ Configuration

### Configuration de l'API Backend

L'URL de l'API backend est configurée dans le fichier `src/app/services/chatbot.service.ts` :

```typescript
// Ligne 30 - Modifier l'URL selon votre configuration
private apiUrl = 'http://127.0.0.1:5555/api/chat';
```

**Options de configuration :**

| Environnement | URL |
|---------------|-----|
| Développement local | `http://127.0.0.1:5555/api/chat` |
| Serveur de développement | `http://votre-serveur:5555/api/chat` |
| Production | `https://votre-domaine.com/api/chat` |

### Configuration des environnements (optionnel)

Pour une gestion avancée des environnements, vous pouvez créer des fichiers d'environnement dans `src/environments/` :

```typescript
// src/environments/environment.ts (développement)
export const environment = {
  production: false,
  apiUrl: 'http://127.0.0.1:5555/api/chat'
};

// src/environments/environment.prod.ts (production)
export const environment = {
  production: true,
  apiUrl: 'https://votre-api-production.com/api/chat'
};
```

## 🎮 Démarrage

### Serveur de développement

```bash
# Démarrer le serveur de développement
ng serve

# Ou avec npm
npm start
```

L'application sera accessible sur `http://localhost:4200/`

### Démarrage avec mode watch

```bash
npm run watch
```

### Démarrage SSR (Server-Side Rendering)

```bash
# Build SSR
npm run build

# Démarrer le serveur SSR
npm run serve:ssr:can-chatbot-front
```

## 📁 Structure du projet

```
can-chatbot-front/
├── src/
│   ├── app/
│   │   ├── bot-component/           # Composant principal du chatbot
│   │   │   ├── bot-component.component.ts
│   │   │   ├── bot-component.component.html
│   │   │   ├── bot-component.component.css
│   │   │   └── bot-component.component.spec.ts
│   │   │
│   │   ├── services/                # Services Angular
│   │   │   ├── chatbot.service.ts   # Service de communication API
│   │   │   └── chatbot.service.spec.ts
│   │   │
│   │   ├── app.component.ts         # Composant racine
│   │   ├── app.component.html
│   │   ├── app.component.css
│   │   ├── app.config.ts            # Configuration de l'application
│   │   ├── app.config.server.ts     # Configuration SSR
│   │   ├── app.routes.ts            # Routes de l'application
│   │   └── app.routes.server.ts     # Routes SSR
│   │
│   ├── index.html                   # Page HTML principale
│   ├── main.ts                      # Point d'entrée client
│   ├── main.server.ts               # Point d'entrée SSR
│   ├── server.ts                    # Serveur Express pour SSR
│   └── styles.css                   # Styles globaux
│
├── public/                          # Assets statiques
├── angular.json                     # Configuration Angular CLI
├── package.json                     # Dépendances npm
├── tsconfig.json                    # Configuration TypeScript
└── README.md                        # Ce fichier
```

## 🧩 Composants

### BotComponentComponent

Le composant principal qui gère l'interface de chat.

**Fichier :** `src/app/bot-component/bot-component.component.ts`

#### Propriétés

| Propriété | Type | Description |
|-----------|------|-------------|
| `messages` | `Message[]` | Liste des messages de la conversation |
| `prompt` | `string` | Texte saisi par l'utilisateur |
| `loading` | `boolean` | État de chargement (attente de réponse) |

#### Interface Message

```typescript
interface Message {
  id: number;           // Identifiant unique du message
  message: string;      // Contenu du message
  sender: "user" | "bot"; // Émetteur du message
  timestamp: Date;      // Date et heure du message
}
```

#### Méthodes principales

| Méthode | Description |
|---------|-------------|
| `ngOnInit()` | Initialise la conversation avec un message de bienvenue |
| `send()` | Envoie le message à l'API et gère la réponse |
| `handleKeyPress(event)` | Gère l'envoi par touche Entrée |
| `scrollToBottom()` | Défile automatiquement vers le bas |

#### Template HTML

Le template utilise la nouvelle syntaxe de flux de contrôle Angular 17+ :

```html
@for (mes of messages; track mes.id) {
  @if (mes.sender === "bot") {
    <!-- Message du bot -->
  } @else {
    <!-- Message de l'utilisateur -->
  }
}
```

## 🔌 Services

### ChatbotService

Service Injectable pour la communication avec l'API backend.

**Fichier :** `src/app/services/chatbot.service.ts`

#### Méthodes

| Méthode | Paramètres | Retour | Description |
|---------|------------|--------|-------------|
| `sendMessage()` | `message: string, history?: Message[]` | `Observable<ChatResponse>` | Envoie un message à l'API |
| `getLocalResponse()` | `message: string` | `string` | Génère une réponse locale de secours |

#### Exemple d'utilisation

```typescript
import { ChatbotService } from './services/chatbot.service';

constructor(private chatbotService: ChatbotService) { }

// Envoi d'un message
this.chatbotService.sendMessage('Quels sont les stades ?').subscribe({
  next: (response) => console.log(response.response),
  error: (error) => console.error(error)
});
```

#### Interface de la réponse API

```typescript
interface ChatResponse {
  response: string;   // Réponse du chatbot
  timestamp: Date;    // Horodatage
}
```

## 🎨 Personnalisation

### Couleurs et thème

Les couleurs principales sont définies dans `bot-component.component.css` :

```css
/* Couleurs du Maroc */
--morocco-red: #c1272d;
--morocco-green: #006233;
--morocco-green-light: #00a651;
--morocco-green-dark: #004d29;
```

### Modification du header

Dans `bot-component.component.html`, personnalisez le titre et la description :

```html
<div class="header-text">
  <h1>Chatbot CAN 2025</h1>
  <p>Coupe d'Afrique des Nations - Maroc 🇲🇦</p>
</div>
```

### Message de bienvenue

Modifiez le message initial dans `bot-component.component.ts` :

```typescript
ngOnInit(): void {
  this.messages.push({
    id: 1,
    message: "Bienvenue au chatbot CAN 2025 Maroc ! 🇲🇦⚽",
    sender: 'bot',
    timestamp: new Date()
  });
}
```

### Réponses de fallback

Personnalisez les réponses locales dans `chatbot.service.ts` :

```typescript
getLocalResponse(message: string): string {
  const msg = message.toLowerCase();
  
  if (msg.includes('date') || msg.includes('quand')) {
    return "La CAN 2025 se déroulera du 21 décembre 2025 au 18 janvier 2026 🗓️";
  }
  // Ajoutez d'autres conditions...
  
  return "Je suis spécialisé dans la CAN 2025. Posez-moi vos questions ! ⚽";
}
```

## 🧪 Tests

### Tests unitaires

```bash
# Exécuter les tests avec Karma
ng test

# Ou avec npm
npm test
```

### Tests en mode watch

```bash
ng test --watch
```

### Couverture de code

```bash
ng test --code-coverage
```

Les rapports de couverture seront générés dans le dossier `coverage/`.

## 📦 Build et déploiement

### Build de production

```bash
# Build standard
ng build

# Ou avec npm
npm run build
```

Les fichiers de build seront générés dans `dist/can-chatbot-front/`.

### Build SSR

Le projet est configuré avec Angular SSR (Server-Side Rendering) :

```bash
ng build
npm run serve:ssr:can-chatbot-front
```

### Déploiement

#### Option 1 : Hébergement statique (sans SSR)

Copiez le contenu de `dist/can-chatbot-front/browser/` vers votre serveur web.

#### Option 2 : Déploiement Node.js (avec SSR)

1. Build le projet : `npm run build`
2. Déployez le dossier `dist/can-chatbot-front/`
3. Exécutez : `node dist/can-chatbot-front/server/server.mjs`

#### Option 3 : Docker

Créez un `Dockerfile` :

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY dist/can-chatbot-front/ .
EXPOSE 4000
CMD ["node", "server/server.mjs"]
```

## 🛠 Dépendances principales

| Package | Version | Description |
|---------|---------|-------------|
| `@angular/core` | ^19.2.0 | Framework Angular |
| `@angular/common` | ^19.2.0 | Modules communs Angular |
| `@angular/forms` | ^19.2.0 | Formulaires réactifs et template-driven |
| `@angular/router` | ^19.2.0 | Routage SPA |
| `@angular/platform-browser` | ^19.2.0 | Plateforme navigateur |
| `@angular/ssr` | ^19.2.19 | Server-Side Rendering |
| `rxjs` | ~7.8.0 | Programmation réactive |
| `express` | ^4.18.2 | Serveur HTTP pour SSR |

## 📚 Ressources complémentaires

- [Documentation Angular](https://angular.dev/)
- [RxJS Documentation](https://rxjs.dev/)
- [Angular CLI Reference](https://angular.dev/tools/cli)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)

## 🤝 Contribution

1. Créez une branche : `git checkout -b feature/ma-fonctionnalite`
2. Committez : `git commit -m 'Ajout de ma fonctionnalité'`
3. Poussez : `git push origin feature/ma-fonctionnalite`
4. Ouvrez une Pull Request

---

⬅️ [Retour au README principal](../README.md)
