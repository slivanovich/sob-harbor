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
NBA 2K9: NBA 2K9 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It is the tenth installment in the "NBA 2K" franchise and the successor to "NBA 2K8".  It was released in 2008 for PlayStation 2, PlayStation 3, Xbox 360, and Microsoft Windows.  Kevin Garnett is the cover athlete of the game.  "NBA 2K9" is the predecessor to "NBA 2K10" in the "NBA 2K" series.

NBA 2K10: NBA 2K10 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It was released in October and November 2009 for Microsoft Windows, PlayStation 3, PlayStation 2, PlayStation Portable, Xbox 360, and Wii.  The eleventh installment in the "NBA 2K" series, it is the successor to "NBA 2K9" and the predecessor to "NBA 2K11".  Kobe Bryant of the Los Angeles Lakers is the cover athlete of the game.  "NBA 2K10" is the first game in the series to be released for the PlayStation Portable and Nintendo Wii platforms; it is also the first game in the series to be released on a Nintendo console since "NBA 2K3" was released for GameCube.

NBA 2K6: NBA 2K6 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It is the seventh installment in the "NBA 2K" franchise and the successor to "ESPN NBA 2K5".  It was released in 2005 for PlayStation 2, Xbox, and Xbox 360.  Shaquille O'Neal of the Miami Heat is the cover athlete of the game.  "NBA 2K6" is the predecessor to "NBA 2K7" in the "NBA 2K" series and is the first NBA 2K title to be released by 2K Sports.

NBA 2K (video game): NBA 2K is a basketball simulation video game developed by Visual Concepts and published by Sega Sports.  The first installment of the "NBA 2K" series, it was initially released for Dreamcast in 1999.  Allen Iverson of the Philadelphia 76ers is featured as the cover athlete.  The game is based on the National Basketball Association and, as such, allows the player to compete in basketball games with the current NBA season's players and teams.  Several game modes are present, including one in which the player can create customizable players.  "NBA 2K" was well-received by critics, who praised it for setting the standard for basketball video games.  The original "NBA 2K" spawned numerous successors, the first being "NBA 2K1", which was released in November 2000.

ESPN NBA 2K5: ESPN NBA 2K5 is a basketball simulation video game developed by Visual Concepts and published by both Sega and Global Star Software.  It was released in September 2004 for PlayStation 2 and Xbox in North America, and February 2005 in Europe.  The sixth installment in the "NBA 2K" series, it is the successor to "ESPN NBA Basketball", and the predecessor to "NBA 2K6".  Ben Wallace of the Detroit Pistons is the cover athlete; this marks the first time in the series that a player other than Allen Iverson was featured as a cover athlete.  It is the last "NBA 2K" game to be released by Sega before the company sold Visual Concepts to Take-Two Interactive, forming 2K Sports.

Paul George: Paul George (born May 2, 1990) is an American professional basketball player for the Oklahoma City Thunder of the National Basketball Association (NBA).  He is a four-time NBA All-Star and has been named three times to the All-NBA Team and NBA All-Defensive Team.

NBA 2K8: NBA 2K8 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports and Spike.  It is the ninth installment in the "NBA 2K" franchise and the successor to "NBA 2K7".  It was released in 2007 for PlayStation 2, PlayStation 3, and Xbox 360.  Chris Paul of the New Orleans Hornets is the cover athlete of the game.  "NBA 2K8" is the predecessor to "NBA 2K9" in the "NBA 2K" series.

NBA 2K7: NBA 2K7 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It is the eighth installment in the "NBA 2K" franchise and the successor to "NBA 2K6".  It was released in 2006 for PlayStation 2, PlayStation 3, Xbox, and Xbox 360.  Shaquille O'Neal of the Miami Heat is the cover athlete of the game.  "NBA 2K7" is the predecessor to "NBA 2K8" in the "NBA 2K" series.

NBA 2K15: NBA 2K15 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It is the sixteenth installment in the "NBA 2K" franchise and the successor to "NBA 2K14".  It was released in October 2014 for Microsoft Windows, Xbox One, Xbox 360, PlayStation 3 and PlayStation 4.  Kevin Durant of the Oklahoma City Thunder, one of the three cover athletes of "NBA 2K13", is the solo cover athlete of "NBA 2K15".  "NBA 2K15" was succeeded by "NBA 2K16".

NBA 2K17: NBA 2K17 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports.  It is the 18th installment in the "NBA 2K" franchise and the successor to "NBA 2K16".  It was released worldwide on September 20, 2016, for Microsoft Windows, PlayStation 4, PlayStation 3, Xbox One, and Xbox 360.  Players who pre-ordered the game received it on September 16, 2016.  Paul George of the Indiana Pacers is the cover athlete for the regular edition of the game, while Kobe Bryant is the cover athlete for the 'Legend Edition'.  In Italy, the cover athlete is Danilo Gallinari, and in Spain, the cover athlete is Pau Gasol.  A version of the game for iOS and Android was released on September 23, 2016.

Question: Who is the American professional basketball player and four-time NBA All-Star in a basketball simulation video game developed by Visual Concepts and published by 2K Sports?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the American professional basketball player."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "nba_all_star_appearances": {
      "type": "integer",
      "description": "The number of times the player has been an NBA All-Star."
    },
    "associated_game": {
      "type": "object",
      "properties": {
        "game_title": {
          "type": "string",
          "description": "The title of the video game the player is associated with."
        },
        "role_in_game": {
          "type": "string",
          "description": "The player's role in the game, e.g., 'cover athlete'."
        },
        "developer": {
          "type": "string",
          "description": "The developer of the video game."
        },
        "publisher": {
          "type": "string",
          "description": "The publisher of the video game."
        }
      },
      "required": [
        "game_title",
        "role_in_game",
        "developer",
        "publisher"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "nationality",
    "nba_all_star_appearances",
    "associated_game"
  ],
  "additionalProperties": false
}
