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
Extremadura UD: Extremadura Unión Deportiva is a Spanish football team based in Almendralejo, in the autonomous community of Extremadura.  Founded in 2007 it plays in Segunda División B – Group 4, holding home games at "Estadio Francisco de la Hera".

List of Miami Marlins seasons: The Miami Marlins (originally the Florida Marlins from 1993 until 2011) are a professional baseball team that has been based in Miami Gardens, Florida since becoming an expansion team in .  The Marlins are a member of both the Major League Baseball's (MLB) National League Eastern Division and the National League (NL) itself.  For the first 19 seasons, the Marlins played their home games at Sun Life Stadium.  Beginning with the season, the Marlins play home games at Marlins Park in Little Havana.

LSU Tigers baseball: The LSU Tigers baseball team represents Louisiana State University in NCAA Division I college baseball.  The team participates in the West Division of the Southeastern Conference.  It is one of the elite college baseball programs in the nation, ranking seventh all-time with 18 College World Series appearances and second all-time with six national championships (1991, 1993, 1996, 1997, 2000, and 2009).  The Tigers play home games on LSU's campus at Alex Box Stadium, Skip Bertman Field, and they are currently coached by Paul Mainieri.

1945–46 Georgetown Hoyas men's basketball team: The 1945–46 Georgetown Hoyas men's basketball team represented Georgetown University during the 1945-46 NCAA Division I college basketball season.  Ken Engles coached it in his only season as head coach.  It played its home games on the campus of The Catholic University of America at Brookland Gymnasium in Washington, D.C., the only Georgetown team to play home games there with the exception of the 1946-47 team, which played four games there the following season.

2005–06 West Indian cricket season: The 2005–06 West Indian cricket season includes all domestic cricket matches played by senior teams with first class status in the West Indies between October 2005 and March 2006, and also the international feats of the West Indies team, who is not scheduled to play any home games during this period but are to play home matches during April, May and June 2006.  The season began on 2005-10-03 with the first matches of the one-day KFC Cup, and is scheduled to last until 2006-03-19 when England A depart after their tour which will include one-day and first class matches against the West Indies A team.  The West Indies will not play any home Tests during their home season, but they have toured Australia (losing the 3-Test series 0–3), and toured New Zealand in February and March, immediately after the conclusion of the 2005-06 Carib Beer Cup, the first class competition.

North Shore Knights: The North Shore Knights are a minor professional ice hockey team in the Federal Hockey League based out of Kingsville, Ontario.  The Knights play the majority of their home games at the Kingsville Arena Complex during their first season.  The team will also play home games in several other cities in Ontario and Quebec.

Sandringham Soccer Club: Sandringham Soccer Club is an Australian soccer club based in Sandringham, Victoria.  Their men's team currently compete in State League 2 South-East, after being promoted from State League 3 South-East in 2014.  While their women's team play in the top tier of women's football in Victoria, the Women's Premier League.  The men's team play home games at RJ Sillitoe Reserve, whereas as the women play home games at Kingston Heath Soccer Complex.

Álex Barrera: Alejandro 'Álex' Barrera García (born 12 May 1991) is a Spanish professional footballer who plays for Extremadura UD as a central midfielder.

Bahama All-Pro Show: The Bahama All-Pro Show were a basketball team representing The Bahamas, and playing their home games in Miami, Florida, U.S.  They played sporadically in the new American Basketball Association (ABA) beginning in the 2007–2008 season.  The team was intended as a showcase for Bahamian players, and organizers hoped to eventually play home games in the Bahamas.  However internal instability caused the team to miss many of its games and suspend operations after the 2008–2009 season.

London Irish: London Irish RFC is an English rugby union club, with an Irish Identity.  It was originally based in Sunbury, Surrey, where the senior squad train, youth teams and senior academy play home games, and the club maintain their administrative offices.  It has competed in the Premiership, the top division of English rugby union, every season since its inception in 1996-97, apart from the 2016-17 season, in which it won the Greene King IPA Championship.  The club also competes in the Anglo-Welsh Cup and has participated in both the European Champions Cup or European Challenge Cup.  In 2016 it played in the British and Irish Cup in addition to the Championship.  The club will play its home games at the Madejski Stadium in Reading, Berkshire until at least 2019.

Question: Where does Alex Barrera play home games?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the player plays for."
    },
    "team_sport": {
      "type": "string",
      "description": "The sport the team plays."
    },
    "home_stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the team plays its home games."
    },
    "team_location": {
      "type": "string",
      "description": "The base location of the team."
    }
  },
  "required": [
    "player_name",
    "team_name",
    "team_sport",
    "home_stadium_name",
    "team_location"
  ],
  "additionalProperties": false
}
