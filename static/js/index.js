var phoneWidth =  parseInt(window.screen.width);
var phoneScale = phoneWidth/640;
var ua = navigator.userAgent;
if (/Android (\d+\.\d+)/.test(ua)){
    var version = parseFloat(RegExp.$1);
    if(version>2.3){
        document.write('<meta name="viewport" content="width=640, minimum-scale = '+phoneScale+', maximum-scale = '+phoneScale+', target-densitydpi=device-dpi">');
    }else{
        document.write('<meta name="viewport" content="width=640, target-densitydpi=device-dpi">');
    }
} else {
    document.write('<meta name="viewport" content="width=640, user-scalable=no, target-densitydpi=device-dpi">');
}

window.onload = function(){
   //浏览器窗口缩放时，自动缩放iframe
   $(window).resize(function() {
      var ifm= document.getElementById("luke");
      var subWeb = document.frames ? document.frames["luke"].document : ifm.contentDocument;
      if(ifm != null && subWeb != null) {
         ifm.width = "100%";
      }
   });
}

function defaulIframePageHeight() {
var ifm = document.getElementById("defaulIframePage");
var subWeb = document.frames ? document.frames["defaulIframePage"].document : ifm.contentDocument;
if (ifm != null && subWeb != null) {
ifm.height = subWeb.body.scrollHeight;
}
}