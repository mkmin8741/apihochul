# scripts/generate_master_links.py (진짜 최종 버전)
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
    res, cnt, shuffled = [], {}, random.sample(full_list, len(full_list))
    for item in shuffled:
        if len(res) >= n: break
        base_domain = get_base_domain(item)
        count = cnt.get(base_domain, 0)
        if count < 2:
            res.append(item)
            cnt[base_domain] = count + 1
    return res

output_dir = 'public'
if not os.path.exists(output_dir): os.makedirs(output_dir)

# 5개의 각기 다른 .js 파일을 생성
for i in range(NUM_SITE_GROUPS):
    sites = pick_links(LINKS_PER_GROUP, site_list)
    texts = random.sample(info_texts, len(sites))
    links_data = [{"url": f"https://{sites[j]}", "text": texts[j]} for j in range(len(sites))]
    
    # 각 .js 파일에 들어갈 내용
    js_content = f"""
(function() {{
    var links = {json.dumps(links_data, ensure_ascii=False)};
    var targetDivId = 'dynamic-link-container-{i}';
    var target = document.getElementById(targetDivId);
    if (target && links && links.length > 0) {{
        target.innerHTML = links.map(function(l) {{
            return '<a href="' + l.url + '" target="_blank">' + l.text + '</a>';
        }}).join(' | ');
    }}
}})();
"""
    
    file_path = os.path.join(output_dir, f'site_{i}.js') # site_0.js, site_1.js ...
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Generated script for Site {i} at {file_path}")

