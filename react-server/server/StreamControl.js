'use strict';

let fs = require('fs');
let path = require('path');

let _ = require('lodash');
let log = require('winston');

class StreamControl{

    constructor(path){
        this.path = path;

        this.testPath = this.testPath.bind(this);
        this.readFromJSON = this.readFromJSON.bind(this);
        this.writeToJSON = this.writeToJSON.bind(this);
        this.read = this.read.bind(this);
        this.write = this.write.bind(this);

        log.info('JSON located at: %s', this.path);
    }

    testPath(){
        try{    
            log.verbose('testing file existence');
            let exists = fs.existsSync(this.path);
            log.debug('file existence: %s', exists);
            return exists;
        } catch(e){
            log.error(e);
            throw e;
        }
    }

    readFromJSON(){
        try{
            log.verbose('reading from JSON');
            if(this.testPath()){
                let json = JSON.parse(fs.readFileSync(this.path).toString('utf8'));
                log.debug('Read JSON:', json);
                return json;
            }
        } catch(e){
            log.error(e);
            throw e;
        }
    }

    writeToJSON(newJSON){
        try{
            log.verbose('New JSON input:', newJSON);
            if(this.testPath()){
                let json = this.readFromJSON();
                _.assign(json, newJSON);
                log.debug('Meged JSON:', json)
                fs.writeFileSync(this.path, JSON.stringify(json));
                log.debug('successfully wrote to JSON')
            }
        } catch(e){
            log.error(e);
            throw e;
        }
    }

    write(req, res){
        try{
            if(!this.testPath)
                return req.sendStatus(404);

            this.writeToJSON(req.body);
            res.sendStatus(200);
        } catch(e){
            log.error(e);
            res.sendStatus(500);
        }
    }

    read(req, res){
        try{
            if(!this.testPath)
                return req.sendStatus(404);

            let data = this.readFromJSON();
            res.send(data).status(200);
        } catch(e){
            log.error(e);
            res.sendStatus(500);
        }
    }
}

module.exports = StreamControl;