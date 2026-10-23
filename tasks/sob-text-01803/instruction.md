{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGrambling State Tigers baseball: The Grambling State Tigers baseball team is a varsity intercollegiate athletic team of Grambling State University in Grambling, Louisiana, U.S.  The team is a member of the Southwestern Athletic Conference, which is part of the National Collegiate Athletic Association's Division I.  The team plays its home games at Ralph Waldo Emerson Jones Park and Wilbert Ellis Field in Grambling, Louisiana.  The Tigers are coached by James Cooper.\n\nGrambling State Tigers men's basketball: The Grambling State Tigers men's basketball team represents Grambling State University in Grambling, Louisiana.  The school's team currently competes in the Southwestern Athletic Conference.  They currently play their home games at the Fredrick C. Hobdy Assembly Center.\n\nMelvin Spears: Melvin Spears (born January 16, 1960) is the former head coach at Grambling State University and Alcorn State University.  Previously, he was the sixth head college football coach for the Grambling State Tigers located in Grambling, Louisiana and he held that position for three seasons, from 2004 until 2006.  His coaching record at Grambling was 20 wins, 14 losses, and 0 ties.  He then served as a coach at Texas Southern University, working with the wide receivers in 2008 then moving over to running backs.  He also served as the offensive coordinator of Alabama State University during the 2010 season.  Spears was selected on January 19, 2011 to the post of head coach of his alma mater of Alcorn State University.  Spears was fired by Alcorn State on February 24, 2012.  He had previously been placed on administrative leave.\n\nGrambling State University: Grambling State University (GSU) is a historically black, public, coeducational university, located in Grambling, Louisiana.  The university is home of the Eddie G. Robinson Museum, and is listed on the Louisiana African American Heritage Trail.  The university is a member-school of the University of Louisiana System and Thurgood Marshall College Fund.\n\nGrambling State Tigers: The Grambling State Tigers represent Grambling State University in NCAA intercollegiate athletics.  Grambling's sports teams participate in Division I (I-FCS for football) as a member of the Southwestern Athletic Conference (SWAC).  Currently, the Grambling State University Department of Athletics sponsors men's intercollegiate football, along with men's and women's basketball, baseball, track & field, softball, golf, soccer, tennis, bowling and volleyball.\n\n2016 Grambling State Tigers football team: The 2016 Grambling State Tigers football team represented Grambling State University in the 2016 NCAA Division I FCS football season.  The Tigers were led by third year head coach Broderick Fobbs.  They competed as members of the West Division of the Southwestern Athletic Conference (SWAC) and played their home games at Eddie Robinson Stadium in Grambling, Louisiana.  They finished the season 12–1, 9–0 in SWAC play to be champions of the West Division.  They represented the West Division in the SWAC Championship Game where they defeated Alcorn State.  The Tigers also defeated MEAC champion North Carolina Central in the Celebration Bowl, earning their fifteenth black college football national championship.\n\nGrambling State Tigers women's basketball: The Grambling State Tigers women's basketball team represents Grambling State University in Grambling, Louisiana.  The school's team currently competes in the Southwestern Athletic Conference.\n\n1994 Grambling State Tigers football team: The 1994 Grambling State Tigers football team represented Grambling State University as a member of the Southwestern Athletic Conference (SWAC) during the 1994 NCAA Division I-AA football season.  The Tigers were led by head coach Eddie Robinson in his 52nd year and finished the season with a record of nine wins and three losses (9–3, 6–1 SWAC).  The Tigers offense scored 479 points while the defense allowed only 262 points.  This was the final winning season during Eddie Robinson's tenure as head coach at Grambling.\n\nEddie Robinson Stadium: Eddie Robinson Stadium is a 19,600-seat multi-purpose stadium in Grambling, Louisiana.  It opened in 1983 and is home to the Grambling State Tigers football team and Grambling High School Kittens football team.  The stadium is named in honor of famous Grambling State University head football coach, Eddie Robinson.  It replaced Grambling Stadium.  The stadium is oftentimes affectionately referred to as \"The Hole\" due to the topography of the stadium area.\n\n2013 Grambling State Tigers football team: The 2013 Grambling State Tigers football team represented Grambling State University in the 2013 NCAA Division I FCS football season.  The Tigers were led by head coach Doug Williams in the third season of his second tenure as head coach and ninth overall after coaching the Tigers from 1998 to 2003.  They competed as a member of the West Division of the Southwestern Athletic Conference (SWAC) and played their home games at Eddie Robinson Stadium in Grambling, Louisiana.  The Tigers finished the season with a 1–11 record.\n\nQuestion: Where is the coeducational university which the Grambling State Tigers women's basketball team represents located in\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university.\"\n    },\n    \"university_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of university, e.g., coeducational, public.\"\n    },\n    \"represented_team\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the sports team represented by the university.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the university is located.\"\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"university_type\",\n    \"represented_team\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the university."
      },
      "university_type": {
        "type": "string",
        "description": "The type of university, e.g., coeducational, public."
      },
      "represented_team": {
        "type": "string",
        "description": "The name of the sports team represented by the university."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the university is located."
      }
    },
    "required": [
      "university_name",
      "university_type",
      "represented_team",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
