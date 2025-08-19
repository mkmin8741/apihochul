
(function() {
    var links = [{"url": "https://changwon.lulucast.com", "text": "카드혜택"}, {"url": "https://korea.kr", "text": "재테크비법"}, {"url": "https://bucheon.lulucast.com", "text": "현명한선택"}, {"url": "https://signvalue.co.kr", "text": "일상노하우"}, {"url": "https://support-run.com", "text": "스마트라이프"}, {"url": "https://weddingheal.com", "text": "생활꿀팁"}];
    var targetDivId = 'dynamic-link-container-0';
    var target = document.getElementById(targetDivId);
    if (target && links && links.length > 0) {
        target.innerHTML = links.map(function(l) {
            return '<a href="' + l.url + '" target="_blank">' + l.text + '</a>';
        }).join(' | ');
    }
})();
