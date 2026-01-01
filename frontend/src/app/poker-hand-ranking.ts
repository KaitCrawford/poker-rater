import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class PokerHandRanking {
  url = 'http://localhost:8000/';

  async submitHand(cards: string[]): Promise<string | undefined> {
    console.log(cards.join('&cards='));
    const ranking = await fetch(`${this.url}?cards=${cards.join('&cards=')}`);
    const result = await ranking
    console.log(result)
    return "bla";
  };
}
