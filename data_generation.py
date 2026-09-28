import pprint
import argparse
import json
import random as rand
from tqdm import tqdm
from lookup import run_lookup, ACCRONYM_DICT

REMOVED_CHARS = "{}'\","

COUNTRIES = {"romania",
            "america",
            "sua",
            "england",
            "britain",
            "uk",
            "austria",
            "netherlands",
            "spain",
            "ireland",
            "germany",
            "norway",
            "france",
            "switzerland",
            "portugal",
            "belgium",
            "poland",
            "luxembourg",
            "singapore",
            "india",
            "lithuania",
            "australia",
            "canada",
            "brazil",
            "ukraine",
            "sweden",
            "finland",
            "denmark",
            "iceland",
            "kuwait",
            "korea",
            "new zeeland",
            "italy",
            "china",
            "vietnam",
            "japan",
            "turkey",
            "indonesia",
            "argentina",
            "greece",
            "egypt",
            "chile",
            "taiwan",
            "hong kong",
            "russia",
            "croatia",}
CITIES = set()
MARKETS = set()
MODELS = set()
MINYEAR = 0
MAXYEAR = 0
MINEMP = 0
MAXEMP = 0
MINREV = 0
MAXREV = 0

with open("lookups/all_cities.txt", "r") as f:
    text = str.lower(f.read().strip().translate(str.maketrans("", "", REMOVED_CHARS)))
    locations = text.split("\n")
    for location in locations:
        CITIES.add(location.strip().lower())

with open("lookups/all_markets.txt", "r") as f:
    text = str.lower(f.read().strip().translate(str.maketrans("", "", REMOVED_CHARS)))
    markets = text.split("\n")
    for market in markets:
        MARKETS.add(market.strip().lower())

with open("lookups/all_business_models.txt", "r") as f:
    text = str.lower(f.read().strip().translate(str.maketrans("", "", REMOVED_CHARS)))
    models = text.split("\n")
    for model in models:
        MODELS.add(model.strip().lower())

with open("lookups/minmax_years.txt", "r") as f:
    text = f.read()
    years = text.split(" ")
    MINYEAR = years[0]
    MAXYEAR = years[1]

with open("lookups/minmax_employees.txt", "r") as f:
    text = f.read()
    employees = text.split(" ")
    MINEMP = employees[0]
    MAXEMP = employees[1]

with open("lookups/minmax_revenues.txt", "r") as f:
    text = f.read()
    revenues = text.split(" ")
    MINREV = revenues[0]
    MAXREV = revenues[1]

MIDDLE_WORDS = ["companies", "manufacturers", "businesses", "firms", "vendors"]

INCLUDE_PROBS = {"location": 0.6,
    "market": 0.55,
    "business_model": 0.45,
    "year": 0.5,
    "employees": 0.5,
    "revenue": 0.5,
}
OUTSIDE_PROB = 0.2
YEAR_PROBS = [("exact", 0.3), ("before", 0.35), ("after", 0.35)]
EMP_PROBS = [("exact", 0.2), ("under", 0.4), ("over", 0.4)]
REV_PROBS = [("exact", 0.2), ("less", 0.4), ("more", 0.4)]

def weighted_choice(weights):
    options, probs = zip(*weights)
    return rand.choices(options, weights=probs, k=1)[0]

def select_position(before_words: set(), after_words: set(), element: str):
    position = rand.randint(0, 1)
    if position:
        after_words.add(element)
    else:
        before_words.add(element)

def build_location_filter(before_words, after_words):
    is_country = rand.randint(0, 1)
    location = rand.choice(list(COUNTRIES)) if is_country else rand.choice(list(CITIES))
    outside = rand.random() < OUTSIDE_PROB
    if outside:
        phrase = rand.choice([f"not {location}", f"outside {location}", f"excluding {location}"])
        after_words.add(phrase)
    else:
        select_position(before_words, after_words, location)
    return {"location": location, "outside": outside}

def build_market_filter(before_words, after_words):
    market = rand.choice(list(MARKETS))
    select_position(before_words, after_words, market)
    return {"target_market": market}

def build_business_model_filter(before_words):
    model = rand.choice(list(MODELS))
    if model in ACCRONYM_DICT.keys():
        is_acronym = rand.randint(0, 1)
        if is_acronym:
            model = ACCRONYM_DICT[model]
    before_words.add(model)
    return {"business_model": model}

def build_year_filter(before_words, after_words):
    year = rand.randint(int(MINYEAR), int(MAXYEAR))
    direction = weighted_choice(YEAR_PROBS)
    if direction == "exact":
        phrase, kwargs = str(year), {"year": year}
    elif direction == "before":
        phrase, kwargs = f"before {year}", {"year": year, "before": True}
    else:
        phrase, kwargs = f"after {year}", {"year": year, "after": True}
    select_position(before_words, after_words, phrase)
    return kwargs

def build_employees_filter(after_words):
    employees = rand.randint(int(MINEMP), int(MAXEMP))
    direction = weighted_choice(EMP_PROBS)
    if direction == "exact":
        phrase, kwargs = f"{employees} emp", {"employees": employees}
    elif direction == "under":
        phrase, kwargs = f"under {employees} emp", {"employees": employees, "under": True}
    else:
        phrase, kwargs = f"over {employees} emp", {"employees": employees, "over": True}
    after_words.add(phrase)
    return kwargs

def build_revenue_filter(after_words):
    revenue = rand.randint(int(MINREV), int(MAXREV))
    direction = weighted_choice(REV_PROBS)
    if direction == "exact":
        phrase, kwargs = f"{revenue} rev", {"revenue": revenue}
    elif direction == "under":
        phrase, kwargs = f"with less than {revenue} rev", {"revenue": revenue, "less": True}
    else:
        phrase, kwargs = f"with more than {revenue} rev", {"revenue": revenue, "more": True}
    after_words.add(phrase)
    return kwargs

FILTERS = {
    "location": build_location_filter,
    "market": build_market_filter,
    "business_model": build_business_model_filter,
    "year": build_year_filter,
    "employees": build_employees_filter,
    "revenue": build_revenue_filter,
}

MACRO_REGIONS = {
    "Scandinavia": ["sweden", "norway", "finland", "denmark"],
    "Eastern Europe": ["poland", "romania", "lithuania", "croatia", "ukraine"],
    "Western Europe": ["france", "germany", "austria", "netherlands", "belgium", "switzerland"],
    "North America": ["america", "sua", "canada"],
    "Asia": ["china", "japan", "korea", "singapore", "india", "vietnam", "indonesia", "taiwan"]
}

CONCEPT_PROXIES = {
    "agile startups": {"year": 2018, "after": True, "employees": 100, "under": True},
    "enterprise-scale providers": {"employees": 1000, "over": True},
    "legacy institutions": {"year": 2000, "before": True},
    "fast-growing competitors": {"revenue": 5000000, "more": True, "year": 2015, "after": True},
    "boutique agencies": {"employees": 50, "under": True, "revenue": 2000000, "less": True}
}

TEMPLATES = [
    "Companies that could supply {market} materials or components to {concept} in {region}",
    "Looking for {concept} operating out of {region} that cater to the {market} industry",
    "companies providing {market} solutions for {concept} based in {region}",
    "Disruptive {concept} competing with traditional {market} vendors in {region}",
    "Major players and {concept} focusing on {market} technology across {region}"
]

def generate_complex_example():
    template = rand.choice(TEMPLATES)
    lookup_kwargs = {}

    concept = rand.choice(list(CONCEPT_PROXIES.keys()))
    lookup_kwargs.update(CONCEPT_PROXIES[concept])

    market = rand.choice(list(MARKETS))
    lookup_kwargs["target_market"] = market

    if rand.random() > 0.5:
        region_name = rand.choice(list(MACRO_REGIONS.keys()))
        lookup_kwargs["location"] = MACRO_REGIONS[region_name]
        query = template.format(market=market, concept=concept, region=region_name)
    else:
        location = rand.choice(list(COUNTRIES))
        lookup_kwargs["location"] = location
        query = template.format(market=market, concept=concept, region=location)

    query = " ".join(query.lower().split())
    indices = run_lookup(**lookup_kwargs)

    return {"query": query, "relevant_indices": indices, "filters": lookup_kwargs}

def generate_example():
    if rand.random() < 0.4:
        return generate_complex_example()


    before_words = set()
    after_words = set()
    lookup_kwargs = {}

    active = [name for name, prob in INCLUDE_PROBS.items() if rand.random() < prob]
    if not active:
        active = [rand.choice(list(INCLUDE_PROBS))]

    for name in active:
        if name == "business_model":
            kwargs = FILTERS[name](before_words)
        elif name == "revenue" or name == "employees":
            kwargs = FILTERS[name](after_words)
        else:
            kwargs = FILTERS[name](before_words, after_words)
        lookup_kwargs.update(kwargs)

    middle = rand.choice(MIDDLE_WORDS)
    query = " ".join(list(before_words) + [middle] + list(after_words))
    query = " ".join(query.lower().split())

    indices = run_lookup(**lookup_kwargs)
    return {"query": query, "relevant_indices": indices, "filters": lookup_kwargs}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_examples", type=int, default=1000)
    parser.add_argument("--output", type=str, default="query_dataset.jsonl")
    args = parser.parse_args()

    written = 0
    attempts = 0
    max_attempts = args.num_examples * 50
    seen_indices = set()

    with open(args.output, "w", encoding="utf-8") as f:
        with tqdm(total=args.num_examples, desc="Generating dataset") as pbar:
            while written < args.num_examples and attempts < max_attempts:
                attempts += 1
                example = generate_example()
                if len(example["relevant_indices"]) == 0:
                    continue

                key = tuple(example["relevant_indices"])
                if key in seen_indices:
                    continue
                seen_indices.add(key)

                f.write(json.dumps(example) + "\n")
                written += 1
                pbar.update(1)

    print(f"Wrote {written} examples to {args.output} ({attempts} attempts).")


if __name__ == "__main__":
    main()