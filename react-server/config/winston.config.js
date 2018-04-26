'use strict';

let fs = require('fs');
let path = require('path');

let log = require('winston');
log.remove(log.transports.Console);

log.add(log.transports.Console, {
    level: 'debug',
    colorize: true,
    json: false,
});
log.add(log.transports.File, {
    filename: path.join(__dirname, '..', 'log', 'RCScv-frontend.log'),
    level: 'info',
    colorize: false,
    json: false,
    timestamp: true
});
