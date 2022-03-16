class Audio extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        
        let src = "https://ggace.github.io/mockExamTTS/output/" + this.props.year + "/" + this.props.type + "/" + this.props.year + "_" + this.props.problem + "_" + this.props.type + ".mp3";
        
        return <audio controls src={src} id="audio" onEnded={this.end.bind(this)}></audio>
    }

    end() {
        if(setting.showingTypeIndex == 0){
            document.getElementById("audio").play();
        }
        else if(setting.showingTypeIndex == 1){
            setting.problemIndex = (setting.problemIndex+1)% this.props.problems.length;
            document.getElementById("audio").src= "https://ggace.github.io/mockExamTTS/output/" + this.props.year + "/" + this.props.type + "/" + this.props.year + "_" + this.props.problems[setting.problemIndex] + "_" + this.props.type + ".mp3";
            document.getElementById("audio").play();
        }
        else if(setting.showingTypeIndex == 2){
            setting.problemIndex = (setting.problemIndex+1);
            if(setting.problemIndex < this.props.problems.length){
                document.getElementById("audio").src= "https://ggace.github.io/mockExamTTS/output/" + this.props.year + "/" + this.props.type + "/" + this.props.year + "_" + this.props.problems[setting.problemIndex] + "_" + this.props.type + ".mp3";
                document.getElementById("audio").play();
            }
            
        }
    }
    
}