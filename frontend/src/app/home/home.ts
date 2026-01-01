import { ChangeDetectorRef, Component, inject } from '@angular/core';
import {FormControl, FormControlDirective, FormGroup, ReactiveFormsModule} from '@angular/forms';
import { PokerHandRanking } from '../poker-hand-ranking';
import { RankingResult } from '../ranking-result';

@Component({
  selector: 'app-home',
  imports: [ReactiveFormsModule],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {
  private readonly changeDetectorRef = inject(ChangeDetectorRef);
  rankingService = inject(PokerHandRanking);
  rankingResult: RankingResult | undefined;

  pokerHandForm = new FormGroup({
    firstCard: new FormControl(''),
    secondCard: new FormControl(''),
    thirdCard: new FormControl(''),
    fourthCard: new FormControl(''),
    fifthCard: new FormControl('')
  });

  submitPokerHand() {
    var cards = [
      this.pokerHandForm.value.firstCard ?? '',
      this.pokerHandForm.value.secondCard ?? '',
      this.pokerHandForm.value.thirdCard ?? '',
      this.pokerHandForm.value.fourthCard ?? '',
      this.pokerHandForm.value.fifthCard ?? ''
    ];

    this.rankingService.submitHand(cards).then((rankingResult) => {
      this.rankingResult = rankingResult;
      this.changeDetectorRef.markForCheck();
    })
  };
}
