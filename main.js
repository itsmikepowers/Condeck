const { app, BrowserWindow, ipcMain } = require('electron');
const { exec } = require('child_process');
const fs = require('fs');

function createWindow () {
  const win = new BrowserWindow({
    width: 1200,  // adjust width and height as per your requirement
    height: 1200,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true,
    }
  })

  win.loadFile('index.html')
}

app.whenReady().then(createWindow)

ipcMain.on('run-python-script', (event, script, textInput) => {
  exec(`python ${script} "${textInput}"`, (error, stdout, stderr) => {
    event.reply('python-script-done');
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
});

ipcMain.on('delete-video', (event, filePath) => {
  fs.unlink(filePath, (err) => {
    if (err) {
      console.error(`error deleting file: ${err}`);
    } else {
      console.log('file deleted');
    }
  });
});
