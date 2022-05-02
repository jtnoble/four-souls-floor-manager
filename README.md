# four-souls-floor-manager
A simple manager for a floor-based ruleset for the card game, "The Binding of Isaac: Four Souls"

# What is this?
This is an application that displays the information for each floor in a floor based ruleset for "Four Souls", a card game created for the popular video game "The Binding of Isaac". The original rules in the game do not use a floor based layout, but instead have you attacking monsters directly. This is fine, but sometimes you aren't guarenteed a soul card for many turns. This keeps the pace of the game steady; however, it can be a little hard to remember the rules of the floor you are on. This Tkinter-powered Python application hopefully helps with that.

# Where can I learn about Four Souls?
You can learn more about Four Souls at https://foursouls.com/

# So, what are these new rules?
The application is simply a reminder of these rules so you can possibly display them on a screen during gameplay. The rules are as follows:

• There are 10 floor types. Basement will always be the first two floors, with the variation determined by dice roll. At the start of each floor from floor 3 onwards, roll the 8 sided dice to determine which floor you will be in. Then, roll the dice again and if the result is 6 or higher, the floor is an XL floor.



1. Basement (one of three variations)
• Basement - You feel fine. No special rules apply.
• Flooded basement - You feel soggy. -1 to all dice rolls until the boss is revealed, but enemies can only do a maximum of 1 damage to you at a time.
• Burning basement - You feel hot. +1 to all dice rolls until the boss is revealed, but enemies do +1 damage to you.

2. Catacombs - You feel dead. If you die here, you can respawn by paying 5 cents.

3. Mines - You feel crafty. There are 3 secret rooms on this floor, and bombs are only 3 cents.

4. Sheol/Cathedral - You feel demonic/holy. In Sheol, killing a player here grants you permanent +1 damage. In Cathedral, saving a player from death grants you and that player permanent +1 HP. Determine which floor by rolling a dice. Evens/Cathedral, Odds/Sheol.

5. Depths - You feel scared. Every enemy is revealed from the start, but when you choose to attack, it is a random enemy chosen via dice roll.

6. The Chest - You feel rich. Every enemy drops 1 treasure and 5 coins in addition to their normal drops.

7. The Womb - You feel unborn. Every time you defeat an enemy, you are healed to full HP.

8. Downpour - You feel sad. There is a beggar on this floor. You may donate up to 3 pennies per turn to him to cheer him up. After each penny donated, roll a dice. If the result is 6, the beggar thanks you, disappears, and gives you 1 treasure. The beggar has 1 hp and can be killed for 1 penny. 
