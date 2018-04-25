'use strict';
require('dotenv').config();

let fs = require('fs');
let path = require('path');
let routes = require('./server/Endpoints');

let express = require('express');
let bp = require('body-parser');
let gzip = require('compression');

let server = express();
server.use(bp.json())
server.use(bp.urlencoded());
server.use(gzip());
server.use(routes());
server.use(express.static('webapp'));

server.listen(8080, function(){
    console.log('Listening on 8080');
});