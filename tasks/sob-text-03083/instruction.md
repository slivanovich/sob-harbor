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
M2 (railcar): The M2 railcar is a series of 244 electric multiple unit cars produced for the Metropolitan Transportation Authority and the Connecticut Department of Transportation that ran on the New Haven Line (then part of Penn Central, now part of Metro North).  Built primarily by General Electric in a consortium with the Budd Company, Canadian Vickers and Avco between 1972 and 1977, the cars were initially branded as Cosmopolitans.  Final assembly of the M2 cars using Budd or Vickers bodies was completed at GE's Transportation Division in Erie, Pennsylvania.

Trams in Adelaide: Until 1958, trams formed a network spanning most of suburban Adelaide, with a history dating back to 1878.  Adelaide ran horse trams from 1878 to 1914 and electric trams from 1909, but has primarily relied on buses for public transport since 1958.  Electric trams and trolleybuses were Adelaide's main public transport throughout the life of the electric tram network.  All trams except the Glenelg tram were closed in the 1950s.  The Glenelg tram remains in operation and was upgraded and extended in 2007-2010.

Trolleybuses in Adelaide: The Adelaide trolleybus system formed part of the public transport network in Adelaide, South Australia from 1932 until 1963.

Transport in Adelaide: The metropolitan area of Adelaide, South Australia is served by a wide variety of transport.  Being centrally located on the Australian mainland, it forms a hub for east-west and north-south routes.  The road network includes major expressways such as the Southern Expressway, the South Eastern Freeway, the Port River Expressway, the Northern Expressway and the South Road Superway.  The city also has a public transport system managed by Adelaide Metro, consisting of a contracted bus system including the O-Bahn Busway (a guided busway), six metropolitan railway lines, and the Glenelg-Adelaide-Hindmarsh Tram.  According to a study conducted by the Australian Bureau of Statistics, Adelaide has the highest passenger vehicle travel to work (84%) and the second lowest proportion of people walking to work (2.9%)–something that is being combated by the South Australian government in an effort to increase citizen ridership and use of public transport.

Highway authority in the United States: Highway authority in the United States includes a planning process of different forms of transportation and governmental funding given.  Transportation in the United States creates mobility and access to different resources within cities.  Some forms of transportation in the United States includes trolleys, metros, ferries, bus routes, highways, bicycling, trams and walking.  All these forms are not used in every city.  Each city based on the development and planning process of transportation decides what form of transportation fits best.  One important factor in the planning process of transportation is the government interference such as funding, policies and regulations.  The department of transportation (DOT) plays an important role in the process of developing transportation in different cities.

Adelaide University Boat Club: The Adelaide University Boat Club is a rowing club affiliated with the University of Adelaide.  The club was founded in 1881, and in 1896 helped to form the Adelaide University Sports Association.  The main clubrooms, donated by Robert Barr Smith in 1909, are located on the north bank of the River Torrens on War Memorial Drive, adjacent to the Adelaide University Sports Grounds.  The shed has two boat bays, a gym and weights room and a small bar.  The club also leases a secondary boatshed at the South Australian Rowing Association complex on Military Road at West Lakes, and also trains regularly at Port Adelaide's North Arm Creek and Murray Bridge.  Members have included rowers of all levels, from total beginners to Olympic Gold Medallists.  The club shares the nickname ""The Blacks"" with the Adelaide University Football Club.

Title 49 of the Code of Federal Regulations: CFR Title 49 - Transportation is one of fifty titles comprising the United States Code of Federal Regulations (CFR).  Title 49 is the principle set of rules and regulations (sometimes called administrative law) issued by the Departments of Transportation and Homeland Security, federal agencies of the United States regarding transportation and transportation related security.  This title is available in digital and printed form, and can be referenced online using the Electronic Code of Federal Regulations (e-CFR).

Mule drivers of Metsovo: The mule drivers of Metsovo were one of the most significant professional transporters in the Ottoman Empire.  In the Ottoman Empire and especially in the Balkans, the transportation of goods was performed almost exclusively with mules.  The range and method of operation of the mule owners made the profession of mule driver one of the most important ones for all land commerce of the time.  In 1707, written sources start mentioning them as already having a trade guild established which leads us to believe that they were occupied in the transportation of goods since even older times.  Throughout the 18th and 19th century they form one of the most active groups in the goods transportation industry in the Balkans.  Pouqueville says the Vlach mule drivers are known with the name Metsovites, while he considers the people of Metsovo and the people of Zagori as the most active mule drivers in Turkey’s European market.  Bοué describes the keratzides of Metsovo as the most famous in all "Albania" and among the most renowned in the Balkans.  According to Goudas, the transportation of goods from Bucharest, Constantinople (İstanbul), Belgrade and Adrianople (Edirne) was performed almost exclusively by Metsovites mule drivers, in Turkish kerantsimpasi.

Steve Novick: Steven "Steve" Novick (born February 8, 1963) is a politician in the U.S. state of Oregon and a former environmental lawyer and political activist.  Most recently he served a four-year term as a Portland City Commissioner – a member of the City Council of Portland – from January 2013 to January 2017.  He was elected in May 2012 and assumed office on January 1, 2013.  In 2008, he ran for the Democratic Party's nomination for the United States Senate, for the seat then held by Republican Gordon Smith, but narrowly lost to Oregon House speaker Jeff Merkley.  On the Portland city council, he was in charge of the city's transportation department, among other responsibilities.  Novick ran for reelection to the city council in 2016 but lost to Chloe Eudaly.

Transportation Materiel Command: The Transportation Materiel Command (TMC) was a unit of the US Army, originally headquartered in Marietta, Pennsylvania.  In March 1955, it merged with the Transportation Corps Army Aviation Field Service Office (TCAAFSO) to form the Transportation Supply and Maintenance Command (TSMC) headquartered in St. Louis, Missouri; on 1 October 1959, the TSMC was redesignated back to being the Transportation Materiel Command.  It became the Aviation and Surface Materiel Command on 1 November 1962.

Question: What form of transportation in Adelaide ran from 1932 to 1963?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "transport_type": {
      "type": "string",
      "description": "The specific type of transportation system."
    },
    "city": {
      "type": "string",
      "description": "The city where the transportation system operated."
    },
    "country": {
      "type": "string",
      "description": "The country where the transportation system operated."
    },
    "start_year": {
      "type": "integer",
      "description": "The year the transportation system began operation."
    },
    "end_year": {
      "type": "integer",
      "description": "The year the transportation system ceased operation."
    }
  },
  "required": [
    "transport_type",
    "city",
    "country",
    "start_year",
    "end_year"
  ],
  "additionalProperties": false
}
