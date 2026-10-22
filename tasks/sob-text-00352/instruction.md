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
Jonathan Orr: Jonathan Orr (born March 20, 1983 in Detroit, Michigan) is a former American football wide receiver who played for the NFL's Oakland Raiders and Tennessee Titans.  He was drafted in the sixth round, pick 172 of the 2006 NFL Draft by the Titans.  He played college football at the University of Wisconsin–Madison.

Andrew Robiskie: Andrew Robiskie (born May 18, 1989) is a former American football center.  He played college football at Western Illinois.  He is the son of Tennessee Titans offensive coordinator Terry Robiskie and the younger brother of free agent wide receiver Brian Robiskie.  He is also the older brother of current Western Illinois Leathernecks wide receiver Kyle Robiskie.

Darius Jennings: Darius Jennings (born June 28, 1992) is an American football wide receiver for the Tennessee Titans of the National Football League (NFL).  He was signed by the Cleveland Browns as an undrafted free agent in 2015.  He played college football at Virginia.  He has also played for the Chicago Bears, New York Jets, and Tennessee Titans.

Eric Decker: Eric Thomas Decker (born March 15, 1987) is an American football wide receiver for the Tennessee Titans of the National Football League (NFL).  He was drafted by the Denver Broncos in the third round of the 2010 NFL Draft.  He played college football and college baseball at the University of Minnesota, where he earned a bachelor's degree in business and marketing.

Eric Weems: Eric Grimes Weems (born July 4, 1985) is an American football wide receiver, special teamer, and return specialist for the Tennessee Titans of the National Football League (NFL).  He played college football at Bethune-Cookman and was signed by the Atlanta Falcons as an undrafted free agent in 2007.  He has also played for the Chicago Bears and Tennessee Titans.

Titus Davis: Titus Davis (born January 3, 1993) is an American football wide receiver who is currently a free agent.  He was signed by the San Diego Chargers as an undrafted free agent in 2015.  He played college football at Central Michigan.  His younger brother, Corey Davis is a wide receiver for the Tennessee Titans.

1999 Jacksonville Jaguars season: The 1999 Jacksonville Jaguars season was the team's fifth year in the National Football League.  Wide receiver Jimmy Smith set a franchise record for most receptions and receiving yards in one season.  Smith would finish second in the NFL in receiving yards with 1,636 yards.  The Jaguars' regular season record of 14–2 still stands as their best record in franchise history.  Both losses during the regular season were to the Tennessee Titans, and they lost again to Tennessee in the AFC Championship Game, making the Titans the only team to beat them the entire season.

I Do (Jessie James Decker song): "I Do" is a song written and recorded by American country singer and reality television personality Jessie James Decker.  Inspired by her relationship, the song, which describes a deep love, was written by Decker as a wedding gift for her husband Eric Decker.  It was released independently as a single on October 31, 2013.  "I Do" is the first song released under Decker's married name, having previously been credited as Jessie James.

Jimmy Fryzel: James David Fryzel (born on April 21, 1981 in Youngstown, Ohio) is a former Arena Football League wide receiver for the Orlando Predators.  The Predators cut Fryzel prior to the 2008 season after he tore his ACL.  Previous to signing with Orlando, he played wide receiver with the Miami Dolphins, the Atlanta Falcons, the Tennessee Titans, and the Chicago Bears.

Corey Davis (wide receiver): Corey Davis (born January 11, 1995) is an American football wide receiver for the Tennessee Titans of the National Football League (NFL).  He played college football at Western Michigan, where he became the NCAA's career receiving yards leader.  He was drafted by the Titans fifth overall in the 2017 NFL Draft.

Question: I do was a song written as a gift to which wide receiver for the Tennessee Titans?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "recipient_player": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The full name of the player who received the song as a gift."
        },
        "position": {
          "type": "string",
          "description": "The player's position in American football."
        },
        "team": {
          "type": "string",
          "description": "The NFL team the player plays for."
        }
      },
      "required": [
        "player_name",
        "position",
        "team"
      ],
      "additionalProperties": false
    },
    "gift_purpose": {
      "type": "string",
      "description": "The occasion or reason for the song being a gift."
    }
  },
  "required": [
    "song_title",
    "recipient_player",
    "gift_purpose"
  ],
  "additionalProperties": false
}
