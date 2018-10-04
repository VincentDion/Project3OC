# Project3OC
Welcome in the README file of this MacGyver escapes! game, created by Vincent Dion as a study project for OpenClassrooms. Coded in Python and working thanks to the Pygame library, the main goal of the game is to reach the end of a labyrinth after collecting a certain number of items randomly placed. The main character is controlled by the directional keys of the keyboard and can only do basic movements: left, right, up and down. Items are automatically collected when walking on it, and reaching the end of the labyrinth will automatically trigger the hero’s death, if you didn’t collect all the items, or the enemy’s sleep if you did.


# Current version

The game is functional and therefore is in its 1.1 version. Without additional code development, you may add new level, although you need to change few lines in the main code to let the user choose the appropriate level. Consult the existing level to see how to create another one, as it is relatively straightforward in its structure (W for walls, O for nothing, T for Test, S for start, F for Finish). It is strongly advised to place the Finish in the bottom-right corner, or you may need to alter the code a bit to change the position of the enemy.
You may quit the game at any time by pressing the ESCAPE button. You can’t however reset a level in the current version.
Although the game is working as intended in its current version, I am not satisfied at all with its code architecture which will undergo some change soon. Improvements for the 1.1 version are detailed in the next section.


# Changes compare to 1.0

- New victory screen to comply with copyright regulations
- New home screen to give information about the game, still ugly though


# Improvements for next version

-	Improve the code by reducing number of treatments, especially in the random placement of objects,
-	Diminish the number of code lines by eliminating the repetitive operations that can be add as functions.
-	Diminish to a minimum the number of “hard coded” values for variables in the main game file (such as position of enemy or position of objects in the inventory bar). Goal is to set the game for any change in the number of objects, enemies or levels while making few to none adjustments to the code.

# License

All images, as well as the game, are under WTFPL license, either directly downloaded from the website http://jessefreeman.com/ or created by me.


# Special thanks 

Special thanks to my mentor, Addi Ait-Mlouk, and my “classmate”, Loïc Mangin, for their various and very much welcomed advices.

