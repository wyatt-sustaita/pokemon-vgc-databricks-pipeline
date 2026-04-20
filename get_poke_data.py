import requests
import pandas as pd
base_url = "https://pokeapi.co/api/v2/pokemon?limit=1350"


def get_all_data():
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching Pokémon data: {response.status_code}")
        return None


if __name__ == "__main__":
    poke_list = get_all_data()
    poke_df = pd.DataFrame()
    if poke_list:
        for pokemon in poke_list['results']:
            poke_url = pokemon['url']
            print(f"Retrieving data for {pokemon['name']}...")
            poke_response = requests.get(poke_url)
            if poke_response.status_code == 200:
                poke_data = poke_response.json()
                poke_df = pd.concat(
                    [poke_df, pd.DataFrame([poke_data])], ignore_index=True)

    poke_df.to_json("poke_data.json", orient="records", indent=4)
    print("Pokémon data has been saved to poke_data.json")
