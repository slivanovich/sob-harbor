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
2001–02 San Antonio Spurs season: The 2001–02 NBA season was the Spurs' 26th season in the National Basketball Association, the 29th in San Antonio, and 35th season as a franchise.  During the offseason, the Spurs acquired Steve Smith from the Portland Trail Blazers, and signed free agents Bruce Bowen and second-year guard Stephen Jackson.  This was the Spurs' last season at the Alamodome, as they moved into the brand new AT&T Center the next season.  The Spurs won 20 of their first 24 games, then posted a 13-game winning streak in March and won their final nine games, finishing first place in the Midwest Division with a 58–24 record.  The season saw Tim Duncan earn his first NBA MVP award joining David Robinson as the only Spurs to win the award, and was selected for the 2002 NBA All-Star Game, while first round draft pick Tony Parker made the All-Rookie First Team.

2016–17 San Antonio Spurs season: The 2016–17 San Antonio Spurs season was the 50th season of the franchise, 41st in the National Basketball Association (NBA) and 44th in the San Antonio area.  It was the first season since the 1996–97 season without Tim Duncan, who retired on July 11, 2016.  With the elimination of the Detroit Red Wings from the 2017 Stanley Cup playoffs on March 28, 2017, the San Antonio Spurs now hold the longest active playoff streak in any of the major North American professional sports leagues with 20 consecutive NBA Playoffs appearances.

Tony Parker: William Anthony Parker Jr. (born 17 May 1982) is a French professional basketball player for the San Antonio Spurs of the National Basketball Association (NBA).  The son of a professional basketball player, Parker played for two years in the French basketball league before entering the 2001 NBA draft.  He was selected by the San Antonio Spurs with the 28th overall pick in the draft and quickly became their starting point guard.  Parker has won four NBA Championships (2003, 2005, 2007, and 2014), all of which were with the Spurs.

Spurs Sports &amp; Entertainment: Spurs Sports & Entertainment L.L.C. (SS&E) is a San Antonio, Texas based sports & entertainment organization.  The company owns and operates several sporting franchises including the 5-time National Basketball Association (NBA) champions San Antonio Spurs, the Women's National Basketball Association (WNBA)'s San Antonio Stars, AHL's San Antonio Rampage, NBA G League's Austin Spurs, and the USL club San Antonio FC.  SS&E also operates the Bexar County owned multi-purpose facility, AT&T Center.

Big Three (San Antonio Spurs): The Big Three were a trio of basketball players for the San Antonio Spurs of the National Basketball Association (NBA) from 2002–2016.  The Big Three consisted of Tim Duncan, Tony Parker, and Manu Ginóbili.  Each player of the Big Three was drafted by the San Antonio Spurs and played their entire NBA careers with the San Antonio Spurs.  The Big Three won four NBA Championships during their time together in San Antonio, in 2003, 2005, 2007, and 2014.  The trio is widely regarded as the greatest trio of teammates in NBA history, as they have won over 1,000 games together.

List of San Antonio Spurs head coaches: The San Antonio Spurs are an American professional basketball team based in San Antonio, Texas.  They are a member of the Southwest Division of the Western Conference in the National Basketball Association (NBA).  The franchise was founded as the Dallas Chaparrals of the American Basketball Association (ABA) in 1967.  The team suffered from poor attendance and general disinterest by fans in Dallas, and the name "Dallas" was dropped in favor of "Texas" during the 1970–71 season in an attempt to make the team regional.  This also proved to be a failure, and the team returned full-time to use "Dallas" for the 1971–72 season.  The team was put up for sale after missing the playoffs in the 1972–73 season.  The team was acquired by a group of 36 San Antonio businessmen, led by Angelo Drossos and Red McCombs, who relocated the team to San Antonio, Texas and renamed it to Spurs.  In 1976, the ABA folded, threatening the future of San Antonio's sole professional sports franchise.  The NBA, however, decided to admit four ABA teams into the league, including the Spurs, along with the Denver Nuggets, the Indiana Pacers and the New York Nets.

Manu Ginóbili: Emanuel David "Manu" Ginóbili Maccari (] , born 28 July 1977) is an Argentine professional basketball player for the San Antonio Spurs of the National Basketball Association (NBA).  He is also a member of the Argentine men's national basketball team.  He is one of only two players, along with Bill Bradley, to have won at least a EuroLeague title, an NBA championship, and an Olympic gold medal.

List of San Antonio Spurs seasons: The San Antonio Spurs are a professional basketball team based in San Antonio that competes in the National Basketball Association (NBA).  They were founded in Dallas, Texas as the Dallas Chaparrals, one of the eleven charter franchises of the American Basketball Association (ABA), in 1967.  During the 1970–71 season, in an attempt to make the team a regional one, the name "Dallas" was dropped in favor of "Texas" and some home games were played in Fort Worth and Lubbock, but low attendance figures prompted the team to return full-time to Dallas the following season.  In 1973 the franchise relocated to San Antonio and was renamed the San Antonio Spurs.  Three years later the Spurs were one of four ABA franchises who joined the NBA as a result of the ABA–NBA merger.

Patty Mills: Patrick Sammy Mills (born 11 August 1988) is an Australian professional basketball player for the San Antonio Spurs of the National Basketball Association (NBA).  Mills is the second Indigenous Australian to play in the NBA (after Nathan Jawai) and is of Torres Strait Islander descent.  Mills was drafted by the Portland Trail Blazers with the 55th overall pick in the 2009 NBA draft after playing college basketball for Saint Mary's College of California.  He also played for the Melbourne Tigers of the National Basketball League and the Xinjiang Flying Tigers of the Chinese Basketball Association during the NBA lockout.  He signed with the San Antonio Spurs in 2012 and won an NBA championship with them in 2014.  He plays the point guard position.

Twin Towers (San Antonio Spurs): The Twin Towers is a name applied to the combination of Tim Duncan and David Robinson playing as the frontcourt of the San Antonio Spurs from 1997–2003.  Both players were selected first overall by the San Antonio Spurs in their draft years with Robinson's selection coming in the 1987 NBA draft and Duncan's selection coming ten years later and both played their entire careers with the San Antonio Spurs.

Question: The Big Three were a trio of basketball players for the San Antonio Spurs of the National Basketball Association (NBA) from 2002–2016, it consisted of Tim Duncan, Tony Parker, and Manu Ginóbili, an Argentine professional basketball player for the San Antonio Spurs, of which organization?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the basketball player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the player plays for."
    },
    "league": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the professional sports league."
        },
        "abbreviation": {
          "type": "string",
          "description": "The abbreviation of the professional sports league."
        }
      },
      "required": [
        "full_name",
        "abbreviation"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "team_name",
    "league"
  ],
  "additionalProperties": false
}
