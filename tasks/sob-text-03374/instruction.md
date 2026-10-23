{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNinja Warrior UK (series 2): The second series of Ninja Warrior UK which ITV renewed for a second series on 29 May 2015, and began on 2 January 2016.  The show was presented by Ben Shephard, Chris Kamara and Rochelle Humes.  Owen \"The Stuff\" McKenzie was the contestant to go the furthest in the second series.  As with series 1, no women advanced past the semi-finals.\n\nRochelle Humes: Rochelle Eulah Eileen Humes (née Wiseman; born 21 March 1989) is an English singer and television presenter, best known for her work in pop groups S Club 8 and The Saturdays.  Humes has achieved six Top 10 hits with S Club 8 and thirteen Top 10 hits with girl group The Saturdays, including number-one hit \"What About Us\".\n\nMakoto Nagano: Makoto Nagano (長野 誠 , Nagano Makoto , born March 30, 1972 in Kitakata, Miyazaki) (sometimes known as the World's Strongest Fisherman) is a commercial fisherman and the captain of his vessel, F/V \"Konpira Maru 50\" (第50金比羅丸 ) (He used to be captain of the F/V \"Konpira Maru 28\" (第28金比羅丸 ) ) and musician.  He is regularly seen on the Japanese television show \"Sasuke\" (\"Ninja Warrior\") where he was one of the \"SASUKE All-Stars,\" a group of favored competitors who were thought to possess the greatest potential in completing the four grueling obstacle courses of Ninja Warrior.  He can also be seen on the lesser known precursor to Ninja Warrior, Viking: The Ultimate obstacle course, where he was the only competitor to make it to the final round.\n\nNinja Warrior UK (series 1): The first series of Ninja Warrior UK premiered on 11 April 2015.  The show was presented by Ben Shephard, Chris Kamara and Rochelle Humes.  The top contestant in the first series was Timothy Shieff.  Although many women competed in the competition, no women advanced past the semi-finals.\n\nNinja Warrior UK: Ninja Warrior UK is the British version of the Japanese assault course game show \"Sasuke\".  The show, which began airing on 11 April 2015, is hosted by Ben Shephard, Chris Kamara and Rochelle Humes.\n\nAmerican Ninja Challenge: American Ninja Challenge was a nationwide competition sponsored by G4 TV to send a number of American citizens to Japan to compete in the TBS hit TV show \"Sasuke\" (known as \"Ninja Warrior\" in US).  American Ninja Challenge has been held since \"Sasuke\" 19 (the 19th competition) and currently merged into the TV series \"American Ninja Warrior\" that premiered on December 12, 2009 and succeeded American Ninja Challenge.\n\nEvan Dollard: Evan \"The Rocket\" Dollard is a U.S. athlete and rock climber.  He came to prominence during Season 1 of the rebooted American Gladiators, as the season 1 men's champion.  He earned his nickname \"Rocket\" from his speed in Gladiator competition, taking it as his gladiator name, becoming a Gladiator for season 2 of the rebooted American Gladiators.  He has since appeared prominently in the Ninja Warrior franchise; in American Ninja Warrior (and hence US TV specials for Sasuke called \"Ninja Warrior\") and the standalone American Ninja Warrior, also using his nickname.  Dollard also hosts his own web series, \"Ninja Quickies\".  He has also competed in local editions of Ninja Warrior.\n\nBen Shephard: Benjamin Peter Sherrington \"Ben\" Shephard (born 11 December 1974) is an English television presenter and journalist who is currently employed by ITV and Sky Sports (albeit for Goals on Sunday only).  His most recognised role was as a main presenter on the now defunct breakfast programme \"GMTV\".  He has hosted game shows such as \"The Krypton Factor\" (2009–2010), \"Tipping Point\" (2012–present) and \"Ninja Warrior UK\" (2015–present).\n\nAmerican Ninja Warrior (season 2): The second season of \"American Ninja Warrior\" began on December 8, 2010, in Venice Beach, California where 300 competitors took on the course.  The 16 semi-finalists moved on to the \"\"Ninja Warrior Boot Camp\"\" in the remote California mountains, where they competed in a series of team challenges.  Then, the final moved on to compete in the season finale of \"American Ninja Warrior 2\" as a part of \"Sasuke 26\" at Mount Midoriyama in Japan.  The series concluded on January 2, 2011.\n\nAmerican Ninja Warrior (season 4): The fourth season of \"American Ninja Warrior\" began on May 20, 2012, and aired on NBC and G4.  This was a landmark season for \"Ninja Warrior\", as the entire format was overhauled.  For the first time, the finals took place on U.S. soil.  In addition, regional qualifiers were added, taking place in Dallas, TX, Miami, FL, and the series' flagship location, Venice Beach, CA.  New co-host Jonny Moseley replaced Jimmy Smith, while Angela Sun replaced Alison Haislip.  Again, the winner would have received $500,000 and the coveted \"American Ninja Warrior\" title.  Brent Steffensen became the first contestant to complete the ultimate cliffhanger.\n\nQuestion: What pop groups was the female presenter of the Ninja Warrior UK a part of?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"presenter_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the female presenter of Ninja Warrior UK.\"\n    },\n    \"pop_groups\": {\n      \"type\": \"array\",\n      \"description\": \"A list of pop groups the presenter was a part of.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"number_of_groups\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of pop groups listed.\"\n    }\n  },\n  \"required\": [\n    \"presenter_name\",\n    \"pop_groups\",\n    \"number_of_groups\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "presenter_name": {
        "type": "string",
        "description": "The name of the female presenter of Ninja Warrior UK."
      },
      "pop_groups": {
        "type": "array",
        "description": "A list of pop groups the presenter was a part of.",
        "items": {
          "type": "string"
        }
      },
      "number_of_groups": {
        "type": "integer",
        "description": "The total number of pop groups listed."
      }
    },
    "required": [
      "presenter_name",
      "pop_groups",
      "number_of_groups"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
