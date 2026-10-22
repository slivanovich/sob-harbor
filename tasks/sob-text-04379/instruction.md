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
Lou Little: Luigi "Lou Little" Piccolo (December 6, 1893 – May 28, 1979) was an American football player and coach.  Embarrassed by his Italian name, he changed it to "Little", retaining the meaning.  He served as the head coach at Georgetown College, now Georgetown University, from 1924 to 1929 and at Columbia University from 1930 to 1956, compiling a mediocre career college football record of 151–128–13.  Little played college football as a tackle at the University of Pennsylvania for the 1916 and 1919 seasons and then with the professional football team the Frankford Yellow Jackets from 1920 to 1923.  He was inducted into the College Football Hall of Fame as a coach in 1960.  He appeared as "Lu Libble" in Jack Kerouac's novel "Maggie Cassidy", a fictionalized account of Kerouac's early life.

2015–16 UCF Knights men's basketball team: The 2015–16 UCF Knights men's basketball team represented the University of Central Florida during the 2015–16 NCAA Division I men's basketball season.  The Knights were member of the American Athletic Conference.  The Knights, in the program's 47th season of basketball, were led by sixth year head coach Donnie Jones and played their home games at the CFE Arena on the university's main campus in Orlando, Florida.  They finished the season with a record of 12–18, 6–12 in AAC play to finish in seventh place in conference.  They lost in the first round of the AAC Tournament to Tulane.  After the season, Donnie Jones was fired as UCF's head coach.

List of UCF Knights men's basketball seasons: This is a list of seasons completed by the UCF Knights basketball team since the team's formation in 1969.  Since that season, the Knights have played over 1,100 regular-season games, winning five conference tournament championships and seven regular season championships.  The Knights are a member of the American Athletic Conference (The American), and their current head coach is Donnie Jones, who is in his fifth year with the team.  The Knights play their home games at CFE Arena, which is located on the main campus of UCF in Orlando, Florida.

1979 Iowa State Cyclones football team: The 1979 Iowa State Cyclones football team represented Iowa State University during the 1979 NCAA Division I-A football season.  They played their home games at Cyclone Stadium in Ames, Iowa.  They participated as members of the Big Eight Conference.  The team was coached by head coach Donnie Duncan.

Texas Longhorns football: The Texas Longhorns football program is the intercollegiate team representing the University of Texas at Austin (variously Texas or UT) in the sport of American football.  The Longhorns compete in the NCAA Division I Football Bowl Subdivision (formerly Division I-A) as a member of the Big 12 Conference.  The team is coached by Tom Herman and home games are played at Darrell K Royal – Texas Memorial Stadium in Austin, Texas.

Donnie Little: Donnie Little (born October 14, 1959) is a former American football quarterback.  He was the quarterback of the Texas Longhorns from 1978 to 1980, and in 1978 was the first black quarterback to play for The University of Texas.  He is credited with "opening doors" for future black quarterbacks at Texas, such as James Brown and Vince Young.

List of Dallas Mavericks head coaches: The Dallas Mavericks are an American professional basketball team based in Dallas, Texas.  They play in the Southwest Division of the Western Conference in the National Basketball Association (NBA).  The team joined the NBA in 1980 as an expansion team, and won their first Western Conference championship in 2006.  The Mavericks have played their home games at the American Airlines Center since 2001.  The Mavericks are owned by Mark Cuban, and Donnie Nelson is their general manager.

Kim Little: Kim Alison Little (born 29 June 1990) is a Scottish footballer who is a leading scorer on the Scotland women's national football team.  She currently plays for Arsenal Ladies in the FA WSL.  She previously played for NWSL club Seattle Reign FC and Melbourne City in the Australian W-League.  During her first spell at Arsenal from 2008–2013, the team won four league titles, three WSL Continental Cups, three FA Cups and one Premier League Cup.  Prior to her six years with Arsenal, Little played for Hibernian L.F.C. in the Scottish Women's Premier League (SWPL).  During her 18 months with the club, they won the SWPL championship title, Scottish Cup, and the Premier League Cup.

2011–12 UCF Knights men's basketball team: The 2011–12 UCF Knights men's basketball team was a NCAA Division I college basketball team that represented the University of Central Florida and competes in Conference USA.  They played their home games at UCF Arena in Orlando, Florida and were led by second-year head coach Donnie Jones.

2014–15 Tennessee Volunteers basketball team: The 2014–15 Tennessee Volunteers basketball team represented the University of Tennessee in the 2014–15 NCAA Division I men's basketball season.  The team's head coach was Donnie Tyndall, who was in his first season at Tennessee.  The team played their home games at the Thompson–Boling Arena in Knoxville, Tennessee as a member of the Southeastern Conference.  They finished the season 16–16, 7–11 in SEC play to finish in tenth place.  They advanced to the quarterfinals of the SEC Tournament where they lost to Arkansas.

Question: Donnie Little played for the team that was in what conference?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the football player."
    },
    "team_played_for": {
      "type": "string",
      "description": "The name of the team the player was a quarterback for."
    },
    "sport": {
      "type": "string",
      "description": "The sport the player participated in."
    },
    "team_conference": {
      "type": "string",
      "description": "The conference the team was a member of."
    },
    "notable_achievement": {
      "type": "string",
      "description": "A significant historical achievement of the player related to the team."
    }
  },
  "required": [
    "player_name",
    "team_played_for",
    "sport",
    "team_conference",
    "notable_achievement"
  ],
  "additionalProperties": false
}
