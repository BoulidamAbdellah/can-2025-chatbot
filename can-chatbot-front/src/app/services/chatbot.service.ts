import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';

// Interface pour la requête API
interface ChatRequest {
  message: string;
  conversationHistory?: Message[];
}

// Interface pour la réponse API
interface ChatResponse {
  response: string;
  timestamp: Date;
}

// Interface Message
interface Message {
  id: number;
  message: string;
  sender: 'user' | 'bot';
  timestamp: Date;
}

@Injectable({
  providedIn: 'root'  // Service disponible dans toute l'app
})
export class ChatbotService {
  // URL de votre API backend
  private apiUrl = 'http://127.0.0.1:5555/api/chat';  // ← Changez cette URL
  
  // Ou pour une API locale
  // private apiUrl = 'http://localhost:3000/api/chat';

  constructor(private http: HttpClient) { }

  /**
   * Envoyer un message à l'API et recevoir une réponse
   */
  sendMessage(message: string, history?: Message[]): Observable<ChatResponse> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      // Ajoutez votre clé API si nécessaire
      // 'Authorization': 'Bearer VOTRE_CLE_API'
    });

    const body: ChatRequest = {
      message: message,
      conversationHistory: history
    };

    return this.http.post<ChatResponse>(this.apiUrl, body, { headers })
      .pipe(
        catchError(this.handleError)
      );
  }

  /**
   * Gestion des erreurs
   */
  private handleError(error: any) {
    console.error('Erreur API:', error);
    
    let errorMessage = 'Une erreur est survenue';
    
    if (error.error instanceof ErrorEvent) {
      // Erreur côté client
      errorMessage = `Erreur: ${error.error.message}`;
    } else {
      // Erreur côté serveur
      errorMessage = `Code erreur: ${error.status}\nMessage: ${error.message}`;
    }
    
    return throwError(() => new Error(errorMessage));
  }

  /**
   * Réponse locale simulée (pour tester sans API)
   */
  getLocalResponse(message: string): string {
    const msg = message.toLowerCase();
    
    if (msg.includes('date') || msg.includes('quand')) {
      return "La CAN 2025 se déroulera du 21 décembre 2025 au 18 janvier 2026 🗓️";
    }
    if (msg.includes('stade') || msg.includes('où') || msg.includes('lieu')) {
      return "Les matchs auront lieu dans 5 stades principaux : Casablanca, Rabat, Agadir, Marrakech 🏟️";
    }
    if (msg.includes('équipe') || msg.includes('pays')) {
      return "24 équipes nationales participeront à la CAN 2025 🌍";
    }
    if (msg.includes('maroc')) {
      return "Le Maroc accueille la CAN 2025 ! 🇲🇦👑";
    }
    if (msg.includes('bonjour') || msg.includes('salut')) {
      return "Bonjour ! Comment puis-je vous aider sur la CAN 2025 ? 🙌";
    }
    
    return "Je suis spécialisé dans la CAN 2025. Posez-moi vos questions ! ⚽";
  }
}