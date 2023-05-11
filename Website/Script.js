var ctx = document.getElementById('myChart');

var points = [2100, 2132, 2147, 2130, 2113, 2128, 2100, 2075, 2093, 2077, 2061, 2077, 2141, 2154, 2170, 2174];
var matchIds = ['0', 'EUW1_5277021446', 'EUW1_5277037103', 'EUW1_5277181730', 'EUW1_5277157717', 'EUW1_5278992518', 'EUW1_5283899374', 'EUW1_5285873929', 'EUW1_5293043461', 'EUW1_5296587040', 'EUW1_5296682403', 'EUW1_5296697697', 'EUW1_5303303675', 'EUW1_5307309095', 'EUW1_5307484532', 'EUW1_5310515532']

console.log(points);

var myChart = new Chart(ctx, {
 type: 'line',
 data: {
    labels: matchIds,
    datasets: [{
        label: 'Points',
        data: points
    }]
 },
})