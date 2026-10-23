{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBrendon Urie: Brendon Boyd Urie (born April 12, 1987) is an American singer, songwriter, musician and multi-instrumentalist.  He is best known as the lead vocalist of Panic!  at the Disco, of which he is the sole remaining original member.\n\nCrazy=Genius: \"Crazy=Genius\" is a song by American rock band Panic!  at the Disco and is the sixth track on the band's fifth studio album, \"Death of a Bachelor\" (2016).  It was written by Brendon Urie, Sam Hollander, and Jake Sinclair and was produced by Sinclair.  The song makes references to musicians Dennis Wilson, Brian Wilson, and Mike Love from The Beach Boys.\n\nLA Devotee: \"LA Devotee\" is a song by American rock band Panic!  at the Disco.  It was released as the second promotional single from the band's fifth studio album, \"Death of a Bachelor\", on November 26, 2015 through Fueled by Ramen and DCD2.  The song was written by Brendon Urie, White Sea and Jake Sinclair and was produced by Sinclair.\n\nProfessional Rapper (Lil Dicky album): Professional Rapper is the debut studio album by American rapper Lil Dicky.  It was released on July 31, 2015, by Commission Records, distributed by ADA.  The album features guest appearances from American rappers Snoop Dogg, Rich Homie Quan, Fetty Wap and Jace, and musicians Brendon Urie and T-Pain, alongside narrations from American comedian Hannibal Buress, and Lil Dicky's parents.\n\nNew Perspective (song): \"New Perspective\" is a song by American rock band Panic!  at the Disco, released on July 28, 2009 as a single promoting the film \"Jennifer's Body\".  Vocalist Brendon Urie began writing the song two years prior to its recording regarding a lucid dream he had.  The song was completed in the summer of 2009, and was co-written by producer John Feldmann.  \"New Perspective\" was Panic!  at the Disco's first single in aftermath of the departure of guitarist Ryan Ross and bassist Jon Walker, both of whom had no involvement in the track.\n\nVictorious (Panic! at the Disco song): \"Victorious\" is a song by American rock band Panic!  at the Disco released as the second single from the band's fifth studio album, \"Death of a Bachelor\", on September 29, 2015 by Fueled by Ramen and DCD2.  The song was written by Brendon Urie, Christopher J Baran, Mike Viola, White Sea, Jake Sinclair, Alex DeLeon, and Rivers Cuomo and was produced by Urie and Sinclair.  A music video for the song was released on YouTube on November 13, 2015.\n\nPanic! at the Disco: Panic!  at the Disco is an American rock band from Las Vegas, Nevada, formed in 2004 and featuring the current lineup of vocalist Brendon Urie, accompanied on tour by bassist Dallon Weekes, guitarist Kenneth Harris and drummer Dan Pawlovich.  Founded by childhood friends Ryan Ross, Spencer Smith, Brent Wilson and Urie, Panic!  at the Disco recorded its first demos while its members were in high school.  Shortly after, the band recorded and released its debut studio album, \"A Fever You Can't Sweat Out\" (2005).  Popularized by the second single, \"I Write Sins Not Tragedies\", the album was certified double platinum in the US.  In 2006, founding bassist Brent Wilson was fired from the band during an extensive world tour and subsequently replaced by Jon Walker.\n\nMoney Sucks, Friends Rule: Money Sucks, Friends Rule is the debut studio album by Dillon Francis, an American electronic music producer known for being one of the pioneers of moombahton and moombahcore.  The album features collaborations from artists such as Major Lazer, Martin Garrix, Mad Decent label-mate DJ Snake, rapper Twista, Panic!  at the Disco's Brendon Urie and more.  It was released on October 27, 2014 on Mad Decent in collaboration with Columbia Records.\n\nDeath of a Bachelor: Death of a Bachelor is the fifth studio album by American rock band Panic!  at the Disco, released January 15, 2016 on Fueled by Ramen and DCD2.  It is the follow-up to the band's fourth studio album, \"Too Weird to Live, Too Rare to Die! \" (2013), with the entire album written and recorded by lead vocalist/multi-instrumentalist Brendon Urie, among external writers.  It is the band's first album to not feature drummer Spencer Smith and also follows bassist Dallon Weekes' departure from the official line-up, subsequently becoming a touring member once again.\n\nJack Evans (musician): Jack Evans (born March 3, 1953, Anamosa, Iowa) is an American musician and songwriter.\n\nQuestion: Are Brendon Urie and Jack Evans both songwriters?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"are_both_songwriters\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether both individuals are songwriters.\"\n    },\n    \"individuals_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"is_songwriter\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is identified as a songwriter in the context, false otherwise.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_songwriter\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for the answer based on the provided context.\"\n    }\n  },\n  \"required\": [\n    \"are_both_songwriters\",\n    \"individuals_involved\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "are_both_songwriters": {
        "type": "boolean",
        "description": "Indicates whether both individuals are songwriters."
      },
      "individuals_involved": {
        "type": "array",
        "description": "Details about each individual mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "is_songwriter": {
              "type": "boolean",
              "description": "True if the individual is identified as a songwriter in the context, false otherwise."
            }
          },
          "required": [
            "name",
            "is_songwriter"
          ],
          "additionalProperties": false
        }
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for the answer based on the provided context."
      }
    },
    "required": [
      "are_both_songwriters",
      "individuals_involved",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
