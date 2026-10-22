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
Bill Goggin: William "Bill" Goggin (born 4 January 1941) is a former Australian rules football player in the Victorian Football League for Geelong Football Club and later coached Footscray and Geelong football clubs.  Goggin ranks as one of Geelong's greatest ever players in a career that spanned more than a decade.  He was a dual best and fairest winner, premiership player and captain of the Cats.

Variations of Australian rules football: Variations of Australian rules football are games or activities based on or similar to the game of Australian rules football, in which the player uses common Australian rules football skills.  They range in player numbers from 2 (in the case of kick-to-kick) up to the minimum 38 required for a full Australian rules football.

Geoff Ablett: Geoff Ablett (born 13 March 1955) is a former Australian rules footballer who played in the Victorian Football League (VFL) during the 1970s and 1980s.  Ablett spent the majority of his career with Hawthorn playing 202 games on the wing.  Ablett finished with short stints at Richmond and St Kilda.  His younger brother Gary Ablett Sr is a Hall of Fame inductee.  A third brother, Kevin, also played for Hawthorn, Richmond and Geelong.  Geoff Ablett was known for his burst of speed as player, winning the Grand Final Sprint competition four times.

Teia Miles: Teia Miles (born 2 November 1996) is a professional Australian rules footballer playing for the Hawthorn Football Club in the Australian Football League (AFL).  He is a highly rated young midfielder, with the ability to play forward or back when required, and is renowned for his endurance.  He is the son of former Collingwood, West Coast Eagles and Geelong player, Geoff Miles, and the cousin of Carlton player, Dylan Buckley.  Miles' sister is the partner of Geelong player, Mitch Duncan.

Tim Callan: Timothy Callan (born 6 January 1984) is a former Australian rules football player for the Western Bulldogs, and the Geelong Football Club.  He is the son of former Geelong player, Terry Callan.

Sam Simpson (footballer): Sam Simpson (born 14 June 1998) is a professional Australian rules footballer playing for the Geelong Football Club in the Australian Football League (AFL).  The son of former Geelong player, Sean Simpson, he was drafted by Geelong with their fourth selection and fifty-third overall in the 2017 rookie draft under the father–son rule.  He made his debut in the draw against Greater Western Sydney at Spotless Stadium in round fifteen of the 2017 season.

Luke Ablett: Luke Ablett (born 22 November 1982) is a former Australian rules footballer with the Sydney Swans of the AFL.  He is the son of former Hawthorn player Kevin Ablett, who was less well known than his older brother and fellow Hawthorn player Geoff Ablett and younger brother, the legendary Geelong player Gary Ablett.  He is also the cousin of current Gold Coast captain, Gary Ablett Jr..

Troy Menzel: Troy Menzel (born 22 September 1994) is a professional Australian rules footballer playing for the Adelaide Football Club in the Australian Football League (AFL).  He was drafted at pick 11 in the 2012 National Draft by Carlton , and was traded to Adelaide after the 2015 season.  He is the younger brother of Geelong player Daniel Menzel.

Brian Cook (football administrator): Brian Carlyle Cook (born 14 November 1955) is a Scottish-born Australian businessman and former Australian rules football player and coach who is the current Chief Executive Officer (CEO) of the Geelong Football Club in the Australian Football League (AFL).  Cook played for a number of different clubs in several Australian states and territories, including the Box Hill Football Club in the Victorian Football Association (VFA), the Melbourne Football Club in the Victorian Football League (VFL), and the East Perth and Subiaco Football Clubs in the Western Australian National Football League (WANFL), and later captain-coached the Ainslie Football Club in the Australian Capital Territory Football League (ACTFL).  After his retirement from coaching, Cook occupied positions with the Australian Sports Commission and the West Australian Football Commission, before being appointed CEO of the West Coast Eagles in 1990.  He quit this position in 1999 to take up the same role with Geelong.

List of Geelong Football Club players: Since becoming a foundation club of the Victorian Football League (VFL)—which is now known as the Australian Football League (AFL)—in 1897, there have been 1053 players who have represented the Geelong Football Club in a senior VFL/AFL match.  A senior VFL/AFL match is an Australian rules football match between two clubs that are, or were at the time, members of the VFL/AFL.  A senior VFL/AFL match is played under the laws of Australian football, and includes regular season matches, as well as finals series matches.  It doesn't include pre-season competition matches, Night Series matches, interstate matches or international rules football matches.  The list is arranged in the order in which each player made his debut for Geelong in a senior VFL/AFL match.  Where more than one player made his debut in the same match, those players are listed alphabetically by surname.

Question: Which Australian rules football player played during the 1970s and 1980s and had had a younger brother who was a legendary Geelong player?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the Australian rules football player."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the player."
    },
    "playing_decades": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The decades during which the player was active in the VFL."
    },
    "primary_club": {
      "type": "string",
      "description": "The club where the player spent the majority of their career."
    },
    "games_played_for_primary_club": {
      "type": "integer",
      "description": "The number of games played for their primary club."
    },
    "other_clubs": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other clubs the player had short stints with."
    },
    "notable_achievements": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Notable achievements or characteristics of the player."
    },
    "brother_information": {
      "type": "object",
      "properties": {
        "brother_name": {
          "type": "string",
          "description": "The name of the player's brother."
        },
        "brother_relationship": {
          "type": "string",
          "description": "The relationship to the player (e.g., younger brother)."
        },
        "brother_status": {
          "type": "string",
          "description": "The legendary status or recognition of the brother."
        },
        "brother_club": {
          "type": "string",
          "description": "The club the legendary brother played for."
        }
      },
      "required": [
        "brother_name",
        "brother_relationship",
        "brother_status",
        "brother_club"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "playing_decades",
    "brother_information"
  ],
  "additionalProperties": false
}
