'''
For my final project, I will be implementing an anime reccomendation 
program that will help the user decide what to watch based on genre.
This is just a small program that will include at least 10 anime of
each genre.
By storing a whole bunch of anime into a dict and list, this will
easily pull one anime for the user. I would also like to mix genres
if possible. 
I would like to work on this further after finishing this project to make 
the program better, so this is a simple/rough draft.
'''
import random

def main():
    print('Welcome to AniPicker! Where we help you decide what to watch next.')
    print('------------------------------------------------------------------')
    print('Please choose from a list of these genres: slice of life, horror, mecha, action, shoujo, shounen, fantasy, or kids')
    reccomend = input('What kind of anime to you feel like watching today? ')
    if reccomend == 'horror':
        horror = ['Devilman Crybaby', 'Future Diary', 'Deadman Wonderland', 'Another', 'The Promised Neverland', 'Elfen Lied', 'Monster', 'Tokyo Ghoul', 'High School of the Dead', 'Parasite']
        #figuring out how to shuffle/randomize my list of strings
        print('I reccomend watching', random.choice(horror) + '.')
        #in my print statement, I learned that random.choice() is a way to 
        #randomize/shuffle the output from strings in a list.
    if reccomend == 'slice of life':
        slice_of_life = ['Silver Spoon', 'The Pet Girl of Sakurasou', 'Bunny-Girl Senpai', 'The Devil is a Part-Timer!', 'A Silent Voice', 'Spice and Wolf', 'Blend S', 'Violet Evergarden', 'March Comes in Like a Lion', 'My Teen Romantic Comedy SNAFU']
        print('I reccomend watching', random.choice(slice_of_life) + '.')
    if reccomend == 'mecha':
        mecha = ['Neon Genesis Evangelion', 'Macross Frontier', 'Code Geass', 'Guilty Crown', 'Gurren Lagann', 'Mobile Suit Gundam: Iron-Blooded Orphans', 'Accel World', '', '', '']
        print('I reccomend watching', random.choice(mecha) + '.')
    if reccomend == 'action':
        action = ['Food Wars!', 'Beastars', 'Inuyasha', 'Cowboy Bebop', 'City Hunter', 'Banana Fish', 'Yu Yu Hakusho', 'Kill la Kill', 'No Game No Life', 'Soul Eater']
        print('I reccomend watching', random.choice(action) + '.')
    if reccomend == 'shoujo' or reccomend == 'shojo':
        shoujo = ['Fruits Basket', 'Chobits', 'Maid-Sama!', 'Revolutionary Girl Utena', 'Cardcaptor Sakura', 'Kamisama Hajimemashita', 'Ouran High School Host Club', 'Horimiya', "Monthly Girl's Nozaki Kun", 'Nana']
        print('I reccomend watching', random.choice(shoujo) + '.')
    if reccomend == 'shounen' or reccomend == 'shonen':
        shounen = ['My Hero Academia', 'Naruto', 'One Piece', 'Sword Art Online', 'Attack on Titan', 'Assassination Classroom', 'Gintama', 'One Punch Man', 'Hunter X Hunter', 'Demon Slayer']
        print('I reccomend watching', random.choice(shounen) + '.')
    if reccomend == 'fantasy':
        fantasy = [ 'Fairy Tail', 'Fate/Stay Night', 'Fullmetal Alchemist', 'The Seven Deadly Sins', 'Magi: The Labyrinth of Magic', "The Ancient Magus' Bride", 'Black Clover', 'Overlord', 'The Familiar of Zero', 'A Certain Magical Index' ]
        print('I reccomend watching', random.choice(fantasy) + '.')
    if reccomend == 'kids':
        kids = ['Pokemon', 'Digimon Adventure', 'Hamtaro', 'Doraemon', 'Yugioh', 'Sonic X', 'Yokai Watch', 'Finn Family Moomintroll', 'Pingu', 'Kimba the White Lion']
        print('I reccomend watching', random.choice(kids) + '.')

def list_of_genres():
    #this function stores variables named as different genres and 
    #contains a list of 10 different anime titles of each genre.
    slice_of_life = ['Silver Spoon', 'The Pet Girl of Sakurasou', 'Bunny-Girl Senpai', 'The Devil is a Part-Timer!', 'A Silent Voice', 'Spice and Wolf', 'Blend S', 'Violet Evergarden', 'March Comes in Like a Lion', 'My Teen Romantic Comedy SNAFU']
    horror = ['Devilman Crybaby', 'Future Diary', 'Deadman Wonderland', 'Another', 'The Promised Neverland', 'Elfen Lied', 'Monster', 'Tokyo Ghoul', 'High School of the Dead', 'Parasite']
    mecha = ['Neon Genesis Evangelion', 'Macross Frontier', 'Code Geass', 'Guilty Crown', 'Gurren Lagann', 'Mobile Suit Gundam: Iron-Blooded Orphans', 'Accel World', '', '', '']
    action = ['Food Wars!', 'Beastars', 'Inuyasha', 'Cowboy Bebop', 'City Hunter', 'Banana Fish', 'Yu Yu Hakusho', 'Kill la Kill', 'No Game No Life', 'Soul Eater']
    shoujo = ['Fruits Basket', 'Chobits', 'Maid-Sama!', 'Revolutionary Girl Utena', 'Cardcaptor Sakura', 'Kamisama Hajimemashita', 'Ouran High School Host Club', 'Horimiya', "Monthly Girl's Nozaki Kun", 'Nana']
    shounen = ['My Hero Academia', 'Naruto', 'One Piece', 'Sword Art Online', 'Attack on Titan', 'Assassination Classroom', 'Gintama', 'One Punch Man', 'Hunter X Hunter', 'Demon Slayer']
    fantasy = [ 'Fairy Tail', 'Fate/Stay Night', 'Fullmetal Alchemist', 'The Seven Deadly Sins', 'Magi: The Labyrinth of Magic', "The Ancient Magus' Bride", 'Black Clover', 'Overlord', 'The Familiar of Zero', 'A Certain Magical Index' ]
    kids = ['Pokemon', 'Digimon Adventure', 'Hamtaro', 'Doraemon', 'Yugioh', 'Sonic X', 'Yokai Watch', 'Finn Family Moomintroll', 'Pingu', 'Kimba the White Lion']

if __name__ == '__main__':
    main()
