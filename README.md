# imgur_nude_bot

Simple bot that goes through random images from imgur.com and checks if it's a nude using DeepAI.
Have fun! :)

This code is not of my property, i just made some changes and a google colab to execute it. This is a improved code, but if you want it, here is the original: https://github.com/kszmigiel/imgur_nude_bot

# Executing on Google Colab
I made a google colab adaptation of the algorith
1. Go to this page: https://gist.github.com/ricardo01l/ab0e5a5834822833f4e27d897a0bd6cf
2. Then click "Open in colab" and follow the steps it indicates you.

# Executing on your computer
If you want to execute this on your computer, you need to do this:

Open comand line.

1. Go to the folder you want the code and Clone git
```
> git clone https://github.com/ricardo01l/detect-nude-imgur.git
```

2. install dependencies and move to the folder we cloned
```
> pip install requests
> cd imgur_nude_bot/
```


  1. You need to have an acount in deepAI.org You can execute the next cell
  2. Go to dashboard and copy your api-key (this gives you unlimited access to the apis of deepAI)
  3. In the files of the present proyect, go to imgur_nude_bot/ and open "main.py", then paste your api-key where the code indicates you "your deepAI api-key goes here".


Note: you only need to do this steps once, then you can execute next step the times you want (and you don't have to execute the step number 1 and 2)

3. Execute the algorith
```
> python main.py
```
or

```
> main.py
```
