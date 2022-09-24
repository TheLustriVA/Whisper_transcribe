#!/bin/bash

echo "Checking for ffmpeg installation:"

if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found."
    echo "Installing ffmpeg from Github."
    git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
fi

echo "Checking for Python installation:"

if ! [ command -v python3 &> /dev/null ] && [ command -v python &> /dev/null ]
then
    echo "Python could not be found."
    echo "Please install Python before continuing."
fi

if ! command -v pip &> /dev/null
then
    echo "pip could not be found."
    echo "Please install pip before continuing."
fi

echo "Installing Whisper from GitHub"

pip install git+https://github.com/openai/whisper.git 