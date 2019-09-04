import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Book

# Starting session
engine = create_engine('sqlite:///bookstorecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Creating Categories

arts = Category(name="Arts & Photography")
session.add(arts)
session.commit()

biographies = Category(name="Biographies & Memoirs")
session.add(biographies)
session.commit()

business = Category(name="Business & Investing")
session.add(business)
session.commit()

children = Category(name="Children's Books")
session.add(children)
session.commit()

cookbook = Category(name="Cookbook, Food & Wine")
session.add(cookbook)
session.commit()

history = Category(name="History")
session.add(history)
session.commit()

literature = Category(name="Literature & Fiction")
session.add(literature)
session.commit()

mystery = Category(name="Mistery & Suspense")
session.add(mystery)
session.commit()

romance = Category(name="Romance")
session.add(romance)
session.commit()

scifi = Category(name="Sci-Fi & Fantasy")
session.add(scifi)
session.commit()

teens = Category(name="Teens & Young Adult")
session.add(teens)
session.commit()

# Creating Books

# Arts & Photography
billCunnigham = Book(
    title="Bill Cunningham: On the Street: Five Decades of Iconic Photography",
    description="Bill Cunningham: On the Street is the work of a great anthropologist and fashion genius. "
                "Through his skilled eyes and his camera lens, he chronicled a half-century of fashion, capturing "
                "the high road, as well as the man or woman, in the fashion parade of daily life. This book is a "
                "dazzling kaleidoscope from the gaze of an artist who saw beauty at every turn.",
    category=arts)
session.add(billCunnigham)
session.commit()

love5 = Book(
    title="The 5 Love Languages: The Secret to Love that Lasts",
    description="In the #1 New York Times bestseller The 5 Love Languages, you'll discover the secret that has "
                "transformed millions of relationships worldwide. Whether your relationship is flourishing or "
                "failing Dr. Gary Chapman's proven approach to showing and receiving love will help you experience"
                " deeper and richer levels of intimacy with your partner-starting today.",
    category=arts)
session.add(love5)
session.commit()

manuscript = Book(
    title="Standard Wirebound Manuscript Paper",
    description="(Manuscript Paper). 96-page wirebound book; 12 staves per page; 8 1/2 x 11 ; Music Notation Guide.",
    category=arts)
session.add(manuscript)
session.commit()

katieDaisy = Book(
    title="Katie Daisy 2019 - 2020 On-the-Go Weekly Planner: 17-Month Calendar with Pocket ",
    description="Celebrate your daily adventures with the whimsical and uplifting artwork of Katie Daisy as your"
                " companion. Each month of this special-edition planner begins with a captivating two-page color "
                "spread of illustrations in Katie's signature watercolor style.",
    category=arts)
session.add(katieDaisy)
session.commit()

bornACrime = Book(
    title="Born a Crime: Stories from a South African Childhood ",
    description="#1 NEW YORK TIMES BESTSELLER  The compelling, inspiring, and comically sublime story of one man's"
                " coming-of-age, set during the twilight of apartheid and the tumultuous days of freedom that followed",
    category=arts)
session.add(bornACrime)
session.commit()

# Biographies & Memoirs

educated = Book(
    title="Educated: A Memoir",
    description="Born to survivalists in the mountains of Idaho, Tara Westover was seventeen the first time she set"
                " foot in a classroom. Her family was so isolated from mainstream society that there was no one to "
                "ensure the children received an education, and no one to intervene when one of Tara's older brothers "
                "became violent. When another brother got himself into college, Tara decided to try a new kind of life."
                " Her quest for knowledge transformed her, taking her over oceans and across continents, to Harvard and "
                "to Cambridge University. Only then would she wonder if she'd traveled too far, if there was still a "
                "way home.",
    category=biographies)
session.add(educated)
session.commit()

become = Book(
    title="Become",
    description="In a life filled with meaning and accomplishment, Michelle Obama has emerged as one of the most iconic"
                " and compelling women of our era. As First Lady of the United States of America-the first African "
                "American to serve in that role-she helped create the most welcoming and inclusive White House in "
                "history, while also establishing herself as a powerful advocate for women and girls in the U.S. and"
                " around the world, dramatically changing the ways that families pursue healthier and more active "
                "lives, and standing with her husband as he led America through some of its most harrowing moments."
                " Along the way, she showed us a few dance moves, crushed Carpool Karaoke, and raised two down-to-earth"
                " daughters under an unforgiving media glare. ",
    category=biographies)
session.add(become)
session.commit()

lastBlackUnicorn = Book(
    title="The Last Black Unicorn",
    description="Growing up in one of the poorest neighborhoods of South Central Los Angeles, Tiffany learned to "
                "survive by making people laugh. If she could do that, then her classmates would let her copy their "
                "homework, the other foster kids she lived with wouldn't beat her up, and she might even get a "
                "boyfriend. Or at least she could make enough money-as the paid school mascot and in-demand Bar "
                "Mitzvah hype woman-to get her hair and nails done, so then she might get a boyfriend.",
    category=biographies)
session.add(lastBlackUnicorn)
session.commit()

trevorNoah = Book(
    title="Trevor Noah: A Biography Booklet",
    description="Trevor Noah is a South African comedian, writer, producer, political commentator, actor, and television"
                " host. He is best known for being the host of The Daily Show on Comedy Central since September 2015."
                " Noah began his career as an actor, presenter, and comedian in his native South Africa. He held several"
                " television hosting roles with the South African Broadcasting Corporation, and was the runner-up in "
                "their fourth season of Strictly Come Dancing in 2008. From 2010 to 2011, Noah was the creator and host"
                " of Tonight with Trevor Noah on M-Net and DStv. His stand-up comedy career attained international "
                "success, leading to appearances on American late-night talk shows and British panel shows. In 2014, "
                "Noah became the Senior International Correspondent for The Daily Show, an American satirical news "
                "program. The following year, he was announced as the successor of long-time host Jon Stewart. Although "
                "ratings for the show declined following Stewart's departure, Noah's tenure has been generally "
                "favourably reviewed, attracting particular attention for his interview with young conservative "
                "personality Tomi Lahren in late 2016.",
    category=biographies)
session.add(trevorNoah)
session.commit()

# Business & Investing

callSignChaos = Book(
    title="Call Sign Chaos: Learning to Lead",
    description="Call Sign Chaos is the account of Jim Mattis's storied career, from wide-ranging leadership roles in "
                "three wars to ultimately commanding a quarter of a million troops across the Middle East. Along the "
                "way, Mattis recounts his foundational experiences as a leader, extracting the lessons he has learned "
                "about the nature of warfighting and peacemaking, the importance of allies, and the strategic "
                "dilemmas-and short-sighted thinking-now facing our nation. He makes it clear why America must return "
                "to a strategic footing so as not to continue winning battles but fighting inconclusive wars. ",
    category=business)
session.add(callSignChaos)
session.commit()

the7Habits = Book(
    title="The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change",
    description="What are the habits of successful people? The 7 Habits of Highly Effective People has captivated "
                "readers for 25 years. It has transformed the lives of Presidents and CEOs, educators, parents, and "
                "students-in short, millions of people of all ages and occupations have benefited from Dr. Covey's 7 "
                "Habits book. And, it can transform you.",
    category=business)
session.add(the7Habits)
session.commit()

howToWin = Book(
    title="How To Win Friends and Influence People",
    description="Dale Carnegie's rock-solid, time-tested advice has carried countless people up the ladder of success"
                " in their business and personal lives. One of the most groundbreaking and timeless bestsellers "
                "of all time.",
    category=business)
session.add(howToWin)
session.commit()

# Children's Books

caterpillar = Book(
    title="The Very Hungry Caterpillar",
    description="The very hungry caterpillar literally eats his way through the pages of the book-and right into your"
                " child's heart...",
    category=children)
session.add(caterpillar)
session.commit()

goodnightMoon = Book(
    title="Goodnight Moon",
    description="In a great green room, tucked away in bed, is a little bunny. 'Goodnight room, goodnight moon.'"
                " And to all the familiar things in the softly lit room-to the picture of the three little bears "
                "sitting on chairs, to the clocks and his socks, to the mittens and the kittens, to everything one by "
                "one-the little bunny says goodnight.",
    category=children)
session.add(goodnightMoon)
session.commit()

placesGo = Book(
    title="Oh, the Places You'll Go! ",
    description="From soaring to high heights and seeing great sights to being left in a Lurch on a prickle-ly perch, "
                "Dr. Seuss addresses life's ups and downs with his trademark humorous verse and illustrations, while "
                "encouraging readers to find the success that lies within. In a starred review, Booklist notes, "
                "'Seuss's message is simple but never sappy: life may be a 'Great Balancing Act,' but through it all "
                "'There's fun to be done.''' A perennial favorite and a perfect gift for anyone starting a new phase "
                "in their life!",
    category=children)
session.add(placesGo)
session.commit()

# Cookbooks, Food & Wine

lowCarb = Book(
    title="The 30-Minute Low-Carb Cookbook: 100 Simple & Satisfying Recipes for a Healthy Diet",
    description="Featuring 100 recipes you can prepare in less than half an hour, The 30-Minute Low-Carb Cookbook is "
                "your first stop on the path to healthier eating for life. Delicious enough for non-dieters, these "
                "hearty favorites will be dinnertime-or anytime-hits with partners, kids, guests, and more.",
    category=cookbook)
session.add(lowCarb)
session.commit()

dessert = Book(
    title="Dessert Cooking for Two: 115 Perfectly Portioned Sweets for Every Occasion",
    description="Say goodbye to pre-packaged sweets and hello to fresh and flavorful desserts. From The Very Best "
                "Chocolate Chip Cookies to Cinnamon Sugar Monkey Bread, Dessert Cooking for Two helps you create "
                "delicious desserts that are just the right size for two. Enjoy all the fun treats you crave without "
                "worrying about overindulging or wasting lots of leftovers.",
    category=cookbook)
session.add(dessert)
session.commit()

# History

callSign = Book(
    title="Call Sign Chaos: Learning to Lead",
    description="Call Sign Chaos is the account of Jim Mattis's storied career, from wide-ranging leadership roles in "
                "three wars to ultimately commanding a quarter of a million troops across the Middle East. Along the "
                "way, Mattis recounts his foundational experiences as a leader, extracting the lessons he has learned "
                "about the nature of warfighting and peacemaking, the importance of allies, and the strategic "
                "dilemmas-and short-sighted thinking-now facing our nation. He makes it clear why America must "
                "return to a strategic footing so as not to continue winning battles but fighting inconclusive wars.",
    category=history)
session.add(callSign)
session.commit()

seaStories = Book(
    title="Sea Stories: My Life in Special Operations",
    description="Admiral William H. McRaven is a part of American military history, having been involved in some of "
                "the most famous missions in recent memory, including the capture of Saddam Hussein, the rescue of "
                "Captain Richard Phillips, and the raid to kill Osama bin Laden.",
    category=history)
session.add(seaStories)
session.commit()

noBetterFriend = Book(
    title="No Better Friend, No Worse Enemy: The Life of General James Mattis",
    description="The first in-depth look at the marine hero who has become one of the most beloved and admired men in "
                "America today: Secretary of Defense James Mattis.",
    category=history)
session.add(noBetterFriend)
session.commit()

# Literature & Fiction

theWorldDoesnt = Book(
    title="The World Doesn't Require You: Stories",
    description="Established by the leaders of the country's only successful slave revolt in the mid-nineteenth "
                "century, Cross River still evokes the fierce rhythms of its founding. In lyrical prose and singular "
                "dialect, a saga beats forward that echoes the fables carried down for generations-like the screecher "
                "birds who swoop down for their periodic sacrifice, and the water women who lure men to wet deaths.",
    category=literature)
session.add(theWorldDoesnt)
session.commit()

theInstitute = Book(
    title="The Institute: A Novel",
    description="In the middle of the night, in a house on a quiet street in suburban Minneapolis, intruders "
                "silently murder Luke Ellis's parents and load him into a black SUV. The operation takes less than two"
                " minutes. Luke will wake up at The Institute, in a room that looks just like his own, except there's"
                " no window. And outside his door are other doors, behind which are other kids with special "
                "talents-telekinesis and telepathy-who got to this place the same way Luke did: Kalisha, Nick, "
                "George, Iris, and ten-year-old Avery Dixon. They are all in Front Half. ",
    category=literature)
session.add(theInstitute)
session.commit()

fahrenheit = Book(
    title="Fahrenheit 451",
    description="Guy Montag is a fireman. In his world, where television rules and literature is on the brink of "
                "extinction, firemen start fires rather than put them out. His job is to destroy the most illegal of "
                "commodities, the printed book, along with the houses in which they are hidden.",
    category=literature)
session.add(fahrenheit)
session.commit()

outsiders = Book(
    title="The Outsiders",
    description="No one ever said life was easy. But Ponyboy is pretty sure that he's got things figured out. He knows "
                "that he can count on his brothers, Darry and Sodapop. And he knows that he can count on his "
                "friends-true friends who would do anything for him, like Johnny and Two-Bit. But not on much else "
                "besides trouble with the Socs, a vicious gang of rich kids whose idea of a good time is beating up on"
                " 'greasers' like Ponyboy. At least he knows what to expect-until the night someone takes things too "
                "far.",
    category=literature)
session.add(outsiders)
session.commit()

alchemisty = Book(
    title="The Alchemist",
    description="Paulo Coelho's masterpiece tells the mystical story of Santiago, an Andalusian shepherd boy who "
                "yearns to travel in search of a worldly treasure. His quest will lead him to riches far different-and "
                "far more satisfying-than he ever imagined. Santiago's journey teaches us about the essential wisdom "
                "of listening to our hearts, of recognizing opportunity and learning to read the omens strewn along "
                "life's path, and, most importantly, to follow our dreams.",
    category=literature)
session.add(alchemisty)
session.commit()

# Mystery, Thriller & Suspense

womanWindow = Book(
    title="The Woman in the Window",
    description="For readers of Gillian Flynn and Tana French comes one of the decade's most anticipated debuts, "
                "published in forty-one languages around the world and in development as a major film from Fox: a "
                "twisty, powerful Hitchcockian thriller about an agoraphobic woman who believes she witnessed a crime "
                "in a neighboring house.",
    category=mystery)
session.add(womanWindow)
session.commit()

skye = Book(
    title="Skye",
    description="Skye Parker is the only daughter of the Sun God and his Moon. She is also a woman of many talents... "
                "A Princess, an Heir, a designer, and a beautiful woman who is confident in who she is...and has no "
                "problem going after what she wants.",
    category=mystery)
session.add(skye)
session.commit()

mockingbird = Book(
    title="To Kill a Mockingbird",
    description="One of the most cherished stories of all time, To Kill a Mockingbird has been translated into more "
                "than forty languages, sold more than forty million copies worldwide, served as the basis for an "
                "enormously popular motion picture, and was voted one of the best novels of the twentieth century by "
                "librarians across the country. A gripping, heart-wrenching, and wholly remarkable tale of "
                "coming-of-age in a South poisoned by virulent prejudice, it views a world of great beauty and "
                "savage inequities through the eyes of a young girl, as her father-a crusading local lawyer-risks "
                "everything to defend a black man unjustly accused of a terrible crime.",
    category=mystery)
session.add(mockingbird)
session.commit()

theInn = Book(
    title="The Inn",
    description="he Inn at Gloucester stands alone on the rocky shoreline. Its seclusion suits former Boston police "
                "detective Bill Robinson, novice owner and innkeeper. As long as the dozen residents pay their rent, "
                "Robinson doesn't ask any questions. Neither does Sheriff Clayton Spears, who lives on the second "
                "floor.",
    category=mystery)
session.add(theInn)
session.commit()

# Romance

mermaids = Book(
    title="When We Believed in Mermaids",
    description="Josie Bianci was killed years ago on a train during a terrorist attack. Gone forever. It's what her "
                "sister, Kit, an ER doctor in Santa Cruz, has always believed. Yet all it takes is a few "
                "heart-wrenching seconds to upend Kit's world. Live coverage of a club fire in Auckland has captured "
                "the image of a woman stumbling through the smoke and debris. Her resemblance to Josie is unbelievable."
                " And unmistakable. With it comes a flood of emotions-grief, loss, and anger-hat Kit finally has a "
                "chance to put to rest: by finding the sister who-s been living a lie.",
    category=romance)
session.add(mermaids)
session.commit()

dressmaker = Book(
    title="The Dressmaker's Gift",
    description="Paris, 1940. With the city occupied by the Nazis, three young seamstresses go about their normal "
                "lives as best they can. But all three are hiding secrets. War-scarred Mireille is fighting with the "
                "Resistance; Claire has been seduced by a German officer; and Vivienne's involvement is something she "
                "can't reveal to either of them.",
    category=romance)
session.add(dressmaker)
session.commit()

brokenKnight = Book(
    title="Broken Knight",
    description="Underneath the meek, tomboy exterior everyone loves (yet pities) is a girl who knows exactly what, "
                "and who, she wants-namely, the boy from the treehouse who taught her how to curse in sign language. "
                "Who taught her how to laugh. To live. To love. ",
    category=romance)
session.add(brokenKnight)
session.commit()

theVine = Book(
    title="The Vine Witch",
    description="For centuries, the vineyards at Chateau Renard have depended on the talent of their vine witches, "
                "whose spells help create the world-enowned wine of the Chanceaux Valley. Then the skill of divining"
                " harvests fell into ruin when sorciere Elena Boureanu was blindsided by a curse. Now, after breaking "
                "the spell that confined her to the shallows of a marshland and weakened her magic, Elena is struggling"
                " to return to her former life. And the vineyard she was destined to inherit is now in the possession "
                "of a handsome stranger.",
    category=romance)
session.add(theVine)
session.commit()

# Science Fiction & Fantasy

blacksmith = Book(
    title="The Blacksmith Queen",
    description="When a prophesy brings war to the Land of the Black Hills, Keeley Smythe must join forces with a "
                "clan of mountain warriors who are really centaurs in a thrilling new fantasy romance series from "
                "New York Times bestselling author G.A. Aiken.",
    category=scifi)
session.add(blacksmith)
session.commit()

gideon = Book(
    title="Gideon the Ninth",
    description="Tamsyn Muir's Gideon the Ninth unveils a solar system of swordplay, cut-throat politics, and lesbian"
                " necromancers. Her characters leap off the page, as skillfully animated as arcane revenants. The "
                "result is a heart-pounding epic science fantasy.",
    category=scifi)
session.add(gideon)
session.commit()

handmaid = Book(
    title="The Handmaid's Tale",
    description="In Margaret Atwood's dystopian future, environmental disasters and declining birthrates have led to"
                " a Second American Civil War. The result is the rise of the Republic of Gilead, a totalitarian regime "
                "that enforces rigid social roles and enslaves the few remaining fertile women. Offred is one of these,"
                " a Handmaid bound to produce children for one of Gilead's commanders. Deprived of her husband, her "
                "child, her freedom, and even her own name, Offred clings to her memories and her will to survive. "
                "At once a scathing satire, an ominous warning, and a tour de force of narrative suspense, The "
                "Handmaid's Tale is a modern classic.",
    category=scifi)
session.add(handmaid)
session.commit()

# Teen & Young Adult

hpone = Book(
    title="Harry Potter and the Sorcerer's Stone",
    description="Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at "
                "number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are"
                " swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great "
                "beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter "
                "is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure"
                " is about to begin!",
    category=teens)
session.add(hpone)
session.commit()

hptwo = Book(
    title="Harry Potter and the Chamber of Secrets",
    description="Harry Potter's summer has included the worst birthday ever, doomy warnings from a house-elf called "
                "Dobby, and rescue from the Dursleys by his friend Ron Weasley in a magical flying car! Back at "
                "Hogwarts School of Witchcraft and Wizardry for his second year, Harry hears strange whispers echo "
                "through empty corridors - and then the attacks start. Students are found as though turned to stone... "
                "Dobby's sinister predictions seem to be coming true.",
    category=teens)
session.add(hptwo)
session.commit()

pjone = Book(
    title="the Lightning Thief",
    description="Percy Jackson is a good kid, but he can't seem to focus on his schoolwork or control his temper. "
                "And lately, being away at boarding school is only getting worse-Percy could have sworn his pre-algebra"
                " teacher turned into a monster and tried to kill him.",
    category=teens)
session.add(pjone)
session.commit()

pjtwo = Book(
    title="The Sea of Monsters",
    description="After a summer spent trying to prevent a catastrophic war among the Greek gods, Percy Jackson finds"
                " his seventh-grade school year unnervingly quiet. His biggest problem is dealing with his new friend,"
                " Tyson-a six-foot-three, mentally challenged homeless kid who follows Percy everywhere, making it hard"
                " for Percy to have any 'normal' friends. But things don't stay quiet for long...",
    category=teens)
session.add(pjtwo)
session.commit()

hungerGames = Book(
    title="The Hunger Games",
    description="In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol"
                " surrounded by twelve outlying districts. The Capitol keeps the districts in line by forcing them "
                "all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual "
                "Hunger Games, a fight to the death on live TV.",
    category=teens)
session.add(hungerGames)
session.commit()

print "Books and Categories ADDED!!!"