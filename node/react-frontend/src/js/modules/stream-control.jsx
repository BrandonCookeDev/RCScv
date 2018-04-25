import React from 'react';
import axios from 'axios'

const JSON_PATH = '';
const API_URL = '';
const UPDATE_JSON_URL = API_URL + '/';
const READ_JSON_URL = API_URL + '/';

export default class StreamControl extends React.Component{

    constructor(props){
        super(props);

        this.state = {
            p1_name: '',
            p1_games: 0,
            p1_char: '',
            p1_sponsor: '',
            p2_name: '',
            p2_games: 0,
            p2_char: '',
            p2_sponsor: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.updateState  = this.updateState.bind(this);
        this.readFromFile = this.readFromFile.bind(this);
        this.writeToFile  = this.writeToFile.bind(this);
    }


    handleChange(e){
        this.setState({value: e.target.value});
    }

    handleSubmit(){
        let postParams = this.state;
        axios.post()
    }

    updateState(json){
        this.state = json;
    }

    readFromFile(){
        //Call json file for reading
        axios.get(JSON_PATH)
            .then(r => r.json)
            .then(json => {
                this.updateStateFromJSON(json);
            })
            .catch(console.error);
    }

    writeToFile(){
        let oldState = this.state;

        //Call server to update file
        axios.post(UPDATE_JSON_URL, postParams)
            .then(status => {
                if(!status == 200){
                    console.error('Got non 200 back from write operation: ' + status);
                }
            })
            .catch(console.error);
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
