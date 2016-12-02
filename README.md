# Card-Trick-Game
A Magic Trick I found in a Christmas Cracker - and coded into a Python Game 

When I wrote this I had literally been coding for a few weeks, using PDF guides and tutorials to help

I got my Pi for xmas and wrote the card trick into Python early January. I remember I knew my Bro was giving me a Pi for xmas and I had NO coding experience - my Bro gave me Python and Scratch for my PC a few weeks before to get me practising...Thats where it all started for me - Anyway enough babbling - just a bit if background info

So, The game....



The original card trick was inside a xmas cracker as I said, it came with 6 cards and an instruction card

Each of the 6 cards has a Grid of numbers on it

The player is asked to Choose ANY number from one of the cards (and remember the card it was from)

Then the player is asked then, to make a note of EVERY other grid containing their number (including their chosen one)

Then the FIRST number of those grids will add up to the chosen number - and it does work


The way I coded it was very basic, and was all I knew how to do at the time, I remember following a tutorial book and wrote something like a Magic 8 Ball game, which had a List of possible answers, Im sure it was a previous example like that I used to store the grid information 

There may be and probably is better ways to write this, and I do plan to improve it over time, for now I want to get the number grids to display properly as they look a bit chaotic in the Shell. Eventually I will use either Tkinter or Pygame to visually improve everything

Anyway Enjoy....this was the first program I wrote alone - not using a guide or tutorial....meaning it was the first idea I had for a program 0 and I havent seen it in Python anywherelse yet

I welcome ANY feedback, and I also welcome any ideas for improvement

raserppsprograms@gmail.com

Ben


NOTE
======
02.12.2016

I ended up pretty much rewriting this whole program

I put a question up on Stack Overflow asking about a neater way to display the grids as they were very messy, and someone gave me a nice little function to put the 32 numbers into 6 x 4 grids. I played with it and it worked...so I ended up applying it to all 6 grids. Then I wasn't happy with the rest of it. I wrote the original version very early on when I started Python, like within the first weeks and I just had all the code in one huge block.

It worked, but when I re-did the grids, I also decided to put all of the questions (the main game) into a function, so at the end I just called the game function and the replay function.

I also added a few "Press enter to continue" situations because it was all moving too fast, this way the player can take their time to look over the grids and read the instructions, then continue when ready. 

It is a lot tidier now to look at, and it feels better to play, the little time delays mixed with the enter prompts seem to really help!


It feels good when you take a code you wrote a while back, and apply all of your new knowledge to make it better in little ways - feels like progress!





