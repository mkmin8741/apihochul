import os
import json
import random
from urllib.parse import urlparse

# --- 설정 값 ---
NUM_SITE_GROUPS = 5  # 데이터를 생성할 사이트 그룹 수 (우리의 경우 5개)
LINKS_PER_GROUP = 6  # 각 그룹(사이트)에 할당할 링크 수

# --- Secrets에서 데이터 읽어오기 ---
site_list_str = os.environ.get('SITE_LIST', '')
info_texts_str = os.environ.get('INFO_TEXTS', '')

site_list = [site.strip() for site in site_list_str.split(',') if site.strip()]
info_texts = [text.strip() for text in info_texts_str.split(',') if text.strip()]

# --- 기존 로직을 Python으로 구현 ---
def get_base_domain(url):
    try:
        if not url.startswith('http'):
            url = 'https://' + url
        hostname = urlparse(url).hostname.replace('www.', '')
        parts = hostname.split('.')
        return '.'.join(parts[-2:]) if len(parts) > 1 else hostname
    except:
        return url

def pick_max_per_base_domain(max_same, n, full_list):
    res = []
    cnt = {}
    shuffled = random.sample(full_list, len(full_list))
    for item in shuffled:
        if len(res) >= n:
            break
        base_domain = get_base_domain(item)
        count = cnt.get(base_domain, 0)
        if count < max_same:
            res.append(item)
            cnt[base_domain] = count + 1
    return res

# --- 5개 그룹을 위한 마스터 데이터 생성 ---
master_data = {"groups": []}
for _ in range(NUM_SITE_GROUPS):
    selected_sites = pick_max_per_base_domain(2, LINKS_PER_GROUP, site_list)
    random.shuffle(info_texts)
    selected_texts = info_texts[:len(selected_sites)]
    
    group_links = []
    for i, site in enumerate(selected_sites):
        group_links.append({
            "url": f"https://{site}",
            "text": selected_texts[i]
        })
    master_data["groups"].append(group_links)

# --- master_links.json 파일로 저장 ---
# 이 파일이 GitHub Pages에 배포됩니다.
with open('master_links.json', 'w', encoding='utf-8') as f:
    json.dump(master_data, f, ensure_ascii=False, indent=2)

print("master_links.json for 5 groups generated successfully.")
