# CHARACTERS, Yes library is a character shut up

define ra = Character("Radio Announcer")
define e = Character("Ellie", color = "#0e6f0e")
define b = Character("Beatrice", color = "#322407")
define et = Character("Ellie's Thoughts", color = "#546849", what_color = "#848883")
define a = Character("Artie", color = "#104f7e")
define L = Character("Library")
define ed = Character("Edmund", color = "#572c25")
define v = Character("Vee", color = "#8b6113")
define r = Character("Room")

#Backgrounds

image bg bedroom = "BG BedRoom.png"
image bg hallway = "BG Hallway.jpg"
image bg kitchen = "BG Kitchen.jpg"
image bg library = "BG Library.jpg"
image bg office = "BG Office.jpg"
image bg outside mansion = "BG Outside Mansion.jpg"
image bg stairs = "BG Stairs.jpg"

#Characters Expressions sorry mahaba gays
image Ellie Normal = "Ellie Expr 1.png" 
image Ellie Surprised = "Ellie Expr 2.png"
image Ellie Mad = "Ellie Expr 3.png"
transform ellie_lower:
    zoom 0.70
    xalign 0.90
    yalign 0.25
image Beatrice Normal = "Bea Expr 1.png" 
image Beatrice Thought = "Bea Expr 2.png"
image Beatrice Mad = "Bea Expr 3.png"
transform beatrice_lower:
    zoom 0.70
    xalign 0.90
    yalign 0.25
image Arthie Normal = "Art Expr 1.png" 
image Arthie Thought = "Art Expr 2.png"
image Arthie Suprised = "Art Expr 3.png"
transform arthie_lower:
    zoom 0.70
    xalign 0.90
    yalign 0.25
image Vee Normal = "Vee Expr 1.png" 
image Vee Surprised = "Vee Expr 2.png"
image Vee Smug = "Vee Expr 3.png"
transform vee_lower:
    zoom 0.70
    xalign 0.90
    yalign 0.25
image Julian Normal = "Jul Expr 1.png" 
image Julian Smile = "Jul Expr 2.png"
image Julian Thought = "Jul Expr 3.png"
transform julian_lower:
    zoom 0.70
    xalign 0.90
    yalign 0.25
image Ed Normal = "Ed Expr 1.png" 
image Ed Sad = "Ed Expr 2.png"
image Ed Surprised = "Ed Expr 3.png"
transform ed_lower:
    zoom 0.85
    xalign 0.90
    yalign 0.25

# FOR uh, idk.. wait west wing! yeur six seven 

default west_wing_choice = ""
default kitchen_choice = ""
default path_choice = ""

# FOR SCENE 4! awooga

default room1_done = False
default room2_done = False
default room3_done = False


#okay lets fucking do this

label splashscreen:

    scene black

    show text "INSERT SPLASHSCREEN" at truecenter

    pause 5.0

    return


# SCENE 1: EXT. MOUSEWELL MANOR Setting: An elegant English country guesthouse stands amid a thick blanket of snow. The approaching blizzard threatens to isolate the manor from the outside world.


label start:
    
    scene bg hallway

    ra "Good eve Ladies and Gentle men, Twenty years ago, a great fire befell an orphanage, claiming nearly every soul within. Of all the children, but one survived."

    ra "Rumours later emerged that the orphanage's owner had abused the children and deliberately set the building ablaze to conceal his crimes. However, no conclusive evidence was ever found."

    ra "Two decades have passed, yet the mystery remains. What truly happened that night, and what does the sole survivor remember?"

    menu:

        "Someone must have been responsible.":
            show Ellie Mad at ellie_lower with dissolve

            e "Children do not simply perish in such numbers without cause. Perhaps the fire was only the beginning of something far worse."

        "Rumours are easy to spread when the dead cannot speak.":
            show Ellie Mad at ellie_lower with dissolve

            e "Perhaps the owner was a monster. Perhaps he was merely convenient to blame. I wonder what the surviving child remembers."

        "I wonder what became of the owner?":
            show Ellie Mad at ellie_lower with dissolve

            e "Did he ever answer for his alleged crimes? Or did he simply disappear into the world, leaving the dead behind?"

    jump scene_2


# SCENE 2: INT. BREAK ROOM_P2 Setting: A modest servants' break room sits away from the manor's elegant guest areas. Ellie rests beside a radio, enjoying a rare moment without demanding guests or impatient employers.

label scene_2:

    scene bg bedroom

    ra "An urgent weather advisory for residents across the surrounding counties. Heavy snowfall and strong winds are expected to worsen throughout the evening."
    ra "Residents are advised to remain indoors and avoid unnecessary travel until conditions improve."

    show Ellie Normal at ellie_lower with dissolve

    e "A snowstorm. Just what the household needed. At least it might give me some peace and quiet."

    menu:

        "At least the storm gives me an excuse to stay inside.":

            scene bg bedroom
            show Ellie Normal at ellie_lower with dissolve

            e "A little peace and quiet is hardly unreasonable. Though I doubt Mrs Ashcombe would agree."

        "I should stop before someone catches me.":

            scene bg bedroom
            show Ellie Mad at ellie_lower with dissolve

            e "Some people never listen to warnings. Then they expect everyone else to rescue them from their own stupidity."

        "Being trapped indoors with other people sounds dreadful.":

            scene bg bedroom
            show Ellie Mad at ellie_lower with dissolve

            e "Especially when everyone believes their time is more valuable than mine."

    e "Nobody pays much attention to a chambermaid. They notice clean sheets, polished furniture, and whether their tea arrives on time. The person responsible for all of it rarely matters."

    show Ellie Mad at ellie_lower with dissolve

    e "Perhaps that is why I prefer observing people rather than speaking to them. People leave little pieces of themselves everywhere: letters tucked beneath mattresses, drawers left unlocked, and belongings placed where they ought not to be."

    menu:

        "They should have hidden their secrets better.":

            show Ellie Normal at ellie_lower with dissolve

            e "Careless people make it remarkably easy. One would think they had nothing to hide."

        "I should stop before someone catches me.":

            show Ellie Normal at ellie_lower with dissolve

            e "Curiosity is hardly worth losing my position. A chambermaid without employment would have very little to look forward to."

        "I'm not hurting anyone. I'm only looking.":

            show Ellie Normal at ellie_lower with dissolve

            e "I put everything back where I found it. That must count for something."

    e "I ought to return to work. Mrs Ashcombe has little patience for idleness, and I have no desire to endure another lecture."

    jump scene_3


# SCENE 3: INT. HALLWAY The manors refined hallway is lined with dark wood panelling, polished floors, and framed portraits of stern-looking ancestors. The atmosphere reflects the household's strict standards. Ellie leaves the break room and turns into the hallway, only to encounter Beatrice Ashcombe, the elegant and exacting wife of Mousewell Manor's owner.

label scene_3:

    scene bg hallway

    show Beatrice Mad at beatrice_lower with dissolve

    b "Miss Pritchard. Your break has ended, I presume?"

    hide Beatrice Mad at beatrice_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve

    e "Yes, madam."

    hide Ellie Surprised at ellie_lower with dissolve
    show Beatrice Mad at beatrice_lower with dissolve

    b "Then what, precisely, are you going?"

    menu:

        "The Library":

            scene bg library

            show Ellie Surprised at ellie_lower with dissolve

            e "I intended to see whether anything required attention in the library, madam."

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Mad at beatrice_lower with dissolve

            b "The library is not a place for idle wandering. I have business in the west wing myself see that you attend to your duties, Miss Pritchard."

            show Beatrice Mad at beatrice_lower with dissolve

            b "(Beatrice turns and walks briskly down the hallway towards the west wing.)"

            hide Beatrice Mad at beatrice_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve 

            e "Books are apparently harmless until someone decides to read them. Still, there may be interesting things among those shelves."

        "The Kitchen":

            scene bg kitchen

            show Ellie Surprised at ellie_lower with dissolve
            e "I thought I might make myself useful in the kitchen, madam."

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Mad at beatrice_lower with dissolve

            b "See to your own responsibilities before concerning yourself with everyone else's."

            hide Beatrice Mad at beatrice_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve
            e "Initiative when convenient. Interference when it is not. One does begin to wonder whether there is a correct answer to anything in this house."

        "Straight to Work":

            scene bg hallway

            show Ellie Surprised at ellie_lower with dissolve

            e "I was returning to my duties, madam."

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Mad at beatrice_lower with dissolve

            b "See that you remain focused, Miss Pritchard. I expect the household to be maintained regardless of the weather."

            hide Beatrice Mad at beatrice_lower with dissolve
            show Ellie Mad at ellie_lower with dissolve

            et "People rarely reveal much when questioned directly. They become guarded, choose their words carefully, and pretend there is nothing worth knowing."

            et "But give them time to forget that anyone is watching, and the truth has a way of showing itself."

            et "Sometimes in the things they leave behind. Sometimes in the things they hide. And sometimes in the things they insist nobody should ask about."

            et "Perhaps that is why I have never been particularly good at minding my own business."

            jump scene_3C

    jump scene_3A


label scene_3A:

    scene bg library
    pause 2.0
    hide text

    L "The west wing is quieter than the rest of Mousewell Manor. Dim wall lamps illuminate the portraits and polished wooden doors lining the corridor. Outside, the snowstorm rattles the windows."

    e "(Ellie walks towards the library, her footsteps softened by the carpet. As she passes one of the private rooms, she hears a faint rustling sound from within, followed by the unmistakable turning of a page.)"

    show Ellie Surprised at ellie_lower with dissolve

    et "Someone is inside. Reading during the day, no less. I wonder what could hold their attention when everyone is supposed to be working."

    menu:

        "Listen Through the Door":

            $ west_wing_choice = "listened"

            show Ellie Surprised at ellie_lower with dissolve

            e "(Ellie leans closer to the door, careful not to make a sound. Through the wood, she hears the quiet turning of pages)"

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Normal at beatrice_lower with dissolve
 
            b "(Beatrice from Inside) Honestly, what dreadful writing. And yet, somehow, I cannot put it down"

            hide Beatrice Normal at beatrice_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve

            et "Mrs Ashcombe? Reading in secret? How very unlike her. I wonder what sort of book could hold her attention so thoroughly"

        "Look Through the Keyhole":

            $ west_wing_choice = "peeked"

            show Ellie Surprised at ellie_lower with dissolve
    
            e "(Curiosity gets the better of Ellie. She crouches and peers through the keyhole.)"

            e "(Inside, Beatrice sits comfortably in an armchair, absorbed in a book glancing cautiously towards the door as if ready to conceal it at the slightest sound.)"

            hide Ellie Surprised at ellie_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve

            et "Well, well. Mrs Ashcombe has a private interest after all. I wonder whether her husband knows what she reads behind closed doors."

            e "(Ellie quietly retreats before she attracts attention.)"

        "Open the Door":

            $ west_wing_choice = "opened"

            e "(Ellie slowly turns the handle and slips the door open, hoping to satisfy her curiosity without being noticed.)"

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Mad at beatrice_lower with dissolve

            b "Miss Pritchard!"

            hide Beatrice Mad at beatrice_lower with dissolve
            show Ellie Surprised at ellie_lower with dissolve

            e "(Ellie freezes. Beatrice sits in an armchair, a book clutched firmly in her hands)"

            e "Madam! I beg your pardon. I thought I heard something and wanted to make certain everything was in order."

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Mad at beatrice_lower with dissolve

            b "By entering a private room without permission? How reassuring to know that your duties now include trespassing."

            hide Beatrice Mad at beatrice_lower with dissolve
            show Ellie Surprised at ellie_lower with dissolve

            e "I apologise, madam. It will not happen again."

            hide Ellie Surprised at ellie_lower with dissolve
            show Beatrice Mad at beatrice_lower with dissolve

            b "See that it doesn't. Leave at once."

            e "(Ellie retreats and closes the door behind her)"

            hide Beatrice Mad at beatrice_lower with dissolve
            show Ellie Surprised at ellie_lower with dissolve

            et "That could have gone considerably better. Still, I did discover something. Whether it was worth the scolding is another matter"


    scene bg library
    show text "The library is a grand, wood-panelled room filled with towering bookshelves, leather-bound volumes, and the faint smell of old paper. A fireplace provides some warmth against the winter cold."
    pause 6.0
    hide text

    e "(Ellie enters the library and finds Arthur “Artie” Pembry, the shy librarian, struggling to balance a stack of books.)"

    show Arthie Suprised at arthie_lower with dissolve

    a "Oh! Goodness. Please excuse me. I thought I had them balanced properly."

    a "(One book slips from the stack. Artie fumbles to catch it, only to knock another book onto the floor.)"

    hide Arthie Suprised at arthie_lower with dissolve
    show Arthie Thought at arthie_lower with dissolve

    a "Right. That was entirely avoidable"

    hide Arthie Thought at arthie_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve

    e "Are you quite all right, Mr Pembry?"

    hide Ellie Surprised at ellie_lower with dissolve
    show Arthie Thought at arthie_lower with dissolve

    a "Yes, yes. Perfectly. I merely seem to have developed an unfortunate disagreement with these books."

    a "(He bends to retrieve them, nearly dropping the remaining stack.)"

    hide Arthie Thought at arthie_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    e "Perhaps they would cooperate if you carried fewer of them at once."

    hide Ellie Normal at ellie_lower with dissolve
    show Arthie Thought at arthie_lower with dissolve

    a "A sensible suggestion. I shall endeavour to remember it next time."

    hide Arthie Thought at arthie_lower with dissolve
    show Arthie Normal at arthie_lower with dissolve

    a "(He gives her an embarrassed smile before carefully placing the books on a nearby table.)"


    if west_wing_choice == "listened":

        menu:
            "Tell Artie what she heard.":

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "I happened to pass Mrs Ashcombe's room. She seemed rather engrossed in a book."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Thought at arthie_lower with dissolve

                a "Mrs Ashcombe? Reading? I should think she reads quite often."

                hide Arthie Thought at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "Not quite the sort of reading one would expect from her, perhaps."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Thought at arthie_lower with dissolve

                a "Oh. I see. Well, I suppose everyone has their private interests."

                hide Arthie Thought at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                et "Artie is remarkably good at pretending not to be curious. Not that he is particularly convincing."

            "Keep it to herself.":

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "Nothing worth mentioning. I was merely passing through the west wing."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Normal at arthie_lower with dissolve

                a "Right. Well, I hope you have a pleasant afternoon, Miss Pritchard."

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                et "Some secrets are best kept to oneself. Especially when sharing them serves no immediate purpose."


    elif west_wing_choice == "peeked":

        menu:
            "Tell Artie what she saw.":

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "You would hardly believe what I saw in the west wing. Mrs Ashcombe was reading a rather interesting book."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Thought at arthie_lower with dissolve

                a "Is that so? I should have thought she preferred something more... traditional."

                hide Arthie Thought at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "She certainly seemed keen to keep it private."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Thought at arthie_lower with dissolve

                a "Well, I suppose there is no harm in a little privacy."

                hide Arthie Thought at arthie_lower with dissolve   
                show Ellie Normal at ellie_lower with dissolve

                et "An agreeable response. A little too agreeable, perhaps. I wonder whether he is simply polite or knows more than he lets on."

            "Keep it to herself.":

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "I came across nothing unusual. I was simply making my way here."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Normal at arthie_lower with dissolve

                a "Then I shall not keep you. I imagine you have plenty of work waiting."

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                et "Best not to spread a discovery before I understand its value."


    elif west_wing_choice == "opened":

        menu:
            "Tell Artie about the incident.":

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "I made a rather embarrassing mistake in the west wing. I entered Mrs Ashcombe's room without permission."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Thought at arthie_lower with dissolve

                a "Oh, dear. Was she terribly cross?"

                hide Arthie Thought at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "Cross enough to remind me that doors are apparently there for a reason."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Thought at arthie_lower with dissolve

                a "Well, we all make mistakes. Though I would recommend knocking next time."

                hide Arthie Thought at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "A revolutionary idea, Mr Pembry."

                a "(Artie lets out a nervous laugh.)"

                e "At least someone in this house can laugh at an uncomfortable situation. Even if he does look as though he might apologise to the furniture for it."

            "Say nothing about it.":

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                e "Nothing of importance. I was just checking whether the library needed attention."

                hide Ellie Normal at ellie_lower with dissolve
                show Arthie Normal at arthie_lower with dissolve

                a "Oh, I see. Thank you for offering, though I believe everything is in order."

                hide Arthie Normal at arthie_lower with dissolve
                show Ellie Normal at ellie_lower with dissolve

                et "Mrs Ashcombe has already made her opinion perfectly clear. There is little sense in inviting another lecture."

    jump scene_3B


label scene_3B:

    scene bg library
    show text "Ellie glances towards the library door, remembering the encounter in the west wing. The manor has plenty of books, plenty of secrets, and an extraordinary number of people who prefer to keep both to themselves." at truecenter
    pause 8.0
    hide text

    show Ellie Normal at ellie_lower with dissolve

    et "People are peculiar creatures. They hide the most ordinary things as though they were priceless treasures, then wonder why others become curious."

    et "Still, I have work to do. And unlike secrets, work rarely waits patiently."

    hide Ellie Normal at ellie_lower with dissolve

    e "(Ellie bids Artie farewell and leaves the library. Making her way out of the west wing and across the main hall towards the east wing.)"

    e "(she turns the corner near the dining area and nearly collides with Edmund Ashcombe, who is carrying a pastry in one hand.)"

    show Ed Surprised at ed_lower with dissolve

    ed "Careful there, Ellie! Wouldn't want either of us losing our lunch."

    hide Ed Surprised at ed_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve

    e "My apologies, sir."

    hide Ellie Surprised at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Think nothing of it! Just the person I was looking for, actually."

    ed "(Edmund takes another bite of his pastry before continuing.)"

    ed "I need you to meet me at my office. There's a private matter we ought to discuss."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    e "Certainly, sir."

    hide Ellie Normal at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Splendid! Don't keep me waiting too long."

    ed "(Edmund continues down the corridor towards his office, leaving Ellie to follow)"

    hide Ed Normal at ed_lower with dissolve

    jump scene_3BKitchen


label scene_3BKitchen:

    scene bg kitchen
    show text "The east wing is quieter than the servants' quarters but less grand than the manor's main hall. Portraits hang along the walls, and the windows are clouded by frost as the snowstorm grows stronger outside." at truecenter
    pause 8.0
    hide text

    e "(Ellie makes her way towards the kitchen, hoping to finish her duties before the weather worsens. Something metallic catches her eye near the edge of the corridor.)"

    e "(She bends slightly and notices a cigarette lighter lying on the floor.)"

    menu:
        "Pick Up the Lighter":

            $ kitchen_choice = "PickUp"

            e "(Ellie picks up the lighter and examines it briefly before slipping it into her pocket.)"

            show Ellie Mad at ellie_lower with dissolve

            et "(Rather careless of someone. I shall keep it for now. Its owner may come looking for it.)"

            hide Ellie Mad at ellie_lower with dissolve
          

        "Leave the Lighter Behind":

            $ kitchen_choice = "LeaveBehind"

            e "(Ellie considers picking it up but decides against it, leaving the lighter where it lies.)"

            show Ellie Mad at ellie_lower with dissolve

            et "Not my responsibility. If someone cannot keep track of their own belongings, I see no reason to make it my problem."

            e "(Ellie continues down the corridor towards the dining area.)"

            hide Ellie Mad at ellie_lower with dissolve

    # INT. DINING AREA_P3B

    scene bg kitchen
    show text "The dining area is furnished with a long mahogany table, polished silverware, and elaborate china. Despite the elegance of the room, a half-finished plate of food and several crumbs suggest that someone has been enjoying a rather generous meal." at truecenter
    pause 8.0
    hide text

    ed "(Edmund Ashcombe, the owner of Mousewell Manor and Beatrice's husband, sits at the table, happily eating as though the approaching blizzard were a minor inconvenience.)"

    show Ed Normal at ed_lower with dissolve

    ed "Ah, Ellie! Just the person I wanted to see."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve 

    e "Good afternoon, Mr Ashcombe."

    hide Ellie Normal at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Good afternoon! Splendid weather we're having, isn't it? Well, perhaps not splendid for travelling. But there's something rather comforting about a good meal while the world freezes outside."

    ed "Now, I need you to come to my office later. There's a private matter I'd like to discuss with you."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    e "Certainly, sir. Is there anything I should prepare?"

    hide Ellie Normal at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Nothing at all! Just come by when you can. We'll have a little chat."

    ed "(Edmund wipes his mouth with a napkin, rises from his chair with his plate, and leaves the dining area with a cheerful hum.)"

    hide Ed Normal at ed_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    et "A private matter? How mysterious. Though, knowing Mr Ashcombe, it could concern anything from a missing document to the disappearance of his afternoon pudding."

    e "(As Ellie prepares to leave, a sudden clatter comes from the kitchen, followed by a muffled curse)"

    show Ellie Surprised at ellie_lower with dissolve

    et "That sounded expensive. Or painful. Possibly both."

    menu:

        "Investigate The Noise":

            $ path_choice = "kitchen"

            e "(Ellie turns towards the kitchen, deciding that a brief look cannot hurt.)"

            show Ellie Surprised at ellie_lower with dissolve

            et "I should make certain nobody has injured themselves. Besides, I would rather not explain why I ignored a commotion if something has gone wrong."

            hide Ellie Surprised at ellie_lower with dissolve

        "Go Straight to Edmund's Office":

            $ path_choice = "Office"

            e "(Ellie hesitates, then turns away from the kitchen.)"

            show Ellie Mad at ellie_lower with dissolve

            et "I'm expected at Mr Ashcombe's office. Whatever that noise was, someone else can attend to it."

            hide Ellie Mad at ellie_lower with dissolve

  
    if path_choice == "kitchen":

        scene bg kitchen
        show text "The kitchen is warm and bustling, with copper pots hanging above the counters and the smell of freshly prepared food lingering in the air. A large stove occupies one side of the room." at truecenter
        pause 8.0
        hide text

        v "(Vera “Vee” Collins, the manor's charismatic but notoriously rebellious receptionist, is crouched beside the stove. She struggles with its stubborn door while holding an unlit cigarette between her lips.)"

        show Vee Normal at vee_lower with dissolve

        v "Oh, come on, you miserable old thing. Open up!"

        v "(She gives the stove another pull. It refuses to budge.)"

        v "Wonderful. First the snow traps us all in this glorified museum, and now the stove has decided to join the rebellion."

        e "(Ellie steps into the kitchen.)"

        hide Vee Normal at vee_lower with dissolve
        show Ellie Normal at ellie_lower with dissolve

        e "Having some trouble, Miss Collins?"
        
        hide Ellie Normal at ellie_lower with dissolve
        show Vee Smug at vee_lower with dissolve

        v "Ellie! Just the woman I need. This wretched thing refuses to cooperate, and I've a cigarette that's beginning to feel neglected."

        v "(Vee gestures towards the stove, then notices Ellie looking at the cigarette.)"

        hide Vee Smug at vee_lower with dissolve


        if kitchen_choice == "PickUp":

            show Ellie Normal at ellie_lower with dissolve

            e "Is this what you're looking for?"

            hide Ellie Normal at ellie_lower with dissolve
            show Vee Smug at vee_lower with dissolve

            v "Well, would you look at that! My lucky day."

            v "(Vee takes the lighter and flicks it open.)"

            v "You may have just saved me from a very tragic afternoon."

            hide Vee Smug at vee_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve

            e "I hardly think a cigarette constitutes a tragedy."

            hide Ellie Normal at ellie_lower with dissolve
            show Vee Smug at vee_lower with dissolve

            v "Spoken like someone who has never had a decent smoke after a dreadful shift."

            v "(Vee lights her cigarette, takes a brief drag, and grins at Ellie.)"

            v "Remind me to repay you sometime. Preferably with something more interesting than a lighter."

            hide Vee Smug at vee_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve

            et "Vee has a remarkable talent for making even the smallest favour sound like the beginning of an adventure. I suspect that is how she gets herself into trouble."

            hide Ellie Normal at ellie_lower with dissolve

        elif kitchen_choice == "LeaveBehind":

            show Ellie Normal at ellie_lower with dissolve

            e "You do realise smoking near a stove is a health hazard, don't you?"

            hide Ellie Normal at ellie_lower with dissolve
            show Vee Smug at vee_lower with dissolve

            v "Health hazard? Ellie, darling, this stove is already trying to kill me. I hardly think a cigarette will make much difference."

            hide Vee Smug at vee_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve

            e "That is not particularly reassuring."

            hide Ellie Normal at ellie_lower with dissolve
            show Vee Smug at vee_lower with dissolve

            v "Neither is being lectured by someone who looks as though she'd apologise to a candle for blowing it out."

            v "(Vee chuckles and gives the stove one last unsuccessful tug.)"

            v "Besides, if worrying about my health kept me out of trouble, I'd have been unemployed months ago."

            hide Vee Smug at vee_lower with dissolve
            show Ellie Normal at ellie_lower with dissolve

            et "Vee has a reply for everything. It is a wonder Mrs Ashcombe has not dismissed her already. Though, from what I've heard, she has come remarkably close."

            v "(Vee finally gives up on the stove and straightens her uniform.)"

        hide Ellie Normal at ellie_lower with dissolve
        show Vee Normal at vee_lower with dissolve 
     
        v "Anyway, what brings you here? Surely you haven't come to admire my excellent work with kitchen appliances."

        hide Vee Normal at vee_lower with dissolve
        show Ellie Normal at ellie_lower with dissolve

        e "I heard a noise and thought I should check whether everything was all right."

        hide Ellie Normal at ellie_lower with dissolve
        show Vee Smug at vee_lower with dissolve

        v "Thoughtful of you. As you can see, I'm perfectly fine. The stove, however, may require professional intervention."

        hide Vee Smug at vee_lower with dissolve
        show Ellie Surprised at ellie_lower with dissolve

        e "I should be going. Mr Ashcombe asked me to meet him at his office."

        hide Ellie Surprised at ellie_lower with dissolve
        show Vee Smug at vee_lower with dissolve

        v "(Vee's expression shifts slightly at the mention of Edmund, though her smile remains.)"

        v "His office, is it? Well, don't let me keep you. Wouldn't want to leave the gentleman waiting."

        hide Vee Smug at vee_lower with dissolve
        show Ellie Normal at ellie_lower with dissolve

        e "Is there something I should know?"

        hide Ellie Normal at ellie_lower with dissolve
        show Vee Smug at vee_lower with dissolve

        v "Not a thing, darling. Just remember that when a gentleman says he wants a private conversation, it's usually best to listen carefully."

        v "(Vee takes another drag of her cigarette.)"

        hide Vee Smug at vee_lower with dissolve
        show Vee Normal at vee_lower with dissolve

        v "And try not to let him talk you into anything ridiculous."

        hide Vee Normal at vee_lower with dissolve
        show Ellie Surprised at ellie_lower with dissolve

        et "An oddly specific warning. Perhaps Vee knows something. Or perhaps she simply enjoys making ordinary conversations sound suspicious."

        e "(Ellie leaves the kitchen and heads towards Edmund's office.)"

        hide Ellie Surprised at ellie_lower with dissolve

        jump scene_3C

    else:

      
        e "(As Ellie walks through the manor, she recalls Edmund's invitation.)"

        show Ellie Surprised at ellie_lower with dissolve

        et "Mr Ashcombe wants a private conversation. Best not to keep him waiting."

        hide Ellie Surprised at ellie_lower with dissolve

        jump scene_3C


# SCENE 3C: THE OFFICE 

label scene_3C:

    # INT. EDMUND'S OFFICE_P3C

    scene bg office
    show text "Edmund's office is a spacious room furnished with dark wooden shelves, a large desk, and leather-bound folders. Despite its respectable appearance, the room is somewhat cluttered with papers, personal belongings, and a half-finished cup of tea." at truecenter
    pause 8.0
    hide text

    ed "(Edmund sits behind his desk, finishing the last bite of his pastry. He gestures for Ellie to take the chair opposite him.)"

    show Ed Normal at ed_lower with dissolve

    ed "Come in, Ellie! Have a seat. Tea? No? Very well, then."

    ed "(He sets his plate aside and leans back in his chair.)"

    hide Ed Normal at ed_lower with dissolve
    show Ed Sad at ed_lower with dissolve

    ed "Now, I'll get straight to the point. One of our guests has reported a missing possession. Something rather valuable, I'm told."

    hide Ed Sad at ed_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve

    e "Has it been misplaced, sir?"

    hide Ellie Surprised at ellie_lower with dissolve
    show Ed Sad at ed_lower with dissolve

    ed "Possibly. Though our guest seems convinced that it has disappeared entirely. And given the circumstances, we cannot afford to take the matter lightly."

    ed "This guest is someone of considerable importance. Their satisfaction is essential to the reputation of Mousewell Manor. If word gets out that we cannot safeguard our guests' belongings, it could cause considerable trouble for the household."

    hide Ed Sad at ed_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve

    e "I understand, sir. Would you like me to search the rooms?"

    hide Ellie Surprised at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Precisely! You see, Ellie, you're rather well-liked around here. The guests find you pleasant, dependable, and easy to talk to. They seem comfortable around you."

    ed "(Edmund smiles, pleased with his own reasoning.)"

    ed "I thought you might be the ideal person to look into this matter. You know the rooms, you know the staff, and you have a knack for noticing things that others overlook."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Mad at ellie_lower with dissolve

    et "That's an interesting way of putting it. I wonder what else he knows about me."

    hide Ellie Mad at ellie_lower with dissolve

    ed "(Edmund folds his hands on the desk.)"

    show Ed Normal at ed_lower with dissolve

    ed "Of course, I also know about your little habit, Ellie."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve

    e "My habit, sir?"

    hide Ellie Surprised at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Your curiosity. The occasional look through a drawer, a letter left unattended, a guest's belongings when you think nobody is watching."

    hide Ed Normal at ed_lower with dissolve    
    show Ellie Surprised at ellie_lower with dissolve

    e "(Ellie's expression stiffens.)"

    hide Ellie Surprised at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Please, don't look so alarmed. I'm not particularly interested in making a fuss over it. But I do believe your curiosity might prove useful for once."

    hide Ed Normal at ed_lower with dissolve 
    show Ellie Surprised at ellie_lower with dissolve

    e "Sir, I assure you, I have never intended to cause any trouble."

    hide Ellie Surprised at ellie_lower with dissolve
    show Ed Sad at ed_lower with dissolve

    ed "And I would prefer to keep it that way. You understand, of course, that this household has standards to uphold. If I discover that you've been snooping again without a good reason, I may have no choice but to dismiss you."

    ed "(He pauses, allowing the threat to settle before returning to his pleasant tone.)"

    hide Ed Sad at ed_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "However, if you help me recover this possession, I am perfectly willing to overlook certain indiscretions. Consider it an opportunity to put your talents to better use."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Mad at ellie_lower with dissolve

    et "So that is the arrangement. My job in exchange for a favour. How generous of him to give me a choice when he has already decided the answer."

    hide Ellie Mad at ellie_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    e "I understand, Mr Ashcombe. I'll do what I can to find the missing possession."

    hide Ellie Normal at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Splendid! I knew I could count on you."

    ed "(Edmund rises from his chair and reaches for his plate, apparently satisfied that the matter has been settled.)"

    ed "I'll provide you with whatever information I can. For now, keep your eyes open and speak to anyone who might know something. And, naturally, discretion is essential."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve 

    e "Of course, sir."

    hide Ellie Normal at ellie_lower with dissolve
    show Ed Normal at ed_lower with dissolve

    ed "Excellent. Off you go, then. I have every confidence you'll manage this beautifully."

    hide Ed Normal at ed_lower with dissolve
    show Ellie Mad at ellie_lower with dissolve

    e "(Ellie stands and makes her way towards the door.)"

    et "A valuable possession, an important guest, and a threat hanging over my head. I had hoped for an uneventful afternoon. It seems Mousewell Manor has other plans."
    
    e "(She leaves Edmund's office and returns to her duties, now burdened with a task she never asked for.)"

    hide Ellie Mad at ellie_lower with dissolve

    jump scene_4

    # END OF SCENE 3C

label scene_4:

    #fuck this scene yo I hate you Nitro

    scene bg hallway
    show text "The hallway stretches across the guest wing, illuminated by warm wall lamps. Beyond the windows, snow continues to fall, covering the manor grounds in white. Ellie stands beside a small service table, checking her list of duties." at truecenter
    pause 6.0
    hide text

    scene bg hallway 
    show text "Ellie unfolds her to-do list and runs a finger down the page. Three guest rooms remain to be tended to, each requiring a different amount of work." at truecenter
    pause 6.0
    hide text

    show Ellie Mad at ellie_lower with dissolve

    et "Three rooms to clean, a missing possession to find, and Mr Ashcombe's threat hanging over my head. One would think working here would be enough trouble without being given an additional investigation."

    e "(She looks down at the list again.)"

    hide Ellie Mad at ellie_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    et "I ought to begin somewhere. The sooner I finish my duties, the sooner I can look into this business with the missing possession."

    hide Ellie Normal at ellie_lower with dissolve

    scene bg bedroom
    show text "This room is noticeably messier than the first. Clothes lie across a chair, papers are scattered over the desk, and various discarded items clutter the floor." at truecenter
    pause 6.0
    hide text

    label guest_rooms:

   
    if room1_done and room2_done and room3_done:
        jump after_guest_rooms

    scene bg bedroom
    show text "Ellie must inspect the guest rooms and finish her duties before proceeding." at truecenter
    pause 4.0
    hide text

    menu:
        "Room 1: A Relatively Tidy Guest Room" if not room1_done:
            call guest_room_1
            jump guest_rooms

        "Room 2: A Messy Room with Items to Discard" if not room2_done:
            call guest_room_2
            jump guest_rooms

        "Room 3: A Disorganized Room with Misplaced Belongings" if not room3_done:
            call guest_room_3
            jump guest_rooms






label guest_room_1:

    scene bg bedroom
    show text "The guest room is neat and well-maintained. The bed is properly made, the curtains are drawn, and the furniture is arranged with care. Only a few scattered belongings and minor imperfections remain." at truecenter
    pause 6.0
    hide text

    e "(Ellie enters with her cleaning supplies and surveys the room.)"

    show Ellie Normal at ellie_lower with dissolve

    e "Someone has been rather considerate. This should not take long."

    e "(She begins tidying the room when she notices an object that appears out of place.)"

    et "Now, what have we here? I ought to have a closer look."

    menu:
        "Inspect the object":
            
            et "Interesting. A small detail, perhaps, but details have a habit of becoming important when one knows where to look."

            e "(She examines the object before putting it back where she found it.)"

        "Leave the object alone":
            et "Perhaps I should leave it where it is for now. I have other duties to attend to."

            e "(Ellie leaves the object untouched and continues cleaning.)"

    hide Ellie Normal at ellie_lower with dissolve

    e "(Ellie finishes the remaining cleaning.)"

    show Ellie Normal at ellie_lower with dissolve

    e "One room finished. Two more to go."

    hide Ellie Normal at ellie_lower with dissolve

    $ room1_done = True

    return





label guest_room_2:

    scene bg bedroom
    show text "This room is noticeably messier than the first. Clothes lie across a chair, papers are scattered over the desk, and various discarded items clutter the floor." at truecenter
    pause 6.0
    hide text

    e "(Ellie enters and pauses at the sight of the room.)"

    show Ellie Surprised at ellie_lower with dissolve

    e "Good heavens. One might think the occupant had been searching for something in a hurry."

    e "(She begins gathering the clutter, separating rubbish from the guest's belongings. Among the mess, she notices an object that catches her attention.)"

    et "Some things are best thrown away. Others might prove useful, depending on what one intends to do with them."

    hide Ellie Surprised at ellie_lower with dissolve

    menu:
        "Discard the object":
           

            e "(Ellie picks up the object and throws it away.)"

            show Ellie Normal at ellie_lower with dissolve

            et "An object can be more than a possession. Discard it, and it may no longer serve its intended purpose. Naturally, one ought to have a reason for doing so."

            hide Ellie Normal at ellie_lower with dissolve

        "Leave the object alone":
           

            e "(Ellie decides to leave the object alone and returns to her housemaid duties.)"

            show Ellie Mad at ellie_lower with dissolve

            et "It may be better to leave it where it is until I know whether it serves any purpose."

            hide Ellie Mad at ellie_lower with dissolve

    e "(Ellie resumes her work, clearing the floor and arranging the remaining belongings.)"

    show Ellie Normal at ellie_lower with dissolve

    e "Much better. At least the room is beginning to resemble a place where a person actually lives."

    et "Still, I should remember what I found here. One never knows when an apparently useless object might become important."

    hide Ellie Normal at ellie_lower with dissolve

    $ room2_done = True

    return






label guest_room_3:

    scene bg bedroom
    show text "The third room is neither particularly dirty nor entirely tidy. A chair sits at an awkward angle, a book has been left on the wrong shelf, and several personal belongings are scattered around the room." at truecenter
    pause 6.0
    hide text

    e "(Ellie enters and studies the disorder.)"

    show Ellie Mad at ellie_lower with dissolve

    e "Not quite a mess, but certainly not in order. Somehow, I suspect this will take longer than it ought to."

    e "(She begins putting things back in their proper places. As she works, she considers how easily an object can be moved without its owner noticing.)"

    hide Ellie Mad at ellie_lower with dissolve
    show Ellie Normal at ellie_lower with dissolve

    et "People grow accustomed to their surroundings. They expect their belongings to be where they left them. It is remarkable how much can change when something is moved."

    hide Ellie Normal at ellie_lower with dissolve

    menu:
        "Plant an object":
            scene bg bedroom
            show text "Ellie considers whether to place an object in the room or leave everything as she found it." at truecenter
            pause 4.0
            hide text

            show Ellie Normal at ellie_lower with dissolve

            et "An object placed in the right room might appear perfectly ordinary. After all, people tend to trust what they find in familiar surroundings."

            hide Ellie Normal at ellie_lower with dissolve

            menu:
                "Plant the object":
                  

                    e "(Ellie places the selected object in the room, potentially affecting what its occupant or another person might discover.)"

                    show Ellie Normal at ellie_lower with dissolve

                    et "There. Someone might notice it, or they might never give it a second thought."

                    hide Ellie Normal at ellie_lower with dissolve

                "Leave things as they are":
                    

                    e "(Ellie decides not to plant anything and leaves the room's belongings undisturbed beyond the cleaning required.)"

                    show Ellie Normal at ellie_lower with dissolve

                    et "Sometimes, it is better not to interfere."

                    hide Ellie Normal at ellie_lower with dissolve

        "Leave things as they are":
          

            e "(Ellie straightens the furniture and returns the misplaced items to their proper places.)"

            show Ellie Normal at ellie_lower with dissolve

            e "There. A little order makes all the difference."

            et "Of course, there is a difference between putting things where they belong and putting them where someone expects them to be. A useful distinction, under the circumstances."

            hide Ellie Normal at ellie_lower with dissolve

    e "(Ellie finishes cleaning the room.)"

    $ room3_done = True

    # END OF SCENE 4!

    # INT. HALLWAY 4

    scene bg hallway
    show text "Having finished all three guest rooms, Ellie gathers her cleaning supplies and checks her to-do list one last time." at truecenter
    pause 6.0
    hide text

    show Ellie Normal at ellie_lower with dissolve
    
    et "(Finally. Every room accounted for, every task completed. Now, if Mr Ashcombe has no further demands, I might actually enjoy a moment's peace.)"

    e "(Ellie makes her way towards the storage room to return her supplies and end her shift. As she approaches the door, something catches her eye.)"

    e "(A dark red liquid seeps from beneath the door, spreading slowly across the floorboards.)"

    hide Ellie Normal at ellie_lower with dissolve
    show Ellie Surprised at ellie_lower with dissolve
    
    e "What on Earth..?"

    e "(She steps closer, staring at the growing pool of blood. For a moment, she considers calling for help. Instead, she cautiously reaches for the handle.)"

    et "Please, let this be something else."

    e "(Ellie slowly opens the door, it's fucking Robert Downey Jr.)"

    et "IS THAT IRON MAN????"

    # END OF PROLOGUE!

    return

    

  
    
   