
(function() {
    var links = [{"url": "https://gwanak.lulucast.com", "text": "스마트라이프"}, {"url": "https://bupyeong.lulucast.com", "text": "지원금신청"}, {"url": "https://lawstery.com", "text": "궁금한이야기"}, {"url": "https://youtube.com", "text": "알아두면좋은것"}, {"url": "https://weddingheal.com", "text": "신청하기"}, {"url": "https://support-run.com", "text": "최신업데이트"}];
    var targetDivId = 'dynamic-link-container-1';
    var target = document.getElementById(targetDivId);
    if (target && links && links.length > 0) {
        target.innerHTML = links.map(function(l) {
            return '<a href="' + l.url + '" target="_blank">' + l.text + '</a>';
        }).join(' | ');
    }
})();
