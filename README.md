# Streaming Text to Speech via gTTS
<p align = "center">
<img src = "images/cover.png" width = 90%>
</p>

## From the [gTTS repository](https://github.com/pndurette/gTTS):
**gTTS** *(Google Text-to-Speech)*, a Python library and CLI tool to interface with Google Translate's text-to-speech API. Write spoken ```mp3``` data to a file, a file-like object (bytestring) for further audio manipulation, or ```stdout```. https://gtts.readthedocs.io/

## Introduction:
I love the gTTS library. It is an incredible hack on Google Translate's speech functionality. From the [repo's disclaimer](https://github.com/pndurette/gTTS/tree/main#disclaimer):

>  This project is leveraging the undocumented Google Translate speech functionality and is different from Google Cloud Text-to-Speech.

However, the repo does not detail how to do the following:
1. Play the audio without saving it
2. Stream the audio as the text is being processed.

> **This is a simple one-file script that seeks to stream gTTS audio given a large piece of text.**



## Usage:
#### Download the repo 
```
https://github.com/SwamiKannan/Stream-Text-to-Speech-via-gTTS.git
```
#### Import the function
```
from src import stream_stt
```

#### Run the function
```
stream_stt(text)
```

## Sample outputs
[Sample output for the script](/example/README.md)
