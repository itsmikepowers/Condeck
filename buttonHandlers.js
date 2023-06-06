window.onload = function() {
  const video = document.getElementById('videoPlayer');
  const videoSource = document.getElementById('videoSource');
  const loading = document.getElementById('loading');
  const textInput = document.getElementById('textInput');
  const audio = document.querySelector('audio');
  const audioSource = document.querySelector('audio source');

  const { ipcRenderer } = require('electron');

  function refreshVideo() {
    const timestamp = new Date().getTime();
    const videoSourceOldSrc = videoSource.src.split('?')[0]; // remove old query string if there is one
    videoSource.src = `${videoSourceOldSrc}?timestamp=${timestamp}`;
    video.load();
    video.play();
  }

  function refreshAudio() {
    const timestamp = new Date().getTime();
    const audioSourceOldSrc = audioSource.src.split('?')[0]; // remove old query string if there is one
    audioSource.src = `${audioSourceOldSrc}?timestamp=${timestamp}`;
    audio.load();
  }

  document.getElementById('newAudio').addEventListener('click', () => {
    const text = textInput.value;
    loading.style.display = "block";
    ipcRenderer.send('run-python-script', './Scripts/NewAudio.py', text);
  });

  document.getElementById('cutVideo').addEventListener('click', () => {
    loading.style.display = "block";
    ipcRenderer.send('run-python-script', './Scripts/CutVideo.py');
  });

  document.getElementById('blackWhite').addEventListener('click', () => {
    loading.style.display = "block";
    ipcRenderer.send('run-python-script', './Scripts/BlackWhite.py');
  });

  document.getElementById('addCaptions').addEventListener('click', () => {
    loading.style.display = "block";
    ipcRenderer.send('run-python-script', './Scripts/AddCaptions.py');
  });

  document.getElementById('addMusic').addEventListener('click', () => {
    loading.style.display = "block";
    ipcRenderer.send('run-python-script', './Scripts/AddMusic.py');
  });
  
  document.getElementById('saveVideo').addEventListener('click', () => {
    const videoName = document.getElementById('videoNameInput').value;
    loading.style.display = "block";
    ipcRenderer.send('run-python-script', './Scripts/SaveVideo.py', videoName);
  });


  document.getElementById('refreshVideo').addEventListener('click', refreshVideo);

  document.getElementById('deleteVideo').addEventListener('click', () => {
    ipcRenderer.send('delete-video', './final_video.mp4');
    ipcRenderer.send('delete-video', './transcript.json');
    ipcRenderer.send('delete-video', './audio.mp3');
    ipcRenderer.send('delete-video', './audio.wav');
  });

  ipcRenderer.on('python-script-done', () => {
    loading.style.display = "none";
    refreshVideo();
    refreshAudio();
  });

  video.play();
};
