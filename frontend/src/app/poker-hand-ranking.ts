import { Injectable } from '@angular/core';
import { RankingResult } from './ranking-result';

@Injectable({
  providedIn: 'root',
})
export class PokerHandRanking {
  url = 'http://localhost:8000/';

  async submitHand(cards: string[]): Promise<RankingResult | undefined> {
    try {
      const response = await fetch(`${this.url}?cards=${cards.join('&cards=')}`);
      if (!response.ok){
        // NOTE: This error handling isn't great. Ideally we'd display this next to the
        // correct input field, and the message would be more user friendly.
        // For now we just concat all the errors and display them instead of the result
        const errorBody = await response.json().catch(() => null);
        var msg = ""
        for (const err of errorBody.detail) {
          msg += "\n" + err.msg
        }
        return {"msg": msg};
      }
      const ranking = await response.json()
      return ranking;
    } catch (error) {
      console.log(error)
      return {"msg": "An error occured. Please try again later."}
    }
  };
}
