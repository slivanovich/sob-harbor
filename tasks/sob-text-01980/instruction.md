Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Tim Buchanan: Timothy Buchanan (born May 26, 1946) is a former American football linebacker.  He attended college at the University of Hawaiʻi at Mānoa and played for the Cincinnati Bengals for one season, where he was a backup for Bill Bergey.

Bill Kennedy (basketball): William R. "Bill" Kennedy (May 17, 1938 – August 31, 2006), born in Philadelphia, Pennsylvania, was an American professional basketball player.  He was a 5'11" (180 cm) 180 lb (82 kg) guard and played collegiately at Temple University.  He played briefly in the National Basketball Association (NBA).

Arkansas State University: Arkansas State University (also known as "A-State"")" is a public research university and is the flagship campus of the Arkansas State University System, the state's second largest college system and second largest university by enrollment.  It is located atop 1,376 acres (5.6 km2) on Crowley's Ridge at Jonesboro, Arkansas, United States.  The university marked its centennial year in 2009.  Arkansas State has Sun Belt rivalries with all West Division schools (Little Rock, Louisiana-Lafayette, Louisiana-Monroe, Texas State, and UT Arlington).  Their primary Sun Belt rivals are Little Rock and Louisiana-Monroe.

Adam Harrington (basketball): Adam Philip Harrington (born July 5, 1980) is an American former professional basketball player and coach who is currently an assistant coach and the director of player development for the Brooklyn Nets of the National Basketball Association (NBA).  Adam formerly played basketball both collegiately and professionally.  He played collegiately at Auburn University and North Carolina State University and has played professionally in the United States, various European countries and China.

Bill Buntin: William L. "Bill" Buntin (May 5, 1942 – May 9, 1968) was an American basketball player.  He played collegiately for the University of Michigan and in the National Basketball Association (NBA).

Jake Bergey: Jake Bergey (born May 4, 1974 in Covington, Kentucky) is a retired lacrosse player.  Bergey played ten seasons for the Philadelphia Wings in the National Lacrosse League.  Bergey is the son of former NFL star Bill Bergey, and brother of fellow lacrosse player Josh Bergey.

Bill Bergey: William Earl Bergey (born February 9, 1945) is a former American collegiate and Professional Football player.  He played collegiately for Arkansas State University and for the American Football League's Cincinnati Bengals and the National Football League's Philadelphia Eagles.

Kailee Wong: Kailee Wong (born May 23, 1976) is a former linebacker in the National Football League.  He currently is the owner of The Athletic Room in Houston, Texas.  Wong was recruited by Bill Walsh, and subsequently played collegiately as an All-American at Stanford University.  He attended North Eugene High School.  Walsh recruited Wong with the stipulation that he would not have to play offense, despite being a record-setting fullback at the high school level.

List of Philadelphia Eagles broadcasters: The Eagles games were first broadcast in 1939 on WCAU (as in Where Cheer Awaits U] and have been continuously broadcast since.  Beginning with the 2008 season, Eagles games were broadcast on both WYSP (now WIP-FM) and Sports Radio 610 WIP, as both stations are owned and operated by CBS Radio.  Merrill Reese, who joined the Eagles in the mid-1970s, is the play-by-play announcer, and former Eagles wide receiver Mike Quick is the color analyst.  Former Eagles linebacker Bill Bergey is among several Eagles post-game commentators on the FM.

Bill Martin (basketball): William "Bill" Martin (born August 16, 1962) is a retired American professional basketball player.  He was a 6'7" (201 cm) 205 lb (93 kg) forward and played collegiately at Georgetown University from 1981–85.

Question: How large is the campus of the university for which Bill Bergey played collegiately?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "university_name": {
      "type": "string",
      "description": "The name of the university."
    },
    "campus_size_acres": {
      "type": "integer",
      "description": "The size of the university campus in acres."
    },
    "campus_size_km2": {
      "type": "number",
      "description": "The size of the university campus in square kilometers."
    },
    "location_city": {
      "type": "string",
      "description": "The city where the university is located."
    },
    "location_state": {
      "type": "string",
      "description": "The state where the university is located."
    }
  },
  "required": [
    "university_name",
    "campus_size_acres",
    "campus_size_km2",
    "location_city",
    "location_state"
  ],
  "additionalProperties": false
}
