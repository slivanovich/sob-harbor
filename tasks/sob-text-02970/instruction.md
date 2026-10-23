{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJune Jones: June Sheldon Jones III (born February 19, 1953) is an American football coach and former player, currently serving as a head coach of the Hamilton Tiger-Cats of the Canadian Football League (CFL).  He was the head football coach at Southern Methodist University (SMU), where he served as head coach from 2008 to 2014, before resigning on September 8, 2014.  Jones was also the head football coach at the University of Hawaii at Manoa from 1999 to 2007.  Previously, he coached in the National Football League (NFL): a three-year tenure as head coach of the Atlanta Falcons from 1994 to 1996 and a ten-game stint as interim head coach of the San Diego Chargers in 1998.\n\nK. C. Keeler: Kurt Charles \"K. C.\" Keeler (born July 26, 1959) is an American football coach and former player.  He is currently the head football coach at Sam Houston State University.  He was the head football coach at the University of Delaware from 2002 to 2012.  Keeler served as the head football coach at Rowan University from 1993 to 2001.  His 2003 Delaware Fightin' Blue Hens squad won the NCAA Division I-AA Football Championship, and returned to the Division I Championship game in 2007 and 2010.\n\nWillie Fritz: Willie Fritz (born April 2, 1960) is an American football coach and former player.  He is the current head coach at Tulane University.  From 2014 to 2015, he was head coach at Georgia Southern University.  From 2010 to 2013, he was the head football coach at Sam Houston State University.  From 1997 to 2009, Fritz served as the head football coach at the University of Central Missouri.  From 1993 to 1996, he was the head football coach at Blinn College, a junior college in Brenham, Texas.\n\nTed Karras Jr.: Theodore George \"Ted\" Karras Jr. (born December 10, 1964) is an American football coach and former player.  He was most recently head football coach at Walsh University, a position he held from December 2012 to November 2016.  Previously, Karras served as the first head football coach at Marian University in Indianapolis, Indiana.  He held that position from the program's inception in 2007 through the 2012 season in which Marian won the NAIA Football National Championship.  Karras played college football as a defensive tackle at Northwestern University from 1983 to 1986 and for one year (1987) in the National Football League (NFL) with the Washington Redskins.  From 2003 to 2005, he served as the head football coach at Rose-Hulman Institute of Technology.  His father, Ted Karras Sr., played for the Chicago Bears in the 1960s.  His uncles also played in the NFL: Alex Karras for the Detroit Lions and Lou Karras for the Washington Redskins.\n\nTom Keele: Tom Keele (born c. 1933) is a former American football coach.  He served as the head football coach at California State University, Northridge from 1979 to 1985, compiling a record of 31–42–1.  Keele graduated from Jefferson High School in Portland Oregon in 1951.  He attended the University of Oregon, where he played football for the Oregon Webfoots as a tackle from 1957 to 1959.  Keele began his coaching career in 1960 at North Eugene High School in Eugene, Oregon, working two years as an assistant football coach and sophomore basketball coach.  He moved to Oregon City High School in Oregon City, Oregon in 1962, serving as head football coach and leading his team to a 9–1–1 record.  The following year, he was hired as head football coach at the newly-formed Sheldon High School in Eugene.\n\n2013 North Carolina Central Eagles football team: The 2013 North Carolina Central Eagles football team represented North Carolina Central University in the 2013 NCAA Division I FCS football season.  They were led by interim head coach Dwayne Foster after former coach Henry Frazier, III was fired following a domestic dispute on August 22, 2013.  The Eagles played their home games at O'Kelly–Riddick Stadium.  They were a member of the Mid-Eastern Athletic Conference.  They finished the season 5–7, 3–5 in MEAC play to finish in a tie for eighth place.\n\nHenry Frazier III: Henry Frazier III (born March 20, 1968) is an American football coach and former player.  Most recently, Frazier was the head football coach at North Carolina Central University, a position he assumed in December 2010 and held until August 2013.  Frazier has served as the head football coach at Bowie State University (1999–2003) and Prairie View A&M University (2004–2010).\n\nErnest T. Jones: Ernest T. Jones (born January 18, 1970) is the current head coach at ASA Miami, a two-year college starting its first football season in 2015.  He was briefly running backs coach for the University of Connecticut Huskies football team.  He was head football coach at Alcorn State University.  He was named the head football coach after the 2007 season and served as head coach in 2008.  He was controversially fired from this position in December 2008.  He returned to the University of Cincinnati as the Director of Player Services in 2009.  For the 2010 he will be an assistant coach at the University at Buffalo under former University of Cincinnati assistant coach and now UB head football Coach Jeff Quinn.\n\nBowie State University: Bowie State University (\"Bowie State\") is a public university located on 355½ acres (1.4 km²) in unincorporated Prince George's County, Maryland, United States, north of the suburban city of Bowie.  Bowie State is part of the University System of Maryland.  Bowie State is Maryland's oldest historically black university and one of the ten oldest in the country.  Bowie State is a member-school of the Thurgood Marshall College Fund.\n\nTim McCarty: Tim McCarty is an American football coach and former player.  He is currently the head football coach at East Central University in Ada, Oklahoma, a position he first held from 2004 to 2005 and then resume in 2009.  From 1999 to 2003 McCarty was the head football coach at Tabor College in Hillsboro, Kansas.  His two tenures at East Central were sepeated by a three-year stint at the assistant head football coach at Kansas State University.\n\nQuestion: Henry Frazier III served as the head football coach from 1999-2003 at a university located in what state?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"coach_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football coach.\"\n    },\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university where the coach served.\"\n    },\n    \"coaching_tenure\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the coaching tenure.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the coaching tenure.\"\n        }\n      },\n      \"required\": [\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"university_location_state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the university is located.\"\n    }\n  },\n  \"required\": [\n    \"coach_name\",\n    \"university_name\",\n    \"coaching_tenure\",\n    \"university_location_state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "coach_name": {
        "type": "string",
        "description": "The name of the football coach."
      },
      "university_name": {
        "type": "string",
        "description": "The name of the university where the coach served."
      },
      "coaching_tenure": {
        "type": "object",
        "properties": {
          "start_year": {
            "type": "integer",
            "description": "The start year of the coaching tenure."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the coaching tenure."
          }
        },
        "required": [
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "university_location_state": {
        "type": "string",
        "description": "The state where the university is located."
      }
    },
    "required": [
      "coach_name",
      "university_name",
      "coaching_tenure",
      "university_location_state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
