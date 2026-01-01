import { Injectable } from '@angular/core';
import { RankingResult } from './ranking-result';

@Injectable({
  providedIn: 'root',
})
export class PokerHandRanking {
  url = 'http://localhost:8000/';

  async submitHand(cards: string[]): Promise<RankingResult | undefined> {
    console.log(cards.join('&cards='));
    const ranking = await fetch(`${this.url}?cards=${cards.join('&cards=')}`);
    return ranking.json()
  };
}
