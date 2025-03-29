import requests

    with open("lichess_token.txt", "r") as file:
        token = file.read().strip()

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://lichess.org/api/account", headers=headers)

    if response.status_code == 200:
        print("Lichess API connected successfully!")
        print(response.json())
    else:
        print("Failed to connect. Check your token.")
    