/*获得btn*/
var btn = document.getElementById('btn')
var spread = document.getElementById('spread')
var iSpread = false
/*高度*/
var height = spread.scrollHeight
/*总时间*/
var time = 420;
/*间隔*/
var interval = 8.4
/*速度*/
var speed = height/(time/interval)
/*点击事件*/
btn.onclick = function (e) {
    btn.disabled = 'disabled'
    if(!iSpread){
        var speeds = 0
        var timer = setInterval(function () {
            speeds += speed
            spread.style.height = speeds + 'px'

            if(parseInt(spread.style.height) >=height){
                clearTimeout(timer)
                btn.disabled = ''
            }
        },interval)
        this.innerHTML = '收起答案'
    }else {
        var speeds = height
        this.innerHTML = '查看答案'
        var timer = setInterval(function () {
            speeds -= speed
            spread.style.height = speeds + 'px'
            if(speeds <= 0){
                clearTimeout(timer)
                btn.disabled = ''
            }
        },interval)
    }
    iSpread = !iSpread
}
