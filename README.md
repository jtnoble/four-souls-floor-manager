# four-souls-floor-manager
A simple manager for a floor-based ruleset for the card game, "The Binding of Isaac: Four Souls"

# What is this?
This is an application that displays the information for each floor in a floor based ruleset for "Four Souls", a card game created for the popular video game "The Binding of Isaac". The original rules in the game do not use a floor based layout, but instead have you attacking monsters directly. This is fine, but sometimes you aren't guarenteed a soul card for many turns. This keeps the pace of the game steady; however, it can be a little hard to remember the rules of the floor you are on. This Tkinter-powered Python application hopefully helps with that.

# Where can I learn about Four Souls?
You can learn more about Four Souls at https://foursouls.com/

# So, what are these new rules?
The application is simply a reminder of these rules so you can possibly display them on a screen during gameplay. The rules are as follows:

There are 11 floor types. Basement and caves will aways be floor 1 and 2, and cannot show up again. Floor 3 and onwards, roll the 8 sided dice. The number corresponds with the category of floors below. (Bandaid fix for not having a 9 sided die, but if an 8 is rolled, roll again. If the number is 1-4, choose Void/Home, if 5-8, choose ???/Corpse) 

1. Downpour/Dross
2. Mines/Ashpit
3. Depths/Dank Depths/Necropolis
4. Mausoleum/Gehenna
5. Womb/Scarred Womb/Utero
6. Cathedral/Sheol
7. Chest/Dark Room
8. Void/Home or ???/Corpse

Once a floor has been determined, roll the dice again. 6 or higher = XL floor 

1. Basement/Cellar/Burning Basement
• Basement - You feel fine. No special rules.
• Cellar - You feel confident. Begin your turn with +1 damage on your next attack.
• Burning basement - You feel hot. +1 to all dice rolls, and all enemies do +1 damage to you.
2. Downpour/Dross
• Downpour - You feel sad. There is a beggar on this floor. During your turn, you may donate up to 3 pennies to him. After each penny, roll the 8 sided dice. If the result is 8, the beggar thanks you, and gives you 1 treasure. After 3 treasures have been claimed, the beggar disappears.
• Dross - You feel disgusting. Every time you roll a 1, poop yourself. When you poop yourself, you are protected from 1 point of the next damage you would take this floor.
3. Caves, Flooded Caves, Catacombs
• Caves - You feel spelunky. When you defeat a monster, +1 loot.
• Flooded Caves - You feel soggy. -1 to all dice rolls, and enemies cannot do more than 1 damage to you.
• Catacombs - You feel spooky. If you die here, you can respawn by paying 5 cents, and if it is your turn, end your turn.
4. Mines, Ashpit
• Mines - You feel crafty. There are 3 secret rooms, and your first bomb purchased is only 3 cents.
• Ashpit - You feel ashy. Each enemy has a 50% chance to miss when damaging you.
5. Depths, Dank Depths, Necropolis
• Depths - You feel cautious. You may choose to look at a room before exploring, but if you don't explore it, you may not explore any others.
• Dank Depths - You feel dank. Everyone has +1 HP in this floor.
• Necropolis - You feel scared. Every enemy (including bosses) is revealed from the start, but when you choose to attack, it is a random enemy chosen via dice roll.
6. Mausoleum, Gehenna
• Mausoleum - You feel sneaky. At the start of your turn, you may look at one players hand.
• Gehenna - You feel demonic. During your turn, you may pay 1 HP to gain 5 pennies.
7. Womb, Scarred Womb, Utero
• Womb - You feel unborn. Every time you defeat an enemy, you are fully healed.
• Scarred Womb - You feel betrayed. If you defeat an enemy, discard 1 loot card.
• Utero - You feel whole. All players are healed at the end of every turn.
8. ???, Corpse
• ??? - You feel REDACTED. This floor only has one room, which is guaranteed to be a boss. (2 bosses if an XL floor) Each player gains 1 treasure. Every player rolls the 8 sided dice, and whoever rolls highest gets to play this floor first.
• Corpse - You feel undead. You cannot die on this floor. If you would die, instead, end your turn.
9. Cathedral, Sheol
• Cathedral - You feel holy. If you save another player from death, you and that player gain a permanent +1 max HP.
• Sheol - You feel evil. If you take damage here, deal 1 damage to every face-up monster.
10. Chest, Dark Room
• Chest - You feel rich. Every enemy drops 1 treasure and 5 coins.
• Dark Room - You feel risky. When you defeat a monster, you may choose to open a red chest.
11. Void, Home
• Void - You feel corrupted. At the start of your turn, you may choose to use another players active items in addition to your own. If you choose that player, they cannot respond by using their active items.
• Home - You feel safe. During your turn, no other players are allowed to play an active item.
