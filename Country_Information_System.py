#!/usr/bin/env python
# coding: utf-8

# In[34]:


class country:
    def __init__(self):
        print('Countries')
        l=['India','USA','Russia','Japan']
        for k in range(len(l)):
            print(k,'.',l[k])
class India(country):
    def info(self):
        print('-------States-------')
        l=["Rajasthan","Gujrat","UP","MP","Haryana","Punjab"]
        for k in range(len(l)):
            print(k,'.',l[k])
    def raj(self):
        print('''Rajasthan, known as the "Land of Kings" and India's largest desert state, is a captivating destination in northern 
        India that mesmerise travellers from around the world. The state presents a harmonious blend of lively cities, hospitable locals, exquisite cuisine, majestic palaces, and grand forts. Rajasthan offers a perfect travel experience, seamlessly fusing timeless allure with contemporary charm. This enchanting state beckons you with a symphony of vibrant cultures, a canvas painted with tales of valour, and landscapes that will steal your heart.''')
    def gujrat(self):
        print('''Gujarat is one of the most diverse States in India. Its history stretches over a long years from the age old Harappa Civilization to the Mughal period. Gujarat’s endless journey from roots to wings is timeless with historical and cultural traditions glorifying the State. The diverse and vibrant state of Gujarat has a significant contribution to the cultural aspect of India. The sheer simplicity and amiability of Gujarati’s have made them a flourishing community. The state of Gujarat boasts a vibrant art, architecture, culture, and heritage; all of which is quite evident in the day-to-day lives of the locals. The diversity exhibited by Gujarat is a result of the various ethnic groups constituting Gujarat’s population; including Indic and Dravidian groups.''')
    def up(self):
        print('''Uttar Pradesh, the heartland of India, awaits travellers with a treasure trove of experiences and landmarks. This sprawling state is a testament to India's rich heritage, boasting 3 UNESCO World Heritage Sites - the majestic Taj Mahal, Fatehpur Sikri and Agra Fort – all three in the city of Agra! Uttar Pradesh is home to the ancient and spiritual city of Varanasi, where rituals along the sacred Ganges River mesmerise one and all. Explore the royal grandeur of Lucknow's historic palaces, savour delectable cuisine that tantalises the taste buds, and delve into the spiritual tapestry of Ayodhya and Mathura.''')
    def mp(self):
        print('''In the heart of India lies a realm where history whispers through ancient corridors, where nature's beauty reigns supreme, and where vibrant cultures flourish in harmony with the land. Madhya Pradesh, a state steeped in captivating narratives, stands as a testament to the richness of India's heritage and the magnificence of its diverse landscapes. The state boasts of three UNESCO World Heritage sites that serve as living testimonies to its historical significance. The mystical temples of Khajuraho, the sacred aura of Sanchi Stupa, and the ancient artistry preserved in Bhimbetka Rock Shelters all converge to tell the stories of a bygone era, each engraving its unique mark on the canvas of time.
Madhya Pradesh is also called the ‘Tiger State of India,’ a title well-deserved as its national parks and wildlife reserves provide a sanctuary for these majestic creatures. Within its sprawling forests and lush landscapes, the elusive tigers roam freely, embodying the untamed spirit of the wild and adding to the state's allure as a biodiversity hotspot.''')
    def hr(self):
        print('The name of Haryana instantly conjures up the image of a State which astonishingly combines both-antiquity and plenty. The Vedic land of Haryana has been a cradle of Indian culture and civilization. Indian traditions regard this region as the matrix of creation of northern altar’ where Brahma performed the pristine sacrifice and created the universe. This theory of creation has been confirmed to a large extent by archaeological investigations carried out by Guy E. Pilgrim in 1915, who has established that 15 million years ago, early man lived in the Haryana Shivaliks. The Vamana Purana states that King Kuru ploughed the field of Kurukshetra with a golden ploughshare drawn by the Nandi of Lord Shiva and reclaimed an area of seven Kosas.')
    def pb(self):
        print('In the northwest region of India, lies the state of Punjab, a vibrant and culturally diverse land that offers heritage, a bounty of nature, and an array of experiences to enthral every traveller. From its rich past and heritage to its lush landscapes, from its delectable cuisine to its lively festivals, Punjab is a treasure trove of culture and heritage that spans millennia. Its history dates back to ancient civilizations, and its rich cultural heritage is evident in its architecture, art, and traditions.')
class USA(country):
    def info1(self):
        print("-------States-------")
        l=["California", "Texas", "New York", "Florida", "Alaska"]
        for k in range(len(l)):
            print(k,'.',l[k])
    def california(self):
        print('More than 20,000 years ago, the first people arrived in what is now California. They walked from Asia, crossing on a strip of land that’s now submerged under a body of water between Russia and the United States called the Bering Strait. For thousands of years, hundreds of Native American tribes thrived on this land.Europeans landed in the 16th century, with Spanish explorers leading the way. But when Mexico gained its independence from Spain in 1821, it also gained control of California. That didn’t last long: in 1848, at the end of the Mexican-American War, California became a U.S. territory. After gold was struck in 1848 at Sutter’s Mill in Coloma, more than 100,000 people, nicknamed “forty-niners,” rushed to California in 1849 to seek their fortunes. Just a year later, in 1850, California officially became a state')
    def texas(self):
        print('''Texas, constituent state of the United States of America. It became the 28th state of the union in 1845. Texas occupies the south-central segment of the country and is the largest state in area except for Alaska. The state extends nearly 1,000 miles (1,600 km) from north to south and about the same distance from east to west.
Water delineates many of its borders. The wriggling course of the Red River makes up the eastern two-thirds of Texas’s boundary with Oklahoma to the north, while the remainder of the northern boundary is the Panhandle, which juts northward, forming a counterpart in the western part of that state. The Sabine River forms most of the boundary with Louisiana to the east, where by land it is bounded by Arkansas as well. The crescent-shaped coastline of the Gulf of Mexico lies to the southeast, and the Rio Grande carves a shallow channel that separates Texas from Mexico to the southwest. The state of New Mexico lies to the west. Austin, in the south-central part of the state, is the capital.''')
    def new(self):
        print('''New York, constituent state of the United States of America, one of the 13 original colonies and states. New York is bounded to the west and north by Lake Erie, the Canadian province of Ontario, Lake Ontario, and the Canadian province of Quebec; to the east by the New England states of Vermont, Massachusetts, and Connecticut; to the southeast by the Atlantic Ocean and New Jersey; and to the south by Pennsylvania. The capital is Albany.
Until the 1960s New York was the country’s leading state in nearly all population, cultural, and economic indexes. Its displacement by California beginning in the middle of that decade was caused by the enormous growth rate that has persisted on the West Coast rather than by a large decline in New York itself. Texas overtook New York as the second most populous state in 2000. Still, New York remains one of the most populous states in the country, and its gross economic product exceeds those of all but a handful of countries throughout the world.''')
    def florida(self):
        print('''Florida, constituent state of the United States of America. It was admitted as the 27th state in 1845. Florida is the most populous of the southeastern states and the second most populous Southern state after Texas. The capital is Tallahassee, located in the northwestern panhandle.

Intracoastal Waterway, Fort Lauderdale, Florida
1 of 2
Intracoastal Waterway, Fort Lauderdale, FloridaThe Intracoastal Waterway (right) at Fort Lauderdale, Florida.
Key Largo
2 of 2
Key LargoPalm trees lining a beach in Key Largo, Florida Keys, Florida, U.S..
Geographic location has been the key factor in Florida’s long and colorful development, and it helps explain the striking contemporary character of the state. The greater part of Florida lies on a peninsula that protrudes southeastward from the North American continent, separating the waters of the Atlantic Ocean from those of the Gulf of Mexico and pointing toward Cuba and the Caribbean Sea beyond. Florida shares a land border with only two other states, both along its northern boundary: Georgia (east) and Alabama (west). The nearest foreign territory is the island of Bimini in the Bahamas, some 50 miles (80 km) to the east of the state’s southern tip. Florida is the southernmost of the 48 conterminous United States, its northernmost point lying about 100 miles (160 km) farther south than California’s southern border. The Florida Keys, a crescent of islands that forms the state’s southernmost portion, extend to within about 75 miles (120 km) of the Tropic of Cancer. Florida’s marine shoreline totals more than 8,400 miles (13,500 km), including some 5,100 miles (8,200 km) along the gulf; among U.S. states, only Alaska has a longer coastline.''')
    def alaska(self):
        print('''Alaska, constituent state of the United States of America. It was admitted to the union as the 49th state on January 3, 1959.

Alaska lies at the extreme northwest of the North American continent, and the Alaska Peninsula is the largest peninsula in the Western Hemisphere. Because the 180th meridian passes through the state’s Aleutian Islands, Alaska’s westernmost portion is in the Eastern Hemisphere. Thus, technically, Alaska is in both hemispheres.

Quick Facts
Alaska: flag1 of 4
See article: flag of Alaska
 
Seal of Alaska2 of 4
Seal of Alaska
 
Alaska: state bird3 of 4
Alaska: state bird
 
Alaska: state flower4 of 4
Alaska: state flower
Capital: Juneau
Population1: (2020) 733,391; (2024 est.) 740,133
Governor: Michael J. Dunleavy (Republican)
Date Of Admission: January 3, 1959
U.S. Senators: Lisa Murkowski (Republican) Daniel Sullivan (Republican)
Alaska is bounded by the Beaufort Sea and the Arctic Ocean to the north, Canada’s Yukon territory and British Columbia province to the east, the Gulf of Alaska and the Pacific Ocean to the south, the Bering Strait and the Bering Sea to the west, and the Chukchi Sea to the northwest. The capital is Juneau, which lies in the southeast, in the panhandle region.''')
class Russia(country):
    def info2(self):
        print("-------States-------")
        l=['Moscow', 'Saint Petersburg','Tatarstan']
        for k in range(len(l)):
            print(k,'.',l[k])
    def Moscow(self):
        print('''Moscow, city, capital of Russia, located in the far western part of the country. Since it was first mentioned in the chronicles of 1147, Moscow has played a vital role in Russian history. It became the capital of Muscovy (the Grand Principality of Moscow) in the late 13th century; hence, the people of Moscow are known as Muscovites. Today Moscow is not only the political center of Russia but also the country’s most populous city and its industrial, cultural, scientific, and educational capital. For more than 600 years Moscow also has been the spiritual center of the Russian Orthodox Church.
The capital of the Union of Soviet Socialist Republics (U.S.S.R.) until the union dissolved in 1991, Moscow attracted world attention as a center of communist power; indeed, the name of the seat of the former Soviet government and the successor Russian government, the Kremlin (Russian: Kreml), was a synonym for Soviet authority. The dissolution of the U.S.S.R. brought tremendous economic and political change, along with a significant concentration of Russia’s wealth, into Moscow. Area 414 square miles (1,035 square km). Pop. (2010) city, 11,738,547; (2020 est.) city, 12,678,079.''')
    def SaintPetersburg(self):
        print('''St. Petersburg, city and port, extreme northwestern Russia. A major historical and cultural centre and an important port, St. Petersburg lies about 400 miles (640 km) northwest of Moscow and only about 7° south of the Arctic Circle. It is the second largest city of Russia and one of the world’s major cities. St. Petersburg has played a vital role in Russian history since its founding in 1703. For two centuries (1712–1918) it was the capital of the Russian Empire. The city is remembered as the scene of the February (March, New Style) and October (November, New Style) Revolutions of 1917 and for its fierce defense while besieged during World War II. Architecturally, it ranks as one of the most splendid and congenial cities of Europe. Its historic district was designated a UNESCO World Heritage site in 1990. The city is also home to the 87-story Lakhta Centre, the tallest builiding in Russia and Europe and one of the tallest buildings in the world. Area city, 550 square miles (1,400 square km). Pop. (2010) 4,879,566; (2012 est.) 4,953,219.''')
    def Tatarstan(self):
        print('''Tracing its history back more than a millennium to the Volga Bolgars, the area now known as the Republic of Tatarstan came under the influence and later control of Moscow in the 16th century. Conquered by Ivan IV, the Kazan Khanate was reformed as the Kazan Governorate in the Russian Empire, where it played an important role in both the geographic expansion and economic development of the Tsar’s domains. After the Bolshevik Revolution in 1917, Tatarstan was declared an Autonomous Soviet Socialist Republic; the fall of the USSR in 1991 led to a name change to the Republic of Tatarstan, now a subject of the Russian Federation. Today, its capital, Kazan, is one of Russia’s largest and most economically vibrant cities, where the post-Soviet period has seen a revitalization, not only of various educational and business ventures, but a reemergence of cultural and linguistic assertions of autonomy.''')
class Japan(country):
    def info3(self):
        print("-------States-------")
        l=['Hokkaido', 'Tohoku', 'Kanto']
        for k in range(len(l)):
            print(k,'.',l[k])
    def Hokkaido(self):
        print('Hokkaido is Japan’s largest prefecture and the ultimate getaway for nature-lovers! That’s why we’re covering a bunch of interesting facts about Hokkaido for your next visit, from its climate for each season to the prefecture’s history, culture, and geography. From the Natural World Heritage Site of the Shiretoko Peninsula to the diverse plant life in the Kushiro Marsh, Hokkaido brims with natural phenomena seldom seen elsewhere. We can’t wait for you to travel to Hokkaido and experience it for yourself.')
    def Tohoku(self):
        print('''Tohoku, literally “East-North” of Japan, is just north of Tokyo and is easily accessible by train. Tohoku is rich in breathtaking nature, intriguing history, and warm culture. Tohoku is beautiful during all four seasons, with unique features that make the North-East region worth visiting all year round. During the spring, Tohoku is home to some of the most famous and beautiful cherry blossom viewing sites. In summer, Tohoku becomes lush and verdant, hosting three of the largest Natsu Matsuri (summer festivals) in Japan. During autumn, Tohoku’s vast natural sites are famous for early fall foliage. In the winter, Tohoku has unique natural phenomena and is a paradise for winter sports such as skiing and snowboarding.

Tohoku’s rich history includes the famous Fujiwara clan of ancient times, as well as the Date clan of the feudal era. Many of Tohoku’s most famous monuments incorporate its naturally mountainous terrain and diverse natural life (both plant and animal), creating a naturally tranquil atmosphere with picturesque scenery referenced in historical poems and stories. With many undeveloped regions, the unspoiled forests are home to rare plants and animals of Japan. Beyond forests, Tohoku lies along the coast with beautiful views of the ocean allowing for a bountiful aquatic ecosystem as well.

Whether it is a hot spring bath in rural Tohoku or a stay in the city, the local delicacies are delicious and diverse, offering meals from both land and sea. From a fresh, rustic meal to grilled beef tongue, the flavors of Tohoku are a unique experience. Visit Tohoku and take a journey to the northern regions of Honshu, full of nature, culture, and history— easily accessed in just 2-4 hours by transit from Tokyo!''')
    def Kanto(self):
        print('''Kantō Range, mountain range, on Honshu, Japan, lying to the west of the Kantō Plain. Extending 80 miles (130 km) from north to south and 50 miles (80 km) from east to west, it forms the physical division between Kantō region (chihō; east) and Chūbu region (west).
Geologically the range displays crystalline schists and formations about 2.6 to 540 million years old, which are zonally arranged from north to south. The Kantō Range joins with the Akaishi Range in the west.
The range may be divided into two distinct sections, which are separated by the Katsura River, a tributary of the Sagami River. The Chichibu Mountains in the north are the highest mountains of northeastern Japan, containing Mount Kimpō, which rises to 8,514 feet (2,595 meters). The mountains are dissected by narrow, canyonlike valleys and are dominated by steep slopes. River terraces provide habitable regions in the interior. The intermontane basin of Chichibu, near the eastern limit of the range, has been an important settlement area throughout Japanese history.''')


# In[35]:


obj =India()


# In[29]:


obj1 = USA()


# In[19]:


obj2 = Russia()


# In[32]:


obj3 = Japan()


# In[37]:


obj =India()

x = input("Enter the country name: ")

if x == "0":

    obj.info()

    y = input("Enter the state index: ").lower()

    if y == "0":
        obj.raj()
    elif y == "1":
        obj.gujrat()
    elif y == "2":
        obj.up()
    elif y == "3":
        obj.mp()
    elif y == "4":
        obj.hr()
    elif y == "5":
        obj.pb()
    else:
        print("Invalid State...")

elif x == "1":

    obj1.info1()

    y = input("Enter the state name: ").lower()

    if y == "0":
        obj1.california()
    elif y == "1":
        obj1.texas()
    elif y == "2":
        obj1.new()
    elif y == "3":
        obj1.florida()
    elif y == "4":
        obj1.alaska()
    else:
        print("Invalid State...")

elif x == "2":

    obj2.info2()

    y = input("Enter the state name: ").lower()

    if y == "0":
        obj2.Moscow()
    elif y == "1":
        obj2.SaintPetersburg()
    elif y == "2":
        obj2.Tatarstan()
    else:
        print("Invalid State...")

elif x == "3":

    obj3.info3()

    y = input("Enter the state name: ").lower()

    if y == "0":
        obj3.Hokkaido()
    elif y == "1":
        obj3.Tohoku()
    elif y == "2":
        obj3.Kanto()
    else:
        print("Invalid State...")

else:
    print("Invalid Country...")


