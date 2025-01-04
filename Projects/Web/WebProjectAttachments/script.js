const playBtn = document.getElementById('play');
const audio = document.getElementById('audio');
const musicContainer = document.getElementById('music-container');
const title = document.getElementById('title');

let musicName = audio.src.split('/').pop().replace(/\.[^/.]+$/, '');
title.innerHTML = decodeURIComponent(musicName);

function togglePlayPause() {
  if (audio.paused) {
    playSong();
  } else {
    pauseSong();
  }
}

function playSong() {
  musicContainer.classList.add('play');
  playBtn.querySelector('i.fas').classList.remove('fa-play');
  playBtn.querySelector('i.fas').classList.add('fa-pause');
  audio.play();
}

function pauseSong() {
  musicContainer.classList.remove('play');
  playBtn.querySelector('i.fas').classList.add('fa-play');
  playBtn.querySelector('i.fas').classList.remove('fa-pause');
  audio.pause();
}

playBtn.addEventListener('click', togglePlayPause);
