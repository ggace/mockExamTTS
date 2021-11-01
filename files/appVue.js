let app = new Vue({
    el: '#app',
    data: {
        isError : true,
        problems: [18,19,20,21,22,23,24,29,30,31,32,33,34,35,36,37,38,39,40,41,43],
        path: "",
        playsrcindex : 0,
        pw : "",
        isChekced : false,
        message : "",
        speed : '1.0'
    },
    methods: {
        setSpeeds : function(){
            let audios = document.getElementsByTagName("audio")
            for(let i = 0; i< audios.length; i++){
                audios[i].playbackRate = Number(this.speed)
            }
        },
        addSpeed : function(){
            
            if(Number(this.speed) < 2){
                console.log(this.speed)
                this.speed = String( Math.round( (Number(this.speed) + 0.1 ) * 10 )/10 )
            }
            this.setSpeeds()
            
        },
        reduceSpeed : function(){
            console.log(this.speed)
            if(Number(this.speed) > 0.1){
                this.speed = String(Math.round((Number(this.speed) - 0.1) * 10)/10)
            }
            
            this.setSpeeds()
        },
        setClass : function(index){
            let titles = document.getElementsByClassName("title")
            for(let i = 0; i < titles.length; i++){
                if(i == index){
                    titles[i].className = "title text-purple-500 font-bold text-base";
                }
                else{
                    titles[i].className = "title text-blue-500";
                }
            }
            
        },
        loop : function(){
            this.playsrcindex += 1;
            
            setTimeout(function(){document.getElementById("loop").play();}, 1500);
        },
        setPath : function(path){
            this.path = path;
        },
        checkPw : function(){
            if(this.pw == "system"){
                this.isChekced = true;
                
            }
            else {
                this.message = "wrong pw"
            }
        },
        getQueryString: function (key) {

            // 전체 Url을 가져온다.
            var str = location.href;
        
            // QueryString의 값을 가져오기 위해서, ? 이후 첫번째 index값을 가져온다.
            var index = str.indexOf("?") + 1;
        
            // Url에 #이 포함되어 있을 수 있으므로 경우의 수를 나눴다.
            var lastIndex = str.indexOf("#") > -1 ? str.indexOf("#") + 1 : str.length;
        
            // index 값이 0이라는 것은 QueryString이 없다는 것을 의미하기에 종료
            if (index == 0) {
                return "";
            }
        
            // str의 값은 a=1&b=first&c=true
            str = str.substring(index, lastIndex); 
        
            // key/value로 이뤄진 쌍을 배열로 나눠서 넣는다.
            str = str.split("&");
        
            // 결과값
            var rst = "";
        
            for (var i = 0; i < str.length; i++) {
        
                // key/value로 나눈다.
                // arr[0] = key
                // arr[1] = value
                var arr = str[i].split("=");
        
                // arr의 length가 2가 아니면 종료
                if (arr.length != 2) {
                    break;
                }
        
                // 매개변수 key과 일치하면 결과값에 셋팅
                if (arr[0] == key) {
                    rst = arr[1];
                    break;
                }
            }
            return rst;
        }
    },
    created: function () {
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
        }
        
    }
});