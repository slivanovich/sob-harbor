{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVengeance (2005): Vengeance (2005) was a professional wrestling pay-per-view (PPV) event produced by World Wrestling Entertainment (WWE) and presented by THQ's \"Juiced\", which took place on June 26, 2005, at the Thomas & Mack Center in Las Vegas, Nevada.  It was the fifth annual Vengeance event.  Professional wrestling is a type of sports entertainment in which theatrical events are combined with a competitive sport.  The buildup to the matches and the scenarios that took place before, during, and after the event were planned by WWE's script writers.  The event starred wrestlers from the Raw brand: storyline expansions of the promotion where employees are assigned to wrestling brands under the WWE banner.\n\nWWE Judgment Day: Judgment Day was a professional wrestling pay-per-view event, produced every May by WWE, a professional wrestling promotion based in Connecticut.  The event was created in 1998, with its inaugural event produced as an In Your House event in October of that year.  The event was then replaced in 1999 by the PPV Over the Edge, which saw the death of Owen Hart.  The event was then brought back in 2000 and was rebranded as an annual PPV event for WWE.  To coincide with the brand extension, the event was made exclusive to the SmackDown!  brand in 2004.  In 2007, following WrestleMania 23, brand-exclusive pay-per-view events were discontinued.  The final event was held in 2009, with Over the Limit replacing Judgment Day in 2010.\n\nWhatever It Takes (Imagine Dragons song): \"Whatever It Takes\" is a song by American rock band Imagine Dragons.  The song was released on May 8, 2017 through KIDinaKORNER and Interscope.  It is a promotional single from the band's third studio album, \"Evolve\".  It also has been the official theme song for WWE's PPV event, Battleground in addition to its inclusion in the video game \"Madden NFL 18\".\n\nNew Blood Rising: New Blood Rising was a professional wrestling pay-per-view (PPV) event produced by World Championship Wrestling (WCW) that replaced WCW's August PPV event Road Wild held from 1997 to 1999 on a Saturday.  It took place on August 13, 2000 from the Pacific Coliseum in Vancouver, British Columbia.  The name is a reference to the New Blood faction within WCW (which dissolved before the pay-per-view).  This WCW PPV event was held on a Sunday instead of a Saturday.  Despite never being announced before or during the show, every match on the card was contested under no disqualification rules.\n\nHappy? (Mudvayne song): \"Happy?\"  is a single from Mudvayne's third album, \"Lost and Found\".  It was released in 2005 and is a highly played song on the radio.  The song was the theme song of \"WWE Vengeance 2005\" and has been played as a commercial bumper track for \"The Jim Rome Show\".  \"Happy?\"  was named both the No. 1 Headbangers Ball Video of 2005 and \"Billboard\" Monitor's Active Rock Song of the Year.  The song held the No. 1 spot on the \"Billboard\" Hot Mainstream Rock Tracks chart for one week, and reached No. 8 on the Hot Modern Rock Tracks chart.\n\nTNA Turning Point: Turning Point is a professional wrestling pay-per-view (PPV) event, produced by the American professional wrestling promotion Total Nonstop Action Wrestling (TNA).  The event was created in 2004 and was originally held annually in December.  TNA changed the date of the 2008 event to be held in November.  The event has been held as an annual PPV event for TNA.  The 2004 event was the second TNA PPV to be produced annually.  Since its inception in 2004, the event has been held exclusively in Orlando, Florida.  Every event has been held in an indoor arena, with all of the events taking place in the Impact Zone.  Each event features talent from TNA competing in various professional wrestling match types.  Since the inaugural event, five championship matches have taken place in the main event.\n\nWCW Sin: Sin was a professional wrestling pay-per-view (PPV) event produced by World Championship Wrestling (WCW) that replaced WCW's January PPV event, Souled Out which was held from 1997 to 2000.  Sin was the antepenultimate WCW PPV before the company was absorbed by the World Wrestling Federation (now World Wrestling Entertainment) in March 2001.  It took place on January 14, 2001 from the Conseco Fieldhouse in Indianapolis, Indiana.\n\nBeach Blast: Beach Blast was a professional wrestling pay-per-view (PPV) event promoted by World Championship Wrestling (WCW) and held in the summers of 1992 and 1993.  The 1992 WCW Beach Blast PPV event was held in June on a Saturday while the 1993 WCW Beach Blast PPV event was held in July on a Sunday.  It was replaced by Bash at the Beach in 1994.  WCW closed in 2001 and all rights to their television and PPV shows was bought by WWE, including the Beach Blast shows.  With the launch of the WWE Network in 2014 the 1992 and 1993 Beach Blast shows became available on demand for network subscribers.\n\nFeedback (Rush album): Feedback is a cover album by Canadian rock band Rush, released in 2004.  The album features eight covers of songs that were influential for the band members during the 1960s.  The album marked the 30th anniversary of the release of Rush's debut album though the current lineup of Geddy Lee, Alex Lifeson and Neil Peart established just following the first album's release.  The tour in support of the \"Feedback\" album was called the .  Their cover of \"Summertime Blues\" was also used as an official theme song for WWE's Summerslam PPV event in 2004.  The album has been remastered and reissued in 2013 as a part of the box set \"The Studio Albums 1989–2007\".\n\nTriplemanía XXII: Triplemanía XXII was a professional wrestling pay-per-view (PPV) produced by the AAA promotion.  It took place on August 17, 2014, at \"Arena Ciudad de México\" in Mexico City, Mexico.  The event was the twenty-second annual \"Triplemanía\", which is AAA's biggest show of the year, airing in Mexico as a regular PPV and internationally as an internet pay-per-view (iPPV).  This was the first AAA PPV event to be broadcast simultaneously in English through SAP, having Hugo Savinovich and Vampiro as announcers.\n\nQuestion: Mudvayne's single \"Happy?\" was the theme song of a PPV event that was held in what city?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"artist\": {\n      \"type\": \"string\",\n      \"description\": \"The artist who performed the song.\"\n    },\n    \"ppv_event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the pay-per-view event.\"\n    },\n    \"event_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the pay-per-view event took place.\"\n    },\n    \"event_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the pay-per-view event was held.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"artist\",\n    \"ppv_event_name\",\n    \"event_year\",\n    \"event_city\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "artist": {
        "type": "string",
        "description": "The artist who performed the song."
      },
      "ppv_event_name": {
        "type": "string",
        "description": "The name of the pay-per-view event."
      },
      "event_year": {
        "type": "integer",
        "description": "The year the pay-per-view event took place."
      },
      "event_city": {
        "type": "string",
        "description": "The city where the pay-per-view event was held."
      }
    },
    "required": [
      "song_title",
      "artist",
      "ppv_event_name",
      "event_year",
      "event_city"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
