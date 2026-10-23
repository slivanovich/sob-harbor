{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSpeak n Spell Music: Speak n Spell Music (or Speak n Spell Music Publishing Pty Ltd) was an Australia and New Zealand based Record Label, Artist Management, International Touring Company and music licensing company.  The record label was based in Collingwood, it was founded by Jonathan Wilson, David Shrimpton and David Benge.  It released over 120 titles that were distributed via by Inertia and Universal.  Some artists released on Speak n Spell included Editors, Midlake, School of Seven Bells, Warpaint and Dappled Cities.  The management company looked after four acts signed to both independent and major labels locally and internationally in the UK, Europe and the USA.  The Management roster included Cut Off Your Hands (NZ), Violent Soho, Jack Ladder (AMP Winner 2008), Kid Sam (2009 J Award nominee), Ghoul and producer Scott Horscroft.  Speak and Spell Music was conceived and established in 2004 and closed in April 2011.\n\nMerck Mercuriadis: Merck Mercuriadis (born October 2, 1963, in Schefferville, Quebec, Canada) is a Canadian–American music executive and a music manager.  He is the current CEO, Founder and managing partner of Hipgnosis Music Ltd., an artist management firm, publisher and record label based in London and Los Angeles.  Mercuriadis is also known as the former manager of several notable rock and pop bands and musicians including Guns N' Roses, Iron Maiden, Elton John, Morrissey, Pet Shop Boys, Macy Gray, Mary J. Blige, Joss Stone, Jane's Addiction and Wheatus Mercuriadis is notable for serving from October 1986 to June 2007, as director and CEO of the Sanctuary Group PLC, a major management company, an independent record label, a merchandise company, and a booking agency based in London, New York and Los Angeles.\n\nUK Project: UK Project (stylized as UK.PROJECT) is a Japanese independent record label and an artist management company which runs various music labels, artist management agencies and concert venues under its umbrella company.\n\nE.G. Records: E.G. Records was a British artist management company and independent record label, mostly active during the 1970s and 1980s.  The initials stood for its founders, David Enthoven and John Gaydon.  The pair signed on as managers of King Crimson in early 1969, during the formative stage of the band and prior to the release of debut \"In the Court of the Crimson King\".  They also signed T. Rex, Emerson, Lake & Palmer and Roxy Music to management.  Gaydon left in 1971 and Enthoven in 1977.  Sam Alder and Mark Fenwick (later managing Roger Waters) reformed the label several years later, re-releasing material from King Crimson in addition to others such as Penguin Cafe Orchestra, Brian Eno, Killing Joke, Loose Tubes, Human Chain, Man Jumping, Iain Ballamy, Elan Sicroff, Earthworks, and U.K.\n\nUrban Jungle (record label): Urban Jungle is an artist management company, booking agency and independent record label based in São Paulo, Brazil, inspired by the local Brazilian urban music scene, it has been releasing albums and representing artists like Céu, Curumin, Chico César and Lucas Santtana worldwide.\n\nRock Ridge Music: Rock Ridge Music is an independent record label and artist management company based in Nashville, TN.  Founded in 2004, it has signed, managed, and/or promoted artists including Reel Big Fish, Sister Hazel, Rachel Platten, Matthew Perryman Jones, Tony Lucca, Matt Hires, The Damnwells, Attack!  Attack! , The Ike Reilly Assassination, and Fiction Family.\n\nHer Royal Majesty's Records: Her Royal Majesty's Records (HRMR) is a Canadian independent record label founded in Vancouver in 1995 by Bif Naked and Peter Karroll and managed by Peter Karroll.  Originally HRM Records was created to be a home for Bif Naked's music after Plum Records folded up shop after the release of Bif Naked's self-titled release.  Peter Karroll licensed Bif's songs to many major labels and did co-venture music projects including mixing and recording tracks for Films and Television.  Peter Karroll co-wrote, produced and mixed many successful tracks including Platinum and Gold selling albums and singles with Bif Naked.  In 2005 Peter Karroll merged the music label with Bodog to create Bodog Music and Bodog Entertainment.  Her Royal Majesty's Records was the backbone of the Bodog entertainment juggernaut and combined with the Artist Management company TKO Entertainment Corp the Bodog Entertainment entity produced over 150 Network Television shows in the USA and licensed in many countries.  As well live events on In Demand and music television programing on the Fuse Network all contributed to the overall success of Bodog Entertainment.  In 2008 the entertainment companies were unmerged and Peter Karroll moved forward more albums with Bif Naked and DMX the American rap / hip hop superstar.  During the Bodog Era Peter signed and released the Legendary Hip Hop group the WuTang Clan.  Thousands of Live events were produced with the Artists from HRMR / Bodog with them touring extensively on major festivals and tours such as Warped Tour, Family Values, Rock Am Ring, Rock Am Park, Hultsfred Festival Bif Naked's largest attendance in the headline position was 2011 in Cloverdale BC where she performed in front of 110,000 estimated audience.\n\nJennifer Lopez: Jennifer Lynn Lopez (born July 24, 1969), also known by her nickname J.Lo, is an American singer, actress, dancer and fashion designer.  In 1991, Lopez appeared as a Fly Girl dancer on \"In Living Color\", where she remained a regular until she decided to pursue an acting career in 1993.  For her first leading role in the 1997 Selena biopic of the same name, Lopez received a Golden Globe nomination and became the first Latin actress to earn over US$1 million for a film.  She went on to star in the adventure horror \"Anaconda\" (1997) and crime comedy \"Out of Sight\" (1998), later establishing herself as the highest paid Latin actress in Hollywood.  Lopez ventured into the music industry in 1999 with her debut studio album \"On the 6\", preceded by the \"Billboard\" Hot 100 number-one single \"If You Had My Love\".\n\nHardline Entertainment: Hardline Entertainment is an American independent record label, created and owned by Ken Seaton.  The label started as a management company and developed into an independent record label/management company.  Hardline is based in Hermosa Beach, California, United States, and features bands in the alternative music scene, with genres including folk, metal, pop, punk, rap, reggae, rock and singer/songwriter.  As of recent the management side of Hardline has merged with Regime72.com\n\nCSP Music Group: CSP Music Group is an independent record label and artist management company based in Atlanta, GA.  Founded in 1999, it has signed, produced, engineered, managed, and/or promoted artists including Chris Brown, Amanda Cole, Jennifer Lopez, Damita Chandler, Christina Aguilera, Dawn Richard, Karlie Redd and others.\n\nQuestion: CSP Music Group is an independent record label and artist management company, which of their promoted artists, was born on July 24, 1969?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music company.\"\n    },\n    \"company_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Roles of the company, e.g., record label, artist management.\"\n    },\n    \"promoted_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the artist promoted by the company.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The birth date of the artist in YYYY-MM-DD format.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"company_roles\",\n    \"promoted_artist\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the music company."
      },
      "company_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Roles of the company, e.g., record label, artist management."
      },
      "promoted_artist": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the artist promoted by the company."
          },
          "birth_date": {
            "type": "string",
            "format": "date",
            "description": "The birth date of the artist in YYYY-MM-DD format."
          }
        },
        "required": [
          "name",
          "birth_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "company_name",
      "company_roles",
      "promoted_artist"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
