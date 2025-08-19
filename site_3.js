
(function() {
    var links = [{"url": "https://gwanak.lulucast.com", "text": "이슈분석"}, {"url": "https://songpa.lulucast.com", "text": "핵심정보"}, {"url": "https://living.benefitview.co.kr", "text": "알아보기"}, {"url": "https://laiis.go.kr", "text": "숨겨진팁"}, {"url": "https://korea.kr", "text": "완전정복"}, {"url": "https://youtube.com", "text": "알아두면좋은것"}];
    var targetDivId = 'dynamic-link-container-3';
    var target = document.getElementById(targetDivId);
    if (target && links && links.length > 0) {
        target.innerHTML = links.map(function(l) {
            return '<a href="' + l.url + '" target="_blank">' + l.text + '</a>';
        }).join(' | ');
    }
})();
