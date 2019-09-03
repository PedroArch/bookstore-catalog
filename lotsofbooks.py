import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Book

# Starting session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Creating Categories

arts = Category("Arts & Photography")
session.add(arts)
session.commit()

biographies = Category("Biographies & Memoirs")
session.add(biographies)
session.commit()

business = Category("Business & Investing")
session.add(business)
session.commit()

children = Category("Children's Books")
session.add()
session.commit()

cookbook = Category("Cookbook, Food & Wine")
session.add(cookbook)
session.commit()

history = Category("History")
session.add(history)
session.commit()

literature = Category("Literature & Fiction")
session.add(literature)
session.commit()

mystery = Category("Mistery & Suspense")
session.add(mystery)
session.commit()

romance = Category("Romance")
session.add(romance)
session.commit()

scifi = Category("Sci-Fi & Fantasy")
session.add(scifi)
session.commit()

teens = Category("Teens & Young Adult")
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
    description="In the #1 New York Times bestseller The 5 Love Languages, you’ll discover the secret that has "
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