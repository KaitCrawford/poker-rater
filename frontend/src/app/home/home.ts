import { ChangeDetectorRef, Component, inject } from '@angular/core';
import {FormControl, FormControlDirective, FormGroup, ReactiveFormsModule} from '@angular/forms';
import { PokerHandRanking } from '../poker-hand-ranking';
import { RankingResult } from '../ranking-result';
import {Card} from '../card';

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

  pokerCardList: Card[] = [
    {display: "Ace of Spades", value: "AS"},
    {display: "Two of Spades", value: "2S"},
    {display: "Three of Spades", value: "3S"},
    {display: "Four of Spades", value: "4S"},
    {display: "Five of Spades", value: "5S"},
    {display: "Six of Spades", value: "6S"},
    {display: "Seven of Spades", value: "7S"},
    {display: "Eight of Spades", value: "8S"},
    {display: "Nine of Spades", value: "9S"},
    {display: "Ten of Spades", value: "0S"},
    {display: "Jack of Spades", value: "JS"},
    {display: "Queen of Spades", value: "QS"},
    {display: "King of Spades", value: "KS"},
    {display: "Ace of Hearts", value: "AH"},
    {display: "Two of Hearts", value: "2H"},
    {display: "Three of Hearts", value: "3H"},
    {display: "Four of Hearts", value: "4H"},
    {display: "Five of Hearts", value: "5H"},
    {display: "Six of Hearts", value: "6H"},
    {display: "Seven of Hearts", value: "7H"},
    {display: "Eight of Hearts", value: "8H"},
    {display: "Nine of Hearts", value: "9H"},
    {display: "Ten of Hearts", value: "0H"},
    {display: "Jack of Hearts", value: "JH"},
    {display: "Queen of Hearts", value: "QH"},
    {display: "King of Hearts", value: "KH"},
    {display: "Ace of Diamonds", value: "AD"},
    {display: "Two of Diamonds", value: "2D"},
    {display: "Three of Diamonds", value: "3D"},
    {display: "Four of Diamonds", value: "4D"},
    {display: "Five of Diamonds", value: "5D"},
    {display: "Six of Diamonds", value: "6D"},
    {display: "Seven of Diamonds", value: "7D"},
    {display: "Eight of Diamonds", value: "8D"},
    {display: "Nine of Diamonds", value: "9D"},
    {display: "Ten of Diamonds", value: "0D"},
    {display: "Jack of Diamonds", value: "JD"},
    {display: "Queen of Diamonds", value: "QD"},
    {display: "King of Diamonds", value: "KD"},
    {display: "Ace of Clubs", value: "AC"},
    {display: "Two of Clubs", value: "2C"},
    {display: "Three of Clubs", value: "3C"},
    {display: "Four of Clubs", value: "4C"},
    {display: "Five of Clubs", value: "5C"},
    {display: "Six of Clubs", value: "6C"},
    {display: "Seven of Clubs", value: "7C"},
    {display: "Eight of Clubs", value: "8C"},
    {display: "Nine of Clubs", value: "9C"},
    {display: "Ten of Clubs", value: "0C"},
    {display: "Jack of Clubs", value: "JC"},
    {display: "Queen of Clubs", value: "QC"},
    {display: "King of Clubs", value: "KC"}
  ];

  pokerHandForm = new FormGroup({
    firstCard: new FormControl(null),
    secondCard: new FormControl(null),
    thirdCard: new FormControl(null),
    fourthCard: new FormControl(null),
    fifthCard: new FormControl(null)
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
