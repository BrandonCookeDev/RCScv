'use strict';

let express = require('express');
let router = express.Router();

const JSON_PATH = '../resources/test.json';

let StreamControl = require('./StreamControl');
let sc = new StreamControl(JSON_PATH);

function routes(){
    router.route('/streamcontrol/write').post(sc.write);
    router.route('/streamcontrol/read').get(sc.read);
    return router;
}

module.exports = routes;