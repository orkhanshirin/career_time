def parse_linkedin_id(url: str) -> str:
    parts = url.strip('/').split('/')
    return parts[-1] if parts else ""

def parse_linkedin_ids(urls: list[str]) -> list[str]:
    return [parse_linkedin_id(url) for url in urls if url.strip()]
