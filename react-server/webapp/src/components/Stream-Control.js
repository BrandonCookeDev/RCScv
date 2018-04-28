import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import { Button, Grid, Row, Col } from 'react-bootstrap';

const JSON_PATH = '../../../../resources/test.json'; // todo change
const API_URL = 'http://localhost:8080';
const WRITE_JSON_URL = API_URL + '/streamcontrol/write';
const READ_JSON_URL = API_URL + '/streamcontrol/read';

const characters = [
    "Sheik",
    "Falco",
    "Fox"
]

export default class StreamControl extends React.Component{

    constructor(props){ 
        super(props);

        this.state = {
            p1_name: '',
            p1_games: 0,
            p1_char: '',
            p2_name: '',
            p2_games: 0,
            p2_char: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.updateState  = this.updateState.bind(this);
        this.readFromFile = this.readFromFile.bind(this);
        this.writeToFile  = this.writeToFile.bind(this);
    }


    handleChange(e){
        let newState = this.state;
        newState[e.target.name] = e.target.value;
        this.setState(newState);
    }

    handleSubmit(){
        let postParams = this.state;
        this.writeToFile();
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
        //Call server to update file
        axios.post(WRITE_JSON_URL, this.state)
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
                    <Grid>
                        <Row className="showGrid">
                            <Col md={6} sm={12}>
                                <table>
                                    <tr>
                                        <td><label>Player1:</label> </td>
                                        <td>
                                            <input type="text" name="p1_name" placeholder="tag" 
                                                onChange={this.handleChange} value={this.state.p1_name}/>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><label>Score: </label></td>
                                        <td>
                                            <input type="number" name="p1_games" 
                                                onChange={this.handleChange} value={this.state.p1_games} />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><label>Character: </label></td>
                                        <td> 
                                            <select name='p1_char' id='p1_char' 
                                                value={this.state.p1_char} onChange={this.handleChange}>
                                                {
                                                    characters.map(character => {
                                                        return <option>{character}</option>
                                                    })
                                                }
                                            </select>
                                        </td>
                                    </tr>
                                </table>
                            </Col>
                            <Col md={6} sm={12}>
                                <table>
                                    <tr>
                                        <td><label>Player2:</label></td>
                                        <td>
                                            <input type="text" name="p2_name" placeholder="tag" 
                                                onChange={this.handleChange} value={this.state.p2_name} />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><label>Score: </label></td>
                                        <td>
                                            <input type="number" name="p2_games" 
                                                onChange={this.handleChange}  value={this.state.p2_games} />
                                        </td>
                                    </tr>
                                    <tr>
                                        <td><label>Character: </label></td>
                                        <td>
                                            <select name='p2_char' id='p2_char' 
                                                value={this.state.p2_char} onChange={this.handleChange}>
                                                {
                                                    characters.map(character => {
                                                        return <option>{character}</option>
                                                    })
                                                }
                                            </select>
                                        </td>
                                    </tr>
                                </table> 
                            </Col>
                            <input type='submit' value='submit' />
                        </Row>
                    </Grid>
                </form>
            </div>
        )
    }
}
