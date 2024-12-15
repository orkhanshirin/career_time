import json
import os
from career_time.experience import calculate_total_years
from career_time.data_providers import load_sample_data, fetch_talent_data, parse_linkedin_ids

def read_linkedin_urls(file_path: str) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def process_linkedin_ids(linkedin_ids: list[str], sample_data: dict) -> list[dict]:
    results = []
    for _id in linkedin_ids:
        talent_data = fetch_talent_data(_id, sample_data)
        experiences = talent_data.get("member_experience_collection", [])
        total_years = calculate_total_years(experiences)
        results.append({
            "linkedin_id": _id,
            "total_years_of_experience": total_years
        })
    return results

def print_results(results: list[dict]) -> None:
    print(json.dumps(results, indent=4))

def main() -> None:
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    url_file = os.path.join(base_dir, 'data', 'input_urls.txt')
    sample_data_file = os.path.join(base_dir, 'data', 'sample_profile.json')

    linkedin_urls = read_linkedin_urls(url_file)
    linkedin_ids = parse_linkedin_ids(linkedin_urls)

    if not linkedin_ids:
        print("No LinkedIn URLs found. Please provide input in data/input_urls.txt.")
        return

    sample_data = load_sample_data(sample_data_file)
    results = process_linkedin_ids(linkedin_ids, sample_data)
    print_results(results)

if __name__ == "__main__":
    main()
