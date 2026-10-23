{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouthland Mall (Hayward, California): Southland Mall is a major shopping mall in Hayward, California, owned and managed by Rouse Properties after General Growth Properties spun off the mall and some of its other properties to form Rouse in 2012.  The mall is primarily a single-level structure, with a small lower level beneath anchor retailer JC Penney, and free standing restaurants in the outlying parking areas.  The center is located off I-880 at Winton Avenue, at the western end of the city.  The mall currently houses anchor stores like, Sears, Macy's, and JC Penney.  Other businesses include Ross, Foot Locker, Forever 21, Gamestop, Applebee's, Ashley Stewart and Bath & Body Works, among others.  The mall has a food court and a TimeOut Arcade.\n\nCrozet Historic District: The Crozet Historic District is a national historic district located in Crozet, Albemarle County, Virginia.  The historic district was listed on the National Register of Historic Places on November 28, 2012.  It includes 227 properties deemed to contribute to the historic character of the area along with 73 additional non-contributing properties for a total of 300 properties.  They include representative examples of the mid-19th century Greek Revival and Gothic Revival styles, late-Victorian Italianate, Queen Anne, and Victorian styles and from the late-19th century- and early-20th century, Colonial Revival, Tudor Revival, Bungalow/Craftsman and Commercial styles.  The district also includes examples of modern-era Postmodern style.\n\nThe Cockpit (Leeds): The Cockpit was a club and music venue in Leeds, West Yorkshire, England.  Formerly the Cock of the North pub, the venue was located on Swinegate, close to Leeds station.  It hosted small to medium-sized touring artists as well as occasional showcases for local acts.  The venue's main room held 500, whilst the second room held 250, and the small upstairs room held 125.\n\nTennis at the 2012 Summer Olympics: The tennis tournaments at the 2012 Summer Olympics in London were staged at the All England Club in Wimbledon, from 28 July to 5 August.  This was the first Olympic grass court tournament since tennis was reintroduced as an Olympic sport and the first to be held at a Grand Slam venue in the Open era.  (Two other 2012 Summer Olympic bid finalists had also offered Grand Slam venues – second-place finisher Paris offered the French Open venue, the Stade Roland Garros, while fourth-place finisher New York offered the US Open venue, the USTA Billie Jean King National Tennis Center in Flushing Meadows-Corona Park, Queens.)\n\nCochrane Park: Cochrane Park, located at Newcastle upon Tyne, England, is the principal competitive venue for football, rugby and cricket at Newcastle University.  It has three county standard football pitches, three county standard rugby pitches, a cricket square, a lacrosse pitch and five tennis courts.  The site also offers a pavilion with team changing facilities, function suite and bar facilities.  Newcastle University was an official Games-Time Training Venue for the London 2012 Olympic Games, and the University's Cochrane Park sports ground was a dedicated football training venue for the Games in July 2012.\n\nCaesars Palace: Caesars Palace is a AAA Four Diamond luxury hotel and casino in Paradise, Nevada, United States.  The hotel is situated on the west side of the Las Vegas Strip between Bellagio and The Mirage.  It is one of the most prestigious casino hotels in the world and one of Las Vegas's largest and best known landmarks.\n\nWildhorse Saloon: The Wildhorse Saloon is a country/western-themed restaurant, live music venue, and dance club located in downtown Nashville, Tennessee.  It is managed by Marriott and owned by Ryman Hospitality Properties (formerly known as Gaylord Entertainment Company).  Originally opened on June 1, 1994 in a converted warehouse, the Wildhorse initially capitalized on the line dancing craze of the early-to-mid-1990s.  While it continues to enjoy success as a bar and line dance venue, it has become a successful concert venue in recent years for all genres of music.  Because of its downtown location, open bar, large atrium, and permanent stage, the Wildhorse is also often used as a formal banquet hall.\n\nHistory of Bolivia (1982–present): The history of Bolivia since 1982 begins with the restorations of democracy after the rule of the military junta of 1982.  Evo Morales has held the presidency since 2006.  A new constitution was enacted in 2009.  Bolivia's population has roughly doubled over this period, from 5 million in 1980 to 10 million as of 2012.\n\nEvo 2012: The 2012 Evolution Championship Series (commonly referred to as Evo 2012 or EVO 2012) was a fighting game event held at Caesars Palace, Las Vegas on July 6–8.  The event featured a major tournament for six fighting games, including \"\" and \"Ultimate Marvel vs. Capcom 3\", as well as various smaller-scale competitions.\n\nHōheikan: The Hōheikan (豊平館 , Hōheikan ) is a historical building and a wedding venue, located in Nakajima Park, Chūō-ku, Sapporo, Hokkaidō, Japan.  The building has previously been a hotel, guest house, event venue, and military camp.  Currently, the Hōheikan is registered as one of the National Important Cultural Properties, and used as a wedding venue, restaurant and meeting facility.  The building is run by the Sapporo city.\n\nQuestion: Between which properties is the venue, at which Evo 2012 was held, located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the event.\"\n    },\n    \"venue_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the venue where the event was held.\"\n    },\n    \"venue_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the venue (e.g., hotel, casino).\"\n    },\n    \"located_between_properties\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of properties between which the venue is located.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"venue_name\",\n    \"located_between_properties\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the event."
      },
      "venue_name": {
        "type": "string",
        "description": "The name of the venue where the event was held."
      },
      "venue_type": {
        "type": "string",
        "description": "The type of the venue (e.g., hotel, casino)."
      },
      "located_between_properties": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of properties between which the venue is located."
      }
    },
    "required": [
      "event_name",
      "venue_name",
      "located_between_properties"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
