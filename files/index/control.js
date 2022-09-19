class Controller extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            korVisibleState : true
        };
    }

    render() {
        
        let element = this.props.problems.map((problem) => {
            return <option value={problem}>{problem}</option>
        });

        let yearsElement = this.props.years.map((year)=> {           
            return <option value={year}>{year}</option>
        })

        return (<div className="flex" id="controller">
                <select name="year" id="yearSelect" autoFocus="20" onChange={this.yearChange.bind(this)}>
                    <option disabled selected>연도</option>
                    {yearsElement}
                </select>

                <select name="problem" id="problemSelect" autoFocus="20" onChange={this.problemChange.bind(this)}>
                    <option disabled selected>문제</option>
                    {element}
                </select>

                <button onClick={this.showingtypeChange.bind(this)} id="showingType">{showingType[setting.showingTypeIndex][1]}</button>
                <span id="flex-grow"></span>
                
                <button onClick={this.speedDown.bind(this)} id="speedController_reduce">-</button>
                <span id="speed">{setting.speed}</span>
                <button onClick={this.speedUp.bind(this)} id="speedController_add">+</button>

                <button onClick={this.hideKor.bind(this)} id="hide_kor">hide kor</button>
        </div>)
    }

    hideKor(){
        let ele = document.getElementsByClassName("kor")
        if(this.state.korVisibleState){
            for(let i = 0; i < ele.length; i++){
                ele[i].style.color = "white"
            }
        }
        else{
            for(let i = 0; i < ele.length; i++){
                ele[i].style.color = "black"
            }
        }
        
    }

    yearChange(){
        setting.yearIndex = (document.getElementById("yearSelect").selectedIndex-1)% this.props.problems.length;
        document.getElementById("audio").src= "https://ggace.github.io/mockExamTTS/output/" + years[setting.yearIndex] + "/" + setting.type + "/" + years[setting.yearIndex] + "_" + this.props.problems[setting.problemIndex] + "_" + this.props.type + ".mp3";
        document.cookie = "yearIndex=" + setting.yearIndex
        changeContent();
    }

    problemChange(){
        setting.problemIndex = (document.getElementById("problemSelect").selectedIndex-1)% this.props.problems.length;
        document.getElementById("audio").src= "https://ggace.github.io/mockExamTTS/output/" + years[setting.yearIndex] + "/" + setting.type + "/" + years[setting.yearIndex] + "_" + this.props.problems[setting.problemIndex] + "_" + this.props.type + ".mp3";
        document.cookie = "problemIndex=" + setting.problemIndex
        changeContent();
    }

    showingtypeChange(){
        setting.showingTypeIndex = (setting.showingTypeIndex+1) % showingType.length
        document.getElementById("showingType").innerText  = showingType[setting.showingTypeIndex][1]
    }

    speedUp(){
        setting.speed += 0.1
        document.getElementById("audio").playbackRate = setting.speed;
        document.getElementById("speed").innerText = setting.speed.toFixed(1);
    }

    speedDown(){
        setting.speed -= 0.1
        document.getElementById("audio").playbackRate = setting.speed;
        document.getElementById("speed").innerText = setting.speed.toFixed(1);
    }
}