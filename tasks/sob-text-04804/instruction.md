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
1932 Miami Hurricanes football team: The 1932 Miami Hurricanes football team represented the University of Miami for the 1932 college football season.  The Hurricanes played their home games at Moore Park in Miami, Florida.  The team was coached by Tom McCann, in his second year as head coach for the Hurricanes.  The Hurricanes finished their season 4–3–1 and were invited to the first annual edition of the Festival of Palms Bowl, where they would win against the Manhattan Jaspers by a score of 7-0.

Miami Hurricanes football statistical leaders: The Miami Hurricanes football statistical leaders are individual statistical leaders of the Miami Hurricanes football program in various categories, including passing, rushing, receiving, total offense, defensive stats, and kicking.  Within those areas, the lists identify single-game, single-season, and career leaders.  The Hurricanes represent the University of Miami in the NCAA's Atlantic Coast Conference.

1934 Miami Hurricanes football team: The 1934 Miami Hurricanes football team represented the University of Miami for the 1934 college football season.  The Hurricanes played their home games at Moore Park in Miami, Florida.  The team was coached by Tom McCann, in his fourth and final year as head coach for the Hurricanes.  Finishing the season with a 5–3–1 record, the Hurricanes were invited to play in the first edition of the post-season Orange Bowl.  The Hurricanes lost, 26–0, to the <a href="">Bucknell

Florida–Miami football rivalry: The Florida–Miami football rivalry is an American college football rivalry between the Florida Gators football team of the University of Florida and Miami Hurricanes football team of the University of Miami.  The game was played annually from 1944 until 1987, and is now played intermittently.  The winning team was formerly awarded the Seminole War Canoe Trophy.  Today, the round robin winner of the three biggest schools in the state of Florida (either the Florida Gators, Florida State Seminoles or Miami Hurricanes) receives the Florida Cup for beating the other two schools in the same season.  Miami leads the series 29–26, and has won seven of the past eight match-ups including a 21–16 victory in the most recent game played in 2013.

1983 Miami Hurricanes football team: The 1983 Miami Hurricanes football team represented the University of Miami in 1983 NCAA Division I-A football season.  Led by fifth-year head coach Howard Schnellenberger, the Hurricanes finished the season with a record of 11–1 after defeating the Nebraska Cornhuskers in the Orange Bowl.  Miami finished atop both the AP Poll and the Coaches Poll and is recognized as the consensus national champion of the season.  The national championship was the first of five won by Miami.

1951 Miami Hurricanes football team: The 1951 Miami Hurricanes football team represented the University of Miami for the 1951 college football season.  The Hurricanes played their home games at the Burdine Stadium in Miami, Florida.  The team was coached by Andy Gustafson, in his fourth year as head coach for the Hurricanes.  The Hurricanes participated in the Gator Bowl, in a post-season matchup against Clemson.  The Hurricanes won 14–0.

1970 Miami Hurricanes football team: The 1970 Miami Hurricanes football team represented the University of Miami for the 1970 college football season.  The Hurricanes played their home games at the Miami Orange Bowl in Miami, Florida.  The team was coached by Charlie Tate, in his final year as head coach.  Tate resigned after coaching the first two games of the season.  Walt Kichefski took over as interim head coach for the Hurricanes for the remainder of the season.

Ian Sinclair (Canadian football): Ian Sinclair (born 1960 in Toronto, Ontario) is a former professional Canadian football offensive lineman who played eleven seasons in the Canadian Football League for the BC Lions.  He played college football at the University of Miami where he was part of the 1983 Miami Hurricanes football team national champions.  He also was a part of the Lions Grey Cup victories in 1985 and 1994.

1945 Miami Hurricanes football team: The 1945 Miami Hurricanes football team represented the University of Miami for the 1945 college football season.  The Hurricanes played their home games at the Burdine Stadium in Miami, Florida.  The team was coached by Jack Harding, in his seventh year as head coach for the Hurricanes.  The Hurricanes participated in the Orange Bowl, in a post-season matchup against Holy Cross.  The Hurricanes won 13–6.

Howard Schnellenberger: Howard Leslie Schnellenberger (born March 16, 1934) is a retired American football coach with long service at both the professional and college levels.  He held head coaching positions with the National Football League's Baltimore Colts and in college for the University of Miami, University of Oklahoma, University of Louisville and Florida Atlantic University.  He won a national championship with Miami in 1983.  Schnellenberger also worked extensively as an assistant coach at the college and pro levels, including as part of the staff of the undefeated 1972 Miami Dolphins.  He is also famous for recruiting Joe Namath to Alabama for Bear Bryant in 1961.

Question: The coach of the 1983 Miami Hurricanes football team was born in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the head coach."
    },
    "team_year": {
      "type": "integer",
      "description": "The year of the football team."
    },
    "coach_birth_year": {
      "type": "integer",
      "description": "The birth year of the coach."
    }
  },
  "required": [
    "coach_name",
    "team_year",
    "coach_birth_year"
  ],
  "additionalProperties": false
}
