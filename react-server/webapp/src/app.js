import React from 'react';
import ReactDOM from 'react-dom';

// main app
import App from './components/App';
import Timer from './components/Timer';
import StreamControl from './components/Stream-Control';

ReactDOM.render(<App />, document.getElementById('app'))
ReactDOM.render(<Timer />, document.getElementById('timer'))
ReactDOM.render(<StreamControl />, document.getElementById('stream-control'));