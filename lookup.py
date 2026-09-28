import re
import sys
import json
import pprint
import argparse

COUNTRYCODE_DICT = {"romania": "ro",
                    "america": "us",
                    "sua": "us",
                    "england": "gb",
                    "britain": "gb",
                    "uk": "gb",
                    "austria": "at",
                    "netherlands": "nl",
                    "spain": "es",
                    "ireland": "ie",
                    "germany": "de",
                    "norway": "no",
                    "france": "fr",
                    "switzerland": "ch",
                    "portugal": "pt",
                    "belgium": "be",
                    "poland": "pl",
                    "luxembourg": "lu",
                    "singapore": "sg",
                    "india": "in",
                    "lithuania": "lt",
                    "australia": "au",
                    "canada": "ca",
                    "brazil": "br",
                    "ukraine": "ua",
                    "sweden": "se",
                    "finland": "fi",
                    "denmark": "dk",
                    "iceland": "is",
                    "kuwait": "kw",
                    "korea": "kr",
                    "new zeeland": "nz",
                    "italy": "it",
                    "china": "cn",
                    "vietnam": "vn",
                    "japan": "jp",
                    "turkey": "tr",
                    "indonesia": "id",
                    "argentina": "ar",
                    "greece": "gr",
                    "egypt": "eg",
                    "chile": "cl",
                    "taiwan": "tw",
                    "hong kong": "hk",
                    "russia": "ru",
                    "croatia": "hr",}
ACCRONYM_DICT = {"business-to-business": "b2b",
                "business-to-consumer": "b2c",
                "software-as-a-service": "saas",
                "non-profit organization": "npo",
                "non-governmental organization": "ngo",
                }

def untangle(double_models: list):
    models = set()
    for model in double_models:
            if " " not in model:
                split = model.split("/")
                models.add(split[0])
                models.add(split[1])
            else:
                split = model.split(" ")
                split2 = split[0].split("/")
                models.add(split2[0] + " " + split[1])
                models.add(split2[1] + " " + split[1])
    return models

def load_companies(path):
    companies = []
    index = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                company = json.loads(line)
                address = company["address"]
                if type(company["address"]) == str:
                    json_string = company["address"]
                    json_string = json_string.replace("\'", "\"")
                    json_string = json_string.replace(" d\"", " d'")
                    json_string = json_string.replace("-d\"", "-d'")
                    json_string = json_string.replace("None", "null")
                    json_string = str.lower(json_string)
                    new_address = json.loads(json_string)
                    company["address"] = new_address
                company["index"] = index
                company["description"] = str.lower(company["description"])
                lower_markets = [str.lower(market) for market in company["target_markets"]]
                company["target_markets"] = lower_markets
                lower_business_models = [str.lower(model) for model in company["business_model"]]
                company["business_model"] = lower_business_models
                index = index + 1
                companies.append(company)
    return companies
companies = load_companies("companies.jsonl")

def location_lookup(companies, locations, outside=False):
    if isinstance(locations, str):
        locations = [locations]
        
    locations = [str.lower(loc) for loc in locations]
    valid_indices = set()
    
    for company in companies:
        matched_any = False
        
        for loc in locations:
            address_match = (
                (company["address"]["region_name"] is not None and loc == company["address"]["region_name"]) or
                (company["address"]["town"] is not None and loc == company["address"]["town"]) or
                (loc in company["description"])
            )
            
            code_match = False
            if loc in COUNTRYCODE_DICT:
                country_code = COUNTRYCODE_DICT[loc]
                if company["address"]["country_code"] is not None and company["address"]["country_code"] == country_code:
                    code_match = True
                    
            if address_match or code_match:
                matched_any = True
                break
        
        if not outside and matched_any:
            valid_indices.add(company["index"])
        elif outside and not matched_any:
            valid_indices.add(company["index"])
            
    return valid_indices

def year_lookup(companies, year, before=False, after=False):
    if before and after:
        raise KeyError("Can't lookup both before and after a certain year")

    if not before and not after:
        found_companies = [company for company in companies
                            if company["year_founded"] is not None and
                            company["year_founded"] == year]
    elif before and not after:
        found_companies = [company for company in companies
                            if company["year_founded"] is not None and
                            company["year_founded"] < year]
    elif not before and after:
        found_companies = [company for company in companies
                            if company["year_founded"] is not None and
                            company["year_founded"] > year]

    found_indices = {company["index"] for company in found_companies}
    return found_indices

def employee_lookup(companies, emp_count, under=False, over=False):
    if under and over:
        raise KeyError("Can't lookup both under and over a certain number of employees.")

    if not under and not over:
        found_companies = [company for company in companies
                            if company["employee_count"] is not None and
                            company["employee_count"] == emp_count]
    elif under and not over:
        found_companies = [company for company in companies
                            if company["employee_count"] is not None and
                            company["employee_count"] < emp_count]
    elif not under and over:
        found_companies = [company for company in companies
                            if company["employee_count"] is not None and
                            company["employee_count"] > emp_count]

    found_indices = {company["index"] for company in found_companies}
    return found_indices

def target_market_lookup(companies, market):
    found_companies = [company for company in companies
                        if company["target_markets"] is not None and
                        market in company["target_markets"]]
    found_indices = {company["index"] for company in found_companies}
    return found_indices

def business_model_lookup(companies, model):
    found_companies = []
    for key, value in ACCRONYM_DICT.items():
        if model == value:
            model = key

    for company in companies:
        if company["business_model"] is not None:
            for business_model in company["business_model"]:
                glass = re.sub(r"[^a-zA-Z0-9/]", "", business_model)
                if  re.sub(r"[^a-zA-Z0-9/]", "", model) == glass:
                    found_companies.append(company)
                if "/" in business_model:
                    glass_list = []
                    glass_list.append(glass)
                    untangled_models = untangle(glass_list)
                    if re.sub(r"[^a-zA-Z0-9/]", "", model) in untangled_models:
                        found_companies.append(company)
        
    found_indices = {company["index"] for company in found_companies}
    return found_indices

def revenue_lookup(companies, revenue, less=False, more=False):
    if less and more:
        raise KeyError("Can't lookup both less and more revenue")

    if not less and not more:
        found_companies = [company for company in companies
                            if company["revenue"] is not None and
                            company["revenue"] == revenue]
    elif less and not more:
        found_companies = [company for company in companies
                            if company["revenue"] is not None and
                            company["revenue"] < revenue]
    elif not less and more:
        found_companies = [company for company in companies
                            if company["revenue"] is not None and
                            company["revenue"] > revenue]

    found_indices = {company["index"] for company in found_companies}
    return found_indices

def combine_lookups(*lookup_results):
    if not lookup_results:
        return set()
    
    result = lookup_results[0]
    for lookup_result in lookup_results[1:]:
        result &= lookup_result

    return result

def run_lookup(location=None, outside=False,
                year=None, before=False, after=False,
                employees=None, under=False, over=False,
                target_market=None,
                business_model=None,
                revenue=None, less=False, more=False):
    lookups = []
    if location is not None:
        lookups.append(location_lookup(companies, location, outside=outside))
    if year is not None:
        lookups.append(year_lookup(companies, year, before=before, after=after))
    if employees is not None:
        lookups.append(employee_lookup(companies, employees, under=under, over=over))
    if target_market is not None:
        lookups.append(target_market_lookup(companies, target_market))
    if business_model is not None:
        lookups.append(business_model_lookup(companies, business_model))
    if revenue is not None:
        lookups.append(revenue_lookup(companies, revenue, less=less, more=more))

    if not lookups:
        return sorted(company["index"] for company in companies)

    return sorted(combine_lookups(*lookups))

def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company_name", required=False, type=str)
    parser.add_argument("--location", required=False, type=str, nargs="+")
    parser.add_argument("--outside", required=False, action="store_true")
    parser.add_argument("--before", required=False, action="store_true")
    parser.add_argument("--year", required=False, type=int)
    parser.add_argument("--after", required=False, action="store_true")
    parser.add_argument("--under", required=False, action="store_true")
    parser.add_argument("--employees", required=False, type=int)
    parser.add_argument("--over", required=False, action="store_true")
    parser.add_argument("--target_market", required=False, type=str)
    parser.add_argument("--business_model", required=False, type=str)
    parser.add_argument("--less", required=False, action="store_true")
    parser.add_argument("--revenue", required=False, type=str)
    parser.add_argument("--more", required=False, action="store_true")
    parser.add_argument("--index", required=False, type=int)

    parser.add_argument("--all", required=False, action="store_true")
    parser.add_argument("--all_markets", required=False, action="store_true")
    parser.add_argument("--all_locations", required=False, action="store_true")
    parser.add_argument("--all_employees", required=False, action="store_true")
    parser.add_argument("--all_years", required=False, action="store_true")
    parser.add_argument("--all_business_models", required=False, action="store_true")
    parser.add_argument("--all_revenues", required=False, action="store_true")
    
    args = parser.parse_args()
    lookups = []

    if args.company_name is not None:
        name = str.lower(args.company_name)
        try:
            company = next(
                company for company in companies
                if company["operational_name"] is not None and
                    company["operational_name"].lower() == name
            )
        except KeyError:
            print(f"The dataset doesn't contain the company name {name}.")
        if company is not None:
            pprint.pprint(company)
        print("="*30)

    if args.all:
        args.all_markets = True
        args.all_locations = True
        args.all_years = True
        args.all_revenues = True
        args.all_employees = True
        args.all_business_models = True

    if args.all_markets:
        markets = set()
        for company in companies:
            for market in company["target_markets"]: 
                    markets.add(market)
        with open("all_markets.txt", "w") as f:
            f.write(pprint.pformat(markets))
        print(f"There are {len(markets)} target markets in the dataset.")
        print("="*30)

    if args.all_locations:
        locations = set()
        for company in companies:
            if company["address"]["region_name"] is not None:
                locations.add(company["address"]["region_name"])
            if company["address"]["town"] is not None:
                locations.add(company["address"]["town"])
            if company["address"]["country_code"] is not None:
                for key, value in COUNTRYCODE_DICT.items():
                    if company["address"]["country_code"] == value:
                        locations.add(key)

        with open("all_locations.txt", "w") as f:
            f.write(pprint.pformat(locations))
        print(f"There are {len(locations)} locations in the dataset.")
        print("="*30)

    if args.all_years:
        year_min = sys.maxsize
        year_max = 0
        for company in companies:
            if company["year_founded"] is not None:
                if company["year_founded"] < year_min:
                    year_min = int(company["year_founded"])
                if company["year_founded"] > year_max:
                    year_max = int(company["year_founded"])
        with open("minmax_years.txt", "w") as f:
            f.write(str(year_min) + " " + str(year_max))
        print(f"There are companies are founded from {year_min} to {year_max} in the dataset.")
        print("="*30)

    if args.all_revenues:
        revenue_min = sys.maxsize
        revenue_max = 0
        for company in companies:
            if company["revenue"] is not None:
                if company["revenue"] < revenue_min:
                    revenue_min = int(company["revenue"])
                if company["revenue"] > revenue_max:
                    revenue_max = int(company["revenue"])
        with open("minmax_revenues.txt", "w") as f:
            f.write(str(revenue_min) + " " + str(revenue_max))
        print(f"There are companies have revenues from {revenue_min} to {revenue_max} in the dataset.")
        print("="*30)

    if args.all_employees:
        emp_min = sys.maxsize
        emp_max = 0
        for company in companies:
            if company["employee_count"] is not None:
                if company["employee_count"] < emp_min:
                    emp_min = int(company["employee_count"])
                if company["employee_count"] > emp_max:
                    emp_max = int(company["employee_count"])
        with open("minmax_employees.txt", "w") as f:
            f.write(str(emp_min) + " " + str(emp_max))
        print(f"There are minimum {emp_min} and maximum {emp_max} employees in the dataset.")
        print("="*30)

    if args.all_business_models:
        models = set()
        double_models = set()

        for company in companies:
            for model in company["business_model"]:
                if "/" not in model:  
                    models.add(model)
                else:
                    double_models.add(model)

        untangled_models = untangle(double_models)
        models = models.union(untangled_models)

        with open("all_business_models.txt", "w") as f:
            f.write(pprint.pformat(models))
        print(f"There are {len(models)} business models in the dataset.")
        print("="*30)

    if args.index is not None:
        try:
            company = next(
                company for company in companies
                if company["index"] == args.index
            )
        except KeyError:
            print(f"The dataset doesn't contain the index {args.index}.")
        if company is not None:
            pprint.pprint(company)
        print("="*30)

    if args.location is not None:
        lookups.append(location_lookup(companies, args.location, outside=args.outside))

    if args.year is not None:
        lookups.append(
            year_lookup(
                companies,
                args.year,
                before=args.before,
                after=args.after,
            )
        )

    if args.employees is not None:
        emp_count = args.employees
        lookups.append(
            employee_lookup(
                companies,
                emp_count,
                under=args.under,
                over=args.over,
            )
        )

    if args.target_market is not None:
        market = str.lower(args.target_market)
        lookups.append(target_market_lookup(companies, market))

    if args.business_model is not None:
        model = str.lower(args.business_model)
        lookups.append(business_model_lookup(companies, model))

    if args.revenue is not None:
        revenue = int(args.revenue)
        lookups.append(
            revenue_lookup(
                companies,
                revenue,
                less=args.less,
                more=args.more))

    if lookups != []:
        indices = combine_lookups(*lookups)
        pprint.pprint(sorted(indices))

if __name__ == "__main__":
    run_cli()