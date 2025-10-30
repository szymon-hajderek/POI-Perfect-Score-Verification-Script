import pandas as pd
from collections import defaultdict
from util import replace_polish_chars
import Levenshtein

max_score = defaultdict(int)
perfect_scores_list = []

MAX_EDITION = 32
DOWNLOAD_RANKINGS = False # Set to True to freshly download data from the web
NO_DATA_EDITIONS = {1, 10}  # Editions with no data available

if DOWNLOAD_RANKINGS:
    for edition in range(1, MAX_EDITION + 1):
        if edition in NO_DATA_EDITIONS:
            continue # no data for these years

        url = f"https://oi.edu.pl/l/{edition}oi_1etap_wyniki/"
        tables = pd.read_html(url)  # Returns a list of all tables found
        df = tables[0]

        filtered = df[df["suma"] == df["suma"].max()]
        assert(len(filtered["imię"]) > 0) # Ensure that column name is correct
        
        name_surname = filtered["imię"] + " " + filtered["nazwisko"]

        for full_name in name_surname:
            full_name = replace_polish_chars(full_name.lower().strip())
            perfect_scores_list.append(full_name)
        
    with open("perfect_scores_list.txt", "w", encoding="utf-8") as f:
        for name in perfect_scores_list:
            f.write(f"{name}\n")
else:
    with open("perfect_scores_list.txt", "r", encoding="utf-8") as f:
        for line in f:
            perfect_scores_list.append(line.strip())

CHECK_POSSIBLE_TYPOS = True

if CHECK_POSSIBLE_TYPOS: # For manual inspection - checking for duplicates
    for i in range(len(perfect_scores_list)):
        for j in range(i + 1, len(perfect_scores_list)):
            distance = Levenshtein.distance(
                perfect_scores_list[i],
                perfect_scores_list[j]
            )
            if distance != 0 and distance <= 2: # Word distance 2 is a reasonable cap for a typo
                print(f"Possible duplicate: '{perfect_scores_list[i]}' and '{perfect_scores_list[j]}' (distance: {distance})")

# Manual inspection shows no typos to merge
for name in perfect_scores_list:
    max_score[name] += 1

for name, score in max_score.items():
    if score >= 4:
        print(f"{name}: {score}")