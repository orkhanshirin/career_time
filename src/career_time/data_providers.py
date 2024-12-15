import os
import json

def load_sample_data(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Data file not found at: {file_path}")

    with open(file_path, 'r') as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Wrong format.")

    return data

def fetch_talent_data(linkedin_id: str, data: dict) -> dict:
    if linkedin_id == data.get("member_shorthand_name"):
        return data
    return {}

def parse_linkedin_id(url: str) -> str:
    parts = url.strip('/').split('/')
    return parts[-1] if parts else ""

def parse_linkedin_ids(urls: list[str]) -> list[str]:
    return [parse_linkedin_id(url) for url in urls if url.strip()]