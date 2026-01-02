import { ChangeDetectorRef, Component, inject } from '@angular/core';
import {FormControl, FormControlDirective, FormGroup, ReactiveFormsModule} from '@angular/forms';
import { PokerHandRanking } from '../poker-hand-ranking';
import { RankingResult } from '../ranking-result';
import { CardValue } from '../card';

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

  pokerCardValues: CardValue[] = [
    {'display': "2", "value": "2"},
    {"display": "3", "value": "3"},
    {"display": "4", "value": "4"},
    {"display": "5", "value": "5"},
    {"display": "6", "value": "6"},
    {"display": "7", "value": "7"},
    {"display": "8", "value": "8"},
    {"display": "9", "value": "9"},
    {"display": "10", "value": "0"},
    {"display": "Jack", "value": "J"},
    {"display": "Queen", "value": "Q"},
    {"display": "King", "value": "K"},
    {'display': "Ace", "value": "A"}
  ];
  pokerCardSuits: string[] = ["Spades", "Diamonds", "Hearts", "Clubs"];

  pokerHandForm = new FormGroup({
    firstCardValue: new FormControl(null),
    firstCardSuit: new FormControl(null),
    secondCardValue: new FormControl(null),
    secondCardSuit: new FormControl(null),
    thirdCardValue: new FormControl(null),
    thirdCardSuit: new FormControl(null),
    fourthCardValue: new FormControl(null),
    fourthCardSuit: new FormControl(null),
    fifthCardValue: new FormControl(null),
    fifthCardSuit: new FormControl(null)
  });

  submitPokerHand() {
    var cards = [
      (this.pokerHandForm.value.firstCardValue ?? '') + (this.pokerHandForm.value.firstCardSuit ?? ''), 
      (this.pokerHandForm.value.secondCardValue ?? '') + (this.pokerHandForm.value.secondCardSuit ?? ''),
      (this.pokerHandForm.value.thirdCardValue ?? '') + (this.pokerHandForm.value.thirdCardSuit ?? ''),
      (this.pokerHandForm.value.fourthCardValue ?? '') + (this.pokerHandForm.value.fourthCardSuit ?? ''),
      (this.pokerHandForm.value.fifthCardValue ?? '') + (this.pokerHandForm.value.fifthCardSuit ?? '')
    ];

    this.rankingService.submitHand(cards).then((rankingResult) => {
      this.rankingResult = rankingResult;
      this.changeDetectorRef.markForCheck();
    })
  };
}
