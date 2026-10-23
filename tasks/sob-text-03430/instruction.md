{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBret Michaels: Bret Michael Sychak (born March 15, 1963), professionally known as Bret Michaels, is an American singer-songwriter and musician.  He gained fame as the lead singer of the glam metal band Poison who have sold over 50 million records worldwide and 15 million records in the United States alone.  The band has also charted ten singles to the Top 40 of the \"Billboard\" Hot 100, including six Top 10 singles and a number-one single, \"Every Rose Has Its Thorn\".\n\nAss (album): Ass is the fourth studio album by British rock band Badfinger, and their last album released on Apple Records.  The opening track, \"Apple of My Eye\", refers to the band leaving the label to begin its new contract with Warner Bros.  Records.  The cover artwork, showing a donkey chasing a distant carrot, alludes to Badfinger's feelings that they had been misled by Apple over the years.  The cover was painted by Grammy Award-winning artist Peter Corriston, who would later create album covers for Led Zeppelin (\"Physical Graffiti\") and the Rolling Stones (\"Some Girls\", \"Tattoo You\").\n\nNajat Kaanache: Najat Kaanache is the host of AMC Networks' cooking series \"Cocina Marroqui\" which airs on Canal Cocina in Spain and El Gourmet throughout 20 countries in Latin America.  Kaanache was born and raised in San Sebastián of Spain's Basque Country.  She gained fame as a lead actress on Spanish daytime television series \"Goenkale\" and then traveled throughout the Middle East and South America working in philanthropy to empower women and street kids.  She later attended culinary school and gained fame as \"The Pilgrim Chef\" by blogging throughout her four years training with the world's top chefs: Ferran Adria, Rene Redzepi, Thomas Keller, Grant Achatz, Heston Blumenthal and Martín Berasategui.\n\nPeter Gabriel: Peter Brian Gabriel (born 13 February 1950) is an English singer-songwriter, record producer and humanitarian who rose to fame as the original lead singer and flautist of the progressive rock band Genesis.  After leaving Genesis in 1975, Gabriel launched a successful solo career with \"Solsbury Hill\" as his first single.  His 1986 album, \"So\", is his best-selling release and is certified triple platinum in the UK and five times platinum in the U.S.  The album's most successful single, \"Sledgehammer\", won a record nine MTV Awards at the 1987 MTV Video Music Awards.\n\nPeter Corriston: Peter Corriston is a Grammy-award winning graphic designer currently based in Greenwich Village, notable for designing the album artwork for several major rock bands and musicians. Corriston has worked internationally with such artists as Billy Idol, Badfinger, Chick Corea, Carole King, Debbie Harry, George Benson, The J. Geils Band, Jethro Tull, Led Zeppelin, Mick Jagger, New York Dolls, Pat Benatar, Procol Harum, Rod Stewart, The Rolling Stones and Tom Waits.  Nominated for five Grammy awards, Corriston's work is on permanent collection at the Library of Congress.  and the Museum of Modern Art in New York.\n\nMick Jagger: Sir Michael Philip Jagger, MBE (born 26 July 1943) is an English singer-songwriter, multi-instrumentalist, and composer, who gained fame as the lead singer and one of the founder members of the Rolling Stones (1962-present).  Jagger's career has spanned over five decades, and he has been described as \"one of the most popular and influential frontmen in the history of rock & roll\".  His distinctive voice and performance, along with Keith Richards' guitar style, have been the trademark of the Rolling Stones throughout the career of the band.  Jagger gained press notoriety for his admitted drug use and romantic involvements, and was often portrayed as a countercultural figure.\n\nJeff Lynne: Jeffrey Lynne (born 30 December 1947) is an English songwriter, composer, arranger, singer, multi-instrumentalist and record producer who gained fame in the 1970s as the lead singer and sole constant member of Electric Light Orchestra.  In 1988, under the pseudonyms Otis Wilbury and Clayton Wilbury, he co-founded the supergroup Traveling Wilburys with George Harrison, Bob Dylan, Roy Orbison and Tom Petty.\n\nDarius Rucker discography: American singer Darius Rucker gained fame as the lead singer of the American roots rock band Hootie & the Blowfish before emerging as a major country music singer in 2008.  As a solo artist, his discography comprises five studio albums, including four for Capitol Nashville.  His singles since 2008 have all been released to the country music format, where he has seven number-one singles: \"Don't Think I Don't Think About It\", \"It Won't Be Like This for Long\", \"Alright\", \"Come Back Song\", \"This\", \"Wagon Wheel\", and \"If I Told You\".\n\nJoe Elliott: Joseph Thomas Elliott Jr. (born 1 August 1959) is an English singer-songwriter and musician, best known as the lead singer of the English rock band Def Leppard.  He has also been the lead singer of the David Bowie tribute band the Cybernauts and the Mott the Hoople cover band Down 'n' Outz.  He is one of the two original members of Def Leppard and one of the three to perform on every Def Leppard album.\n\nAlex Shelley: Patrick Martin (born May 23, 1983), is an American professional wrestler, better known by the ring name Alex Shelley.  He is best known for working for Total Nonstop Action Wrestling as one half of The Motor City Machine Guns with Chris Sabin.  He first gained fame on the independent circuit working for Ring of Honor (ROH), as well as in Japan, for Pro Wrestling Zero1-Max.  He has also worked for New Japan Pro-Wrestling, where he is a former three-time IWGP Junior Heavyweight Tag Team Champion.  Aside from wrestling, he is the lead singer of a rock band called The High Crusade, which includes his friends and fellow wrestlers Chris Sabin and Petey Williams.\n\nQuestion: Peter Corriston has worked with an English singer-songwriter who gained fame as the lead singer of what band? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the English singer-songwriter Peter Corriston worked with.\"\n    },\n    \"artist_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the singer-songwriter.\"\n    },\n    \"artist_primary_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role of the artist in the band.\"\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band the artist gained fame as the lead singer of.\"\n    },\n    \"corriston_collaboration_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of work Peter Corriston did in collaboration with the artist or their band.\"\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"artist_nationality\",\n    \"artist_primary_role\",\n    \"band_name\",\n    \"corriston_collaboration_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the English singer-songwriter Peter Corriston worked with."
      },
      "artist_nationality": {
        "type": "string",
        "description": "The nationality of the singer-songwriter."
      },
      "artist_primary_role": {
        "type": "string",
        "description": "The primary role of the artist in the band."
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band the artist gained fame as the lead singer of."
      },
      "corriston_collaboration_type": {
        "type": "string",
        "description": "The type of work Peter Corriston did in collaboration with the artist or their band."
      }
    },
    "required": [
      "artist_name",
      "artist_nationality",
      "artist_primary_role",
      "band_name",
      "corriston_collaboration_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
