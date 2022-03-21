class Header extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {

        let elements = this.props.types.map((type, index) =>{
            let style = {fontSize: '15px', color: "black"}
            if(setting.type == type){
                style = {fontSize: "20px", color: "purple"}
            }
            return <button onClick={this.onclickHeader.bind(this, index)} style={style} className="headerType">{type}</button>
        })

        return (<div>
            <h1 style={{textAlign: 'center'}}>{this.props.year}년 3월</h1>
            <div style={{display: "flex", justifyContent: "space-around"}}>{elements}</div>
        </div>)
    }

    onclickHeader(index) { 
        let headerButtons = document.getElementsByClassName("headerType");
        
        for(let i = 0; i < headerButtons.length; i++){
            if(i == index){
                headerButtons[i].style.fontSize = "20px"
                headerButtons[i].style.color = "purple"
                setting.type = headerButtons[i].innerText
                document.cookie = "type=" + headerButtons[i].innerText
                document.getElementById("audio").src= "https://ggace.github.io/mockExamTTS/output/" + this.props.year + "/" + setting.type + "/" + this.props.year + "_" + this.props.problems[setting.problemIndex] + "_" + setting.type + ".mp3";
            }
            else{
                headerButtons[i].style.fontSize = "15px"
                headerButtons[i].style.color = "black"
            }
        }
    }
}