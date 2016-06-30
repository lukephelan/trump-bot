import os
import time
import random
from slackclient import SlackClient


# trump-bot's ID as an environmental variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('TRUMP_BOT_SLACK_TOKEN'))


def handle_command(command, channel):

    # Arrayed responses

    random_responses = [
    "You make no sense, cuck.",
    "Do you mind if I sit back a little? Because your breath is very bad.",
    "I have an attention span that's as long as it needs to be.",
    "I don't like losers.",
    "People are tired of seeing politicians as all talk and no action.",
    "You don't cure a child molester.",
    "Look at that face!",
    "I like people who weren't captured.",
    "How stupid are the people of Iowa?",
    "I have never seen a thin person drinking Diet Coke.",
    "Try asking me for help."
    "Keep it short, fast and direct.",
    ("Don’t expect people to believe your blarney simply because you’re good at"
    " delivering it."),
    "I like Michael Douglas!"
    ]

    greeting_responses = [
    "Hello.",
    "Hi.",
    "Keep it short, fast and direct."
    ]

    hillary_responses = [
    ("The only card Hillary Clinton has is the woman's card. "
    "She's got nothing else to offer and frankly, if Hillary Clinton were a"
    " man, I don't think she'd get 5 percent of the vote. The only thing "
    "she's got going is the woman's card, and the beautiful thing is, women"
    " don't like her."),
    ("If Hillary Clinton can't satisfy her husband, what makes her think she "
    "can satisfy American?"),
    ("We don't know anything about Hillary in terms of religion. Now, she's "
    "been in the public eye for years and years, and yet there's no... there's "
    "nothing out there.",
    ("The Benghazi victims were left helpless to die as Hillary Clinton "
    "soundly slept in her bed."),
    ("For the amount of money Hillary Clinton would like to spend on refugees, "
    "we could rebuild every inner city in America."),
    "Hillary Clinton said she was under attack in Bosnia, but the attack turned"
    " out to be young girls handing her flowers."),
    ("It is Hillary Clinton's agenda to release the violent criminals from "
    "jail. She wants them all released."),
    "Hillary Clinton wants to abolish the Second Amendment.",
    ("ISIS exploded on Hillary Clinton's watch. She's done nothing about it and"
    " never will. Not capable!"),
    ("Hillary Clinton’s Presidency would be catastrophic for the future of our "
    "country. She is ill-fit with bad judgment."),
    ("Benghazi is just another Hillary Clinton failure. It just never seems to "
    "work the way it's supposed to with Clinton."),
    ("Crooked Hillary is wheeling out one of the least productive senators in "
    "the U.S. Senate, goofy Elizabeth Warren, who lied on heritage."),
    ("Hillary defrauded America as Secy of State. She used it as a personal "
    "hedge fund to get herself rich! Corrupt, dangerous, dishonest."),
    ("Hillary took money and did favors for regimes that enslave women and"
    "murder gays."),
    ("How can Hillary run the economy when she can't even send emails without "
    "putting entire nation at risk?"),
    ("Hillary says this election is about judgment. She's right. Her judgement "
    "has killed thousands, unleashed ISIS and wrecked the economy."),
    ("Crooked Hillary Clinton will be a disaster on jobs, the economy, trade, "
    "healthcare, the military, guns and just about all else. Obama plus!"),
    ("How can Crooked Hillary say she cares about women when she is silent on"
    " radical Islam, which horribly oppresses women?"),
    ("Crooked Hillary wants to get rid of all guns and yet she is surrounded by"
    " bodyguards who are fully armed. No more guns to protect Hillary!"),
    ("If Crooked Hillary Clinton can't close the deal on Crazy Bernie, how is "
    "she going to take on China, Russia, ISIS and all of the others?"),
    ("It was Rosie O'Donnell who ate the cake in the vicious Hillary commercial"
    " about me, not Crooked Hillary!"),
    ("I hope corrupt Hillary Clinton chooses goofy Elizabeth Warren as her "
    "running mate. I will defeat them both.")
    ]

    mexican_responses = [
    "I love the Mexican people.",
    ("I will build a great wall – and nobody builds walls better"
    " than me, believe me – and I’ll build them very inexpensively. I will"
    " build a great, great wall on our southern border, and I will make Mexico"
    " pay for that wall. Mark my words."),
    ("We have to have a wall. We have to have a border. And in "
    "that wall we’re going to have a big fat door where people can come "
    "into the country, but they have to come in legally."),
    ("Our politicians are stupid. And the Mexican government is "
    "much smarter, much sharper, much more cunning. And they send the bad "
    "ones over because they don't want to pay for them. They don't want to "
    "take care of them. Why should they when the stupid leaders of the "
    "United States will do it for them?"),
    ("When Mexico sends its people, they’re not sending their best. They’re not"
    " sending you. They’re not sending you. They’re sending people that have "
    "lots of problems, and they’re bringing those problems with us. They’re "
    "bringing drugs. They’re bringing crime. They’re rapists. And some, I "
    "assume, are good people."),
    "The best taco bowls are made in Trump Tower Grill. I love Hispanics!"
    ]

    immigrant_responses = [
    ("These are people that shouldn't be in our country."
    " They flow in like water."),
    ("We have at least 11 million people in this country that came in illegaly."
    " They will go out, they will come back, some will come back, the best "
    "through a process. It may not be a very quick process, but I think that's"
    " very fair and very fine."),
    ("We admit more than 100,000 lifetime migrants from the Middle East each "
    "year."),
    "Germany is crime-riddled right now because of migration to Europe.",
    ("I have never liked the media term 'mass deportation' - but we must "
    "enforce the laws of the land!"),
    ("We must suspend immigration from regions linked with terrorism until a "
    "proven vetting method is in place."),
    ("Just met with courageous family of Sarah Root in Nebraska. Sarah was "
    "horribly killed by illegal immigrant, but leaves behind amazing legacy.")
    ]

    women_responses = [
    ("All of the women on The Apprentice flirted with me –"
    " consciously or unconsciously. That’s to be expected."),
    "I’ve said if Ivanka weren’t my daughter, perhaps I’d be dating her.",
    ("26,000 unreported sexual assults in the military - only 238 convictions. "
    "What did these geniuses expect when they put men and women together?"),
    ("I’m not just talking about men; women can be equally ruined financially "
    "without a prenup."),
    ("My own mother was a housewife all her life. And yet it’s turned out that "
    "I’ve hired a lot of women for top jobs, and they’ve been among my best "
    "people."),
    ("How can Crooked Hillary say she cares about women when she is silent on"
    " radical Islam, which horribly oppresses women?"),
    ("I gave a woman named Barbara Res a top N.Y. construction job, when that "
    "was unheard of, and now she is nasty. So much for a nice thank you!"),
    ("If it were up to goofy Elizabeth Warren, we’d have no jobs in America "
    "— she doesn’t have a clue."),
    ("Goofy Elizabeth Warren is now using the woman’s card like her friend "
    "crooked Hillary. See her dumb tweet “when a woman stands up to you..."),
    ("Goofy Elizabeth Warren is weak and ineffective. Does nothing. All talk, "
    "no action - maybe her Native American name?"),
    ("Goofy Elizabeth Warren and her phony Native American heritage are on a "
    "Twitter rant. She is too easy! I'm driving her nuts."),
    ("Goofy Elizabeth Warren, Hillary Clinton’s flunky, has a career that is "
    "totally based on a lie. She is not Native American."),
    ("While Bette Midler is an extremely unattractive woman, I refuse to say "
    "that because I always insist on being politically correct.")
    ]

    daughter_responses = [
    ("Yeah, she's really something, and what a beauty, that one."
    " If I weren't happily married and, ya know, her father..."),
    "I’ve said if Ivanka weren’t my daughter, perhaps I’d be dating her.",
    ("I don't think Ivanka would pose for Playboy, although she does have a "
    "very nice figure. I've said if Ivanka weren't my daughter, perhaps I'd "
    "be dating her.")
    ]

    obama_responses = [
    ("An extremely credible source has called my office and "
    "told me that Barack Obama's birth certificate is a fraud."),
    ("The Obama administration was actively supporting Al Qaeda in Iraq, the "
    "terrorist group that became the Islamic State."),
    ("I heard he was a terrible student, terrible. How does a bad student go to"
    " Columbia and then to Harvard?"),
    ("They are very concerned because I am challenging him as to whether or not"
    " he was born in this country where there is a real doubt."),
    ("If I got the nomination, if I decide to run, you may go back and "
    "interview people from my kindergarten. They'll remember me. Nobody comes "
    "forward. Nobody knows who he is until later in his life. It's very "
    "strange. The whole thing is very strange."),
    ("If Obama resigns from office NOW, thereby doing a great service to the "
    "country — I will give him free lifetime golf at any one of my courses!"),
    ("Obama is, without question, the WORST EVER president. I predict he will "
    "now do something really bad and totally stupid to show manhood!"),
    ("How amazing, the State Health Director who verified copies of Obama’s "
    "'birth certificate' died in plane crash today. All others lived."),
    ("Is President Obama going to finally mention the words radical Islamic "
    "terrorism? If he doesn't he should immediately resign in disgrace!"),
    ("Does President Obama ever discuss the sneak attack on Pearl Harbor while "
    "he's in Japan? Thousands of American lives lost.")
    ]

    money_responses = [
    ("You know the funny thing, I don't get along with rich"
    " people. I get along with the middle class and the poor people better than"
    " I get along with the rich people."),
    "The point is, you can never be too greedy.",
    ("That's one of the nice things. I mean, part of the beauty "
    "of me is that I'm very rich. So if I need $600 million, I can put $600"
    " million myself. That's a huge advantage. I must tell you, that's a "
    "huge advantage over the other candidates.")
    ]

    coding_responses = [
    "I don't like losers.",
    "Help yourself, cuck.",
    ("My IQ is one of the highest — and you all know it! Please"
    " don't feel so stupid or insecure; it's not your fault."),
    "You were born stupid."
    ]

    gun_responses = [
    ("Paris would have played out differently with the bullets flying in the "
    "other direction."),
    ("The right of self-defense doesn't stop at the end of your driveway. "
    "That's why I have a concealed carry permit and why tens of millions of "
    "Americans do too. That permit should be valid in all 50 states."),
    ("If you had more guns, you would have more protection because the "
    "right people would have the guns."),
    ("It's not a gun problem, it's a mental illness problem."),
    ("Florida has issued more than 3 million conceal carry permits in the past"
    " 30 years. Only 168 have been revoked."),
    ("Crooked Hillary wants to get rid of all guns and yet she is surrounded by"
    " bodyguards who are fully armed. No more guns to protect Hillary!")
    ]

    foreign_responses = [
    "We will totall dismantle Iran's global terror network.",
    ("We will send a clear signal that there is no daylight between American and"
    " our most reliable ally - the state of Israel.")
    ]

    isis_responses = [
    "I’m the worst thing that’s ever happened to ISIS.",
    ("I will quickly and decisively bomb the hell out of ISIS, will rebuild "
    "our military and make it so strong no-one, and I mean no-one, will "
    "mess with us."),
    "Let them fight each other and pick up the remnants.",
    ("I would just bomb those suckers, and that's right, I'd blow up the pipes,"
    " I'd blow up the refineries, I'd blow up every single inch, there would be"
    " nothing left."),
    ("ISIS is making a tremendous amount of money because of the oil that they "
    "took away, they have some in Syria, they have some in Iraq, I would bomb "
    "the shit out of them."),
    ("The Obama administration was actively supporting Al Qaeda in Iraq, the "
    "terrorist group that became the Islamic State."),
    ("The other thing with the terrorists is you have to take out their families"
    ", when you get these terrorists, you have to take out their families."),
    ("Without looking at the various polling data, it is obvious to anybody the"
    " hatred is beyond comprehension. Where this hatred comes from and why we"
    " will have to determine. Until we are able to determine and understand "
    "this problem and the dangerous threat it poses, our country cannot be the"
    " victims of horrendous attacks by people that believe only in Jihad, and "
    "have no sense of reason or respect for human life. If I win the election "
    "for President, we are going to Make America Great Again."),
    ("The Obama administration was actively supporting Al Qaeda in Iraq, the "
    "terrorist group that became the Islamic State."),
    ("ISIS exploded on Hillary Clinton's watch. She's done nothing about it and"
    " never will. Not capable!"),
    ("The American people are sick and tired of not being able to lead normal "
    "lives and to constantly be on the lookout for terror and terrorists!"),
    ("How can Crooked Hillary say she cares about women when she is silent on"
    " radical Islam, which horribly oppresses women?"),
    ("Is President Obama going to finally mention the words radical Islamic "
    "terrorism? If he doesn't he should immediately resign in disgrace!")


    ]

    tax_responses = [
    ("I try and pay as little taxes as possible, because I hate what they do "
    "with my tax money. I hate the way they spend our money."),
    ("I know people making a tremendous amount of money and paying virtually "
    "no taxes, and I think it's unfair."),
    ("By my calculations 1 percent of Americans who control 90 percent of "
    "the wealth in this country would be affected by my plan. The other 99 "
    "percent of the people would get deep reductions in their federal income "
    "taxes."),
    ("The lobbyists are going to come and see me, but I don't give a shit "
    "about lobbyists."),
    ("I would be happy to pay a lot more if it would help solve our country's "
    "many problems."),
    "Nobody knows more about taxes than I do and income than I do."
    ]

    health_responses = [
    ("We're going to repeal and replace the horror known as Obamacare. It is a"
    " horror."),
    ("We're losing thousands of veterans waiting on line because they can't"
    " get speedy health care from the Veterans Administration."),
    ("Healthy young child goes to doctor, gets pumped with massive shot of many"
    " vaccines, doesn't feel good and changes - AUTISM. Many such cases!"),
    ("I am being proven right about massive vaccinations — the doctors lied. "
    "Save our children and their future."),
    ("No more massive injections. Tiny children are not horses — one vaccine at"
    " a time, over time.")
    ]

    muslim_responses = [

    ("Even among second and third generation Muslims in the United States, "
    "there's no real assimilation."),
    ("Is President Obama going to finally mention the words radical Islamic "
    "terrorism? If he doesn't he should immediately resign in disgrace!")


    ]

    environment_responses = [
    "In California the windmills are killing hundreds and hundreds of eagles.",
    "It’s freezing and snowing in New York – we need global warming!",
    ("Remember, new 'environment friendly' lightbulbs can cause cancer. "
    "Be careful - the idiots who came up with this stuff don't care."),
    ("Wind turbines are not only killing millions of birds, they are killing "
    "the finances and environment of many countries and communities."),
    ("This very expensive GLOBAL WARMING bullshit has got to stop. Our planet "
    "is freezing, record low temps, and our GW scientists are stuck in ice."),
    ("The concept of global warming was created by and for the Chinese in order"
    " to make U.S. manufacturing non-competitive."),
    ("How many bald eagles did wind turbines kill today? They are an "
    "environmental and aesthetic disaster.")
    ]

    katy_responses = [
    ("Katy Perry must have been drunk when she married Russell Brand. But he "
    "did send me a really nice letter of apology!"),
    ("Katy, what the hell were you thinking when you married loser Russell "
    "Brand. There is a guy who has nothing going, a waste!"),
    ("I watched Russell Brand and I think his mind is fried - he looks really "
    "bad. Russell is a total joke, a dummy who is lost!"),
    ("Katy Perry is no bargain but I don't like John Mayer - he dates and tells"
    " - be carefuly Katy (just watch!).")
    ]

    hair_responses = [
    ("I don't wear a 'rug' - it's mine. And I promise not to talk about your "
    "massive plastic surgeries that didn't work."),
    "I actually don't have a bad hairline.",
    "I do not wear a rug. My hair is one hundred percent mine.",
    "No animals have been harmed in the creation of my hairstyle.",
    ("Bette Midler talks about my hair but I'm not allowed to talk about her "
    "ugly face or body - so I won't. Is this a double standard?")
    ]

    help_responses = [
    "You just have to be the kind of guy to get people to do things.",
    ("To me it’s very simple: if you’re going to be thinking anyway, you might "
    "as well think big."),
    "The more you know, the more you realize how much you don’t know.",
    "Get in, get it done, get it done right, and get out.",
    "You can create your own luck.",
    ("If you’re not running into major challenges, you’re doing something easy,"
    " and probably not that valuable – and it’s probably not going to make much"
    " money for you.",
    ("If you think you can complete a six-year project in six months, you "
    "probably can."),
    ("I don’t want someone who is entertaining; I want someone who knows what"
    " he or she is doing."),
    "Think big!",
    ("Sometimes when you start thinking about all the problems you’ve got, it’s"
    " a good idea to focus a little on some of the positives of the situation."),
    ("Vision remains vision until you focus, do the work, and bring it down to"
    " earth where it will do some good."),
    "I have great respect for people who have found their success the hard way.",
    "If you’re not enjoying your work, you’re in the wrong job.",
    "You’re fired!",
    "Learning begets learning.",
    "You don’t have to be a brain surgeon to pay attention to the details.",
    "It pays to trust your instincts.",
    "Sometimes by losing a battle you find a new way to win the war.",
    "The bigger the problem, the bigger your chance for greatness.",
    ("I’ve faced tremendous adversity. It’s something just about everyone can "
    "relate to."),
    "Problems are often opportunities in disguise.",
    "Focus on the solution, not the problem!",
    ("I really had to think in out-of-the-box ways to keep from being buried "
    "alive."),
    "Envision yourself as victorious.",
    "Focus on objective insights and solutions.",
    "Failure is not permanent.",
    ("It’s not just intelligence or luck that gets us places, it’s tenacity in"
    " the face of adversity."),
    ("Problems are a part of life and a big part of business. The bigger your "
    "business, the bigger your life, the bigger your problems are likely to be."),
    "Losers give up.",
    "Never give up!",
    "When I advise you to take risks, there’s a reason for it.",
    "When you do take risks... you better make sure the upside is big.",
    "Like good soldiers we just keep on going.",
    ("It is possible to take problems in stride – if you have the right "
    "attitude and know what you are doing."),
    "My father always said 'Know everything you can about what you’re doing.'",
    "Adversity is a fact of life.",
    "Chances are that you will never wake up to an adversity-free day.",
    "Be ready to fight for your rights, and all will be well.",
    "If you never give up, you’ll be able to give back.",
    "Imagine saying that to someone yourself – 'Because I can!'",
    ("Robert Moses said something that stayed with me - 'You can’t make an "
    "omelet without breaking eggs.'"),
    "You can’t build a skyscraper without breaking a few heads.",
    ("Believe me, you will have problems! It doesn’t matter if your name is "
    "Trump or not, we all experience these things. Expect it!"),
    "Every day is a challenge, and every day is great."),
    "If you want to be lucky, prepare for something big.",
    "Developing your talents requires work, and work creates luck.",
    ("It takes brainpower and energy to think positively and creatively – and "
    "to see creatively and positively. Going negative is the easy way, the lazy"
    " way."),
    "No one can do it for you.",
    "Moving mountains? Moving tortoises? No problem.",
    ("Overcoming tremendous obstacles is all in a day’s work – if you love what"
    " you’re doing."),
    "If you see big problems, look for big opportunities.",
    "Get the right people to work with you.",
    "A big problem often signals a big opportunity.",
    ("Not everything is going to work... you may have to try a lot of things to"
    " get just one thing to work. That’s tenacity..."),
    ("Not long ago I received a letter from my kindergarten teacher. It was a "
    "big surprise... What she remembered most clearly about me is that I never"
    " stopped asking questions. I was the most inquisitive student she had ever"
    " had."),
    "Work despite your fears, and very often they will disappear.",
    "You may be stopped in your tracks. Get back on the horse!",
    ("Try and replace negatives with positives, and you’ll have more successes"
    " waiting for you, even if right now they’re nowhere in sight."),
    ("The higher you aim, the more opposition you will encounter. The more "
    "opposition you encounter... the more energy you get!"),
    "Ignorance is more expensive than education and using your brains.",
    "Ask yourself: What am I pretending not to see?",
    ("You don’t start with a finished skyscraper – you start with blueprint "
    "and a foundation."),
    "Think bigger!",
    "Problem solving is much easier if you think of problems as challenges.",
    "Are you stubborn enough to be a winner?",
    "Brainpower is the ultimate leverage.",
    ("If you look at the back of a beautiful and priceless tapestry, all you "
    "will see is a bunch of knots… Sometimes that’s all people will see because"
    " they haven’t seen the finished design on the other side yet."),
    "Replace your excuses with reasons and everything will become clear.",
    "Sometimes the picture is clearer if you’re not in the picture at all.",
    "Read as much as you can, learn as much as you can, every day.",
    "Raise the bar on yourself. Never settle for doing 'enough.'",
    "Thoroughness is not a choice, it is a prerequisite.",
    "Make sure the product is worth your energy.",
    "Genuine enthusiasm is hard to beat...",
    "How can you fix a problem if you can’t see it to begin with?",
    "It’s not good enough to want it. You’ve got to know how to get it.",
    ("Most successful people have very short attention spans. It has a lot to"
    " do with imagination."),
    "The best way to impress people is through results.",
    "Treat each decision like a lover.",
    "Be curious. A successful person is always going to be curious.",
    "Genius is the ability to assemble in new forms what already exists...",
    "Stick to what you know.",
    "Don’t ask other people questions you should be asking yourself.",
    "Always pretend you’re working for yourself.",
    "We’re all trying to keep up.",
    "Your resources are greater than you might think.",



    ]





    # Responses that return random response based on arrays

    response = random.choice(random_responses)

    if "hello" in command or " hi " in command or " hey " in command:
        response = random.choice(greeting_responses)
    if "hilary" in command or "hillary" in command:
        response = random.choice(hillary_responses)
    if "mexicans" in command or "mexico" in command:
        response = random.choice(mexican_responses)
    if "immigrant" in command or "immigration" in command:
        response = random.choice(immigrant_responses)
    if "women" in command:
        response = random.choice(women_responses)
    if "daughter" in command or "ivanka" in command:
        response = random.choice(daughter_responses)
    if "obama" in command:
        response = random.choice(obama_responses)
    if "greed" in command or "money" in command or "rich" in command:
        response = random.choice(money_responses)
    if "code" in command or "coding" in command:
        response = random.choice(coding_responses)
    if "gun" in command or "terrorism" in command or "terror" in command:
        response = random.choice(gun_responses)
    if "foreign" in command:
        response = random.choice(foreign_responses)
    if "isis" in command:
        response = random.choice(isis_responses)
    if "tax" in command:
        response = random.choice(tax_responses)
    if "health" in command:
        response = random.choice(health_responses)
    if "muslim" in command or "islam" in command:
        response = random.choice(muslim_responses)
    if "environment" in command or "global warming" in command or "turbine" in command:
        response = random.choice(environment_responses)
    if "katy" in command or "perry" in command or "russell" in command:
        response = random.choice(katy_responses)
    if "hair" in command or "wig" in command:
        response = random.choice(hair_responses)
    if "help" in command:
        response = random.choice(help_responses)


    # Specific responses

    if "torture" in command:
        response = ("Don't tell me it doesn't work. Torture works. Waterboarding"
        " is fine, but it's not nearly tough enough, OK?")
    if "robert pattinson" in command or "kristen stewart" in command:
        response = ("Robert Pattinson should not take back Kristen Stewart. She"
         " cheated on him like a dog and will do it again. Just watch. He can do"
         " much better!")
    if "ariana" in command or "huffington" in command:
        response = ("Ariana Huffington is unattractive, both inside and out. I"
        " fully understand why her former husband left her for a man – he made a"
        " good decision.")
    if "media" in command:
        response = ("You know, it really doesn’t matter what the media write as"
         " long as you’ve got a young, and beautiful, piece of ass.")
    if "rosie" in command or "odonnell" in command or "o'donnell" in command:
        response = ("If I were running ‘The View’, I’d fire Rosie O’Donnell. I"
        " mean, I’d look at her right in that fat, ugly face of hers, I’d say "
        "‘Rosie, you’re fired.")
    if "yourself" in command:
        response = "The beauty of me is that I’m very rich."
    if "hand" in command or "finger" in command:
        response = ("My fingers are long and beautiful, as, it has been well"
        " documented, are various other parts of my body.")
    if "coke" in command or "fat" in command:
        response = "I have never seen a thin person drinking Diet Coke."
    if "twitter" in command:
        response = ("My Twitter has become so powerful that I can actually "
        "make my enemies tell the truth.")
    if "iq" in command or "intelligence" in command or "intelligent" in command:
        response = ("My IQ is one of the highest — and you all know it! Please"
        " don't feel so stupid or insecure; it's not your fault.")
    if "gay" in command or "homosexual" in command or "lesbian" in command:
        response = ("It’s like in golf. A lot of people — I don’t want this to"
        " sound trivial — but a lot of people are switching to these really "
        "long putters, very unattractive. It’s weird. You see these great "
        "players with these really long putters because they can’t sink "
        "three-footers anymore. And I hate it. I am a traditionalist. I have "
        "so many fabulous friends who happen to be gay, but I am a traditionalist.")
    if "ted" in command or "cruz" in command:
        response = ("Lyin' Ted Cruz just used a picture of Melania from a shoot"
        " in his ad. Be careful, Lyin' Ted, or I will spill the beans on your "
        "wife!")
    if "911" in command or "9/11" in command or "world trade center" in command\
        or "world trade centre" in command:
        response = ("I was down there, and I watched our police and our firemen, "
        "down on 7-Eleven, down at the World Trade Center, right after it came "
        "down.")
    if "winning" in command or "life" in command:
        response = "My whole life is about winning. I don't lose often. I almost never lose."
    if "politicians" in command:
        response = ("Our politicians are stupid. And the Mexican government is "
        "much smarter, much sharper, much more cunning. And they send the bad "
        "ones over because they don't want to pay for them. They don't want to "
        "take care of them. Why should they when the stupid leaders of the "
        "United States will do it for them?")
    if "passion" in command:
        response = ("Without passion you don't have energy, without energy "
        "you have nothing.")
    if "drink" in command:
        response = ("I'll drink water. Sometimes tomato juice, which I like. "
        "Sometimes orange juice, which I like. I'll drink different things. "
        "But the Coke or Pepsi boosts you up a little.")
    if "bush" in command:
        response = ("So Bush certainly wasn't the greatest, and Obama has not "
        "done the job. And he's created a lot of disincentive. He's created a "
        "lot of great dissatisfaction. Regulations and regulatory is going "
        "through the roof. It's almost impossible to get anything done in the "
        "country.")
    if "moderation" in command:
        response = ("A little more moderation would be good. Of course, my life"
        " hasn't exactly been one of moderation.")
    if "religion" in command or "god" in command:
        response = ("People are so shocked when they find out I am "
        "Protestant. I am Presbyterian. And I go to church, and I love God, and"
        " I love my church.")
    if "wisconsin" in command:
        response = "I love Wisconsin. It's a great place."
    if "trump" in command:
        response = ("Love him or hate him, Trump is a man who is certain about"
        " what he wants and sets out to get it, no holds barred. Women find his"
        " power almost as much of a turn-on as his money.")
    if "jet" in command:
        response = "Private jets cost a lot of money."
    if "wall" in command:
        response = ("We have to have a wall. We have to have a border. And in "
        "that wall we’re going to have a big fat door where people can come "
        "into the country, but they have to come in legally.")
    if "abortion" in command:
        response = "I hate the concept of abortion."
    if "starbucks" in command:
        response = ("Did you read about Starbucks? No more 'Merry Christmas' at"
        " Starbucks. No more. Maybe we should boycott Starbucks.")
    if "scotland" in command:
        response = ("Wind turbines are ripping Scotland apart and killing "
        "tourism. Electric bills in Scotland are skyrocketing. Stop the "
        "madness!")
    if "anthony" in command or "weiner" is command:
        response = ("Pervert alert. Anthony Weiner is back on twitter. All "
        "girls under the age of 18, block him immediately.")
    if "hater" in command:
        response = ("Amazing how the haters and losers keep tweeting the name "
        "F**ckface Von Clownstick like they are so original and like no one "
        "else is doing it...")


    # Post the response to the Slack channel the command came from
    slack_client.api_call("chat.postMessage", channel=channel,
        text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        This parsing function retuns None unless a message is
        directed at the Bot, based on its ID.
    """

    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                    output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Trump-Bot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
