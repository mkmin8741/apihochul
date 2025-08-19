# scripts/generate_master_links.py (가장 단순하고 올바른 최종 버전)
import os, json, random
from urllib.parse import urlparse

NUM_SITE_GROUPS = 5
LINKS_PER_GROUP = 6

site_list = [s.strip() for s in os.environ.get('SITE_LIST', '').split(',') if s.strip()]
info_texts = [t.strip() for t in os.environ.get('INFO_TEXTS', '').split(',') if t.strip()]

def get_base_domain(url):
    try:
        if not url.startswith('http'): url = 'https://' + url
        return '.'.join(urlparse(url).hostname.replace('www.', '').split('.')[-2:])
    except: return url

def pick_links(n, full_list):
    res, cnt = [], {}
    shuffled = random.sample(full_list, len(full_list))
    for item in shuffled:
        if len(res) >= n: break
        base_domain = get_base_domain(item)
        count = cnt.get(base_domain, 0)
        if count < 2:
            res.append(item)
            cnt[base_domain] = count + 1
    return res

master_data = {"groups": []}
for _ in range(NUM_SITE_GROUPS):
    sites = pick_links(LINKS_PER_GROUP, site_list)
    texts = random.sample(info_texts, len(sites))
    group = [{"url": f"https://{sites[i]}", "text": texts[i]} for i in range(len(sites))]
    master_data["groups"].append(group)

# 최상위 경로에 master_links.json 파일 생성
file_path = 'master_links.json'
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print(f"Final data generated at: {file_path}")
