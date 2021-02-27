# DiceWareMultiLan-GUI
A GUI-tool to create secure pass phrases with the DiceWare method. The tool can choose from multiple different word lists, e.g. different languages.

## Passwords by the Diceware method
Good passwords are long and have a high entropy. However, those passwords are difficult to remember. But there is a method for comparably easy memorization of strong passwords called the Diveware method (see https://theworld.com/~reinhold/diceware.html). The effectiveness is well depicted in the famous XKCD comic about password strength: https://xkcd.com/936/.
Originially, and most securely, those passphrases are generated by rolling dice and noting the faces, until the pass phrase is long enough. But not everyone is dedicated enough to take the time to do so. For those there are several online tolls like https://www.rempe.us/diceware/#eff. This page also features Diceware lists in other languages. 

## DiceWareMultiLan-GUI
This tool here tries to improve security by running completly offline. It can also make passwords from custom-wordlists and pass phrases from several word lists at once. In contrast to the command-line tool diceware (https://pypi.org/project/diceware/) this python based script features a PyQt GUI.
