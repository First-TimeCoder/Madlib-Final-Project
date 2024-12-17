import random



#Type of speech in each story
def generate_partsofspeech():

    possible_stories = ["WRITE STORY 1", "WRITE STORY 2", "WRITE STORY 3", "WRITE STORY 4", "WRITE STORY 5"]

    #Choose story for user
    storytype = random.choice(possible_stories)
    user_input = ""

    noun = input("Give me a noun: ")
    noun2 = input("Give me a noun: ")
    noun3 = input("Give me a noun: ")
    adverb = input("Give me an adverb: ")
    verb = input("Give me a verb: ")
    verb2 = input("Give me a verb: ")
    verb3 = input("Give me a verb: ")
    pronoun = input("Give me a pronoun: ")
    adjective = input("Give me an adjective: ")
    adjective2 = input("Give me an adjective: ")
    adjective3 = input("Give me an adjective: ")
    adjective4 = input("Give me an adjective: ")
    aname = input("Give me a person's name:"  )
    pluralverb = input("Give me a plural verb: ")
    pluralnoun = input("Give me a plural noun:")
    pluralnoun2 = input("Give me a plural noun:")
    pluralnoun3 = input("Give me a plural noun:")
    pluralnoun4 = input("Give me a plural noun:")
    bodypart = input("Give me a body part: ")
    verbendingining = input("Give me a verb ending in -ing: ")


    story = "The Madilib Story" + noun + "End of Madlib story"
    print(story)

    if storytype == "WRITE STORY 1":
        storytype = "There once was an old women who" + verb + "over a skateboard as it rolled up next to her. She" + adverb + "came to a stop and turned around to see who had lost their skateboard. She couldn't find" + noun + "who she thought it belonged to.So, she took it" + noun
        print(storytype)

    if storytype == "WRITE STORY 2":
        storytype = "Once upon a time, there was a" + adverb + "princess named" + aname + "she was from" + noun + "she lived in the beautiful kingdom on the hills called" + noun2 + "she had  five" + noun3 + "while she was" + pluralverb + "then she fell off her hourse and ran back to her kingdom" + noun4 + "to wash her dress"
        print(storytype)

    if storytype == "WRITE STORY 3":
        storytype = "It was a" + adjective + ", cold November day. I woke up to the" + adjective2 + "smell of chicken roasting in the" + noun + "downstairs. I" + verb + "down the stairs to see if I could help" + verb2 + "the dinner. My mom said see if" + noun2 + "needs a fresh" + noun3 + "So I carried a tray of glasses full of water to the" + verb3 + "room.  When I got there I couldn't  believe my" + bodypart + "There were" + pluralnoun + "on the" + noun4 + "!"
        print(storytype)

    if storytype == "WRITE STORY 4":
        storytype = "Today, me and my friends are having a" + noun + "party! We're going to go to" + aname + "house." + pronoun + "He has a giant pool. We're plainning to float on" + pluralnoun + "and" + verb + "down the water" + noun2 + ". His mom promised to give us" + pluralnoun2 + "to eat and" + pluralnoun3 + "maybe she'll even get us" + pluralnoun4 + "."
        print(storytype)

    if storytype == "WRITE STORY 5":
        storytype = "O say can you" + verb + "by the dawn's early" + noun + ". What so" + adverb + "we" + verb2 + "at the twilight's last gleaming. Whose broad" + pluralnoun + "and bright" + pluralnoun2 + "through the" + adjective + "fight. O'er the" + pluralnoun3 + "we watched, were so gallantly" + verbendingining + "? And the rocket's red glare, the" + pluralnoun4 + "bursting in" + noun2 + ". Gave proof through the night that our" + noun3 + "was still there; O say does that" + adjective2 + "banner yet" + verb3 + "O'er the land of the" + adjective3 + "and the home of the" + adjective4
        print(storytype)


def continue1():
    repeat = input("Do you want to write another story in Madlibs?")

    while repeat == "yes":
        generate_partsofspeech()
        repeat = input("Do you want to write another story in Madlibs?")

continue1()

