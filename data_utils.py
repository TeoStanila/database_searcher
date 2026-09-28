import json
from lookup import companies, COUNTRYCODE_DICT

CODE_TO_COUNTRY = {}
for name, code in COUNTRYCODE_DICT.items():
    CODE_TO_COUNTRY.setdefault(code, name)

def to_text(company):
    parts = [company["operational_name"]] if company.get("operational_name") else []

    address = company.get("address") or {}
    if isinstance(address, str):
        try:
            address = json.loads(address)
        except (json.JSONDecodeError, TypeError):
            address = {}
    country_code = address.get("country_code")
    country_name = CODE_TO_COUNTRY.get(country_code, country_code)
    location_bits = [address.get("town"), address.get("region_name"), country_name]
    location_bits = [bit for bit in dict.fromkeys(location_bits) if bit]
    if location_bits:
        parts.append("Located in " + ", ".join(location_bits) + ".")

    if company.get("year_founded"):
        parts.append(f"Founded in {int(company['year_founded'])}.")
    if company.get("employee_count"):
        parts.append(f"Has about {int(company['employee_count'])} employees.")
    if company.get("revenue"):
        parts.append(f"Reports revenue of about {int(company['revenue'])}.")

    if company.get("business_model"):
        parts.append("Business model: " + ", ".join(company["business_model"]) + ".")
    if company.get("target_markets"):
        parts.append("Target markets: " + ", ".join(company["target_markets"]) + ".")
    if company.get("core_offerings"):
        parts.append("Offerings include " + ", ".join(company["core_offerings"][:6]) + ".")

    if company.get("description"):
        parts.append(company["description"])

    parts = [str(part) for part in parts if part is not None]
    return " ".join(parts)

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows