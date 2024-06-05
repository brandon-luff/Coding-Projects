import requests
import json

player_id = None
# Gets roster and player info and displays it in the terminal
# Prompts user to search for a player
def roster_info():

    team_id = None
    # API Links
    #BASE_URL = "https://statsapi.web.nhl.com"
    ROSTER_URL = None
    stats_url = None
    teams_url = "https://statsapi.web.nhl.com/api/v1/teams"
    #SCHEDULE_URL = "https://statsapi.web.nhl.com/api/v1/schedule"
    #STANDINGS_URL = "https://statsapi.web.nhl.com/api/v1/standings"

    #Try to reach api if not throw exception
    try:
        response = requests.get(teams_url)
    except:
        print("An error occured:", response.status_code)
        print("Program Closing...")
        quit()

    # Obtain the ID of team in order to display their roster
    if response.status_code == 200:
        teams = response.json()

        while True:
            print()
            team_select = input("Select a team to view roster for: ").title()

            count = 0
            while count < 32:
                if team_select == teams["teams"][count]["name"]:
                    team_id = teams["teams"][count]["id"]
                count += 1
            break

    roster_url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_id) + "/roster"

    # Try to reach api if not throw exception
    try:
        response = requests.get(roster_url)
    except:
        print("An error occured:", response.status_code)
        print("Program Closing...")
        quit()

    #Confirming URL is reachable
    if response.status_code == 200:
        roster = response.json()

        # While loop to iterate through JSON and print the full 23 man roster
        count = 0

        print()
        print("****Current " + team_select + " Roster****")
        print()

        while count < 23:
            print("\t" + "     " + roster["roster"][count]["person"]["fullName"])
            count += 1
        
        while True:
            # Spacing and asking user to select a player
            print ()
            player = input("Select a player to view their bio (Or type 'Q' to Quit): ").title()
            if player == "Q":
                print("Program Closing...")
                print()
                quit()

            # While loop to find the selected players API URL and create working link
            count = 0
            while count <= 23:
                if player == roster["roster"][count]["person"]["fullName"]:
                    stats_url = "https://statsapi.web.nhl.com" + roster["roster"][count]["person"]["link"]
                    break
                count += 1
                if count == 23 and player != roster["roster"][count]["person"]["fullName"]:
                    count = 0
                    print()
                    player = input("Enter a valid player name to view bio: ").title()
                    print()

            response = requests.get(stats_url)

            if response.status_code == 200:

                info = response.json()

                # Obtaining selected players info from JSON
                number = info["people"][0]["primaryNumber"]
                age = info["people"][0]["currentAge"]
                height = info["people"][0]["height"]
                weight = info["people"][0]["weight"]
                handedness = info["people"][0]["shootsCatches"]
                position = info["people"][0]["primaryPosition"]["name"]

                # Printing selected players info
                print("\t" + "     " + "Player Name:", player)
                print("\t" + "     " + "Number:", number)
                print("\t" + "     " + "Age:", age)
                print("\t" + "     " + "Height:", height)
                print("\t" + "     " + "Weight:", weight)
                print("\t" + "     " + "Handedness:", handedness)
                print("\t" + "     " + "Position:", position + "\n")

            # Error message and error code if player URL is unreachable
            else:
                print("An error occured:", response.status_code) 

            # Check to see if user wants to search for player again
            while True:
                query = input("Would you like to view another players info? (Yes/No): ").upper()
                if query == "YES":
                    break
                elif query == "NO":
                    print("Program Closing..." + "\n")
                    quit()
                else:
                    continue

def player_stats():
    BASE_URL = "https://statsapi.web.nhl.com/api/v1/people/"
    player_id = None
    END_URL = "?expand=person.stats&stats=careerRegularSeason&expand=stats.team&site=en_nhl"
    teams_url = "https://statsapi.web.nhl.com/api/v1/teams"

    #Get the players ID

    try:
        response = requests.get(teams_url)
    except:
        print("An error occured:", response.status_code)
        print("Program Closing...")
        quit()

    # Obtain the ID of team in order to display their roster
    if response.status_code == 200:
        teams = response.json()

        while True:
            print()
            team_select = input("Select a team to view roster for: ").title()

            count = 0
            while count < 32:
                if team_select == teams["teams"][count]["name"]:
                    team_id = teams["teams"][count]["id"]
                count += 1
            break

    roster_url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_id) + "/roster"

    # Try to reach api if not throw exception
    try:
        response = requests.get(roster_url)
    except:
        print("An error occured:", response.status_code)
        print("Program Closing...")
        quit()

    #Confirming URL is reachable
    if response.status_code == 200:
        roster = response.json()

        # While loop to iterate through JSON and print the full 23 man roster
        count = 0

        print()
        print("****Current " + team_select + " Roster****")
        print()

        while count < 23:
            print("\t" + "     " + roster["roster"][count]["person"]["fullName"])
            count += 1
        
        while True:
            # Spacing and asking user to select a player
            print ()
            player = input("Select a player to view their stats (Or type 'Q' to Quit): ").title()
            if player == "Q":
                print("Program Closing...")
                print()
                quit()

            # While loop to find the selected players API URL and create working link
            count = 0
            while count <= 23:
                if player == roster["roster"][count]["person"]["fullName"]:
                    stats_url = "https://statsapi.web.nhl.com" + roster["roster"][count]["person"]["link"]
                    break
                count += 1
                if count == 23 and player != roster["roster"][count]["person"]["fullName"]:
                    count = 0
                    print()
                    player = input("Enter a valid player name to view stats: ").title()
                    print()

            response = requests.get(stats_url)

            if response.status_code == 200:

                info = response.json()

                # Obtaining selected players ID from JSON
                player_id = info["people"][0]["id"]

            # Error message and error code if player URL is unreachable
            else:
                print("An error occured:", response.status_code)

            stat_page_url = f"https://statsapi.web.nhl.com/api/v1/people/{player_id}?expand=person.stats&stats=careerRegularSeason&expand=stats.team&site=en_nhl"
            print(stat_page_url)
            
            response = requests.get(stat_page_url)

            if response.status_code == 200:
                stats = response.json()

                # Obtaining selected players info from JSON
                games = info["people"][0]["stats"][0]["splits"][0]["stat"]["games"]
                goals = info["people"][0]["stats"][0]["splits"][0]["stat"]["goals"]
                assists = info["people"][0]["stats"][0]["splits"][0]["stat"]["assists"]
                hits = info["people"][0]["stats"][0]["splits"][0]["stat"]["hits"]
                pim = info["people"][0]["stats"][0]["splits"][0]["stat"]["pim"]
                shots = info["people"][0]["stats"][0]["splits"][0]["stat"]["shots"]
                faceoff_pct = info["people"][0]["stats"][0]["splits"][0]["stat"]["faceOffPct"]
                shot_pct = info["people"][0]["stats"][0]["splits"][0]["stat"]["shotPct"]
                points = goals + assists

                # Printing selected players info
                print("\t" + "     " + "Player Name:", player)
                print("\t" + "     " + "Games:", games)
                print("\t" + "     " + "Goals:", goals)
                print("\t" + "     " + "Assists:", assists)
                print("\t" + "     " + "Points:", points)  
                print("\t" + "     " + "Hits:", hits)
                print("\t" + "     " + "PIMs:", pim)
                print("\t" + "     " + "Shots:", shots)
                print("\t" + "     " + "Shooting %:", shot_pct)
                print("\t" + "     " + "Faceoff %:", faceoff_pct + "\n")

            else:
                print("An error occured:", response.status_code)

            while True:
                query = input("Would you like to view another players stats? (Yes/No): ").upper()
                if query == "YES":
                    break
                elif query == "NO":
                    print("Program Closing..." + "\n")
                    quit()
                else:
                    continue


# Funtion calls   
#roster_info()
roster_info()
#player_stats()
