class Controller extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        
        let element = this.props.problems.map((problem) => {
            return <option value={problem}>{problem}</option>
        });

        return (<div className="flex" id="controller">
                            
                <select name="problem" id="problemSelect" autoFocus="20" onChange={this.problemChange.bind(this)}>
                    <option disabled selected>문제</option>
                    {element}
                </select>

                <button onClick={this.showingtypeChange.bind(this)} id="showingType">{showingType[setting.showingTypeIndex][1]}</button>
                <span id="flex-grow"></span>
                
                <button onClick={this.speedDown.bind(this)} id="speedController_reduce">-</button>
                <span id="speed">{setting.speed}</span>
                <button onClick={this.speedUp.bind(this)} id="speedController_add">+</button>
        </div>)
    }

    problemChange(){
        setting.problemIndex = (document.getElementById("problemSelect").selectedIndex-1)% this.props.problems.length;
        document.getElementById("audio").src= "https://ggace.github.io/mockExamTTS/output/" + this.props.year + "/" + setting.type + "/" + this.props.year + "_" + this.props.problems[setting.problemIndex] + "_" + this.props.type + ".mp3";
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