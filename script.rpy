# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("narration")
define mr= Character("Mr. Jade")
define ms= Character("Mrs. Jade")
define b= Character("Baroness Burgundy")
define l= Character("Lady Lavander")
define cb= Character("Colonel Cobalt")
define dr= Character("Doctor Indigo")
define cr= Character("Countess Coral")
define i= Character("Madame Ivory")
define a= Character("all")

$ letter = false
$ tree = false
$ fuse = false

$ clues = []

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    n "You are driving up a precarious hillside at sunset, the beautiful glow of the evening light through the trees almost— though not quite— offsetting the discomfort of guiding your car around the tight switchback corners of the half-paved mountain road."
    n  "You and your wife, Mrs. Jade, have been to the mansion that lies at the top of this road a few times before, but the drive never gets any easier. It was inherited years ago by your close friend," 
    n "who writes mystery novels under the pseudonym Baroness Burgundy, and tonight she has invited you and several other mystery-loving friends to join her for a murder mystery themed party to celebrate the major publishing deal she has just signed for her newest book." 
    n "She doesn’t need the money, but you’re happy for her all the same."

    n "As you and your wife slowly ascend the mountain, the growing altitude presses on all of your senses. The air through the open car windows, which moments ago was warm with the dying sunbeams, grows thin and howls hauntingly through the trees,"
    n "piercing your thin coat with a biting chill. You roll up the windows against the suddenly-sharp lash of wind as you crest the hill and leave behind the arched tunnel of trees that had blocked your view for most of the drive up"

    n "The unpleasantness of the weather aside, the view is well worth it. You see a vast mountain range robed in emerald evergreen trees. A silver river traces its way through the valleys far below. Somewhere past the craggy cliffs to your west lies the city you left just an hour ago, but it’s" 
    n "difficult to imagine there are people anywhere nearby. The forest you can see from this mountaintop looks ancient and untouched, and the only sign of human activity in sight is the mansion you now find yourself pulling up in front of."
   
    mr "I hope the drive is going to be worth it. Don’t get me wrong— the nature is lovely, but there is only so long someone can look at the same trees. Not to mention, it’s been what, four years since her last “publishing party”? I haven’t seen any of these people in a long while. This book had better be a damn masterpiece,"
    mr "keeping us waiting so long after that cliffhanger in the last one…"

    mr "Also, I can’t help but wonder about this “single color” dress code, it seems a bit silly. Not that I am complaining, dear, I think we pulled it off."

    ms "Hey, with that mindset, you won’t be satisfied even if the book is perfect. Just try to keep an open mind. Having any resolution would be good at this point for the series," 
    ms "I think it puts too much stress on the baroness trying to live up to the success of the original book and she feels like she has to keep one upping herself each book and at a certain point it takes a toll." 
    ms "So, whatever comes of the books let's just look around at these… beautifully similar trees. There is some truly pristine nature all around us. Let’s just stop worrying about what could or couldn’t go wrong and just focus on what you have now."

    n "Mrs. Jade leans in for a quick peck on the lips as you navigate the car into a line of others in front of the massive mansion."

    mr "Thanks, darling. You always know just what to say."

    n "As you park the car and climb out, the host— your friend— Baroness Burgundy appears in the doorway, silhouetted against the lights inside, which outshine the quickly dimming glow of the last sliver of sun visible over the verdant peaks. She curtseys dramatically, then gestures for you both to join her inside."

    b "Please, do come in. I hope the drive was not too troublesome."

    mr "Well, with great company it wasn’t so bad."

    b "I’m glad to hear that. Well, with you both here, that should be everyone. Now that you are all here I will address my cryptic emails. I wanted to keep everything a surprise until my book was complete, and I didn’t want to have to draft any non-disclosure contracts. But now that it is off to print, I don’t have to worry." 
    b "So, what better way to celebrate finally being done than bringing back an old tradition, a murder mystery party!"

    a "Shocked murmuring<i>italics</i>"

    b "The reason I had everyone dress a specific color is so we can deduct an in person investigation. The person who solves my mystery at the end will take home their own custom leather-backed signed author’s edition of my new book. Since I write under the Burgundy pseudonym,"
    b "I thought it was only fair if everyone had their own color, too! For tonight, let’s refer to each other only by the character names I had you pick! Oh, this will be so much fun. Dinner will be served shortly so take this time to catch up with each other."

    $ talked = []
    menu intro:
        "Lady Lavender":
            ms "Hey, how’s it going? It’s been forever! I am sure Burgundy has been putting you through the editorial equivalent of a meat grinder. I know her books are never small."
            l "Actually, about ¾ of the way through it just stopped feeling fun and felt like a chore and I knew something had to change. And I figured I have been correcting stories for long enough I wanted to make my own. How about you?"
            mr "Oh! I had no idea. I’m sorry to hear that you aren’t working with Burgundy anymore, but I suppose it’s wonderful that you’re pursuing your own dreams. Are you sticking with the same genre, or…?"
            l "Oh yes, I do plan to stick with mystery. “The devil you know”, right? It’s been the main thing I’ve read for so long, I’m not sure I’d know how to read a different sort of book— much less write one. I’m working on a proper murder mystery right now,"
            l "actually… maybe Burgundy’s event this evening will make for good inspiration!"
            ms "We can only hope. It was nice chatting like this. I’ll catch up with you some more at dinner. In the meantime there are other guests I would like to meet."
            $ talked.append("l")
            jump intro
        "Colonel Cobalt":
            mr "Evening, “Colonel Cobalt”. Nice color choice, by the way. How’ve you been?"
            cb "Ah, the same, the same. Finally got that escape room business off the ground, though let me tell you, it’s excruciating to watch people figure out the answers you already know."
            mr "Oh, that’s good to hear! You’ve been talking about that for ages. Last time we got together, I remember you musing on an idea for one of the rooms, right? Something about a wine cellar under an old shop…"
            cb "Ah, haha, yeah. I didn’t end up getting to use that one. Baroness Burgundy over there actually ended up adapting it for one of her short stories about two years back, before I even started constriction for the escape rooms! She did it more justice than I could have, though."
            ms "Ah, now I know which book you’re talking about! I had no idea you had a hand in creating that one. It was a good one!"
            cb "Yes, yes, but it was Burgundy who brought it to life, not me. Anyway… I’m off to go mingle some more. You should do the same."
            $ talked.append("cb")
            jump intro
        "Doctor Indigo":
            dr "Well good evening to you two! Don’t you both just look positively dashing in emerald."
            mr "Why thank you— though, actually, it’s “Jade”."
            dr "Well haven’t I just stuck my foot in it. I could just about die of embarrassment. A pleasure to “meet” you, Mr. and Mrs. Jade"
            ms "Haha, don’t get too worked up about it. I have to say, you’ve pulled together a lovely outfit yourself, to nobody’s surprise. Where did you even find a monocle, much less an indigo one?"
            dr "Why yes, yes I am. For my next trick, I’ll make this cocktail disappear! Haha. Goodness, I need a drink. I swear, Burgundy over there has me in my cups— she’s been going out to seedy parts of town for inspiration, putting herself in danger just so she can “Feel what her characters would feel.”"
            dr "I don’t care if it’s how she “connects with her inner murder victim,” she's gonna get killed if she keeps this up. If she doesn't stop, I'm gonna have to slap some sense into her myself! Haha."
            ms "That does sound… rough. You enjoy that drink, then. I’d guess that it’s “just what the doctor ordered”?"
            dr "Oh my darling Jade, you crack me up. Go! Mingle. I’m going to go write myself a prescription for another one of these."
            $ talked.append("dr")
            jump intro
        "Countess Coral":
            cr "Ah! Good evening. So glad to see you made the drive safely, that hill certainly never gets any easier. I mean, honestly, that’s why I never visited her out here."
            ms "Sorry, “Her”?"
            mr "Oh, sorry dear. I should have told you before we got to the party. You see, Countess Coral here was dating Burgundy for a while, and—"
            cr "And we parted about two weeks ago. Amicably."
            ms "Oh, I’m so sorry to hear that. I’ve been through that before. You call me if you need anything, alright?"
            cr "Thank you, that means a great deal. But I will be fine, I assure you. I just… need some time. It’s certainly not the best atmosphere for a party. I’m sorry, I’ve ruined the mood now, haven’t I?"
            ms "No, darling, not at all. Why don’t you take a minute to collect yourself— we’ll keep mingling."
            cr "Thank you, love."
            $ talked.append("cr")
            jump intro
        "Madame Ivory":
            mr "Hey! Coral! It’s been too long."
            i "I couldn’t agree more! We simply have to find reasons to get together that aren’t centered around my sister’s newest publications. And perhaps somewhere a bit less isolated, eh? Not that this isn’t a lovely house, of course. But I don’t know how she keeps up with it— I’d have sold it right off the bat."
            ms "And miss out on all these views?"
            i "And miss out on all these storms. And driving most of an hour anytime I want to make a grocery run. Honestly, I will never understand why she adores the place so much."
            mr "Well, if nothing else, it makes for an atmospheric mystery setting?"
            i "That’s true enough, I suppose. But lord, look at the size of this place. Think of the dust."
            mr "You’ve got me there, I suppose."
            i "Still, I guess there are family memories here that wouldn’t be easy to move… I’m glad that she likes it here, even if I don’t see it. Though, just think of the views you could get from a city penthouse if you sold off this crusty old house!"
            ms "That’s why there’s two of you sisters, I suppose. One to like the country, one to like the city. Like that story with the two mice—"
            i "Ugh! Mice. Another reason not to live in the middle of nowhere."
            ms "Well, we might as well do our best to enjoy it while we’re here. We’re going to mingle some more, but we’ll keep an eye out for any stray critters!"
            i "Don’t even joke about it."
            $ talked.append("i")
            jump intro
        "Stop socializing":
            if len(talked) >= 5:
                jump out
            else:
                n "You haven't talked to everyone yet."
                jump intro
    label out:
#LIGHTS OUT: THE “MURDER”
    n "Abruptly, everything seems to flash white. Lightning, just outside the house, followed immediately by a deafening peal of bone-shaking thunder. You duck instinctively, hearing the cut-glass decanter Mrs. Jade was holding shatter agaisnt the ground next to you. You register a few sensations at once— alcohol," 
    n "soaking your left shoe and probably part of your coat— screaming, a few voices in discordant carol— clatters and footsteps, muddled and indistinguishable— quieter voices, calmer, murmuring something you can’t make out— starlight through the window— and then the lights return."
    n "You stand back up slowly, looking around at everyone else in the room, the frantic noise of a few moments ago fading to silence. “Check on Burgundy, she hates storms” someone said (you aren’t sure who), so you latch on to the instruction and walk into the kitchen, halting in the doorway when you see it."
    n "Burgundy’s body, laid out haphazardly against the cold tile of the floor. Still. You think for a moment that this was all part of the plan, that this is the mystery she had prepared for you, but as Mrs. Jade joins you in the doorway you feel in your gut that this is real."
    n "You kneel for a moment beside Burgundy, just long enough to feel for a pulse, and (finding none) stumble backwards into the room."
    n "Cobalt is already at the landline near the front door, evidently on the phone to the police."

    cb "Yes, a murder. I’m certain. I don’t know the address— it’s the big house up in the mountains— yes, that’s the one."
    define p = Character("Phone")
    p "..."
    cb "You don’t understand, we need someone here now! Yes— yes— I know there’s a storm, I know the roads aren’t great, but there’s been a murder!"
    p "..."
    cb "Oh, what good are you! Yes, send officers as soon as it’s clear. Fat lot of good it’ll do us if we all get murdered."
    p "..."
    cb "Sorry, ma’am. That was uncalled for. I suppose I might be just a bit in shock. Yes ma’am. We’ll wait out the storm here, then."
    n "<i>Cobalt hangs up the phone</i>"
    cb "Well, they can’t send anyone up into the mountains until the rain clears up a bit— the downside of living on the up-side, haha. Sorry, that was terrible."

#Investigation begins

    ms "Well, we can hardly just sit here and twiddle out thumbs til they arrive. I propose we figure out what happened, so that if one of us here is the murderer, we can… I don’t know. Lock them in the basement."
    dr "That’s all well and good, but how can we trust you or Mr. Jade? You could have done it yourselves, and now you’re trying to cover it up by pretending to investigate the rest of us!"
    ms "ndigo. First off, I know you don’t believe that either of us could have done this. You’re just playing devil’s advocate— but you’re right. Look, Mr. Jade’s shoes and coat are half-soaked with whiskey. I dropped the decanter, the shards are over there,"
    ms "and there’s only one trail of wet footprints leading to each of us. We didn’t move until the lights were on. Satisfied?"
    dr "Very much so, yes. Thank you. Do carry on."
    mr "Okay, everyone, split up. We’ll talk to you all separately, so we can figure out what really happened."

#Character Scenes
    $ end = []
    
    menu character:
        "Lady Lavender":
            mr "Okay, Lavender, we need to talk about what happened during the blackout."
            l "Oh my gosh, I swear I didn’t do it, I wasn’t even in the room, and even if I were in the room I never would have done anything like this, I swear,"
            l "I swear, you have to believe me that I’d never lay a hand on Burgundy or anyone else for that matter and I promise I didn’t do anything and I can’t believe she’s really dead and—"
            ms "Shh, shh, it’s okay. Take some deep breaths, honey. In and out. Real slow. That’s it, just breathe. We aren’t trying to say anyone did anything, not yet. We just want to talk."
            l "I… okay. In and out. I can do this. What do you need to know?"
            $ lav = []
            menu lave:
                "What did you do when the lights went out?":
                    l "Well, first I screamed— I’m sure you heard me, I was so surprised— and then I thought I remembered a candelabra in the corner, so I went to see if I could grab one of those candles."
                    l "Not sure what I meant to light it with, though… thank goodness the lights came back on before I had to figure out where Burgundy keeps, er, kept, her matches."
                    $ lav.append("what")
                    jump lave
                "Did you see or hear anything?":
                    l "I don’t think so. Some other people screamed when the lights went out, I think, but that’s not exactly helpful. I guess I was mostly just focused on getting some light. By the time my eyes adjusted enough to see in the faint moonlight, someone had already gone and fixed the lights."
                    $ lav.append("did")
                    jump lave
                "Did you have any reason to wish Burgundy harm?":
                    l "No, not at all! I know we had a bit of a fight when I quit as her editor, but that’s all in the past! We’ve actually been writing each other letters— I bet she has the letters I sent to her somewhere around here." 
                    l "Those would prove that we’re close again! I swear I’d never do anything to hurt her. I just needed some creative freedom, that’s all."
                    $ lav.append("wish")
                    jump lave
                "That's all":
                    if len(lav) >= 3:
                        ms "Thank you, dear. That’s all the questions we had to ask."
                        $ end.append("lav")
                        jump out1
                    else:
                        n "You haven't asked all of your questions yet."
                        jump lave 
            label out1:
#can find letters now in kitchen                
        "Colonel Cobalt":
            cb "Hey, Mr. and Mrs. Jade. Wow, that’s a mouthful. You know, I really appreciate you stepping up to figure things out here. For all the time I spend locking people up and making them solve mysteries, I find it’s not nearly as fun when it happens to you in real life, huh?"
            mr "You could certainly say that. We’ll try to get this sorted as soon as possible. Now, do you mind if we ask you a few questions?"
            cb "Not at all. Ask away, what do you need to know?"
            $ cob = []
            menu coba:
                "What did you do when the lights went out?":
                    cb "Let me think. I was scoping out a seat at the dining table– you know I hate to sit on the ends, so I wanted to get first pick, you see."
                    cb "I was just setting down my bag on a seat when the lights went out. I dropped my bag, then, and some things spilled out, so I set to picking them up so nobody would slip on them."
                    cb "Everything’s back in my bag now, though, so I suppose I have no way to prove that."
                    $ cob.append("what")
                    jump coba
                "Did you see or hear anything?":
                    cb "Hm, I’m not sure. There was some yelling at the start, that’s for sure— I think someone here must be very afraid of lightning. In any case, I guess that once my eyes were adjusted to the dark, I was just looking for all the pens that spilled out of my bag."
                    cb "I think I might have too many pens… didn’t realize they could be a hazard."
                    $ cob.append("did")
                    jump coba
                "Did you have any reason to wish Burgundy harm?":    
                    cb "Oh hell, absolutely not! I could never. I mean, literally, I could physically never do that. Not that I’d ever try, but I mean… I er, don’t like to show this to people, but about a decade back, I messed up in the workshop and, well. Look for yourself."
                    n "Cobalt peels off one of his gloves to reveal a prosthetic hand. He moves it around a little, demonstrating that while he can use it for simple tasks like picking things up or eating, it doesn’t have the range of motion or strength to have strangled Burgundy. He smiles weakly, shrugging."
                    cb "So, yeah. I couldn’t have done it, even if I’d wanted to. Which I didn’t. Obviously. But even if I did."
                    $ cob.append("wish")
                    jump coba
                "That's all":
                    if len(cob) >= 3:
                        ms "Thank you for showing us this. We’ll keep looking"
                        $ end.append("cob")
                        jump out2
                    else:
                        n "You haven't asked all of your questions yet."
                        jump coba 
            label out2:    
                
        "Doctor Indigo":
            ms "Hey there, Dr Indigo. Do you mind if we—"
            dr "Ask me a few questions? Not at all. I hoped you would, in fact. You see, I am innocent, and would love to get that proven and out of the way post-haste, so that we can focus on finding the actual murderer."
            mr "Okay then, let’s get started."
            $ jad= []
            menu ind:
                "What did you do when the lights went out?":
                    dr "Well, last time I was up here visiting Burgundy, I tried to use the oven, but the fuse for that part of the kitchen was blown. Who knows how long she’d left it like that— goodness knows I’m the only one who ever bakes anything in this house."
                    dr "Anyway, when the lights went out, I realized I was probably the only person who knew where the fuse box was besides Burgundy (and she probably wouldn’t know how to work it if she tried). So, I felt my way down into the basement, grabbed a fresh fuse, and replaced it."
                    dr "I left the burnt one down there, if you feel the need to check my story!"
                    $ jad.append("what")
                    jump ind
                "Did you see or hear anything?":
                    dr "Nothing helpful. Some shouting and screaming. I went to the fusebox right away, so everything was kind of muffled, and I couldn’t see a thing until I opened the box and the little emergency light went on."
                    $ jad.append("did")
                    jump ind
                "Did you have any reason to wish Burgundy harm?":
                    dr "Absolutely the hell not! We’ve been best friends for ages. If anything, I have been trying to keep her out of situations while she seems to try to get herself killed! Like I said earlier,"
                    dr "she’s been going to seedy parts of town to try and “connect” with the way a character might feel if they were in genuine danger."
                    dr "What kind of research method is that? I’ve had to pull her out of dangerous situations too many times as she’s wrapped up this book."
                    $ jad.append("wish")
                    jump my_menu
                "That's all":
                    if len(jad) >= 3:
                        ms "Thanks, Indigo. And thanks for getting the lights back on. We’ll get to the bottom of this."
                        $ end.append("jad")
                        jump out3
                    else:
                        n "You haven't asked all of your questions yet."
                        jump ind
            label out3:    
        "Madame Ivory": 
            ms "Ivory? How are you holding up? I know this can’t be easy."  
            i "Honestly? I’m very much not okay. I don’t think I’ve really come to terms with it yet— it still feels like this has to be one of her elaborate stunts, that she’ll get up any minute and laugh at us for being so dramatic. I can’t believe my sister… she’s really gone. It just doesn’t seem real."
            i "I guess, right now, that’s for the best."
            ms "Oh honey, I’m so sorry. I can’t imagine losing a sibling like this. We’re here for you."
            mr "I’m sorry to ask this, Ivory, but we’re trying to figure out what happened. Do you mind if we ask you a few questions?"
            i "Yeah. Okay. I guess now’s as good a time as ever."
            mr "Thank you. We’ll try to be brief."
            $ ivo= []
            menu ivor:
                "What did you do when the lights went out?":
                    i "Well, Burgundy has always been afraid of lightning, so my first thought was to try and find her in the dark so I could help her through the panic. I ran into a chair in the dark, and then somebody grabbed my arm in a vice grip— I thought it was Burgundy at first,"
                    i "since whoever it was couldn’t stop hyperventilating,"
                    i "but I figured out pretty quickly that it was Countess Coral. I just let her hang on to me for a moment until she could calm down, and by the time she was settled the lights were back on, and well… <i>it</i> had already happened."
                    $ ivo.append("what")
                    jump ivor
                "Did you see or hear anything?":
                    i "Just Countess Coral, really. A few people screamed at the start, I think, but she definitely screamed the loudest. Then she found me in the dark and held on for dear life— the poor dear, she and Burgundy could never stand the storms." 
                    i "It’s a wonder they ever dated— they must have both gone catatonic every time there was a little thunder."
                    i "But yes, I was busy calming her down, so I wasn’t really looking or listening for anything else. I didn’t think there would be anything else."
                    $ ivo.append("did")
                    jump ivor
                "Did you have any reason to wish Burgundy harm?":
                    i "What kind of question is that? I don’t know how you could insinuate such a thing. The woman is— uh, was. She was like a sister to me."
                    ms "Wait, “like a sister”? I thought you two were sisters"
                    i "Oh, well. We’ve always called each other sisters, ever since we were little. We met in elementary school, you see, in the library. We were the only two who ever actually wanted to be in there, so we usually had the place to ourselves."
                    i "Neither of us had siblings, or really any friends our age, so we swore to be each other’s sisters and best friends forever— I know, it sounds corny, but hey, we were kids."
                    i "Anyway, her parents never liked me much, so I never really came up to this house until after they’d passed away and left it to her. I tried to convince her to sell it, but she said it reminded her of the mystery novels we initially bonded over. Given her choice of career,"
                    i "I suppose I can’t fault her for that. But just look where it got her…"
                    i "In any case, if you need any proof that we weren’t related, there’s a painting somewhere in here— a family tree, with just one branch."
                    $ ivo.append("wish")
                    jump ivor
                "That's all":
                    if len(ivo) >= 3:
                        ms "Thank you, Ivory. We’ll give you some time to yourself while we keep looking."
                        $ end.append("ivo")
                        jump out4
                    else:
                        n "You haven't asked all of your questions yet."
                        jump ivor
            label out4: 
        "Countess Coral": 
            ms "Coral? How are you—"  
            cr "AAAAA!!!"
            cr "Sorry. You just surprised me, and I suppose I’m a bit on-edge from the whole… situation. Not to mention it’s still storming outside and oh my goodness what if the lights go out again—"
            mr "Coral."
            cr "...Yes?"
            mr "Everything will be fine. We will figure out what happened. If the lights go out, we will fix them again."
            cr "Okay. Okay, I trust you. What did you need?"
            mr "We just wanted to ask you a few questions. We’re asking everybody, trying to make sure we get a full picture of what happened. Do you feel up to answering a few questions?"
            cr "I think so. Go ahead."
            $ cor = []
            menu cora:
                "What did you do when the lights went out?":
                    cr "Well, you know I hate thunder. Can’t stand it. I know it’s not logical, but the lightning and then the sound like the sky is falling apart… it just terrifies me. So I screamed, and started to try to get away from the window."
                    cr "I guess I ran into Madame Ivory, because the next thing I knew I was holding on to her arm like it was the only thing keeping me afloat, and she was talking to me, trying to help me calm down. It did help, I guess, eventually."
                    $ cor.append("what")
                    jump cora
                "Did you see or hear anything?":
                    cr "I can’t say I did. I was mostly panicking, not listening. Sorry."
                    $ cor.append("did")
                    jump cora
                "Did you have any reason to wish Burgundy harm?":
                    cr "Goodness no! I know she and I broke up recently, but it was mutual. We didn’t spend enough time together anymore, and there was just no spark left in the relationship. I loved her, and kept loving her even after we parted ways, but it wasn’t the kind of love that we needed."
                    cr "So no, I would never have hurt a hair on her beautiful head, even if I wasn’t busy screaming my head off into Ivory’s ear."
                    $ cor.append("wish")
                    jump cora
                "That's all":
                    if len(cor) >= 3:
                        mr "Don't worry we will get to the bottom of this! Now if you will excuse us there are more suspects to interrogate"
                        $ end.append("cor")
                        jump out5 
                    else:
                        n "You haven't asked all of your questions yet."
                        jump cora
            label out5: 
        "Investigate elsewhere":
            menu elsewhere:
                "Kitchen":
                    n "In front of you lies an ornate kitchen with a seemingly endless supply of miscellaneous kitchen appliances."
                    n "After some through investigating you open a drawer full of letters. Most are of no consequence such as bills or the odd magazine here and there. But at the bottom lies a stack of letters signed from Lavender to Burgundy."
                    n "The letters discuss the gradual tension rising in the workplace, but it looks like both sides were respectful and they did break off amicably"
                    n "Clue found: Lavender's letters"
                    $ letter = true
                    $ clues.append("letter")
                    jump elsewhere 
                "Library":
                    n "You walk your way up the manor stairs to the top floor and make your way to the library. Inside you are greated to the sight of hundreds, maye even thousands of books"
                    n "On the farthest side from the entrance lies a large tapestry showing a branch of the family tree of Burgendy"
                    n "The fabric is torn, you wonder if this branch was a peice of a larger tree"
                    n "Clue found: Burgendy's family branch"
                    $ tree = true
                    $ clues.append("tree")
                    jump elsewhere 
                "Basement":
                    n "You decend into the stone basement. The basement is mostly unfernished and used for storrage"
                    n "The value of some of the artifacts down here must be in the millions. There is a full set of samurai armor accompanied with a katana, myan pottery, and some old flintlock weaponry to name some of the items."
                    n "if you weren't such a good friend you may have considered taking something."
                    n "Along a wall you see a fusebox. On the floor you see a burt out fuse"
                    n "Clue found: burnt fuse"
                    $ fuse = true
                    $ clues.append("fuse")
                    jump elsewhere 
                    
                "Return to dining room":
                    jump character
                
        "Accuse someone":
            if len(end) >= 5:
                if len(clues) >= 3:
                    ms "Okay, I think we’ve heard and found just about everything we can. So, who do you think did it?"
                    menu accuse:
                        "Lady Lavender":
                            mr "I think it must be Lady Lavender. She must’ve felt so frustrated working under Burgundy that she couldn’t stand it anymore, and seeing the Burgundy’s name on another publication must have burnt her up inside."
                            ms "But remember, we saw those letters she sent— she was frustrated, but they were mending fences. Why spend so much time making up with a woman you mean to kill? Plus, the poor girl was shaking like a leaf at the mere thought of what happened."
                            ms "I don’t think she could have done it."
                            jump accuse
                        "Colonel Cobalt":
                            mr "I think it was Colonel Cobalt. He said himself that one of his ideas was used in Burgundy’s short stories— and I’ve read that book, she doesn’t even credit him! That must have made him feel so frustrated," 
                            mr "especially since he’s been trying so hard to get the escape room business off the ground at all."
                            ms "I really don’t think he holds that against her, though. And even if he did— don’t you remember what he showed us? He couldn’t have been the one who strangled Burgundy, since her neck has two hand marks on it, and Cobalt only has the one working hand."
                            jump accuse
                        "Dr. Indigo":
                            mr "It must have been Indigo. You heard what he said earlier, all “she’s gonna get killed” and “I'm gonna have to slap some sense into her myself!” He probably didn’t mean for it to go this far, but the man never does anything halfway."
                            ms "I don’t think he has it in him! He’s such a protective sort, he’d never hurt Burgundy. Besides, the burnt fuse— and the fact that the lights are currently on— prove that he went downstairs during the power outage to deal with the fuse box. And thank goodness he did!"
                            jump accuse
                        "Madame Ivory":
                            mr "I believe it was Ivory. She and Burgundy were sisters— she’d stand to inherit all of Burgundy’s wealth and property if she died. She could probably even collect on the publishing deal, since Burgundy always wrote under an alias."
                            ms "That doesn’t make sense, though. Ivory and Burgundy weren’t blood-related— you saw the family tree, Burgundy was an only child. Ivory wouldn’t see a cent if Burgundy died, nor does she seem to want this secluded bit of property." 
                            ms "Besides, Coral was holding on to her the whole time, so she wouldn’t have had the opportunity."
                            jump accuse
                        "Countess Coral":
                            mr "Coral must have done it. She and Burgundy were dating up until a few weeks ago, and the split must have hurt Coral more than she let on— she saw her chance when the lightning struck, and took out Burgundy in some sort of misguided revenge."
                            ms "Surely you can’t mean that. Coral is as afraid of the storms as Burgundy ever was, and she was clinging on to Ivory the entire time. Ivory has no reason to lie for her, and their stories match up. Coral was mid-panic when Burgundy died, so it couldn’t have been her."
                            jump accuse
                        "Nobody":
                            mr "I don’t get it. Nobody could have done it— they all have rock-solid alibis or clear reasons they couldn’t have been the murderer. But that doesn’t change the fact that our friend is over there, dead, with clear marks of trauma on her throat."
                            ms "You’re right. I don’t see how it could have happened, unless she somehow did it to herself… but listen, there are sirens outside! The storm must have broken while we were talking. Let’s go greet the policemen."
                            n "You and Mrs. Jade walk to the front of the house, where a few police cruisers have joined the line of cars in front of the mansion. You watch as a few uniformed men emerge from the cars and converge at the front door, and answer with confident detail when they ask for an explanation of the incident."
                            n "Once they have the story as you know it, they push inside. Most of them move to interrogate the witnesses, as you have, but one breaks away from the group and kneels to examine Baroness Burgundy’s body. "
                            n "He carefully checks each area of the body, filling out a form as he does— his thorough notes are cramped inside the stark black outlines of each field. After a while, you look away; the sight of someone touching a corpse (even a corpse you knew— especially a corpse you knew) causes bile to rise up in your throat. There’s a reason beyond crime scene preservation why you didn’t look too closely at the body yourself."
                            n "Copious notes seemingly finished, the policeman stands, removes his gloves, and goes to quietly confer with the others. After a moment, one of the other officers— a superior, by the looks of his uniform— approaches you."
                            define po = Character("Police Officer")
                            po "Mr. and Mrs. Jade, I take it?"
                            mr "Yes, that’s us. Or rather, those are the names we were using for this party. Here, I have my ID if you need to see it—"
                            po "No need, son. We’ve looked it over, spoken to everyone here, and there’s no evidence of foul play. You’re all free to go."
                            mr "No evidence of foul play”? There was a murder! A strangulation! My friend is dead!"
                            po "Yes, it appears Ms. Burgundy is dead. It’s a shame, my son adored her books. But if you had taken a closer look, son, you’d have seen that this was no strangulation. She simply choked." 
                            po "My best guess? She was sampling some of the food when the lightning struck, and in her shock and panic she swallowed without chewing. Her windpipe is completely blocked; she was clawing at her own throat when she passed, which explains those contusions. But indeed: no foul play."
                            mr "Oh. Huh"
                            ms "I suppose we were all so swept up in the atmosphere of mystery that we didn’t think of the possibility that the answer might be so banal"
                            po "If it’s worth anything, your investigation here was plenty impressive. If you ever decide you want to join the force, give me a call, eh? Either of you."
                            ms "Thank you officer."
                            mr "Thanks for your help"
                            n "The night bled into morning as everyone collapsed into chairs and couches, exhausted and frazzled by the events of the night. In the morning, everyone said somber goodbyes, the group slowly shrinking until only you and Mrs. Jade are left behind."
                            ms "I think it’s how she would’ve chosen to go, don’t you?"
                            mr "Hm? Oh. Yes, well, I suppose she was always a bit of a dramatic. She would have loved it."
                            ms "I hope she did."
                            n "<i>The End</i>"
                            n "creddits: devs and writers Miles Mattson and Caroline Mcdonough"
                            n "Special thanks: Annie Spratt, Ellen Tanner, Jose Llamas, rahul g, 🇸🇮 Janko Ferlič all on Unsplash"
                            n "Finally, thank you for playing!"
                            return
                        
                else:
                    n "You can't shake the feeling you are missing something"
                    jump character
            else:
                n "You have not talked to everyone yet"
                jump character
        

        
    # This ends the game.

    return
