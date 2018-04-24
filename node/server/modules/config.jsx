import React from '../../node_modules/react/dist/react';
import ReactDOM from '../../node_modules/react/lib/ReactDOM'

export default class Config extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            p1_name: '',
            p1_games: 0,
            p2_name: '',
            p2_games: 0
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(e){
        this.setState({value: e.target.value});
    }

    handleSubmit(){

    }

    render(){
        return(
            <div>
                <form onSubmit={this.handleSubmit}>
                    <div class='row'>
                        <div class='col-md-6'>
                            <label>Player1:</label> 
                            <input type="text" name="p1_name" placeholder="tag" 
                                onChange={this.handleChange} value={this.state.p1_name}/>
                            <br/>
                            <label>Score: </label>
                            <input type="number" name="p1_games" 
                                onChange={this.handleChange} value={this.state.p1_games} />
                        </div>
                        <div class='col-md-6'>
                            <label>Player2:</label>
                            <input type="text" name="p2_name" placeholder="tag" 
                                onChange={this.handleChange} value={this.state.p2_name} />
                            <br/>
                            <label>Score: </label>
                            <input type="number" name="p2_games" 
                                onChange={this.handleChange}  value={this.state.p2_games} />
                        </div>
                    </div>
                </form>
            </div>
        )
    }

}

ReactDOM.render(<Config />, document.getElementById('config'));