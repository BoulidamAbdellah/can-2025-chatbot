import { Component, OnInit, ViewChild, ElementRef, AfterViewChecked } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatbotService } from '../services/chatbot.service';  // ← Importer le service

interface Message {
  id: number;
  message: string;
  sender: "user" | "bot";
  timestamp: Date;
}

@Component({
  selector: 'app-bot-component',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './bot-component.component.html',
  styleUrl: './bot-component.component.css'
})
export class BotComponentComponent implements OnInit, AfterViewChecked {
  @ViewChild('messagesContainer') private messagesContainer!: ElementRef;

  messages: Message[] = [];
  prompt: string = "";
  loading: boolean = false;
  private shouldScroll = false;

  // ← Injecter le service
  constructor(private chatbotService: ChatbotService) { }

  ngOnInit(): void {
    this.messages.push({
      id: 1,
      message: "Bienvenue au chatbot CAN 2025 Maroc ! 🇲🇦⚽",
      sender: 'bot',
      timestamp: new Date()
    });
  }

  ngAfterViewChecked(): void {
    if (this.shouldScroll) {
      this.scrollToBottom();
      this.shouldScroll = false;
    }
  }

  send(): void {
    if (!this.prompt.trim() || this.loading) return;

    this.loading = true;

    // Message utilisateur
    const userMessage: Message = {
      id: this.messages.length + 1,
      message: this.prompt,
      sender: "user",
      timestamp: new Date()
    };

    this.messages.push(userMessage);
    const userQuestion = this.prompt;
    this.prompt = "";
    this.shouldScroll = true;

    // ✅ APPEL API avec le service
    this.chatbotService.sendMessage(userQuestion, this.messages).subscribe({
      next: (response) => {
        // Succès : ajouter la réponse du bot
        const botResponse: Message = {
          id: this.messages.length + 1,
          message: response.response,
          sender: 'bot',
          timestamp: new Date()
        };
        this.messages.push(botResponse);
        this.loading = false;
        this.shouldScroll = true;
      },
      error: (error) => {
        // Erreur : afficher un message d'erreur ou utiliser réponse locale
        console.error('Erreur:', error);
        
        // Fallback : réponse locale si l'API échoue
        const botResponse: Message = {
          id: this.messages.length + 1,
          message: this.chatbotService.getLocalResponse(userQuestion),
          sender: 'bot',
          timestamp: new Date()
        };
        this.messages.push(botResponse);
        this.loading = false;
        this.shouldScroll = true;
      }
    });
  }

  handleKeyPress(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.send();
    }
  }

  private scrollToBottom(): void {
    try {
      this.messagesContainer.nativeElement.scrollTop = 
        this.messagesContainer.nativeElement.scrollHeight;
    } catch(err) { }
  }
}