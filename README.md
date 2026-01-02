# Poker Rater (Ranker):
Demo application made for a tech assessment

## Installation instructions:
1. Clone repo `git clone git@github.com:KaitCrawford/poker-rater.git`
2. Create ve `python3.10 -m venv ve`
3. Activate ve `source ve/bin/activate`
4. Install requirements `pip install -r requirements.txt`
5. Install frontend `cd ./frontend/ && npm install`
5. Install Angular cli `cd ./frontend/ && npm install -g @angular/cli`

## Running instructions:
- To run api: `fastapi run src/api.py`
- To run frontend: `cd ./frontend/ && ng serve`

## API endpoint:
- GET "/" will raise a validation error
- 5 "cards" query parameters are required
- Params must be 2 char strings, first char representing card value, second char representing card suit
- Mapping for card value representation: 10 => 0, Jack => J, Queen => Q, King => K, Ace => A, n => n
- Mapping for card suit representation: Spades => S, Diamonds => D, Hearts => H, Clubs => C
- Example: GET "/?cards=AH&cards=0H&cards=JH&cards=QH&cards=3H"
- Returns JSON response containing the hand ranking as "msg"
- Example: {"msg": "High Card: A}

## Notes:
- More notes can be found in comments starting with "NOTE"

## Test instructions:
1. Install requirements `pip install -r requirements-dev.txt`
2. Run tests `pytest`
