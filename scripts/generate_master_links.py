# scripts/generate_master_links.py (CORS 해결을 위한 최종 JSONP 버전)
import os
import json
import random
from urllib.parse import urlparse

NUM_SITE_GROUPS = 5
LINKS_PER_GROUP = 6

site_list_str = os.environ.get('SITE_LIST', '')
info_texts_str = os.environ.get('INFO_TEXTS', '')
site_list = [site.strip() for site in site_list_str.split(',') if site.strip()]
info_texts = [text.strip() for text in info_texts_str.split(',') if text.strip()]

def get_base_domain(url):
    try:
        if not url.startswith('http'): url = 'https://' + url
        hostname = urlparse(url).hostname.replace('www.', '')
        parts = hostname.split('.')
        return '.'.join(parts[-2:]) if len(parts) > 1 else hostname
    except: return url

def pick_max_per_base_domain(max_same, n, full_list):
    res, cnt, shuffled = [], {}, random.sample(full_list, len(full_list))
    for item in shuffled:
        if len(res) >= n: break
        base_domain = get_base_domain(item)
        count = cnt.get(base_domain, 0)
        if count < max_same:
            res.append(item)
            cnt[base_domain] = count + 1
    return res

master_data = {"groups": []}
for _ in range(NUM_SITE_GROUPS):
    selected_sites = pick_max_per_base_domain(2, LINKS_PER_GROUP, site_list)
    random.shuffle(info_texts)
    selected_texts = info_texts[:len(selected_sites)]
    group_links = [{"url": f"https://{site}", "text": selected_texts[i]} for i, site in enumerate(selected_sites)]
    master_data["groups"].append(group_links)

output_dir = 'public'
if not os.path.exists(output_dir): os.makedirs(output_dir)

# 파일 이름을 master_links.js 로 변경합니다.
file_path = os.path.join(output_dir, 'master_links.js')
json_string = json.dumps(master_data, ensure_ascii=False)

# 데이터를 loadFooterLinks(...) 라는 함수 호출 코드로 감쌉니다.
js_content = f"loadFooterLinks({json_string});"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated: {file_path}")
