!function() {
    function detectDevTool(allow) {
    if(isNaN(+allow)) allow = 100;
    app = undefined;
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

Object.defineProperty(console, '_commandLineAPI', { get: function () { throw '콘솔을 사용할 수 없습니다.' } });


// F12키 금지

$(document).ready(function(){

    $(document).on('keydown',function(e){

        if ( e.keyCode == 123) {  /* F12키 */

            e.preventDefault();

            e.returnValue = false;

        }

    });

});



// 마우스오른쪽 클릭방지

document.onmousedown=disableclick;

status="마우스오른쪽 클릭금지.";

function disableclick(event){

    if (event.button==2) {

        alert(status);

        return false;

    }

}
