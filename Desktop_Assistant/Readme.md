#Desktop-Assistant

The libraies I have used so far are as follows:<br/>
**pyttsx3**<br/>
**speech_recognition**<br/>
**wikipedia**<br/>
**datetime** and **time**<br/>
**smtplib**<br/>
**PyAudio**<br/>
From email.message **EmailMessage**<br/>
**webbrowser**<br/>
**os**<br/>
Check Pipfile and Pipefile.lock to know the exact version I m using and download them<br/>

###Use of above Libraries:<br/>
**pyttsx3**- <br/>
is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is   compatible with both Python 2 and 3. An application invokes the pyttsx3.init() factory function to get a   reference to a pyttsx3. Engine instance. it is a very easy to use tool which converts the entered text   into speech.<br/>
The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.<br/>
<br/>
It supports three TTS engines :<br/>
sapi5 – SAPI5 on Windows<br/>
nsss – NSSpeechSynthesizer on Mac OS X<br/>
espeak – eSpeak on every other platform<br/>
<br/>
**speach_recognition**-<br/>
Allow Adjusting for Ambient Noise:<br/>
 Since the surrounding noise varies, we must allow the program a second or too to adjust the energy threshold of recording so it is adjusted according to the external noise level.<br/>
<br/>
Speech to text translation: <br/>
This is done with the help of Google Speech Recognition. This requires an active internet connection to work. However, there are certain offline Recognition systems such as PocketSphinx, but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use.
<br/>
**wikipedia**:<br/>
Being a writer I need constant access to wikipedia so this module helps me to access wikipedia without using webscraping.
<br/>
**smtplib**:<br/>
This module helps in sending email. There are other alternatives like mailgun but for basic pratice i went for this one.