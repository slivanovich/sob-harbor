Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Hyatt Regency Casablanca: The Hyatt Regency Casablanca is a luxury hotel in the Old Medina of Casablanca, Morocco, located just to the west of Sheraton Casablanca Hotel & Towers.  The hotel has a 255 rooms, including 223 deluxe king and twin rooms, 11 junior suites, 19 executive suites and 3 royal suites, and 8 conference rooms accommodating from 20 to 400 people.  Its restaurants, such as "Cafe M", "Dar Beida", "Bissat" and the outdoor "Les Bougainvillées" cater in Moroccan, fusion or Parisian cuisine.  "Dar Beida" is a traditional Moroccan restaurant resembling an Arab tent and "Bissat" is located under a Moorish dome.

Tulalip Resort Casino: Tulalip Resort Casino is an Indian casino and resort in Quil Ceda Village, Washington, owned and operated by the Tulalip Tribes of Washington.  It opened in 2004 as Tulalip Casino, and was renamed in late 2007 because of the new hotel, which opened August 15, 2008.  In addition to the AAA Four Diamond award-winning 12-story hotel with 370 rooms and suites, the resort includes 192,000 sqft of gaming space.  The property has 7 restaurants: Tulalip Bay, Blackfish, Cedars Cafe, The Draft Bar and Grill, Journeys East, Eagles Buffet and Canoes Carvery.  The T Spa is the resort's onsite spa and features 14,000 sqft of treatment rooms.  There are also meeting facilities, and the Canoes Cabaret, Orca Ballroom, and Tulalip Amphitheatre for entertainment events.

Zen Pinball: Zen Pinball is a series of pinball machine video games for iOS and the PlayStation 3 developed by Zen Studios.  The iOS releases are two separate applications, each containing one table; Zen Pinball: Rollercoaster, released July 7, 2008, and Zen Pinball: Inferno, released October 31, 2008.  "Zen Pinball" for the PlayStation 3 was published by Sony Computer Entertainment and features four tables, plus an additional six tables as downloadable content.  It was released on the PlayStation Network on May 14, 2009.  It is the PlayStation 3 counterpart to the "Pinball FX" series on the Xbox 360, and the first pinball game on the PlayStation 3.  The game was also released on Android devices as Zen Pinball THD on December 1, 2011, and the Nintendo 3DS as Zen Pinball 3D via the Nintendo eShop on December 1, 2011 in Europe and January 12, 2012 in North America.

Trams in France: Trams in France go back to 1837 when a 15 km steam tram line connected Montrond-les-Bains and Montbrison in the Loire.  With the development of electric trams at the end of the 19th century, networks proliferated in French cities over a period of 15 years.  Although nearly all of the country's tram systems were replaced by bus services in the 1930s or shortly after the Second World War, France is now in the forefront of the revival of tramways and light rail systems around the globe.  Only tram lines in Lille and Saint-Étienne have operated continuously since the 19th century; the Marseille tramway system ran continuously until 2004 and only closed then for 3 years (until 2007) for extensive refurbishment into a modern tram network.  Since the opening of the Nantes tramway in 1985, more than twenty towns and cities across France have built new tram lines.  As of 2013, there are 25 operational tram networks in France, with 3 under construction and 4 more planned.  France is also home to Alstom, a leading tram manufacturer.

Menzan Zuihō: Menzan Zuihō (面山瑞方, 1683-1769) was a Japanese Sōtō Zen scholar and abbot of the Zenjo-ji and Kuin-ji temples active during the Tokugawa era.  Born in Ueki, Kyushu, Menzan was the most influential Sōtō Zen writer of his time and his work continue to influence Sōtō Zen scholarship and practice today.  Menzan's scholarship was part of the Tokugawa movement of returning to original historical sources to revitalize Zen (復古.  "fukko" - "return to the old"), especially the works of Dōgen Zenji.  Before Menzan the works of Dōgen were not widely studied or put into practice, he helped revitalize the Sōtō school by analyzing and building on Dogen's writings.  Menzan used Dōgen to promote a reform of the Sōtō sect, which included reforming the monastic code and meditation practice.  Due to Menzan's efforts, Dōgen studies now occupies a central position in Sōtō Zen thought.  Menzan wrote to advocate the use of the old Song dynasty monk's hall system, in which monks ate, slept, and meditated in one large monk's hall, rather than in separate rooms as was commonly practiced in Japan at the time.  Menzan was the most prolific Sōtō zen scholar, having written over a hundred titles of detailed scholarship on monastic regulations, precepts, ordination, dharma transmission and philology.  Menzan was also involved in lecturing to the public and teaching laymen and laywomen meditation practice.  One of his most famous works, the Buddha Samadhi ("Jijuyu Zanmai") is addressed to laypeople and focuses on the teachings of Dōgen.

Treasure Island Hotel and Casino: Treasure Island Hotel & Casino (also known as "TI") is a hotel and casino located on the Las Vegas Strip in Paradise, Nevada, USA with 2,664 rooms and 220 suites, and is connected by tram to The Mirage as well as pedestrian bridge to the Fashion Show Mall shopping center.  Since March 2009, TI is owned and operated by Phil Ruffin.

Wanova: Wanova, Inc, headquartered in San Jose, California, provides software to help IT organizations manage, support and protect data on desktop and laptop computers.  Wanova’s primary product, Wanova Mirage, was designed as an alternative to server-hosted desktop virtualization technologies, combining the centralization and management capabilities of virtual desktop infrastructure (VDI) with features that allow the system to work for laptops and other WAN-connected desktops.  Mirage enables IT organizations to store the complete contents of each personal computer (PC) in the data center for centralized management and data protection.  End users execute a locally-cached copy of their centrally-stored PC, which makes it possible for users to use their PC whether or not they are connected to the network.  The software includes additional features that optimize the system to work over a wide area network(WAN).  Wanova Mirage (now VMware Mirage) software was designed for information technology organizations supporting distributed enterprises and has three primary components: the Mirage Client, Mirage Server and capabilities that optimize network and storage efficiency.

Viejas Casino: Viejas Casino and Resort is a hotel casino and outlet center owned by the Viejas Band of Kumeyaay Indians, located in Alpine, California.  The casino has over 2,000 slot machines, up to 86 table games, three restaurants, a deli, bingo, an off-track betting facility, lounge, concert venues and multiple indoor and outdoor meeting spaces.  Opened in March 2013, the original hotel had 128 rooms; an expansion was completed in October 2015 with the opening of an additional hotel tower with 109 deluxe rooms and luxury suites increasing hotel accommodations to a total of 237 rooms and suites.

Mark E. Brown: Mark E. Brown is an American businessman and former CEO of Zen Entertainment and a former vice president of The Howard Hughes Corporation.  His company currently has partnership deals with ESPN Radio, Fox Sports Radio, NBCSports.com, Ultimate Fighting Championship, World Wrestling Entertainment, and casinos such as the Treasure Island Hotel and Casino, Hard Rock Hotel.  He is also the former Partner and President of R&R Partners, the ad agency which created the "What Happens in Vegas, Stays in Vegas" advertising campaign for the Las Vegas Convention and Visitors Authority.  In addition, Brown is founder and director of Service 1st Bank of Nevada, valued in 2010 around $210 million, and previously served as the President of MBC Communications.

The Ritz-Carlton, Georgetown: The Ritz-Carlton, Georgetown is a luxury hotel located in the Georgetown neighborhood of Washington, D.C., in the United States.  It is near The Kennedy Center and the Georgetown waterfront.  It is an AAA 5-star luxury hotel, and has 86 rooms, 27 premier suites, and five luxury suites.  All rooms and suites have a view of the Potomac River and historic Georgetown.  It contains a 140 ft smokestack coming from the lobby fireplace.  It is a small hotel and is known to be good for privacy.  The hotel contains a restaurant, bar, and a fitness center with a newly refreshed spa after a $1.5 million dollar renovation in 2016.  The rooms are on average 450 sqft in size and is located in a historic industrial building.

Question: Zen Entertainment has partnership with which casino that has 2,664 rooms and 220 suites, and is connected by tram to The Mirage?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "casino_name": {
      "type": "string",
      "description": "The name of the casino."
    },
    "room_details": {
      "type": "object",
      "properties": {
        "total_rooms": {
          "type": "integer",
          "description": "The total number of rooms in the casino hotel."
        },
        "total_suites": {
          "type": "integer",
          "description": "The total number of suites in the casino hotel."
        }
      },
      "required": [
        "total_rooms",
        "total_suites"
      ],
      "additionalProperties": false
    },
    "connection_details": {
      "type": "object",
      "properties": {
        "connected_by_tram_to": {
          "type": "string",
          "description": "The name of the location or entity the casino is connected to by tram."
        }
      },
      "required": [
        "connected_by_tram_to"
      ],
      "additionalProperties": false
    },
    "is_zen_entertainment_partner": {
      "type": "boolean",
      "description": "Indicates if the casino has a partnership with Zen Entertainment."
    }
  },
  "required": [
    "casino_name",
    "room_details",
    "connection_details",
    "is_zen_entertainment_partner"
  ],
  "additionalProperties": false
}
