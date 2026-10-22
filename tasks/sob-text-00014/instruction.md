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
Norb Hecker: Norbert Earl Hecker (May 26, 1927 – March 14, 2004) was an American football player and coach who was part of eight National Football League championship teams, but may be best remembered as the first head coach of the NFL's Atlanta Falcons.

Nobby Wirkowski: Norbert "Nobby" Wirkowski (August 20, 1926 – October 15, 2014) was an American and Canadian football player and coach.  He is best known as quarterback of the Toronto Argonauts.  The touchdown he engineered in the 1952 Grey Cup turned out to be the last offensive touchdown by the Argonauts in a Grey Cup for 30 years.

Norbert Siegmann: Norbert Siegmann (born 20 May 1953) is a retired German football player.  He spent 11 seasons in the Bundesliga with VfB Stuttgart, Tennis Borussia Berlin and SV Werder Bremen.  As of February 2009, he is managing the low-level amateur club SV Weser 08 Bremen.  He is probably best known for seriously injuring Ewald Lienen in 1981.  That foul was called "the most well-known foul in the history of Bundesliga".

Norbert Ringels: Norbert Ringels (Mönchengladbach, 16 September 1956) is a retired German football player.  He spent ten seasons in the Bundesliga with Borussia Mönchengladbach, where he was known as "Nonno" to his teammates.

Norbert Hrnčár: Norbert Hrnčár (born 9 June 1970) is a former football player from Slovakia and currently manager of Spartak Myjava.  His forme club was FC Petržalka 1898.

Chuck Bednarik Award: The Chuck Bednarik Award is presented annually to the defensive player in college football adjudged by the Maxwell Football Club to be the best in the United States.  The award is named for Chuck Bednarik, a former college and professional American football player.  Voters for the Maxwell College Awards are NCAA head college football coaches, members of the Maxwell Football Club, and sportswriters and sportscasters from across the country.  The Maxwell Club is located in Philadelphia, Pennsylvania and the presentations are held in Atlantic City, New Jersey.  Club members are given voting privileges for the award.

Maxwell Award: The Maxwell Award is presented annually to the college football player judged by a panel of sportscasters, sportswriters, and National Collegiate Athletic Association head coaches and the membership of the Maxwell Football Club to be the best all-around in the United States.  The award is named after Robert "Tiny" Maxwell, a Swarthmore College football player, coach and sportswriter.  Johnny Lattner (1952, 1953) and Tim Tebow (2007, 2008) are the only players to have won the award twice.  It is the college equivalent of the Bert Bell Award of the National Football League, also given out by the Maxwell Club.

Ewald Lienen: Ewald Lienen (born 28 November 1953) is a German former football player and current technical director of FC St. Pauli.

Norbert Eilenfeldt: Norbert Eilenfeldt (born 17 February 1956 in Gelsenkirchen) is a retired German football player.  He spent eight seasons in the Bundesliga with Arminia Bielefeld, 1.  FC Kaiserslautern and FC Schalke 04.  The best league finish he achieved was fourth place.

John Worsfold: John Richard Worsfold (born 25 September 1968) is a former Australian rules football player and current coach best known for his career for the West Coast Eagles in the Australian Football League (AFL).  He made his senior debut for the South Fremantle Football Club in the West Australian Football League (WAFL), and was named an inaugural squad member of West Coast on their formation in 1986.  After winning the club's best and fairest award in 1988, Worsfold was appointed captain of the club in 1991, a position he would hold until his retirement in 1998.  During his period at the club, Worsfold played in 209 games, which including the 1992 and 1994 premiership sides.  During this time, he also appeared in five State of Origin matches for Western Australia, captaining his state twice.

Question: Norbert Siegmann is best known for injuring the football player who is now director of which club?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "injured_player": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the football player who was injured."
        },
        "injury_year": {
          "type": "integer",
          "description": "The year the injury occurred."
        }
      },
      "required": [
        "name",
        "injury_year"
      ],
      "additionalProperties": false
    },
    "current_role": {
      "type": "string",
      "description": "The current role of the injured player."
    },
    "club_name": {
      "type": "string",
      "description": "The name of the club where the injured player is currently a director."
    }
  },
  "required": [
    "injured_player",
    "current_role",
    "club_name"
  ],
  "additionalProperties": false
}
