{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Chardon Polka Band: The Chardon Polka Band is an American, Ohio-based, Cleveland-Style polka band.  It was started by Jake Kouwe in 2003 when he recruited four other teenagers to form a polka band at Chardon High School, and the group was originally called \"The Chardon High School Polka Band\" and included an accordion, trumpet, saxophone, clarinet, electric guitar, and tuba.  The group got their start in the school's music room and played at local senior centers and nursing homes in the Chardon area.  Kouwe cites Weird Al Yankovic as his inspiration for playing the accordion as he started lessons on the accordion after seeing Yankovic in a VH1 special.  The popular satirist remains a role model for The Chardon Polka Band.  The band had slowly gained notoriety among Polka fans and in the Cleveland music scene in general, but got mainstream attention when they were featured in a reality show named \"Polka Kings\" on Reelz in 2015, even though the show was quickly cancelled.  The band currently plays over 200 shows a year and has grown to be one of the Cleveland music scene's most recognizable performers but also tours nationally and headlines many of the nation's top folk festival and Oktoberfest celebrations, playing a mixture of original music, classic polkas, and covers of pop songs.The band has released five full-length albums, all independently, three of which were nominated for a Polka Hall of Fame award for either the album or one or more songs.\n\nBayan (accordion): The bayan (Russian: бая́н ; ] ) is a type of chromatic button accordion developed in Russia in the early 20th century and named after the 11th-century bard Boyan.\n\nGünter Platzek: Günter Platzek (18 July 1930 in Hanover, Germany – 29 November 1990 in Hamburg, Germany) was a German keyboard player.  He became known for his longtime work with the James Last Orchestra, of which he was a member from 1965 up until his death.  He was also a member of the NDR (Norddeutscher Rundfunk, or North German Radio) big band, the Alfred Hause tango orchestra and the Bert Kaempfert orchestra.  An accomplished keyboard, accordion and xylophone player, he formed an accordion duet group called The Pop Kids with fellow Last bandmate Harald Ende.  His work with James Last featured his unique improvised piano phrases, which drew on jazz, blues and rock influences and were played with a distinctively dry staccato tone.  During the 1980s, his accordion duet with Jo Ment on the song \"Biscaya\" became a highlight of James Last's live concerts.  He died in Hamburg from a heart attack on 29 November 1990.\n\nSonny Brogan: Sonny (Patrick Joseph) Brogan (4 July 1906 – 1 January 1965) was an Irish accordion player from the 1930s to the 1960s, and was one of Ireland's most popular traditional musicians.  He was one of the earliest advocates of the two-row B/C button accordion in traditional music, and popularised it the 1950s and 60s.  He originally played on a single-keyed Hohner melodeon, and later the two-row Paolo Soprani (pictured) which he used until he died.  Sonny's Paolo Soprani was one of the rarest, the grey model, made in 1948, when the company still made them by hand.  Offaly-born button box player Paddy O'Brien currently has Sonny's accordion.\n\nVladislav Gavriliuc: Vladislav Gavriliuc (born 7 March 1972 in Ukraine) is a retired Moldovan football striker.  He played for FC Nistru Otaci between 1992 and 1994 and FC Zimbru Chişinău between 1994 and 2002.  Gavriliuc was the Moldovan National Division top scorer in successive years in the 1994-95 season scoring 20 goals and in the 1995-96 season scoring 34 goals.  Vladislav Gavriliuc was capped internationally by Moldova between 1995 and 1996 earning four caps.\n\nChromatic button accordion: A chromatic button accordion is a type of button accordion where the melody-side keyboard consists of rows of buttons arranged chromatically.  The bass-side keyboard is usually the Stradella system or one of the various free-bass systems. Included among chromatic button accordions are the Russian bayan and Schrammel accordion.  There can be 3 to 5 rows of vertical treble buttons.  In a 5 row chromatic, two additional rows repeat the first 2 rows to facilitate options in fingering.\n\nFinbarr Dwyer: Finbarr Dwyer (often misspelled as \"Finbar Dwyer\") (20 September 1946 – 8 February 2014) was a traditional Irish accordion player from the famed Dwyer musical family.  He was born in Castletownbere, Co.  Cork on 20 September 1946, began playing accordion at the age of three, and began composing at the age of nine.  Both of his parents played accordion and his father also played fiddle.  His brothers Richard and Michael (died 1996) likewise played accordion, while his brother John, born in 1933, played fiddle.  In 1969 he won the All-England accordion title.  He died on 8 February 2014, in Mallow, Co.  Cork, Ireland.\n\nSchrammel accordion: A Schrammel accordion (German: \"Schrammelharmonika\" ) is an accordion with a melody (right hand) keyboard in the chromatic B-Griff system and a twelve-button diatonic bass keyboard.  It is named for a traditional combination of two violins, accordion and contrabass known as a Schrammelquartet – a group that played Schrammelmusik in the Vienna chamber music tradition.\n\nStéphane Belmondo: The Belmondo family say music came naturally to Stephane, before he could even speak.  His father, Yvan, was proud of his son, but inflexible when it came down to his musical education.  As a former professional saxophonist, he understood the necessity of discipline and practicing music requires.  He was able to instill these values into his son from an early age and Belmondo quickly adopted these principles.  He first started with drums and percussion instruments at the age of 6, accordion at 8, then he chose to take up the trumpet at 10 years old.  Belmondo studied accordion and cornet at the Aix-en-Provence Conservatory of Music, before being admitted to the trumpet class of the Marseille Conservatory at 16.  Belmondo was 14 when he finally took the stage with his accordion joining the big band led by his father and brother Lionel who played saxophone.  When he and his brother started a quintet, Belmondo was 15 years old.\n\nVladislav Zolotaryov: Vladislav Andreyevich Zolotaryov (Russian: Владислав Андреевич Золотарёв , De-Kastri, September 13, 1942 - Moscow, May 13, 1975) was a Soviet composer and bayanist.  He is regarded as one of the greatest Soviet composers for bayan.\n\nQuestion: Which type of accordion was played by Vladislav Zolotaryov?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"instrument_played\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The specific name of the accordion type.\"\n        },\n        \"general_type\": {\n          \"type\": \"string\",\n          \"description\": \"The broader category of the accordion.\"\n        },\n        \"origin_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the instrument was developed.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"general_type\",\n        \"origin_country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_profession\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The professions of the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"instrument_played\",\n    \"person_profession\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "instrument_played": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The specific name of the accordion type."
          },
          "general_type": {
            "type": "string",
            "description": "The broader category of the accordion."
          },
          "origin_country": {
            "type": "string",
            "description": "The country where the instrument was developed."
          }
        },
        "required": [
          "name",
          "general_type",
          "origin_country"
        ],
        "additionalProperties": false
      },
      "person_profession": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The professions of the person."
      }
    },
    "required": [
      "person_name",
      "instrument_played",
      "person_profession"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
