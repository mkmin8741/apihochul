
(function() {
    var links = [{"url": "https://cheongju.lulucast.com", "text": "흥미로운사실"}, {"url": "https://changwon.lulucast.com", "text": "건강가이드"}, {"url": "https://gody.co.kr", "text": "살림정보"}, {"url": "https://living.benefitview.co.kr", "text": "대출정보"}, {"url": "https://korea.kr", "text": "핵심정보"}, {"url": "https://wellnesshub.kr", "text": "다이어트비법"}];
    var targetDivId = 'dynamic-link-container-2';
    var target = document.getElementById(targetDivId);
    if (target && links && links.length > 0) {
        target.innerHTML = links.map(function(l) {
            return '<a href="' + l.url + '" target="_blank">' + l.text + '</a>';
        }).join(' | ');
    }
})();
