main_scenario = """
You've been living here for well over five years now.
Its a quiet little area. Only a few houses per street 
and a nice big yard. Not that you really need one 
since you live alone since the incident. <insert tragic
backstory here> Ever since then, everythings been quiet. 
Somehow your neighbors found out, however, and are way
too nice. They were nice before, but you're resentful 
towards them now. Especially towards John. He always
invites you to cookouts. Its infuriating.

Last weekend, John invited you again. It was the last
time he'd ever do something like that again. You rage
plan his murder, being careful to think through everything.

His wife would be away for the weekend, so you decide it
is the perfect oppurtunity. You sneak in and do the deed.
Just as you're finishing the cleaning of the bedroom, 
Linda (his wife) walks in and sees you. She quickly dials
911 while you're conflicted on what to do next. You know
They're already on their way and they're notorious for
being quick to calls in your area.

Do you...
A. Kill Linda too?
B. Jump out the window that is two stories 
above the ground?
"""


killed_linda_a = """
You still don't know if it was really necessary to also 
kill Linda, but now there are no witnesses. You were smart
and left no finger prints. You feel very proud of youself
after smartly disposing of the bodies. You're tired, yet 
a little lonely. And maybe even a little guilty...

Do you...
A. Go home?
B. Go to your bestfriend's house?
"""

jumped_b = """
You decide to make a break for it. You leave the body and
you leave Linda standing their watching you. There was
obviously nothing else she could do as I was clearly much
bigger than her. The only way to escape was through the
window. It was a two story drop and you sprained your ankle.
Linda definitely saw your face. You have no time to think
about that now though. You have to get out of here.

Do you...
A. Steal a car?
B. Run on foot?
"""

go_home_a = """
You decide you did a good job, a good enough job to go home
and get some rest.

In the morning, more police arrive on the scene. Someone 
knocks on your front door. You have a bad feeling in your
gut but you push through. It's the police. Your jacket was
found at the scene of the crime.

"How could I have been so stupid?" You think to yourself.
"What do I say to them now?"

Do you...
A. Say Linda invited you over
one night and you left it?
B. Say you offered it to John
one cold and rainy day when he
forgot his umbrella?
"""

go_bff_b = """
You don't really feel like staying home. The police would be
arriving soon anyway. You decide to go to your friends
house for the evening.

They say you look terrible, "like you had just killed 
someone." After some nervous laughter, the guilt weighs in on
you and you confess everything to your friend. It was fine,
afterall, they were ride or die.

Were...

Shortly after you fall asleep, your friend calls the 
authroities. Your friend also caught a voice recording of
your confession. You messed up big time.

Your sentenced to life in prison.
You lose.
"""

steal_car_a = """
Because of your injured foot, you know you couldn't run far.
You steal a car. 

Yeah, you know how to hotwire cars.
What did you expect? You're definitely a lunatic.
Who kills their neighbor for being nice?
You, you messed up loon.

The car is loud and definitley suspisious, but what choice
do you have? You drive off. You somehow escaped in time 
before the police arrived.

Now you need to find a place to go.
Do you...
A. Flee the country?
B. Go stay with your family
for a little while?
"""

run_on_foot_b = """
Theres no time to steal a car. You have to make a run for it.
Despite having sprained your ankle, the adrenaline keeps you
going. You run for a long time before the pain in your ankle
becomes unbearable. Walking is ok now. You're far enough away
at this point. You walk for what feels like four hours before
your met with a crossroad.
Do you...
A. Take the tunnel into the city?
B. Continue to follow the long open
country road?
"""

linda_invited_you_a = """
You lie to the officers and claim that Linda had invited you
over to her house a few days ago. You burst into tears and
claim that Linda cam onto you, and you left so quick you 
forgot your jacket. 

The officers believe you but they ask that you come down to 
the station to take a lie test anyway.

Do you...
A. Agree to do the test and possibly 
get caught?
B. Not agree to the test and look
suspisious?
"""

john_borrowed_b = """
You lie to the officers and say that John forgot his umbrella
one day so you offered your jacket. You burst into tears
and cry over your lost "friend".

The officers believe you but they ask that you come down to 
the station to take a lie test anyway.

Do you...
A. Agree to do the test and possibly 
get caught?
B. Not agree to the test and look
suspisious?
"""

flee_country_a = """
You decide you need to get out of the country. Its an 18 
hour drive to the boarder.
Once you finally get there, you're noticed and immediatly
recognized, as Linda had caught a picture of your face.

You're arrested.
You lose.
"""

visit_fam_b = """
You decide its the perfect drive to surprise your mom 
and dad with a visit for the first time in years. You
hope they still love you after the incident.

You drive for 10 hours to get to their little house.
They see you pull in and call the cops.
They didn't still love you unfortunately.

You're arrested.
You lose.
"""

tunnel_a = """
The tunnel to the city looks promising. Maybe nobody will
recognize you. It's not like you've been to the city often
anyway. You walk for a few hours until you finally reach
Big City. You're exhausted. You need sleep.

Do you...
A. Go find a cheap hotel?
B. Find a bridge to sleep under?
"""

open_road_b = """
The long open road seems smarter. You're less likely to run
into anyone this way. Its a long, long, long walk. You may
have been walking for days for all you knew. You're
exhausted.

Just before nearly collapsing, you see a little town in
the distance. You start running out of joy. Once you make
it there, you eat and find a place to sleep. Its kind of
nice there and the few people of the town were quiet and
hostile. It was perfect. You now had to decide...

Do you...
A. Keep moving along the road?
B. Stay in the town and live out 
your life?
"""

agree_a = """
You agree to go to the station with the officers.
They escort you there and quickly set you up on the machine.
They ask you a few questions regarding the murder. You're
nervous but not enough to lose a grip. You're cool as a
cucumber, even under this pressure.

You pass! They let you go and that is the last you ever hear
the death of John and Linda.

You got away with murder.
"""

dont_agree_b = """
You don't know if you can pass, so you lie and tell the cops
you're actually busy at the moment and can't. They get 
suspicisous and you become a suspect.

The guilt and interrogations are starting to weigh on you.
You feel terrible and want to go home and be left in peace.
You really only have two options, confess or keep fighting.

Do you...
A. Confess to the murder?
B. Pay for a laywer with what little
you have?
"""

get_hotel_a = """
A hotel seems like the most comfortable option. You don't 
have much on you and choose a sketchy motel. You were 
desperate for a bed and a complimentary breakfast, even 
if its just cereal. You check in and fall onto the bed.

Turns out, news travels fast in the city. The woman at the 
desk recognized you from news she had seen earlier. She promptly
called the cops after you were out of site.

You were arrested.
You lose.
"""

bridge_b = """
A hotel is too risky and you're paranoid. You also have only
a little cash left on you. It's freezing but you find a bridge
and meet a few people also living under there. 

Some of the were homeless, but some of them were clearly some
kind if hippies or gypsies. You befriended them and they asked
if you'd like to accompany them on their travels. You really
like the bridge, but maybe they could get you out of here.

Do you...
A. Accept the hippies/gypsies offer?
B. Turn them down to stay under the
bridge?
"""

keep_moving_a = """
Despite your love for the town, you feel it is best to move on
and find a farther and hopefully safer place to be. You continue
on your long march down the country road that runs right through
the center of the town.

Days and days of walking and walking went by. They caught up to
you. You don't know how, but you do know you're tired. You
don't even struggle as you're handcuffed and put in the car.

You're arrested.
You lose.
"""

stay_b = """
The town is just too perfect for you in every way. You even met
a wondeful person who was serving your meal. Clearly this town
was pretty isolated from the rest of the world because you never
again heard the names John and Linda.

You got away with murder.
"""

turn_yourself_in_a = """
The guilt got to you. You confess. You tell the cops everything.
You know you'll go to jail, probably for life, but the guilt 
went away just a little.

You're arrested.
You lose.
"""

get_lawyer_b= """
You couldn't afford a great lawyer, but you did the best you
could with what you had. After months of trials and 
questioning, you won the case. By some miricle.

You got away with murder.
"""

go_hippy_a = """
You agree to travel with the hippies/gypsies. It wasn't a bad 
life. They even fed you. They were scary though, so you leaned
more towards them being gypsies. It was perfect. They protected
you until the end.

You got away with murder.
"""

no_go_hippie_b = """
You refuse their offer. They weren't dumb. They knew who you
were and what you had done. They promptely called the cops.
They were definitely gypsies.

You're arrested.
You lose.
"""

scenario_list = [
    (main_scenario, 1, 2), # 0
    (killed_linda_a, 3, 4), 
    (jumped_b, 5, 6), 
    (go_home_a, 7, 8), 
    (go_bff_b, -1, -1), # lose
    (steal_car_a, 9, 10), #5
    (run_on_foot_b, 11, 12), 
    (linda_invited_you_a, 13, 14), 
    (john_borrowed_b, 13, 14), 
    (flee_country_a, -1, -1), # lose
    (visit_fam_b, -1, -1), # lose #10
    (tunnel_a, 15, 16), 
    (open_road_b, 17, 18), 
    (agree_a, -1, -1), # win
    (dont_agree_b, 19, 20),
    (get_hotel_a, -1, -1), # lose #15
    (bridge_b, 21, 22), 
    (keep_moving_a, -1, -1), # lose
    (stay_b, -1, -1), # win
    (turn_yourself_in_a, -1, -1), # lose
    (get_lawyer_b, -1, -1), # win #20
    (go_hippy_a, -1, -1), # win
    (no_go_hippie_b, -1, -1) # lose
]

# asking for user input to allow player to create the characters
# story, allows customization
name = str(input("Enter your character's name: "))
street = str(input("Enter the name of the street your character lives on: "))
town = str(input("Enter the name of the town your character lives in: "))

# formating creates spaces and makes the output look cleaner
# and easier to read
def formating():
    print("      ")
    print("-----------------------------------------------------------------")
    print("      ")

# character is introduced using user input for name, town and street
def create_character():
    print ("Your name is " + name + ". You live on " + street + " street")
    print ("in the quiet town of " + town + ".")

# prints the initial introduction to the character in the story/game
formating()
create_character()

# assigns a value to y and x to avoid error message
x = 0
y = 0
current_scen = 0

def scenario():
    print(scenario_list[current_scen][0])

# main loop that runs the game
while x != "quit":
    scenario()
    
    if scenario_list[current_scen][1] == -1:
        break
    elif scenario_list[current_scen][2] == -1:
        break
    
    # after scenario runs, user answers the question until a vaild 
    # response is answered to the first question
    question_one = 0
    while question_one != "A" and question_one != "B" and question_one != "quit":
        question_one = str(input("A or B or quit? "))
        if question_one == "A":
            break
        elif question_one == "B":
            break
        elif question_one == "a":
            print("Please capitalize your response")
            continue
        elif question_one == "b":
            print("Please capitalize your response")
            continue
        elif question_one == "quit":
            break
        else:
            print("Invalid Response")
            continue
    
    
    if question_one == "quit":
        print("you quit!")
        break
    
    
    if question_one == "A":
        current_scen = scenario_list[current_scen][1]
    else:
        current_scen = scenario_list[current_scen][2]


formating()
print("Thanks for playing!")


