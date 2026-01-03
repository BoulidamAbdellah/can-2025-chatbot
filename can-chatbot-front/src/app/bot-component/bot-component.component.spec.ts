import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BotComponentComponent } from './bot-component.component';

describe('BotComponentComponent', () => {
  let component: BotComponentComponent;
  let fixture: ComponentFixture<BotComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BotComponentComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BotComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
