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
        print("Rajasthan (Hindi: Rājasthāna, pronounced [ɾaːd͡ʒəsˈtʰaːn] ⓘ; lit. 'Land of Kings')[12] is a state in northwestern India.[13][14][15] It is the largest Indian state by area and the seventh largest by population. It covers 342,239 square kilometres (132,139 mi2) or 10.4 per cent of India's total geographical area. It is on India's northwestern side, where it comprises most of the wide and inhospitable Thar Desert (also known as the Great Indian Desert) and shares a border with the Pakistani provinces of Punjab to the northwest and Sindh to the west, along the Sutlej-Indus River valley. It is bordered by five other Indian states: Punjab to the north; Haryana and Uttar Pradesh to the northeast; Madhya Pradesh to the southeast; and Gujarat to the southwest. Its geographical location is 23°3' to 30°12' North latitude and 69°30' to 78°17' East longitude, with the Tropic of Cancer passing through its southernmost tip.")
    def gujrat(self):
        print("Gujarat (Gujarati: Gujarāt, pronounced [ˈɡudʒəɾaːt] ⓘ) is a state along the western coast of India. Its coastline of about 2,340 km (1,450 mi) is the longest in the country, most of which lies on the Kathiawar peninsula. Gujarat is the fifth-largest Indian state by area, covering some 196,024 km2 (75,685 mi2); and the ninth-most populous state, with a population of 60.4 million in 2011. It is bordered by Rajasthan to the northeast, Dadra and Nagar Haveli and Daman and Diu to the south, Maharashtra to the southeast, Madhya Pradesh to the east, and the Arabian Sea and the Pakistani province of Sindh to the west. Gujarat's capital city is Gandhinagar, while its largest city is Ahmedabad.[14] The Gujaratis are indigenous to the state, and their language, Gujarati, is the state's official language.")
    def up(self):
        print("Uttar Pradesh (UTT-ər prə-DESH, abbr. UP; Hindi: Uttar Pradēś, pronounced [ˈʊt̪ːəɾ pɾə.ˈdeːɕ] ⓘ, lit. 'Northern Province') is a state in northern India. With over 241 million inhabitants, it is India's most populated state.[14] The state is bordered by Rajasthan to the west, Haryana, Himachal Pradesh and Delhi to the northwest, Uttarakhand and Nepal to the north, Bihar to the east, Madhya Pradesh, Chhattisgarh and Jharkhand to the south. It is the fourth-largest Indian state by area covering 243,286 km2 (93,933 sq mi), accounting for 7.3 per cent of the total area of India. Lucknow serves as the state capital, with Prayagraj being the judicial capital. It is divided into 18 divisions and 75 districts. Uttar Pradesh is the Indian state with the highest number of bordering states, sharing its boundaries with nine other states and one union territory.")
    def mp(self):
        print("Madhya Pradesh (/ˌmɑːdjə prəˈdɛʃ/;[11] Hindi: [ˈmədʱjə pɾəˈdeːʃ] ⓘ; lit. 'Central Province') is a state in central India. Its capital is Bhopal. Other major cities include Indore, Gwalior, Jabalpur, Chhindwara and Sagar. Madhya Pradesh is the second largest Indian state by area and the fifth largest state by population with over 72 million residents. It borders the states of Rajasthan to the northwest, Uttar Pradesh to the northeast, Chhattisgarh to the east, Maharashtra to the south and Gujarat to the west.[1")
    def hr(self):
        print("Haryana[a] is a state located in the northwestern part of India. It is bordered by Punjab and Himachal Pradesh to the north, by Rajasthan to the west and south, by Delhi to the southeast, while river Yamuna forms its eastern border with Uttar Pradesh. The state capital is Chandigarh, which it shares with the neighbouring state of Punjab. The city of Gurgaon is among India's largest financial and technology hubs.[11] The most populous city is Faridabad, a part of the National Capital Region. In terms of area, it ranks 21st in India, with around 1.5% (44,212 km2 or 17,070 sq mi) of India's land area.[1][12]. Haryana has 6 administrative divisions, 22 districts, 72 sub-divisions, 93 revenue tehsils, 50 sub-tehsils, 140 blocks, 154 cities and towns, 7,356 villages, and 6,222 villages panchayats.[12][")
    def pb(self):
        print("Punjab (/pʌnˈdʒɑːb/ pun-JAHB;[8] Panjabi: pañjāba, pronounced [pəɲˈd͡ʒaːb] ⓘ) is a state in northwestern India. Forming part of the larger Punjab region of the Indian subcontinent, the state is bordered by the Indian states and union territories of Himachal Pradesh to the north and northeast, Haryana to the south and southeast, Rajasthan to the southwest, Jammu and Kashmir to the north. To the west, it shares an international border with the identically named Pakistani province of Punjab.[9] Chandigarh serves as a shared captial for Punjab as well as Haryana. The state covers an area of 50,362 square kilometres (19,445 square miles), which is 1.53% of India's total geographical area,[10] making it the 19th-largest Indian state by area out of 28 Indian states (20th largest, if Union Territories are considered). With over 27 million inhabitants, Punjab is the 16th-largest Indian state by population, comprising 23 districts.[11] Punjabi, written in the Gurmukhi script, is the most widely spoken and the official language of the state.[12] The main ethnic group are the Punjabis, with Sikhs (57.7%) and Hindus (38.5%) forming the dominant religious groups.[13] Three of the five traditional Punjab rivers — the Sutlej, Beas, and Ravi — flow through the state.[14]")
class USA(country):
    def info1(self):
        print("-------States-------")
        l=["California", "Texas", "New York", "Florida", "Alaska"]
        for k in range(len(l)):
            print(k,'.',l[k])
    def california(self):
        print("California is a U.S. state in the Western United States that lies on the Pacific Coast. It borders Oregon to the north, and Nevada and Arizona to the east; it also shares an international border with the Mexican state of Baja California to the south. With over 39 million residents across an area of 163,696 square miles (423,970 km2), it is the largest U.S. state by population and third-largest by area.")
    def texas(self):
        print('''Texas (/ˈtɛksəs/ ⓘ TEK-səss)[c]
        is the most populous state in the Southern United States. It borders the American states of Louisiana to
        the east, Arkansas to the northeast, Oklahoma to the north, and New Mexico to the west.
            To the south and southwest, it has an international border with the Mexican states of Chihuahua,
        Coahuila, Nuevo León, and Tamaulipas, along a natural boundary formed by the Rio Grande. Texas has a coastline on
        the Gulf of Mexico to the southeast. Covering 268,596 square miles (695,660 km2) and with
        an estimated population of over 31.7 million residents in 2025,[8] it is the second-largest 
        U.S. state both by area and by population. Texas is nicknamed the "Lone Star State" for the
    single star on its flag, symbolic of its former status as an independent country, the Republic of Texas.[9]''')
    def new(self):
        print("New York, often called New York City (NYC),[b] is the most populous city in the United States. It is located at the southern tip of New York State on New York Harbor, one of the world's largest natural harbors. The city comprises five boroughs—Manhattan, Brooklyn, Queens, the Bronx, and Staten Island—each being coextensive with its respective county. It is the geographical and demographic center of both the Northeast megalopolis and the New York metropolitan area, the largest metropolitan area in the United States by both population and urban area. New York is a global center of finance[10][11] and commerce, culture, technology,[12] entertainment and media, academics and scientific output,[13] the arts and fashion, and, as home to the headquarters of the United Nations, international diplomacy.[c] New York City is known for its fast pace and continuous urban energy.[19][20][21]")
    def florida(self):
        print("Florida (/ˈflɒrɪdə/ ⓘ FLORR-id-ə, Spanish: [floˈɾiða] ⓘ) is a state in the Southeastern and South Atlantic regions of the United States. It borders the Gulf of Mexico to the west, Alabama to the northwest, Georgia to the north, the Atlantic Ocean to the east, the Straits of Florida to the south, and The Bahamas to the southeast. About two-thirds of Florida occupies a peninsula between the Gulf of Mexico and the Atlantic Ocean. It has the longest coastline in the contiguous United States, spanning approximately 1,350 miles (2,170 km), not including its many barrier islands. It is the only state that borders both the Gulf of Mexico and the Atlantic Ocean. With a population of over 23 million, it is the third-most populous state in the United States and ranks seventh in population density as of 2020. Florida spans 65,758 square miles (170,310 km2), ranking 22nd in area among the states. The Miami metropolitan area, anchored by the cities of Miami, Fort Lauderdale, and West Palm Beach, is the state's largest metropolitan area, with a population of 6.138 million; the most populous city is Jacksonville. Florida's other major population centers include Tampa Bay, Orlando, Cape Coral, and the state capital of Tallahassee.")
    def alaska(self):
        print("Alaska (/ə.ˈlæs.kə/ ⓘ, ə-LASS-kə) is a U.S. state located in the northwestern regions of North America. Part of the Western United States region, it is one of the two non-contiguous U.S. states, alongside Hawaii. Alaska is considered to be the northernmost, westernmost, and, longitudinally, the easternmost state in the United States.[a] It is a semi-exclave of the U.S., bordering the Canadian territory of Yukon and the province of British Columbia to the east. It shares a western maritime border in the Bering Strait with Russia's Chukotka Autonomous Okrug, and is closer to another continent (Asia) than any other U.S. state. The Chukchi and Beaufort Seas of the Arctic Ocean lie to the north, and the Pacific Ocean to the south.")
class Russia(country):
    def info2(self):
        print("-------States-------")
        l=['Moscow', 'Saint Petersburg','Tatarstan']
        for k in range(len(l)):
            print(k,'.',l[k])
    def Moscow(self):
        print("Moscow[a] is the capital and largest city of Russia, standing on the Moskva River in Central Russia. It has a population estimated at over 13 million residents within the city limits,[5] over 19.1 million residents in the urban area,[6] and over 21.5 million residents in its metropolitan area.[14] The city covers an area of 2,511 square kilometers (970 mi2), while the urban area covers 5,891 square kilometers (2,275 mi2),[6] and the metropolitan area covers over 26,000 square kilometers (10,000 mi2).[14] Moscow is among the world's largest cities, being the most populous city entirely in Europe,[b] the largest urban and metropolitan area in Europe,[6][14] and the largest city by land area on the European continent.[15")
    def SaintPetersburg(self):
        print("Saint Petersburg,[c] formerly known as Petrograd (Петроград) and later Leningrad (Ленинград),[d] is the second-largest city in Russia, after Moscow, the nation's capital. Situated on the Neva River at the head of the Gulf of Finland on the Baltic Sea, its area of 1,439 square kilometers (556 sq mi) makes it the smallest administrative division of Russia by area. The city had a population of 5,601,911 residents as of 2021,[3] with more than 6.4 million people living in the metropolitan area. Saint Petersburg is the fourth-most populous city in Europe, the most populous city on the Baltic Sea, and the world's northernmost city of more than 1 million residents. As the former capital of the Russian Empire, and a historically strategic Baltic port, it is governed as a federal city.")
    def Tatarstan(self):
        print("Tatarstan,[a] officially the Republic of Tatarstan,[b] sometimes also called Tataria,[c] is a republic of Russia located in Eastern Europe. It is a part of the Volga Federal District; and its capital and largest city is Kazan, an important cultural centre in Russia. The region's main source of wealth is oil with a strong petrochemical industry.")
class Japan(country):
    def info3(self):
        print("-------States-------")
        l=['Hokkaido', 'Tohoku', 'Kanto']
        for k in range(len(l)):
            print(k,'.',l[k])
    def Hokkaido(self):
        print("Hokkaido[nb 1] is the second-largest and northernmost of Japan's four main islands. Together with its surrounding islands, it comprises the largest and northernmost prefecture, making up its own region.[7] The Tsugaru Strait separates Hokkaido from Honshu. The two islands are connected by railway via the Seikan Tunnel.")
    def Tohoku(self):
        print("Date Masamune (1567–1636), feudal lord of Date clan, expanded trade in the Tōhoku region.[7][8] Although initially faced with attacks by hostile clans, he managed to overcome them after a few defeats and eventually ruled one of the largest fiefdoms of the later Tokugawa shogunate. He built many palaces and worked on many projects to beautify the region.[7] He is also known to have encouraged foreigners to come to his land.[8]")
    def Kanto(self):
        print("Kanto is the main geographical region of Japan that contains Tokyo, Yokohama, and the Kanto Plain. It holds about one-third of the country's total people and serves as the political and money center of Japan.")



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
    elif y == "texas":
        obj1.texas()
    elif y == "1":
        obj1.new()
    elif y == "2":
        obj1.florida()
    elif y == "3":
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


# In[ ]:





# In[ ]:





# In[ ]:




