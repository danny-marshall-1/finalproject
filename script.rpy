default rizz = False
default took_pre = False
default injured = False
default seriously_injured = False
default biggest_pr = False
default big_pr = False
default pr = False
default leg_press_pr = False
default made_friend = False
default socialized = False
default farted = False
default Score = 0

label start:

    "I had been busy doing homework and studying all day, but it was time to take a break and go to the gym."
    "I hadn't worked out in a while because I was so busy. I knew it would be good for me, both physically and mentally."
    "I changed, grabbed my gym bag and car keys, and was about to head out the door when I realized I forgot to take my pre-workout."
    "Me" "I should probably go back and take my pre-workout...but sometimes it does have side effects!"
    menu:
        "Go back and take pre":
            $ took_pre = True
            jump pre
        "Go to the gym without it":
            jump no_pre
    return

label pre:

    "I went back to the kitchen and took my pre-workout."
    "Me" "Okay, it's time to go!"
    "I drove to the gym."
    "Once I got there, I checked my workout log to remind myself which workout I was scheduled for today."
    "Me" "Ugh...leg day? That's the hardest workout of the week...but I can do it."
    "I saw an empty squat rack in the distance. I hurried towards it to make sure nobody would claim it before me."
    "I checked my log again. The last time I did squats, I did three sets of five reps with 235 pounds."
    "Me" "That's pretty good! Let's see how I'm feeling after warming up and hopefully I'll be able to beat that today."
    "I did three warm up sets."
    "Me" "Wow, my warm ups felt really good! I think I'm going to do 245 pounds today and hopefully I'll get around five reps."
    "As I got under the bar, the weight felt noticeably heavy over my shoulders. But I managed to crank out five reps."
    "Me" "That set was hard, but I did it! I'm not sure I'll be able to get five reps on my next two sets though. Realistically I should lower the weight back to 235."
    "Suddenly, I noticed my gym crush warming up in the rack next to mine!"
    "I see her here so often, yet I've never had the courage to say anything to her or even make eye contact."
    "Me" "Maybe I'll try to impress her... Should I add weight and go for a PR? Or should I play it safe and stick to my original plan?"
    menu:
        "Go for PR":
            jump PR
        "Drop the weight":
            $ pr = True
            $ Score += 10
            jump drop
    return

label no_pre:

    "Me" "Okay, looks like I'm good to go!"
    "I drove to the gym."
    "Once I got there, I checked my workout log to remind myself which workout I was scheduled for today."
    "Me" "Ugh...leg day? That's the hardest workout of the week...but I can do it."
    "I saw an empty squat rack in the distance. I hurried towards it to make sure nobody would claim it before me."
    "I checked my log again. The last time I did squats, I did three sets of five reps with 235 pounds."
    "Me" "That's pretty good! Let's see how I'm feeling after warming up and hopefully I'll be able to beat that today."
    "I did three warm up sets."
    "Me" "Ehhhh...those warm up sets didn't feel amazing. I could do 235 and try to just do what I did last time, or I could add weight like I was planning on doing."
    menu: 
        "Go for 245":
            jump forty_five
        "Stick with 235":
            jump thirty_five
    return

label forty_five:

    "I loaded 245 onto the bar. As I got under the bar and walked it out, I could feel how heavy it felt on my shoulders, which made me nervous."
    "I braced and began the set. The first rep moved a bit slower than I hoped. The second, third, and fourth reps were a mounting struggle."
    menu:
        "Go for a fifth rep":
            jump fifth
        "Stop here":
            jump no_fifth
    return

label thirty_five:
    
    "I decided to play it safe and do 235 like last time. I loaded up the bar, and as I got under and walked it out, it felt heavy on my shoulders, but definitely bearable."
    "I braced and began the set. The first rep moved pretty easily. I managed to do all five reps without any serious struggle."
    "Me" "That was a great set!"
    "I rested a few minutes and then did a couple more sets."
    "Me" "All right, 235 for three sets of five. I'll take it!"
    "I glanced over at my crush. She was on her phone, headphones in, not paying much attention to me."
    "Hmmm...should I finally go talk to her? I'm nervous..."
    menu: 
        "Approach her":
            $ rizz = True
            $ Score += 50
            jump approach_girl
        "Don't approach":
            jump no_approach_girl
    return

label fifth:

    "I began to descend into the squat. As soon as I reached the proper depth, I exploded up with all my might."
    "It wasn't enough. My legs simply didn't have the strength to lift the weight. I sank back down and allowed the bar to rest on the safety pins."
    "Me" "Argh! That's frustrating...I shouldn't have gone for the extra rep. Hopefully she didn't see..."
    "I glanced over in her direction. She didn't seem to be paying attention to me, luckily, as she was on her phone, headphones in."
    "I went over to my bench, sat down, and drank some water from my water bottle. Looking at the bar helplessly laying on the safety pins, I realized I wasn't really in the mood to hoist it back onto the hooks to do another set."
    "Me" "All right, I'm just gonna call it a day with squats. But I shouldn't waste the opportunity...maybe I should go say something to her while she's here!"
    menu: 
        "Approach her":
            jump approach_girl
        "Don't approach":
            jump no_approach_girl
    return


label no_fifth:

    "I walked the bar forward, let it come on to the hooks, and dropped it safely."
    "Me" "Phew! That was a tough set...probably good I didn't go for a fifth rep there, even if it means no PR."
    "At that point, I dropped the weight back to 235 and did two more sets."
    "When I was done, I went back to my bench and took some water from my watter bottle. I glanced over in her direction. She didn't seem to be paying attention to me, as she was on her phone, headphones in."
    "Me" "I shouldn't waste the opportunity...maybe I should go say something to her while she's here!"
    menu: 
        "Approach her":
            $ rizz = True
            $ Score += 50
            jump approach_girl
        "Don't approach":
            jump no_approach_girl
    return

label PR:

    "Me" "Okay, I'm going for 275! I've never hit this weight before, but I'm feeling pretty good, so I think I can do it."
    "Unracking the bar, I immediately felt intimidated by the weight. But I sensed that she was watching, and adrenaline was pumping through my body. I took a deep breath, squatted down, and grinded the rep with all my might."
    "Me" "That was hard, but I did it! Do I go for one more?"
    menu:
        "Attempt another rep":
            $ biggest_pr = True
            $ Score += 30
            $ injured = True
            jump attempt_another
        "End the set":
            $ big_pr = True
            $ Score += 20
            jump end_set
    return

label drop:

    "I decided not to let the girl I was trying to impress potentially get me injured. Better safe than sorry!"
    "I lowered the weight back to 235 and completed two more sets of five reps."
    "Me" "Awesome! Not a ridiculous PR, but still my best squat performance to date."
    "I glanced over at my crush. She was on her phone, headphones in, not paying much attention to me."
    "Hmmm...should I finally go talk to her? I'm nervous..."
    menu: 
        "Approach her":
            $ rizz = True
            $ Score += 50
            jump approach_girl
        "Don't approach":
            jump no_approach_girl
    return

label attempt_another:

    "I braced hard and began my descent. I could feel my quads and glutes stretching under the seemingly immense load."
    "As soon as I hit the proper depth, I exploded up once again, but this time, I could hardly move the weight! Sheer panic coursed through my body, but I remained determined to complete the rep."
    "Five whole seconds passed before I was standing up again. I shakily walked the bar back to the rack and let it drop onto the hooks. Exhausted, I clutched the railings of the rack, gasping for breath."
    "I turned around to see if she had been paying attention to my miraculous feat of strength. My heart deflated when I realized that she was on her phone, headphones in, totally not taking any notice of me."
    "Me" "Damn...all that for nothing? I practically sold my soul for that rep, and I'm so exhausted I don't know how I'm going to get through the rest of the workout!"
    "I sat down, drank some water from my water bottle, and allowed myself to come back to my senses for a few minutes."
    "Me" "You know, she might've noticed me, but tried not to make it obvious! I shouldn't give up. Maybe now's a good time to go up and talk to her!"
    menu: 
        "Approach her":
            $ rizz = True
            $ Score += 50
            jump approach_girl
        "Don't approach":
            jump no_approach_girl
    return

label approach_girl:

    "I took a deep breath, glanced in the mirror, fixed my hair, and walked towards her." 
    if rizz:
        "Me" "Hey there."
        "Girl" "Hey"
        "I was so nervous that I almost blanked right then and there. But I remained smiling and cool."
        "Me" "I've seen you around here a lot and I've always wanted to say hi...I think you're really cute."
        "I couldn't believe the words that came out of my mouth. I was really sending it!"
        "Girl" "Wow...that's crazy. I've been wanting to say something to you too."
        "My jaw dropped. There was no way...she was interested in me as well?"
        "Me" "Really?"
        "Girl" "Yeah..."
        "Me" "Wow, that's too good to be true. What's your name?"
        "Girl" "Jane."
        "Me" "That's a nice name. I'm Brad. You mind if I get your phone number?"
        "Jane" "Sure!"
        "She handed over her phone and I typed my number in, making extra sure I didn't make a typo."
        "Now I wasn't sure what to say. I hadn't really planned this far, to be honest."
        "Me" "Well, I'll text you later. Have a good rest of your workout."
        "Jane" "Thanks!"
        "Elated, I put back my weights, wiped down the bar, and took my stuff over to the leg press. I was absolutely thrilled that I got her number." 
        jump leg_press
    else:
        "Me" "Hey there."
        "Girl" "Hey."
        "I was so nervous that I almost blanked right then and there. But I remained smiling and cool."
        "I've seen you around here a lot and I've always wanted to say hi...I think you're really cute."
        "I couldn't believe the words that came out of my mouth. I was really sending it!"
        "Girl" "Oh...uh, thanks."
        "...awkward."
        "Me" "So, uh, I'd really like to get to know you, if you're down...can I get your number or something?"
        "Girl" "Actually, I have a boyfriend. I'm sorry!"
        "My face immediately flushed with embarrassement."
        "Me" "Oh...no, that's my bad! I'll leave you be. Thanks, though!"
        "I hurriedly re-racked my weights, grabbed my things, and made my way over to the leg press."
        "Me" "Damn, that didn't really pan out the way I'd hoped. It's okay, I'll get over it."
        jump leg_press
    return

label leg_press:

    if rizz:
        if injured:
            "As I started loading plates onto the leg press, however, I noticed that my back was hurting...I probably exerted myself too much on those squats!"
            "Me" "Maybe I should do a few warm up sets..."
            menu:
                "Warm up":
                    jump warmup
                "Don't warm up":
                    $ seriously_injured = True
                    $ Score -= 30
                    jump no_warmup
        else:
            "I don't usually warm up on the leg press, and I was feeling good, so I went ahead and did a set of ten with five plates on each side."
            "Me" "That was hard, but I feel good. I might be able to add weight on the next one."
            menu: 
                "Add weight":
                    jump add
                "Keep weight the same":
                    jump no_add
    else:
        if injured:
            "As I started loading plates onto the leg press, I noticed that my back was hurting...I probably exerted myself too much on those squats!"
            "Me" "Maybe I should do a few warm up sets..."
            menu:
                "Warm up":
                    jump warmup
                "Don't warm up":
                    $ seriously_injured = True
                    $ Score -= 30
                    jump no_warmup
        else:
            "I loaded up the leg press with five plates on each side, slid into the seat, and did a set of ten."
            "Me" "That was hard, but I'm feeling surprisingly strong right now. I might be able to add weight on the next one."
            menu: 
                "Add weight":
                    jump add
                "Keep weight the same":
                    jump no_add

label add:

    "I went ahead and added another plate on each side."
    "Me" "Six plates is a lot...hopefully I can handle it!"
    "After resting a few minutes, I got back in the seat, unracked the weight, and gripped the handles. I took a deep breath and began the set."
    "4, 5...6!"
    "That sixth rep took everything I had. There was a slight chance I could go for another rep, but I knew if I went for it, I wouldn't have it in me to do a third set."
    menu:
        "Go for one more rep":
            jump one_more
        "End the set here":
            jump end_set_here
    return

label one_more:

    "I began the slow, painful descent. Pausing at the bottom, I could feel my quads and glutes pumping with blood."
    if took_pre:
        $ farted = True
        $ Score -= 5
        "Suddenly, a loud fart escaped from me."
        "BWOMPFF"
        "Me" "Dammit! The preworkout...I knew it would strike at some point!"
        "Embarassed, I let the sled fall to the safeties and I crawled out of the machine."
        "I looked around, and some people nearby were whispering and laughing under their breaths."
        "Ugh..."
        "I removed the plates, wiped the seat EXTRA thoroughly, and took my stuff over to the leg curl machine."
        "Me" "Oh...it looks like someone is using the machine. I guess I could ask to work in with him, or I could just wait for him to finish."
        menu:
            "Ask to work in":
                jump work_in
            "Wait for him to finish":
                jump wait
    else:
        $ leg_press_pr = True
        $ Score += 5
        "Determined to secure victory over the weights, I pushed up with everything I had. After what felt like eternity, I locked out, racked the weight, and took a sigh of relief."
        "Me" "Wow, that was hard! Seven reps with six plates though...that's a nice little PR."
        "I removed the plates, wiped the seat, and took my stuff over to the leg curl machine."
        "Me" "Oh...it looks like someone is using the machine. I guess I could ask to work in with him, or I could just wait for him to finish."
        menu:
            "Ask to work in":
                jump work_in
            "Wait for him to finish":
                jump wait

label end_set_here:

    "I racked the weight and took a sigh of relief. That last rep would have been hell for sure!"
    "I rested another minute and did one more set. Then I went over to the leg curl machine to finish the workout."
    "Me" "Oh...it looks like someone is using the machine. I guess I could ask to work in with him, or I could just wait for him to finish."
    menu:
        "Ask to work in":
            jump work_in
        "Wait for him to finish":
            jump wait
    return

label no_add:

    "I did two more sets with plates. Then I went over to the leg curl machine to finish the workout."
    "Me" "Oh...it looks like someone is using the machine. I guess I could ask to work in with him, or I could just wait for him to finish."
    menu:
        "Ask to work in":
            jump work_in
        "Wait for him to finish":
            jump wait
    return

label warmup:

    "I took some plates off and did a few sets with light weight. My back felt tight, but after the huge squat PR, I really wanted to see what I could do on the leg press!"
    menu:
        "Proceed to working sets":
            jump proceed
        "Skip working sets":
            jump skip
    return

label proceed:

    "I decided to go for it. I put five plates on the machine - my previous best with that weight was ten reps. Let's see how many I can go for today!"
    "I aligned my feet on the platform, unracked the weight, and began the slow, painful descent. I went as far down as I could, paused, and pressed back up."
    "My back was really feeling it now!"
    menu:
        "Keep going":
            $ seriously_injured = True
            $ Score -= 30
            jump keep_going
        "Stop the set":
            jump stop_set
    return

label keep_going:

    "I took a deep breath and resolved to continue the set."
    "Me" "2, 3, 4..."
    "Each rep was an increasing struggle. I was gasping for breath, I could feel my whole body straining, and most of all, my back was screaming in pain."
    "Halfway through the fifth rep, I felt something in my back I've never felt before. I stopped pushing, and the weight came crashing down to the safety stopper with a bang."
    if rizz:
        jump leave_with_girl
    else:
        jump leave_alone
    return

label leave_with_girl:

    "I crawled out of the machine in agony. I threw out my back for sure!"
    "I looked around the gym in panic, hoping I hadn't caused a scene. A few people looked my way, but I didn't see her anywhere...phew!"
    "Then all of a sudden she appeared out of nowhere."
    "Jane" "Oh my gosh, are you okay?"
    "I was glad she was here, but I was also thoroughly embarrassed!"
    "Yeah...I think I really hurt my back on the leg press just now."
    "Jane" "I'm so sorry. You really do train hard, don't you? I saw your squats earlier. Very impressive, but maybe you shouldn't go so hard all the time or you'll get injured!"
    "Me" "You're right. To be honest, I was actually just trying to impress you..."
    "Jane" "That's silly. I was already impressed. Here, let's get you back to your car."
    "She helped me back to my car. I was limping a little, and my back was stiff, but I knew it could've been worse."
    "Me" "Thanks so much for your help. You really didn't have to."
    "Jane" "Don't mention it. Text me when you get home, and make sure to take painkillers."
    "Me" "I will. Thanks again."
    jump score
    return

label leave_alone:

    "I crawled out of the machine in agony. I threw out my back for sure!"
    "I looked around the gym in panic, hoping I hadn't caused a scene. A few people looked my way, but I didn't see her anywhere...phew!"
    "I got up, took off the plates, wiped off the seat, and hobbled over to the exit. I was done with this workout."
    jump score
    return


label stop_set:

    "I knew it would be unwise to keep going. I racked the weight and got out of the machine."
    "My back was still hurting, but it wasn't too bad. I went over to the leg curl machine to finish the workout."
    "Me" "Oh...it looks like someone is using the machine. I guess I could ask to work in with him, or I could just wait for him to finish."
    menu:
        "Ask to work in":
            jump work_in
        "Wait for him to finish":
            jump wait
    return

label work_in:

    "I waited for him to finish his set and then I approached him."
    "Me" "Excuse me, how many more sets do you have left?"
    "Guy" "I just started, so I have three more sets."
    "Me" "All right. Do you mind if I work in with you?"
    "Guy" "Sure."
    "I adjusted the weight, hopped on the machine, and did a set."  
    "Guy" "Good set man."
    "Me" "Thanks."
    "He seemed like a nice guy. Maybe I could strike up a conversation with him."
    menu:
        "Start a conversation":
            $ made_friend = True
            $ Score += 10
            jump conversation
        "Don't talk":
            jump no_talk
    return

label conversation:
    "Me" "What's your name?"
    "Guy" "Joe."
    "Me" "Cool. I'm Brad."
    "We kept talking for a bit. It turns out that we have many common interests!" 
    "We finished our sets and parted ways. That was it for my workout."
    jump score
    return

label no_talk:

    "I decided not to strike up a conversation. He probably didn't want to be bothered!"
    "We finished our sets and parted ways. That was it for my workout."
    jump score
    return

label wait:

    "I went to the nearest bench to sit down while I waited." 
    "Then, I noticed my friend was nearby on the cable machines! Should I go approach him?"
    menu:
        "Approach friend":
            $ socialized = True
            $ Score += 5
            jump approach_friend
        "Don't approach":
            jump no_approach_friend
    return

label approach_friend:

    "Me" "Hey man!"
    "Friend" "What's up bro! What you hitting today?"
    "Me" "Oh you know, just dragging myself through the annual leg day!"
    "Friend" "Pfff, couldn't be me! I'm hitting arms...trying to catch a huge pump. Good for my depression, you know?"
    "Me" "Yeah, I know what you're saying. You're looking huge, I'll tell you that."
    "Friend" "You too bro."
    "We parted ways. I noticed the leg curl machine was now free, so I hopped on, did my sets, and left the gym."
    jump score
    return

label no_approach_friend:
    "I decided to leave him be. Once the leg curl machine was empty, hopped on, did my sets, and left the gym."
    jump score
    return

label skip:

    "I decided to play it safe and not do any working sets on the leg press. My back was simply not agreeing with me!"
    "I went over to the leg curl machine, which I knew would be easy on my back."
    "Oh...it looks like someone is using the machine. I guess I could ask to work in with him, or I could just wait for him to finish."
    menu:
        "Ask to work in":
            jump work_in
        "Wait for him to finish":
            jump wait
    return

label no_warmup:

    "I decided to go straight into my working weight. Shouldn't be a problem, since I don't usually need any warm up sets"
    "I put five plates on the machine - my previous best with that weight was ten reps. Let's see how many I can go for today!"
    "I aligned my feet on the platform, unracked the weight, and began the slow, painful descent. I went as far down as I could, paused, and began pressing back up."
    "Halfway through the rep, I felt something in my back that I've never felt before. I stopped pushing, and the weight came crashing down to the safety stopper with a bang."
    if rizz:
        jump leave_with_girl
    else:
        jump leave_alone
    return

label no_approach_girl:

    "I couldn't find it in me to approach her. She definitely wasn't interested in me...maybe she already had a boyfriend! Maybe she'd just think I was a creep!"
    "Defeated, I put back my plates, wiped off the bar, and took my stuff over to the leg press."
    jump leg_press

label end_set:

    "I made a business decision and called it there. I took a deep breath and carefully walked the bar back to the rack."
    "Me" "I think I had another rep in me! But maybe it's good I didn't go for it. Who knows what would've happened!"
    "I turned around to see if she had been paying attention to my impressive lift. My heart deflated when I realized that she was on her phone, headphones in, totally not taking any notice of me."
    "Me" "Damn...all that for nothing? Well, I guess I'm glad I didn't try for that extra rep!"
    "I sat down, drank some water from my water bottle, and allowed myself to come back to my senses for a few minutes."
    "Me" "You know, she might've noticed me, but tried not to make it obvious! I shouldn't give up. Maybe now's a good time to go up and talk to her!"
    menu: 
        "Approach her":
            $ rizz = True
            $ Score += 50
            jump approach_girl
        "Don't approach":
            jump no_approach_girl
    return


label score:
    "The End!"
    if Score == 90:
        "Congratulations! Your score is 90/90"
    elif Score == 85:
        "Your score is 85/90"
    elif Score == 80:
        "Your score is 80/90"
    elif Score == 75:
        "Your score is 75/90"
    elif Score == 65:
        "Your score is 65/90"
    elif Score == 60:
        "Your score is 60/90"
    elif Score == 55:
        "Your score is 55/90"
    elif Score == 50:
        "Your score is 50/90"
    elif Score == 45:
        "Your score is 45/90"
    elif Score == 40:
        "Your score is 40/90"
    elif Score == 35:
        "Your score is 35/90"
    elif Score == 30:
        "Your score is 30/90"
    elif Score == 25:
        "Your score is 25/90"
    elif Score == 20:
        "Your score is 20/90"
    elif Score == 15:
        "Your score is 15/90"
    elif Score == 10:
        "Your score is 10/90"
    elif Score == 5:
        "Your score is 5/90"
    else:
        "Your score is 0/90"

