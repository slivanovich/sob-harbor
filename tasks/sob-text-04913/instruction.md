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
1982 Aloha Bowl: The 1982 Aloha Bowl was an American college football bowl game played on December 25, 1982 at Aloha Stadium in Honolulu, Hawaii.  The inaugural Aloha Bowl game pitted the Washington Huskies and the Maryland Terrapins.  This was the first bowl game played in Hawaii since the Pineapple Bowl in 1952.

Hawaii Bowl: The Hawaiʻ i Bowl is a post-season National Collegiate Athletic Association Football Bowl Subdivision college football bowl game that has been played annually at Aloha Stadium in Honolulu, Hawaii since 2002.  Typically played on either Christmas Day or Christmas Eve, the game matches teams from either Conference USA or the Pac-12 and a team from the Mountain West Conference.  As part of the bowl charter, a "Hawaiʻ i guarantee" allows the University of Hawaiʻ i an automatic bid to the bowl provided it is bowl eligible and does not receive a bid to a bowl in the College Football Playoff, which goes to the highest ranking school among the members of the Mountain West, Sun Belt, Mid-American, and American Athletic Conferences and Conference USA.  If Hawaiʻ i is not eligible then another Mountain West team receives the bid.  This continues a tradition started when Hawaiʻ i was a member of the Western Athletic Conference.

Aloha Bowl: The Aloha Bowl was a National Collegiate Athletic Association Football Bowl Subdivision (then known as Division I-A) college football bowl game played in Honolulu, Hawaii at Aloha Stadium.

Miami Beach Bowl: The Miami Beach Bowl was a National Collegiate Athletic Association (NCAA) sanctioned Division I Football Bowl Subdivision (FBS) college football bowl game played for three years (2014–2016) at Marlins Park in Miami, Florida.  The bowl was created and owned by the American Athletic Conference ("The American").

Pineapple Bowl: The Pineapple Bowl is a now-defunct college football bowl game played in Honolulu, Hawaii at Honolulu Stadium.  Played on New Year's Day except in 1939 and 1950, the Pineapple Bowl succeeded the Poi Bowl.  The inaugural game was played in 1939 and the last game was played in 1952.  After the bombing of Pearl Harbor, the bowl game was suspended for five years.  The game featured the Hawaii Rainbows and an invited team from the mainland.  The rise of the Hula Bowl shortly followed the demise of the Pineapple Bowl.  The University of Hawaii attempted to revive the bowl game in 1980, but the NCAA Special Events Committee turned down their request.  However, the Aloha Bowl was created in 1982.

1988 Aloha Bowl: The 1988 Eagle Aloha Bowl was a college football bowl game, played as part of the 1988–89 bowl game schedule of the 1988 NCAA Division I-A football season.  It was the seventh Aloha Bowl.  It was played on December 25, 1988, at Aloha Stadium in Honolulu, Hawaii.  The game matched the <a href="">Houston Cougars

1989 Aloha Bowl: The 1989 Jeep Eagle Aloha Bowl was a college football bowl game, played as part of the 1989-90 bowl game schedule of the 1989 NCAA Division I-A football season.  It was the eighth Aloha Bowl.  It was played on December 25, 1989, at Aloha Stadium in Honolulu, Hawaii.  The game matched the Hawaii Rainbows against the Michigan State Spartans, and was televised on ABC.  The game marked the first ever bowl appearance for Hawaii.  Michigan State won the 1989 contest 33–13.

1995 Aloha Bowl: The 1995 Jeep Eagle Aloha Bowl was a college football bowl game, played as part of the 1995–96 bowl game schedule of the 1995 NCAA Division I-A football season.  It was the 11th Aloha Bowl.  It was played on December 25, 1995, at Aloha Stadium in Honolulu, Hawaii.  The game matched the UCLA Bruins of the Pac-10 Conference against the Kansas Jayhawks of the  Big 12 Conference in Terry Donahue's final game as head coach of the Bruins.

1987 Aloha Bowl: The 1987 Jeep Eagle Aloha Bowl was a college football bowl game, played as part of the 1987-88 bowl game schedule of the 1987 NCAA Division I-A football season.  It was the sxith Aloha Bowl.  It was played on December 25, 1987, at Aloha Stadium in Honolulu, Hawaii.  The game matched the Florida Gators of the Southeastern Conference against the UCLA Bruins of the Pac-10 Conference.  The Bruins were led by quarterback Troy Aikman.

Oahu Bowl: The Oahu Bowl is a now defunct National Collegiate Athletic Association Football Bowl Subdivision (then known as Division I-A) bowl game played in Honolulu, Hawaii at Aloha Stadium.  Played on Christmas Day or Christmas Eve, the Oahu Bowl was sponsored by Jeep motor company.  The inaugural game was played in 1998 and the last game was played in 2000, after it lost its sponsorship as a result of a corporate merger between Jeep parent Chrysler Corporation and Daimler Benz.  The Oahu Bowl was part of a double-header played after the Aloha Bowl on Christmas its first two years; the 2000 game was played on Christmas Eve.

Question: The Pineapple Bowl was replaced by which National Collegiate Athletic Association Football Bowl Subdivision (then known as Division I-A) college football bowl game played in Honolulu, Hawaii at Aloha Stadium?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "replaced_bowl_game_name": {
      "type": "string",
      "description": "The name of the college football bowl game that replaced the Pineapple Bowl."
    },
    "location": {
      "type": "string",
      "description": "The city and state where the replacement bowl game was played."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the replacement bowl game was played."
    },
    "ncaa_division": {
      "type": "string",
      "description": "The NCAA division of the replacement bowl game at the time."
    },
    "year_created": {
      "type": "integer",
      "description": "The year the replacement bowl game was created."
    }
  },
  "required": [
    "replaced_bowl_game_name",
    "location",
    "stadium_name",
    "ncaa_division",
    "year_created"
  ],
  "additionalProperties": false
}
