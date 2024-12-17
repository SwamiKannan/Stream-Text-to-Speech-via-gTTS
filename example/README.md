# Sample exercise:

## Text to be processed
> Good morning sir. The main updates today are as follows: <br />
> News:.<br />
>    1;   Latest in the Middle East as US secretary of state meets with leaders in region.<br />
>    2;   Meet the kids struggling to breathe in India’s choked capital.<br />
>    3;   Buckingham Palace maid arrested after drunken brawl at work Christmas party.<br />
>    4;   Indian Gukesh Dommaraju, 18, becomes the youngest ever chess world champion after Ding Liren blunder.<br />
>        5;   Oldest human DNA reveals lost branch of the human family tree. <br />
>        6;   The game that means everything: Army and Navy get ready to clash for the 125th time in college football’s most unique rivalry. <br />
>        7;   South Korea’s parliament votes to impeach president.<br />
>    The weather:<br />
>        ; 33 degrees centigrade. <br />
>        ; Air Quality Index of 157 which is "Poor".<br />
>        ; The humidity is 42% and .<br />
>        ; The windspeed is 7 km/h.<br />
><br />
>   So what can I do for you today?<br />

## Code:
```
text = '''
    Good morning sir. The main updates today are as follows:
    News:.
        1;   Latest in the Middle East as US secretary of state meets with leaders in region.
        2;   Meet the kids struggling to breathe in India’s choked capital.
        3;   Buckingham Palace maid arrested after drunken brawl at work Christmas party.
        4;   Indian Gukesh Dommaraju, 18, becomes the youngest ever chess world champion after Ding Liren blunder.
        5;   Oldest human DNA reveals lost branch of the human family tree. 
        6;   The game that means everything: Army and Navy get ready to clash for the 125th time in college football’s most unique rivalry. 
        7;   South Korea’s parliament votes to impeach president.
    The weather:
        ; 33 degrees centigrade. 
        ; Air Quality Index of 157 which is "Poor".
        ; The humidity is 42% and .
        ; The windspeed is 7 km/h.

    So what can I do for you today?
    '''
```

### Sample runs:
#### 1. Streaming
```
    print('Streaming output.....')
    taken_time = stream_stt(text)
    print(f' Sentence of {len(text)} characters transcribed and read. First text was processed in {taken_time} seconds')
```
![](/images/streaming_time_to_process_first_output.PNG)

#### 2. Sequential (first conversion the entire text to bytes -> then play the audio)
```
    print('Playing sequential output......')
    taken_time = process_sequential(text)
    print(f' Sentence of {len(text)} characters transcribed and read. First text was processed in {taken_time} seconds')
```
![](/images/sequential_time_to_process_first_output.PNG)
