{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBut It's Better If You Do: \"But It's Better If You Do\" is a song by American rock band Panic!  at the Disco, released on May 16, 2006 as the third single from their debut album \"A Fever You Can't Sweat Out\" (2005).  Taking its title from a quote said by Natalie Portman's character in the 2004 film \"Closer\", the song was written by band members Ryan Ross, Brendon Urie and Spencer Smith, and is about being in and not enjoying the location of a strip club.  \"But It's Better If You Do\" failed to recreate the success the previous single \"I Write Sins Not Tragedies\" had in the United States but found chart prominence in Europe and Oceania, peaking at number 10 in New Zealand, number 15 in Australia and number 23 in the UK.  The accompanying music video for the song, directed by Shane Drake, features the band performing at a masquerade-style strip club.\n\nDéjà Vu (company): Déjà Vu Consulting, Inc., is a U.S. company that (as of 2017 ) operates about 132 strip clubs in 41 U.S. states, as well as multiple clubs in the United Kingdom, Australia, France, Canada, and Mexico.  The company also operates a large chain of adult retail stores, multiple online adult enterprises, gay bars, nightclubs, and has substantial real estate holdings.  It is the largest strip club operator in the world, and one of the largest adult businesses in history.  In 2016, the group opened Deja Vu Showgirls Tijuana, the largest adult entertainment club in the world, at over 140,000 square feet.  It also operates the second largest adult club in the world, Larry Flynt's Hustler Club in Las Vegas.\n\nJiggles: Jiggles, sometimes called Jiggles Strip Club, was a strip club in Tualatin, Oregon, in the United States.  In March 2014, Jiggles received media attention when Jake Stoneking, a 19 year old diagnosed with medulloblastoma, included a visit to the club on his list of activities to complete before his death.  The club shut down and the building in which it was housed was demolished later that year.\n\nThree Sisters Tavern: Three Sisters Tavern, sometimes abridged as Three Sisters and nicknamed \"Six Tits\", was a gay bar and strip club in Portland, Oregon, United States.  The bar was founded in 1964 and began catering to Portland's gay community in 1997 following the deaths of the original owners.  The business evolved into a strip club featuring an all-male revue.  Also frequented by women, sometimes for bachelorette parties, Three Sisters was considered a hub of Portland's nightlife before closing in 2004.\n\nZanies Comedy Club: Zanies Comedy Club (also known simply as Zanies) is a comedy club chain founded by Rick Uchwat in November 1978.  Its first location was in Chicago, Illinois and it is the third longest continually operating comedy club in the United States.\n\nMary's Club: Mary's Club is the oldest strip club in Portland, Oregon, in the United States.  In 1954 Roy Keller bought the business from Mary Duerst Hemming, who owned and operated Mary's as a piano bar beginning in the 1930s.  Keller initially hired go-go dancers as entertainment during the piano player's breaks, later hiring them full-time because of their popularity.  Topless dancers wearing pasties were introduced in 1955.  The club also featured comics, musicians, singers and other acts.  All-nude dancing began in 1985, after a judicial ruling against City of Portland ordinances banning it in venues which served alcohol.\n\nSpearmint Rhino: Spearmint Rhino is a chain of strip clubs that operates venues throughout the United States, United Kingdom, and Australia.  The club opened in 1989 as a supplement to the existing Peppermint Elephant Restaurant.  This first Spearmint Rhino was located in Upland, California.\n\nLas Vegas Dancers Alliance: The Las Vegas Dancers Alliance was an organization of adult entertainment workers in Las Vegas founded in 2002 by Andrea Hackett in response to regulations adopted by Clark County, Nevada that criminalized lap dances.  It grew to include 1,000 members from strip clubs throughout the Las Vegas valley including Crazy Horse Too, Spearmint Rhinoand many others.  Yet despite its size, L.V.D.A. was unable to bring about substantive changes to the law or the adult club industry as a whole.  Part of the blame fell on dancers unwilling to participate in rallies, meetings and events.  Yet much of it fell on club owners who colluded with local law enforcement to intimidate dancers.  Another factor were attacks from the left and a lack of assistance from established unions.  The Huffington Post wrote a hit piece on Ms. Hackett at the height of L.V.D.A's influence which the Nevada State Democratic Party linked on their website.  Unwilling to alienate their left wing allies, the Teamsters, who had promised to help, rescinded their offer.  SEIU followed suit.  This spelled the end of L.V.D.A.\n\nPlayboy Club: The Playboy Club was initially a chain of nightclubs and resorts owned and operated by Playboy Enterprises.  The first club opened at 116 E. Walton Street in downtown Chicago, Illinois, United States, on February 29, 1960.  Each club generally featured a Living Room, a Playmate Bar, a Dining Room, and a Club Room.  Members and their guests were served food and drinks by Playboy Bunnies, some of whom were featured in \"Playboy\" magazine.  The clubs offered name entertainers and comedians in the Club Rooms, and local musicians and the occasional close-up magician in the Living Rooms.  Starting with the London and Jamaica club locations, the Playboy Club became international in scope.  In 1991, the club chain became defunct.  On October 6, 2006 a new club was opened in Las Vegas, and in 2010 new clubs were opened as well in Macao and Cancun.  In time the Las Vegas club closed on June 4, 2012, the Macao club closed in 2013 and the Cancun club closed in 2014.  In May 2014 the Commerce Casino in Los Angeles opened a Playboy themed lounge consisting of gaming tables and Playboy Bunny cocktail waitresses.\n\nCarriage Room: The Carriage Room was a strip club in Portland, Oregon, in the United States.  It operated for eighteen years at 1000 Southwest Broadway, underneath the Broadway Theatre.  It closed in 1988 when the theatre building was demolished.  Carriage Room was one of seven clubs owned by Roy Keller (three in Portland and four in Sacramento, California); only Carriage Room and Mary's Club were strip clubs.\n\nQuestion: What Upland, California strip club chain, with venues in the United States, United Kingdom, and Australia, was a member of the L.V.D.A.?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the strip club chain.\"\n    },\n    \"founding_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the first club was located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the first club was located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the first club was located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"countries_of_operation\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of countries where the strip club chain operates.\"\n    },\n    \"was_lvda_member\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the club was a member of the Las Vegas Dancers Alliance (L.V.D.A.).\"\n    }\n  },\n  \"required\": [\n    \"club_name\",\n    \"founding_location\",\n    \"countries_of_operation\",\n    \"was_lvda_member\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "club_name": {
        "type": "string",
        "description": "The name of the strip club chain."
      },
      "founding_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the first club was located."
          },
          "state": {
            "type": "string",
            "description": "The state where the first club was located."
          },
          "country": {
            "type": "string",
            "description": "The country where the first club was located."
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "countries_of_operation": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of countries where the strip club chain operates."
      },
      "was_lvda_member": {
        "type": "boolean",
        "description": "Indicates whether the club was a member of the Las Vegas Dancers Alliance (L.V.D.A.)."
      }
    },
    "required": [
      "club_name",
      "founding_location",
      "countries_of_operation",
      "was_lvda_member"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
