{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGene Iba: Clarence Eugene \"Gene\" Iba (born November 5, 1940) is a former American college basketball coach.  He was previously the Pittsburg State Gorillas men's basketball coach until 2010.  He was head coach at Houston Baptist from 1977 to 1985, Baylor from 1985 to 1992, and Pittsburg State from 1995 to 2010.  He is the son of college basketball coach Clarence Iba and nephew of college basketball coach Hank Iba.\n\nNorm Sloan: Norman Lesley Sloan, Jr. (June 25, 1926 – December 9, 2003), nicknamed \"Stormin' Norman,\" was an American college basketball player and coach.  Sloan was a native of Indiana and played college basketball and football at North Carolina State University.  He began a long career as a basketball coach months after graduating from college in 1951, and he was the men's basketball head coach at Presbyterian College, The Citadel, North Carolina State University, and two stints as at the University of Florida.  Over a career that spanned thirty-eight seasons, Sloan was named conference coach of the year five times and won the 1974 national championship at North Carolina State, his alma mater.\n\nTad Boyle: Thomas Martin \"Tad\" Boyle (born January 6, 1963) is an American college basketball coach and the current head men's basketball coach at the University of Colorado.  He was named the 18th coach in University of Colorado men's basketball history on April 19, 2010 replacing Jeff Bzdelik.  Boyle was named as an assistant coach for USA Basketball a second time in 2015 He played collegiately at Kansas under coach Ted Owens and Hall of Fame coach Larry Brown.\n\nKen Anderson (basketball): Ken Anderson (born January 16, 1933) is a retired American college basketball coach, who spent 27 seasons at the University of Wisconsin-Eau Claire.  His winning percentage of .806 ranks second in college basketball history, behind only Adolph Rupp and one spot ahead of John Wooden.\n\nLeon Rice (basketball): Leon Paul Rice (born November 25, 1963) is an American college basketball coach, and the head men's basketball coach at Boise State University.  Rice replaced Greg Graham as head coach of the Broncos on March 26, 2010.  In his first season as head coach, he led Boise State to the finals of the 2011 WAC Men's Basketball Tournament and to the semifinals of the 2011 College Basketball Invitational.  He is the first Boise State head coach to win 20 games in two of his first three seasons and has 20 or more wins in six of his first seven seasons.  In 2013, he guided the Broncos to their first ever at-large bid to the NCAA Tournament.  In 2015, he led the Broncos to their first ever Mountain West regular season championship, and first conference title for Boise State since 2008, and was named the Mountain West coach of the year.\n\nDick Davey: Richard James \"Dick\" Davey (born April 5, 1942) is a retired American college basketball coach.  Davey is best known for being head men's basketball coach at Santa Clara University from 1992 to 2007.  Most recently, Davey was the associate head men's basketball coach at Stanford University under head coach Johnny Dawkins from 2008 to 2012 and helped Stanford win the 2012 National Invitation Tournament.\n\nMizzou Arena: Mizzou Arena is an indoor arena located on the south side of the campus of the University of Missouri in Columbia, Missouri.  The facility, home to the school's men's and women's basketball teams, opened in November 2004 and replaced the Hearnes Center as the school's flagship indoor sports facility.  The arena also serves as the Columbia-Springfield market's venue for well-known 'arena' acts such as Rascal Flatts, Luke Bryan and the Eagles.  The arched-roof building seats 15,061, and is located just south of Hearnes and Memorial Stadium.  The arena is host to Missouri State High School Activities Association championships for basketball and wrestling.  The arena was briefly known as Paige Sports Arena.\n\nEddie Sutton: Edward Eugene Sutton (born March 12, 1936) is a retired American college basketball coach.  He was a head coach for 36 years at the Division I level, at Creighton, Arkansas, Kentucky, Oklahoma State (his alma mater), and the University of San Francisco.  Sutton became the first coach to take four schools to the NCAA tournament, and he reached the Final Four with Arkansas in 1978 and Oklahoma State in 1995 and 2004.  He is one of only eight major college men's basketball coaches to have over 800 career wins.\n\nNorm Stewart: Norman Eugene \"Norm\" Stewart (born January 20, 1935) is a retired American college basketball coach.  He coached at the University of Northern Iowa (then known as State College of Iowa) from 1961 to 1967, but is best known for his career with the University of Missouri from 1967 until 1999.  He retired with an overall coaching record of 731-375 in 38 seasons.  The court at Mizzou Arena (and previously at the Hearnes Center) is named in his honor.\n\nErnie Kent: Ernest Kent (born January 22, 1955) is an American college basketball coach.  He is the head men's basketball coach at Washington State University.  He is the former head men's basketball coach at the University of Oregon and at Saint Mary's College of California.  Kent was previously an assistant at Stanford University and also coached abroad in Saudi Arabia.  Kent was a college basketball commentator with the Pac-12 Network.\n\nQuestion: Where is the basketball court named after Norman Eugene \"Norm\" Stewart (born January 20, 1935) is a retired American college basketball coach located\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"honored_coach_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the coach after whom the court is named.\"\n    },\n    \"arena_where_court_is_located\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the arena where the basketball court is located.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"university\": {\n          \"type\": \"string\",\n          \"description\": \"The university associated with the location of the arena.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the arena is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the arena is located.\"\n        },\n        \"full_location_string\": {\n          \"type\": \"string\",\n          \"description\": \"A concise string describing the university and city location.\"\n        }\n      },\n      \"required\": [\n        \"university\",\n        \"city\",\n        \"state\",\n        \"full_location_string\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"honored_coach_name\",\n    \"arena_where_court_is_located\",\n    \"location_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "honored_coach_name": {
        "type": "string",
        "description": "The full name of the coach after whom the court is named."
      },
      "arena_where_court_is_located": {
        "type": "string",
        "description": "The name of the arena where the basketball court is located."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "university": {
            "type": "string",
            "description": "The university associated with the location of the arena."
          },
          "city": {
            "type": "string",
            "description": "The city where the arena is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the arena is located."
          },
          "full_location_string": {
            "type": "string",
            "description": "A concise string describing the university and city location."
          }
        },
        "required": [
          "university",
          "city",
          "state",
          "full_location_string"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "honored_coach_name",
      "arena_where_court_is_located",
      "location_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
