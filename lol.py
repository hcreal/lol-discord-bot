import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue
from collections import Counter


# api_key = os.environ['api-key']
def main():
    cass.set_riot_api_key("APIKEY")  # This overrides the value set in your configuration/settings.
    cass.set_default_region("NA")
    summoner = Summoner(name="truestunna", region="NA")
    summoner = cass.get_summoner(name="truestunna")
    print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                            level=summoner.level,
                                                                            region=summoner.region))

    match_history = summoner.match_history
    match_history(seasons={Season.season_9}, queues={Queue.ranked_solo_fives})
    champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region="NA")}
    played_champions = Counter()
    for match in match_history:
        champion_id = match.participants[summoner.name].champion.id
        champion_name = champion_id_to_name_mapping[champion_id]
        played_champions[champion_name] += 1
    print("Length of match history:", len(match_history))

    # Print the aggregated champion results
    print("Top 10 champions {} played:".format(summoner.name))
    for champion_name, count in played_champions.most_common(10):
        print(champion_name, count)
    print()
    match = match_history[0]
    print('Match ID:', match.id)
    p = match.participants[summoner]
    msg = (f"Huge Nerd {p.summoner.name} wasted {match.duration} minutes playing as {p.champion.name} with {p.stats.kills} kills and died {p.stats.deaths} while some how only doing {p.stats.total_damage_dealt_to_champions} damage to champions")
    return msg
if __name__ == "__main__":
    main.py
