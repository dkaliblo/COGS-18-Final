"""A collection of classes (Player, Character, and Elsa) and functions for doing my project. I included both the functions
and the classes in one file because the classes use some custom functions and some functions use the classes"""

def check_wrong_response_mc(response):
    """checks if an input is suitable for a multiple choice question with options a, b, c, or d
        and requests a new input if it is not
    
    Parameters
    ----------
    response : string
    String input that is checked
    
    Returns
    -------
    response : string
    A resulting input that fits the criteria
    """
    
    while \
            response != "a" and response != "A" \
            and response != "b" and response != "B" \
            and response != "c" and response != "C" \
            and response != "d" and response != "D":
        print('Please just enter the letter of one of the options.')
        response = input()
    
    return(response)
        
    
def quiz_response(response, characteristics):
    """implements the results of a given input in the characteristic quiz Player method used to create characters
    
    Parameters
    ----------
    response : string
    String input given by player
    
    characteristics : dictionary
    A dictionary set up to store the values of player characteristics this quiz determines
    
    Returns
    -------
    characteristics : dictionary
    The dictionary passed in as a parameter, now updated with the player's customized individual characteristic values
    """
    
    response = check_wrong_response_mc(response)
    if response == "a" or response == "A":
        characteristics["Humor"] += 1
        
    elif response == "b" or response == "B":
        characteristics["Relaxation"] += 1
        
    elif response == "c" or response == "C":
        characteristics["Outgoingness"] += 1
        
    elif response == "d" or response == "D":
        characteristics["Grumpiness"] += 1
        
    return(characteristics)


def max_dict_key(my_dict):
    """finds which key in a dictionary has the greatest corresponding value
    
    Parameters
    ----------
    my_dict : dictionary
    Dictionary that has only integers as values (keys do not have to be integers)
    
    Returns
    -------
    max_key
    Whatever key in the parameter my_dict had the highest integer as its value
    """
    
    max_value = -1
    max_key = None
    
    for item in my_dict:
        if my_dict[item] > max_value:
            max_value = my_dict[item]
            max_key = item
            
    return max_key


class Player():
    """The class for the game's player. 
    
    Attributes
    ----------
    name: string
    the player's name
    
    characteristics : dictionary
    each individual personality characteristic and the value for each of those characteristics.
    The characteristics are initially set at zero because they will be given more meaningful values by the quiz method.

    """
    
    def __init__(self, name = ""):
        
        self.name = name
        self.characteristics = {"Humor" : 0, "Relaxation" : 0, "Outgoingness" : 0, "Grumpiness" : 0}
    
    def quiz(self):
        """The quiz used to generate the characteristics for a new player or character"""
        
        print("What's your brand-new character's name?")
        self.name = input() 
        
        print("If you were stranded on a desert island, which of these people would you take with you? \na) John Mulaney \nb) Gordon Ramsay \nc) Rupaul Charles \nd) Donald Trump")
        self.characteristics = quiz_response(input(), self.characteristics)
        
        print("If you want to have a good time, which of these would you choose? \na) Stand-up comedy \nb) Getting a nice blanket and reading a book \nc) Going to a club that has a discount on colorful drinks tonight \nd) Not playing this anymore")
        characteristics = quiz_response(input(), self.characteristics)
        
        print("Which of these video games is your favorite? \na)Octodad: Dadliest Catch \nb) Animal Crossing: New Leaf \nc) Mario Party 4 \nd) Video games are dumb")
        self.characteristics = quiz_response(input(), self.characteristics)
        
        print("How are you today? \na) Oh I'm doing fantastic. Just really great. AMAZING. Thanks SO MUCH for asking. \nb) J chillin, dude \nc) Ready to take on the world \nd) Please go away") 
        self.characteristics = quiz_response(input(), self.characteristics)


class Character(Player):
    """The class for the game's characters. 
    
    Attributes
    ----------
    name: string
    the character's name
    
    characteristics : dictionary
    each individual personality characteristic and the value for each of those characteristics
    
    friendship : integer
    the measure of friendship with the player
    
    vocab : dictionary
    all the phrases the character could say, determined by their characteristics, labeled for when to say them
    """
    
    def __init__(self, name = "", humor = 0, relaxation = 0, outgoingness = 0, grumpiness = 0, friendship = 0):
    
        super().__init__(name)
        self.friendship = friendship
        self.characteristics = {"Humor" : humor, "Relaxation" : relaxation, "Outgoingness" : outgoingness, "Grumpiness" : grumpiness}

        #whichever characteristic is highest is what determines which set of phrases makes up the vocabulary of a Character
        if max_dict_key(self.characteristics) == "Humor":
            self.vocab = {
              "Greeting" : "How's everybody doing tonight?", 
              "Catchphrase" : "So what's the deal with python, folks?", 
              "Disappointment" : "Well darn. That was, like, the opposite of a knee-slapper.", 
              "Goodbye": "Alright then, that's all my time. Bye, folks."
            }
            
        elif max_dict_key(self.characteristics) == "Relaxation":
            self.vocab = {
              "Greeting" : "Yo, what's up?", 
              "Catchphrase" : "Life is crazy dude haha", 
              "Disappointment" : "Dang, dude. That wasn't super chill.", 
              "Goodbye": "Catch you later."
            }
            
        elif max_dict_key(self.characteristics) == "Outgoingness":
            self.vocab = {
              "Greeting" : "Hi !!!!", 
              "Catchphrase" : "I love people! I love meeting people! I love talking to people! I love talking in general! The other day I went to a pottery class and I made this AMAZING vase and it has, like, spots all over it, and, like... \n \n (you fall asleep, but manage to wake up conveniently just as they finish talking)", 
              "Disappointment" : "Wow, you got me all wound up just for that.", 
              "Goodbye": "Cya later !!!"
            }
            
        elif max_dict_key(self.characteristics) == "Grumpiness":
            self.vocab = {
              "Greeting" : "What is it??", 
              "Catchphrase" : "Get off my lawn!", 
              "Disappointment" : "Ha. VERY funny.", 
              "Goodbye": "Finally, you'll stop bothering me."
            }
        
        
    def greet(self, player, friendship_increase):
        """A method that prints the character's greeting and raises friendship with the player.
        It is different based on whether or not the player and this character have already established friendship
        
        Parameters
        ----------
        player : Player object
        this object stores, among other things, the player's name, so the character can reference it in their greeting 
        
        friendship_increase : integer
        the number of friendship points that will be added from this action
        """
        
        if self.friendship == 0:
            print(self.vocab["Greeting"] + " It's nice to meet you, " + player.name + "!")
            self.friendship = friendship_increase
            
        else:
            print(self.vocab["Greeting"])
            self.friendship += friendship_increase
    
    
    def catchphrase(self, friendship_increase):
        """A method that prints the character's catchphrase and raises friendship with the player
        
        Parameters
        ----------
        friendship_increase : integer
        the number of friendship points that will be added from this action
        """
        
        print(self.vocab["Catchphrase"])
        self.friendship += friendship_increase
   
    def disappointment(self, friendship_decrease):
        """A method that prints the character's disappointment phrase and lowers friendship with the player
        
        Parameters
        ----------
        friendship_decrease : integer
        the number of friendship points that will be lowered from this action
        """
        
        print(self.vocab["Disappointment"])
        self.friendship -= friendship_decrease
        
        
    def goodbye(self):
        
        print(self.vocab["Goodbye"])
        
        
class Elsa(Character):
    """this class is almost identical to the Character class, except the vocab is determined regardless of the character's
    characteristics and the name is defaulted to "Elsa".
    """
    
    def __init__(self, name = "Elsa", humor = 0, relaxation = 0, outgoingness = 0, grumpiness = 0, friendship = 0):

        super().__init__(name, humor, relaxation, outgoingness, grumpiness, friendship)
        self.vocab = {
                "Greeting" : "Let it go!", 
                "Catchphrase" : "Let it go, let it go!", 
                "Disappointment" : "Let it go :(", 
                "Goodbye": "The cold never bothered me anyway"
                }

        
def check_character_response(response, characters):
    """checks whether or not the input given is a character that currently exists in the game
    
    Parameters
    ----------
    response : string
    whatever input the player has given, supposed to be the name of one of the characters
    
    characters : dictionary
    all the Character objects in the game labeled by their names
    
    Returns
    -------
    characters[response] : Character object
    the Character that the player has chosen through an input
    """
    
    while response not in characters.keys():
        print("Please enter one of these characters: ")
        
        for char in characters.keys():
            print(char)
            
        response = input()
        
    return(characters[response])
    
    
def play(characters, player):
    """initiates the play sequence in which the player can raise (or lose) friendship with Characters through dialogue.
    Players can choose between different paths of dialogue through multiple choice questions.
    
    Paramaters
    ----------
    characters : dictionary
    all the Character objects in the game labeled by their names
    
    player : Player object
    the object storing the attributes of the player of the game    
    """

    print("Who do you want to hang out with? Look at all these people who are free: ")
    
    for char in characters.keys():
        print(char)
        
    playmate = check_character_response(input(), characters)

    if max_dict_key(playmate.characteristics) == max_dict_key(player.characteristics):
        friendship_factor = 5
        compatible = True
        
    else:
        friendship_factor = 1
        compatible = False
    
    playmate.greet(player, friendship_factor)
    
    response = ""
    #response will soon have a more meaningful value, but it just needs to exist right now to start the dialogue in the 
    #while loop. When response is d, that indicates that the play session with this character should end.
    while response != "d" and response != "D":
        print("Let's play with " + playmate.name + " some more. What do you want to say?")
        print("a) Let's talk! \nb) Uh, do you want to... um... go on a... uh... \nc) Prove your love for me! \nd) Bye")
        response = check_wrong_response_mc(input())

        if response == "a" or response == "A":
            playmate.catchphrase(friendship_factor)

        elif response == "b" or response == "B":
            print(player.name + ': "Uh, do you want to... um... go on a... uh... um... a..."') 
            
            if compatible:
                print(playmate.name + ': "A what? A date?"')
            
            else:
                print(playmate.name + ': "What? Spit it out already."')
            
            print(player.name + ': "a... a waitlist for a class that programs in a language other than python?"')
            playmate.disappointment(friendship_factor)

        elif response == "c" or response == "C":
            print("Who do you think loves you more than me?")
            response = check_character_response(input(), characters)
            
            if response.name == playmate.name:
                print("But that's me! Who are you really asking about?")
                response = check_character_response(input(), characters) 
            #the above if statement is there to make sure the playmate isn't talking to/competing with themselves
            
            if response.friendship > playmate.friendship:
                print("Wow, they like you a lot. It's no use, sorry " + player.name)
                playmate.disappointment(friendship_factor)
                print(response.name + ":")
                response.catchphrase(friendship_factor)
            
            elif response.friendship < playmate.friendship:
                print("oh, I love you more than them for sure, " + player.name)
                print(response.name + " chimes in:")
                response.disappointment(friendship_factor)
                
        elif response == "d" or response == "D":
            playmate.goodbye()

        else:
            check_wrong_response(response)       


def data(characters):
    """prints the friendship values of all the characters in the game
    
    Parameters
    ----------
    characters : dictionary
    all the Character objects in the game labeled by their names
    """
    
    for char in characters.keys():
        print("your friendship level with " + characters[char].name + " is " + str(characters[char].friendship))
    
def create_character(characters):
    """creates a new Character object with characteristics based on the quiz() method
    
    Parameters
    ----------
    characters : dictionary
    all the Character objects in the game labeled by their names
    
    Returns
    -------
    characters : dictionary
    all the Character objects in the game labeled by their names, now including the new character that was just made
    """
    
    new_character = Character()
    new_character.quiz()
    characters.update( {new_character.name : new_character} )
    
    return(characters)
    
def game_loop():
    """initiates the game"""
    
    characters = {
            "Bunny" : Character("Bunny", 0, 0, 100, 0),
            "Mr. Bro" : Character("Mr. Bro", 10, 50, 20, 30),
            "Bozo" : Character("Bozo", 100, 0, 50, 0),
            "Old Man Jim" : Character("Old Man Jim", 1, 0, 50, 100),
            "Uncopyrighted Ice Queen" : Elsa("Uncopyrighted Ice Queen", 10, 50, 49, 20)
            }
    
    print("Welcome! To start playing, let's set up your player with a little quiz.")
    player = Player()
    player.quiz()
    
    dont_stop = True
    while dont_stop:
        print("Hello " + player.name + "! Do you want to play, look at your friendship data, create a new character, or quit?")
        response = input()
        
        if "play" in response or "Play" in response:
            play(characters, player)
        
        elif \
                "look" in response or "Look" in response \
                or "save" in response or "Save" in response \
                or "data" in response or "Data" in response:
            data(characters)
        
        elif \
                "create" in response or "Create" in response \
                or "new" in response or "New" in response \
                or "character" in response or "Character" in response:
            characters = create_character(characters)
        
        elif "quit" in response or "Quit" in response:
            print("see ya!")
            dont_stop = False
        
        else:
            print("Please input 'play', 'data', create', or 'quit'")
    
    
    
    
 