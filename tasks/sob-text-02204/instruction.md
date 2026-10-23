{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoe Maz: Joseph Michael Masurka (born September 29, 1981) better known as Joe Maz, is a Miami-based producer & DJ.  Joe Maz has produced official remixes for Adele\",\" Coldplay & Beyoncé, Kanye West, Katy Perry and Flo Rida.  In 2017, he was voted Remixer of the Year at Summer Sessions in Atlantic City, with the legendary Nile Rodgers presenting the award.\n\nNational Football League Coach of the Year Award: The National Football League Coach of the Year Award is presented annually by various news and sports organizations to the National Football League (NFL) head coach who has done the most outstanding job of working with the talent he has at his disposal.  Currently, the most widely recognized award is presented by the Associated Press (AP), although in the past several awards received press recognition.  First presented in 1957, the AP award did not include American Football League (AFL) teams. \" The Sporting News\" has given a pro football coach of the year award since 1947 and in 1949 gave its award to a non-NFL coach, Paul Brown of the All-America Football Conference's Cleveland Browns.  Other NFL Coach of the Year awards are presented by \"Pro Football Weekly\"/Pro Football Writers of America and the Maxwell Football Club.  The United Press International (UPI) NFL Coach of the Year award was first presented in 1955.  From 1960 to 1969, before the AFL–NFL merger, an award was also given to the most outstanding coach from the AFL.  When the leagues merged in 1970, separate awards were given to the best coaches from the American Football Conference (AFC) and National Football Conference (NFC).  The UPI discontinued the awards after 1996.\n\nAtlantic City Express Service: The Atlantic City Express Service (ACES) was an inter-city train service offered by the Borgata, Caesars Atlantic City, and Harrah's Entertainment, operating from February 2009 until September 2011.  It was operated by New Jersey Transit under contract, and funded by the Casino Reinvestment Development Authority.  The train provided summer seasonal service between New York City and Atlantic City three days a week, operating along the Northeast Corridor and Atlantic City Line.  The train was formally discontinued on March 9, 2012.\n\nHash Pipe: \"Hash Pipe\" is a song by American rock band Weezer.  Released in 2001, it was the first single off the band's long-awaited third album, \"Weezer\" (\"The Green Album\"), and the only one of the SS2K The Summer Sessions songs to make it onto the album, although \"Dope Nose\" and \"Slob\" were released on \"Maladroit\".\n\nSporting News Reliever of the Year Award: The \"Sporting News\" Reliever of the Year Award was an annual award presented to the best relief pitcher in each league in Major League Baseball (MLB).  It was established in by \"The Sporting News\" (TSN) as the Fireman of the Year Award.  At the time, no reliever had ever received a Cy Young Award vote.  The Fireman of the Year Award originally recognized the reliever with the most combined saves and wins in each league in MLB.  The magazine had started publishing the then-unofficial save statistic that same year.  Later, a save was worth two points compared to one for a save in determining the winner.  In the award was chosen based on consensus from TSN editors, and it was renamed to Reliever of the Year Award.  The award was last issued in 2010 before being discontinued.\n\nNile Rodgers: Nile Gregory Rodgers, Jr. (born September 19, 1952) is an American record producer, songwriter, musician, composer, arranger and guitarist.  He is the lead guitarist and co-founding member with Bernard Edwards of the band Chic, which has been active since 1976 and was one of the most successful groups of the disco era.  He is famed for his \"chucking\" rhythm guitar style.\n\nThunder over the Boardwalk: Thunder Over the Boardwalk (also known as the Atlantic City Airshow) is an annual airshow held over the Atlantic City boardwalk every summer.  Since 2003, it has set the bar for beachfront airshows across the United States and is currently one of the largest airshows in North America.  What sets it apart, aside from being a beach show, is the fact that it usually occurs on a Wednesday.  It takes place along the beaches of Atlantic City, New Jersey, in front of the world-famous boardwalk, with the casinos in the background.  Flybys and demonstrations as high as 15000 ft and as low as 50 ft over the water in front of the Atlantic City skyline.\n\nThe Atlantic Club Casino Hotel: The Atlantic Club Casino Hotel, formerly known as Golden Nugget, Bally's Grand, Atlantic City Hilton and ACH, is a closed casino and hotel located at the southern end of the boardwalk in Atlantic City, New Jersey, owned and operated by Colony Capital.  It was the city's first and only \"locals casino\".  The Atlantic Club permanently closed on January 13, 2014, at 12:01 AM.  largely as a result of dwindling casino visitors to Atlantic City due to increased competition in neighboring states.  A third of Atlantic City's boardwalk casinos closed the same year, the others being Revel, Trump Plaza, and Showboat.  Redevelopment proposals include a water park.\n\nTEN Atlantic City: TEN (formerly Revel Casino Hotel Atlantic City) is a closed resort, hotel and casino in Atlantic City, New Jersey, United States.  It is the northernmost casino on the Atlantic City Boardwalk, located on 20 acre of land, adjacent to the Showboat Hotel.  Revel opened on April 2, 2012, and after declaring Chapter 11 bankruptcy for the second time, closed on September 2, 2014.  Revel was the third of four Atlantic City casinos to close in 2014.  It was supposed to open in June 2017 but it didn’t.\n\nWAJM: WAJM, assigned to 88.9 FM and licensed to Atlantic City, New Jersey, is a high school radio station owned by the Atlantic City Board of Education and is operated by the students of Atlantic City High School.  Currently, WAJM broadcasts live Monday thru Friday from 7:00am to 3:30pm and during after hours, on weekends, holidays and when Atlantic City High School is closed due to inclement weather the station operates on an automated system where music, station IDs and PSA are shuffled and broadcast on-air.  Starting at its inception WAJM had been broadcasting with a jazz radio format until 2009 when it flipped to a freeform radio format using the moniker 88.9 The Jam.  The studios, offices and transmitter are located on the campus of Atlantic City High School on North Albany Avenue in Atlantic City.  In 2009 WAJM began simulcasting its live and automated broadcasts via the Internet in both an audio only feed and audio/video feed.  The station was a creation of Mr.Norman Draper.  The first school year of on air broadcasting was 1996-97.  That year the students interviewed \"Sugar\" Ray Leonard, and did a live simulcast from the grand opening of the new Atlantic City Convention Center.\n\nQuestion: Which band was co-founded by the musician who presented Joe Max with the Remixer of the Year award at Summer Sessions in Atlantic City in 2017?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"award_recipient_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who received the award.\"\n    },\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the award received.\"\n    },\n    \"award_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the award was presented.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the event where the award was presented.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the event took place.\"\n        }\n      },\n      \"required\": [\n        \"event_name\",\n        \"city\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"presenter_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"presenter_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who presented the award.\"\n        },\n        \"co_founded_band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band co-founded by the presenter.\"\n        }\n      },\n      \"required\": [\n        \"presenter_name\",\n        \"co_founded_band_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"award_recipient_name\",\n    \"award_name\",\n    \"award_year\",\n    \"event_details\",\n    \"presenter_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "award_recipient_name": {
        "type": "string",
        "description": "The name of the person who received the award."
      },
      "award_name": {
        "type": "string",
        "description": "The name of the award received."
      },
      "award_year": {
        "type": "integer",
        "description": "The year the award was presented."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_name": {
            "type": "string",
            "description": "The name of the event where the award was presented."
          },
          "city": {
            "type": "string",
            "description": "The city where the event took place."
          }
        },
        "required": [
          "event_name",
          "city"
        ],
        "additionalProperties": false
      },
      "presenter_details": {
        "type": "object",
        "properties": {
          "presenter_name": {
            "type": "string",
            "description": "The name of the person who presented the award."
          },
          "co_founded_band_name": {
            "type": "string",
            "description": "The name of the band co-founded by the presenter."
          }
        },
        "required": [
          "presenter_name",
          "co_founded_band_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "award_recipient_name",
      "award_name",
      "award_year",
      "event_details",
      "presenter_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
