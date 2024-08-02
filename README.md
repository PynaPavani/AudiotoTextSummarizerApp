# Audio-to-Text Summarization using GeminiPro

## Overview

This project focuses on implementing an audio-to-text summarization system using **GeminiPro**, a powerful model known for its efficiency in processing audio data and generating concise summaries. The system takes audio files as input and provides a summarized text output, capturing the essential information from the audio content.

## Features

- **Accurate Audio Transcription**: Converts spoken words from audio files into text with high accuracy.
- **Concise Summarization**: Distills the transcribed text into a brief and informative summary, highlighting the key points.
- **Versatile Input Support**: Capable of handling various audio formats, making it suitable for diverse applications like podcast summarization, meeting minutes, and more.

## How It Works

1. **Audio Input**: Users upload an audio file in a supported format.
2. **Transcription**: The GeminiPro model transcribes the audio into text.
3. **Summarization**: The transcribed text is processed to generate a summary, focusing on the most relevant information.

## Installation

To get started with the project, clone the repository and follow the installation instructions provided in the `requirements.txt` file.

```bash
git clone https://github.com/PynaPavani/AudiotoTextSummarizerApp.git
cd audio-to-text-summarization
pip install -r requirements.txt
```

## Usage

1. Place your audio files in the designated input folder.
2. Run the script to process the audio and generate the summaries.

```bash
streamlit run audio_app.py
```

## Dependencies

- **GeminiPro**: The core model used for transcription and summarization.
- **Python 3.x**: The programming language used for implementing the system.

## Contributing

We welcome contributions to improve the system, including bug fixes, feature enhancements, and documentation updates. Please fork the repository and submit a pull request with your changes.
