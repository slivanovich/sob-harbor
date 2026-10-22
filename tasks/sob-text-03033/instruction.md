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
2012 Stanley Cup Finals: The 2012 Stanley Cup Finals was the championship series of the National Hockey League's (NHL)  season, and the culmination of the 2012 Stanley Cup playoffs.  The Western Conference playoff champion Los Angeles Kings defeated the Eastern Conference playoff champion New Jersey Devils four games to two, capturing the first Stanley Cup title in the team's 45-year history, dealing the Devils just their second Stanley Cup Finals defeat in five tries and first since .  Kings goaltender Jonathan Quick was awarded the Conn Smythe Trophy as the Most Valuable Player of the playoffs.

1999 Stanley Cup Finals: The 1999 Stanley Cup Finals was the championship series of the National Hockey League's (NHL) 1998–1999 season, and the culmination of the 1999 Stanley Cup playoffs.  It was contested by the Eastern Conference champion Buffalo Sabres and the Western Conference champion Dallas Stars.  It was the 106th year of the Stanley Cup being contested.  The Sabres were led by captain Michael Peca, coach Lindy Ruff and goalie Dominik Hasek.  The Stars were led by captain Derian Hatcher, coach Ken Hitchcock and goalie Ed Belfour.  It was the Sabres' second Stanley Cup Final appearance, the first being a loss to Philadelphia in 1975.  It was the third appearance for the Stars' franchise, and their first since moving to Dallas from Minnesota in 1993.  Minnesota (known at the time as the North Stars) lost in the Final to the NY Islanders in 1981 and to Pittsburgh in 1991.  The Stars defeated the Sabres four games to two to win their first Stanley Cup, becoming the eighth post-1967 expansion team to earn a championship, and the first Southern team to win the Cup.  This was the first time since 1994 that the Stanley Cup Finals did not end in a sweep.

2015 Stanley Cup Finals: The 2015 Stanley Cup Finals was the championship series of the National Hockey League's (NHL)  season, and the culmination of the 2015 Stanley Cup playoffs.  The Western Conference champion Chicago Blackhawks defeated the Eastern Conference champion Tampa Bay Lightning four games to two to win their sixth championship in franchise history, and their third title in six seasons.  The Lightning, as the club with the better regular-season record, held home-ice advantage in the series.  The best-of-seven series was played in a 2–2–1–1–1 format, with Tampa Bay hosting games one, two, and five; and Chicago hosting games three, four and six.  Tyler Johnson and Patrick Kane led the 2015 Stanley Cup playoffs in points scored with 23 points each.  The series started June 3 and ended on June 15.

Edmonton Oilers: The Edmonton Oilers are a professional ice hockey team based in Edmonton, Alberta.  They are members of the Pacific Division of the Western Conference of the National Hockey League (NHL).

2001 Stanley Cup Finals: The 2001 Stanley Cup Finals was the championship series of the National Hockey League's (NHL) 2000–01 season, and the culmination of the 2001 Stanley Cup playoffs.  It was contested between the Eastern Conference champion and defending Stanley Cup champion New Jersey Devils and the Western Conference champion and Presidents' Trophy winning Colorado Avalanche.  It was Colorado's second appearance in the Final, and the first since the team won the Cup in 1996.  It was New Jersey's third appearance in the Final and second straight appearance after winning the Cup in the 2000 Final.  Colorado defeated New Jersey in seven games to win their second Stanley Cup in franchise history.  Colorado's Patrick Roy would win the Conn Smythe Trophy as the MVP of the 2001 Playoffs.  This was the first Stanley Cup Final since that would be decided in the maximum seven games.  This was also the first and, as of 2017, most recent Finals since that the number one seeds in each conference met.

2011–12 Vancouver Canucks season: The 2011–12 Vancouver Canucks season was the 42nd season in the modern Canucks history.  The Vancouver Canucks were the defending Western Conference champions and three time defending Northwest Division champions.  The Canucks opened the regular season against the Pittsburgh Penguins at home on October 6.  Their final regular season game was held at Rogers Arena against the Edmonton Oilers on April 7, 2012.  The Canucks entered the season expected to again contend for their first ever Stanley Cup.  The Canucks struggled out of the gate, hovering around .500 until roughly the 20 game mark due to weak defensive play and a slow start from Roberto Luongo.  The Canucks then rebounded, playing their best hockey of the season from the end of November until the beginning of January.  The team dominated much like they did the season prior during this stretch, as goals came in bunches and the offense was backed up by strong goaltending from the tandem of Luongo and Cory Schneider.  The peak of the Canucks' season came on January 7, 2012, in a game against the Boston Bruins, a 2011 Stanley Cup Final rematch.  The Canucks prevailed 4–3 in a hard-fought playoff atmosphere, and they seemed to state to the hockey world that they would be heard from again come playoff time.  The winning ways continued for the rest of the season, but the team did not play with the same heart they played with that January afternoon again.  The Canucks often played down to their competition, barely beating some of the weakest teams in the league as the offense seemed to disappear.  The Canucks pulled a shocking deal at the trade deadline, trading blue-chip prospect Cody Hodgson to the Buffalo Sabres for a skilled, but unproven prospect Zack Kassian.  While Kassian should eventually emerge as a solid NHLer, this deal was probably pulled too soon as the offensive mojo disappeared but the team was lucky to have outstanding goaltending that led them to their second consecutive Presidents' Trophy on the final day of the regular season when they defeated the Edmonton Oilers.  Despite entering the playoffs as the top seed, the Canucks were eliminated in the first round of the Stanley Cup Playoffs in five games by the Los Angeles Kings.

2014 Stanley Cup Finals: The 2014 Stanley Cup Finals was the championship series of the National Hockey League's (NHL)  season, and the culmination of the 2014 Stanley Cup playoffs.  The League realigned its divisions prior to the season, and changed the structure of the playoffs, but the championship series remained the same.  The Western Conference champion Los Angeles Kings defeated the Eastern Conference champion New York Rangers four games to one to win their second championship in franchise history, marking the first time since 2007 that the championship series was determined in fewer than six games.  Their Stanley Cup–winning run of 26 playoff games was the longest of any Stanley Cup–winning team in history.

1998 Stanley Cup Finals: The 1998 Stanley Cup Finals was the championship series of the National Hockey League's (NHL) 1997–1998 season, and the culmination of the 1998 Stanley Cup playoffs.  It was contested by the Western Conference champion and defending Stanley Cup champion Detroit Red Wings and the Eastern Conference champion Washington Capitals.  It was the 105th year of the Stanley Cup being contested.  The series was the Capitals' first appearance in a Stanley Cup Final since the franchise's inception in 1974.  The Red Wings won the series for the second year in a row, four games to none.  It was the Wings' ninth Stanley Cup, and the most recent time when a Finals concluded with a sweep (as of 2017).  This was also the last time until that a Stanley Cup Finals ended after an NBA Finals in the same season had concluded.  Detroit coach Scotty Bowman won his eighth Stanley Cup in that capacity (having previously done so with the Montreal Canadiens in , , , , and , the Pittsburgh Penguins in , and the Wings the previous year), tying him with former Canadiens coach Toe Blake for the record of most Cups won by a coach (which he would break when he helped the Red Wings win the 2002 Cup).

List of San Jose Sharks players: The San Jose Sharks are a professional ice hockey team based in San Jose, California, United States.  They are members of the Pacific Division of the Western Conference in the National Hockey League (NHL).  Founded in 1991 as an expansion team, the Sharks have won the Pacific Division six times: in 2002, 2004, 2008, 2009, 2010 and 2011, and have made the Stanley Cup playoffs in 18 of their 24 years in the League.  San Jose has not won a Stanley Cup championship to date; the Sharks' longest run in the playoffs came in 2016, when they defeated the St. Louis Blues in the Western Conference Finals to reach the 2016 Stanley Cup Finals.

1988 Stanley Cup playoffs: The 1988 Stanley Cup playoffs, the championship of the National Hockey League (NHL), began on April 6, after the conclusion of the 1987–88 NHL season.  It concluded on May 26, with the defending champion Edmonton Oilers defeating the Boston Bruins to win their second straight Stanley Cup and fourth in five years.

Question: The 1988 Stanley Cup playoffs were won by a team who play in what division of the Western Conference?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "playoff_year": {
      "type": "integer",
      "description": "The year the Stanley Cup playoffs concluded."
    },
    "winning_team": {
      "type": "string",
      "description": "The name of the team that won the Stanley Cup."
    },
    "team_conference": {
      "type": "string",
      "description": "The conference the winning team belongs to."
    },
    "team_division": {
      "type": "string",
      "description": "The division the winning team belongs to."
    }
  },
  "required": [
    "playoff_year",
    "winning_team",
    "team_conference",
    "team_division"
  ],
  "additionalProperties": false
}
