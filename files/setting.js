const LOOP_ONE = [10001, '1']
const LOOP_ALL = [10002, 'A*']
const ONCE_All = [10003, 'A->']

var showingType = [LOOP_ONE, LOOP_ALL, ONCE_All]

var cookie = {}

if(document.cookie != null){
    document.cookie.split("; ").map((value)=>{
        cookie[value.split("=")[0]] = value.split("=")[1]
    })
}

var setting = {
    type: cookie['type']!=null&& cookie['type']!=""?cookie['type']:0,
    yearIndex: 0,
    problemIndex: cookie['problemIndex']!=null&& cookie['problemIndex']!=""?cookie['problemIndex']:0,
    showingTypeIndex: 0,
    speed: 1.0
}