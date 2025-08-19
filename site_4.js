
(function() {
    var links = [{"url": "https://yeonsu.lulucast.com", "text": "바로가기"}, {"url": "https://flowrapid.com", "text": "경제트렌드"}, {"url": "https://gangnam.lulucast.com", "text": "정보센터"}, {"url": "https://laiis.go.kr", "text": "다이어트비법"}, {"url": "https://lawstery.com", "text": "궁금한이야기"}, {"url": "https://korea.kr", "text": "실시간정보"}];
    var targetDivId = 'dynamic-link-container-4';
    var target = document.getElementById(targetDivId);
    if (target && links && links.length > 0) {
        target.innerHTML = links.map(function(l) {
            return '<a href="' + l.url + '" target="_blank">' + l.text + '</a>';
        }).join(' | ');
    }
})();
