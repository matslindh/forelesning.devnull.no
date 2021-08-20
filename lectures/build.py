import os
import json
from utils import youtube_url_to_id
from jinja2 import Environment, PackageLoader, select_autoescape

current_dir = os.path.dirname(__file__)
build_dir = os.path.join(current_dir, '../build')
configuration_path = os.path.join(current_dir, '../site.json')
configuration = json.load(open(configuration_path, 'rb'))

template_env = Environment(
    loader=PackageLoader('lectures', 'templates'),
    autoescape=select_autoescape()
)

template_env.filters['youtube_url_to_id'] = youtube_url_to_id

os.makedirs(build_dir, mode=0o600, exist_ok=True)
output_file = os.path.join(build_dir, 'index.html')

with open(output_file, 'wb') as f:
    f.write(
        template_env.get_template('index.html').render(
            **configuration
        ).encode('utf-8')
    )

