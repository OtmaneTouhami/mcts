import csv
import random

# Some sample names and countries
FIRST_NAMES = ["Mohamed", "Sara", "John", "Emily", "Hakim", "Anna", "Youssef", "David", "Lina", "Omar"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Garcia", "Martinez", "Williams", "Hassan", "Takagi", "Chen", "Ahmed"]
COUNTRIES = ["USA", "Morocco", "France", "Japan", "Germany", "Canada", "UK", "Spain", "Italy", "Brazil"]

OUTPUT_FILE = "./people_1M.csv"
NUM_ROWS = 1_000_000  # 1 million rows

def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_country():
    return random.choice(COUNTRIES)

def random_height():
    return random.uniform(140, 215)  # Height in cm

# Write CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["index", "person_name", "country", "height"])

    for i in range(1, NUM_ROWS + 1):
        writer.writerow([i, random_name(), random_country(), f"{random_height():.2f}"])

print("CSV file generated successfully:", OUTPUT_FILE)