from urllib.parse import urlparse, parse_qs


def youtube_url_to_id(url: str):
    parsed_url = urlparse(url)

    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path.strip('/')

    params = parse_qs(parsed_url.query)

    if 'v' not in params:
        return None

    return params['v'][0]