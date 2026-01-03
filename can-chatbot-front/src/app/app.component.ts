import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BotComponentComponent } from './bot-component/bot-component.component';

@Component({
  selector: 'app-root',
  imports: [BotComponentComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'can-chatbot-front';
}
