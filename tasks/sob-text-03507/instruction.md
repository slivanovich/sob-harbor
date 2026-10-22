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
Obed Rincón: Obed Isai Rincon Lopez (born 4 February 1985 in Monterrey, Nuevo Leon, Mexico, is a professional footballer, currently playing as a left back for C.F. La Piedad in the Ascenso MX.  He started his professional career with club Necaxa in 2008.

Andy Rincon: Andrew John Rincon (born March 5, 1959) is a former Major League Baseball pitcher born in Monterey Park, California on March 5, 1959.  He was drafted out of St. Paul High School in Santa Fe Springs California by the St. Louis Cardinals in the 5th round of the 1977 Major League Baseball Draft.  He was a "September Call-up" in 1980.  He started four games, going 3–1 with a 2.61 ERA.  This earned him another brief look the next year, when he had a similar 3–1 record, this time with a 1.77 ERA in five starts.  That season, he was hit in the arm by a line drive by Phil Garner, thus hampering his career.  Rincon Cardinals started six games and relieved in five games, finishing with a 2–3 record and 4.72 ERA.  The next year, Rincon did not make it to the Major Leagues at all, and the Cardinals released him at the end of 1983.  The San Diego Padres signed him that offseason, but he never pitched in the majors again.

Dix Stadium: Dix Stadium is a multi-purpose stadium in Kent, Ohio, United States.  It is primarily used for American football, and is the home field of the Kent State Golden Flashes football team.  In addition, the stadium was home to the Kent State field hockey team from 1997 to 2004, and is a secondary home for the Kent State women's soccer team.  It opened on September 13, 1969 and was named in 1973 after Robert C. Dix, former publisher of the "Record-Courier" and a member of Kent State's Board of Trustees for more than three decades.  It was built as an expansion and relocation of Memorial Stadium, with all of Memorial Stadium's main seating areas used at the current stadium in a new configuration.

Sports in Richmond, Virginia: Richmond, Virginia, United States, is home to three professional sports teams, though none of which compete in any major professional league.  Virginia is the most populated state without a major sports team.  In 2008, the Richmond Braves minor league baseball team left for Gwinnett County, Georgia, and was replaced by the Richmond Flying Squirrels in 2010.  But now, the Flying Squirrels' owner has threatened to leave Richmond if they do not replace their current stadium, The Diamond.  The Richmond Kickers are a non-profit soccer team that plays at City Stadium.

Campo Municipal da Nogueira: Campo Municipal da Nogueira is the home stadium of Associação Desportiva da Camacha (AD Camacha), a football team from the Portuguese island of Madeira.  The stadium has a capacity of 3,300.  The current stadium has one stand around the stadium which is on the west side of the stadium and has engraved on the spectators seats the name of the club in blue.  The stadium was built when the club was founded in 1978.

Copeland Park: Copeland Park, also referred to as "The Lumber Yard," is a stadium in La Crosse, Wisconsin.  It is primarily used for baseball, and is the home field of the La Crosse Loggers baseball team.  The current stadium was built in 2003, although a substantially smaller baseball diamond existed at the site prior to the construction of the new ballpark.  At the time of its construction, the stadium held approximately 2,000 people; however, the success of the Loggers prompted expansions to the grandstand, bringing the capacity to its current 3,550 people.  The field dimensions are 325 ft. to left field, 365 ft. to center, and 315 ft. to right.

St. Louis Cardinals: The St. Louis Cardinals are an American professional baseball team based in St. Louis, Missouri.  The Cardinals compete in Major League Baseball (MLB) as a member club of the National League (NL) Central division.  Busch Stadium has been their home ballpark since 2006.  With origins as one of the early professional baseball clubs in St. Louis, entrepreneur Chris von der Ahe purchased a barnstorming club in 1881, then known as the Brown Stockings, and established them as charter members of the American Association (AA) the following season.  Upon the discontinuation of the AA, St. Louis joined the NL in 1892; at that time, they were called the Browns and the Perfectos before they were officially renamed as the Cardinals in 1900.

Griffiths Stadium: Griffiths Stadium is a stadium located on the grounds of the University of Saskatchewan in Saskatoon, Saskatchewan.  The current stadium was opened on June 23, 1967 to host the Saskatchewan Huskies football team.  There was previously a Griffiths Stadium 200 metres to the east of the current location from October 3, 1936 until the new site was opened.

List of New Orleans Saints head coaches: The New Orleans Saints are a professional American football team based in New Orleans, Louisiana.  They are a member of the South Division of the National Football Conference (NFC) in the National Football League (NFL).  The NFL awarded the city of New Orleans the 16th franchise in the league in November 1, 1966, All Saints Day, five months after the 89th United States Congress approved the merger of the NFL with the American Football League (AFL) in June of that year.  In January 1967, the team was given the current "New Orleans Saints" name, and began playing in their first season in September of that year.  Since the franchise's creation, it has been based in New Orleans.  The team's home games were originally played at Tulane Stadium from 1967 to 1974, it was demolished in 1979, when the team relocated its home games to its current stadium, the Mercedes-Benz Superdome (formerly Louisiana Superdome from 1975 to 2011).

2004 Dallas Burn season: The 2004 Dallas Burn season was the eighth season of the Major League Soccer team.  The season saw the team fail to make the playoffs for the second consecutive year.  The season was also the first full season under head coach Colin Clarke.  The team moved from Dragon Stadium back to the Cotton Bowl.  It would be the last season for the team in the Cotton Bowl, as they would move to their current stadium in Frisco.  It was also the team’s final season as the Burn.  With the move to their own stadium the next year, the team would be rebranded as FC Dallas in 2005.  Burn forward Eddie Johnson shared the Golden Boot Award with Brian Ching, tying him for the most goals in the MLS with 12.  Johnson was the second Burn player to win the award, with Jason Kreis previously winning it in 1999.

Question: What is the current stadium for the team Andy Rincon started his professional career with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player."
    },
    "first_professional_team": {
      "type": "string",
      "description": "The team the player started their professional career with."
    },
    "team_current_stadium": {
      "type": "string",
      "description": "The current stadium of the player's first professional team."
    },
    "stadium_opened_year": {
      "type": "integer",
      "description": "The year the current stadium of the team opened."
    }
  },
  "required": [
    "player_name",
    "first_professional_team",
    "team_current_stadium",
    "stadium_opened_year"
  ],
  "additionalProperties": false
}
