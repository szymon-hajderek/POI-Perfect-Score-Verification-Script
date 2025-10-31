# POI Perfect Score Verification Script

This python script is used to find all the contestant to have achieved a perfect score **four times** in the first stage of Polish Olympiad in Informatics.

**Note:** *Editions 1 and 10 have no publicly available data.*

# Features

The script downloads publicly available data from the official POI site.
It then cleans and normalizes names, including handling Polish characters.
Potential typos in contestant names are detected and reported. 
The script outputs all contestant to have ever achieved four perfect scores (based on available data).

# Notes:
- CHECK_POSSIBLE_TYPOS is set to True by default to detect minor inconsistencies in contestant names.
- Designed for educational and verification purposes only.

# Acknowledgements

- Data source: oi.edu.pl
- Python libraries: `pandas`, `Levenshtein`.