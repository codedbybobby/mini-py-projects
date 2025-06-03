import requests


def pick_a_card_f(name):
    url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
card_name = 'kuriboh'.title()
pick_a_card = pick_a_card_f(card_name)

if pick_a_card:
    card = pick_a_card['data'][0]
    print(f"Name:\n", card['name'])
    print(f"\nType:\n", card['desc'])
    print(f"\nAttribute:\n", card['attribute'])
