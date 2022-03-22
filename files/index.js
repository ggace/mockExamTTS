!function() {
    function detectDevTool(allow) {
      if(isNaN(+allow)) allow = 100;
    var start = +new Date();
    debugger;
    var end = +new Date();
    if(isNaN(start) || isNaN(end) || end - start > allow) {
        alert('DEVTOOLS detected. all operations will be terminated.');
      document.write('DEVTOOLS detected.');
    }
  }
  if(window.attachEvent) {
      if (document.readyState === "complete" || document.readyState === "interactive") {
        detectDevTool();
      window.attachEvent('onresize', detectDevTool);
      window.attachEvent('onmousemove', detectDevTool);
      window.attachEvent('onfocus', detectDevTool);
      window.attachEvent('onblur', detectDevTool);
    } else {
        setTimeout(argument.callee, 0);
    }
  } else {
      window.addEventListener('load', detectDevTool);
    window.addEventListener('resize', detectDevTool);
    window.addEventListener('mousemove', detectDevTool);
    window.addEventListener('focus', detectDevTool);
    window.addEventListener('blur', detectDevTool);
  }
}();

Object.defineProperty(console, '_commandLineAPI', { get: function() { throw '콘솔을 사용할 수 없습니다.' } });


// F12키 금지

$(document).ready(function() {

    $(document).on('keydown', function(e) {

        if (e.keyCode == 123) { /* F12키 */

            e.preventDefault();

            e.returnValue = false;

        }

    });

});



// 마우스오른쪽 클릭방지

document.onmousedown = disableclick;

status = "마우스오른쪽 클릭금지.";

function disableclick(event) {

    if (event.button == 2) {

        alert(status);

        return false;

    }

}

/*
this.path = this.getQueryString("path");
        if(this.path == ""){
            this.path = "topic_kor_eng"
        }

        this.playsrcindex = 0;
        var varUA = navigator.userAgent.toLowerCase(); //userAgent 값 얻기

        if ( varUA.indexOf('android') > -1) {
            //안드로이드
            var os = "android";
        } else if ( varUA.indexOf("iphone") > -1||varUA.indexOf("ipad") > -1||varUA.indexOf("ipod") > -1 ) {
            //IOS
            var os =  "ios";
        } else {
            //아이폰, 안드로이드 외
            var os =  "other";
        }
        if(os == "android" || os == "ios"){
            this.isError = false;
        }*/