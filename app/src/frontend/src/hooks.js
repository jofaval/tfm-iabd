#! /usr/bin/env node

const { exec } = require('child_process');
const fs = require('fs');

const executeCommand = (command) => {
    exec(command, (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(`echo global error while removing the hooks`, err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        // console.log(`echo stdout: ${stdout}`);
        // console.log(`echo stderr: ${stderr}`);
    });
};

const getCommandName = () => {
    let command = '';

    switch (process.platform) {
        case 'win32':
            command = `rmdir /s /q`
            break;

        default:
            command = 'rm -rf';
            break;
    }

    return command;
}

const init = () => {
    const command = getCommandName();
    const basepath = '../../../..';
    const hooksFilename = '.git/hooks/';

    // https://flaviocopes.com/how-to-check-if-file-exists-node/
    fs.access([basepath, hooksFilename].join('/'), fs.F_OK, (err) => {
        if (err) {
            // console.error(err)
            console.log('The hooks have already been deleted, or couldn\'t be found');
            return;
        }

        //file exists
        executeCommand(`cd ${basepath} && ${command} "./${hooksFilename}"`);
    });
};
init();