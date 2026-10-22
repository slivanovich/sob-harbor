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
UEFA Men's Player of the Year Award: The UEFA Men's Player of the Year Award (previously known as the UEFA Best Player in Europe Award) is an association football award given to the footballer playing for a football club in Europe that is considered the best in the previous season.  The award, created in 2011 by UEFA, is aimed at reviving the European Footballer of the Year Award (Ballon d'Or), which was merged with the FIFA World Player of the Year Award in 2010 to become the FIFA Ballon d'Or.  It also replaced the UEFA Club Footballer of the Year award.

PFA Scotland Players' Player of the Year: The Professional Footballers' Association Scotland Players' Player of the Year (often called the PFA Scotland Players' Player of the Year, the Players' Player of the Year, or simply the Scottish Player of the Year) is an annual award given to the player who is adjudged to have been the best of the season in Scottish football.  The award has been presented since the 1977–78 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association Scotland (PFA Scotland).  The award was formerly known as the Scottish Professional Footballers' Association Players' Player of the Year, but was renamed after the SPFA merged with the (English) Professional Footballers' Association to become PFA Scotland.

Colin Todd: Colin Todd (born 12 December 1948) is an English football manager and former player.  He was most recently the manager of Esbjerg fB.  As a player, he made more than 600 appearances in the Football League, playing for Sunderland, Derby County, Everton, Birmingham City, Nottingham Forest, Oxford United and Luton Town, and also played in the North American Soccer League for the Vancouver Whitecaps.  He won two Football League titles with Derby County during the 1970s, and won the PFA Players' Player of the Year award in 1975.  He was capped by England on 27 occasions.

PFA Young Player of the Year: The Professional Footballers' Association Young Player of the Year (often called the PFA Young Player of the Year, or simply the Young Player of the Year) is an annual award given to the player aged 23 or under at the start of the season who is adjudged to have been the best of the season in English football.  The award has been presented since the 1973–74 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).  The first winner of the award was Ipswich Town defender Kevin Beattie.  The current holder is Dele Alli, who won the award for his performances throughout the 2016–17 campaign for Tottenham Hotspur.

N'Golo Kanté: N'Golo Kanté (] ; born 29 March 1991) is a French professional footballer who plays as a defensive midfielder for English club Chelsea and the France national team.

Alan Shearer: Alan Shearer, CBE, DL ( ; born 13 August 1970) is a retired English footballer.  He played as a striker in the top level of English league football for Southampton, Blackburn Rovers, Newcastle United and the England national team.  He is Newcastle's and the Premier League's record goalscorer.  He was named Football Writers' Association Player of the Year in 1994 and won the PFA Player of the Year award in 1995.  In 1996, he was third in the FIFA World Player of the Year awards.  In 2004 Shearer was named by Pelé in the FIFA 100 list of the world's greatest living players.

Rex Kingsley Footballer of the Year: The Rex Kingsley Footballer of the Year was an award given annually to the Scottish footballer who was adjudged to have been the best of that year (calendar year and not season) in Scottish football between 1951–1964.  The award was handed out by Rex Kingsley of the "Sunday Mail".  As there were no Football Writers' awards (until the SWFA awards in 1965) or Players' Association awards (until the PFA Scotland awards in 1978), the Rex Kingsley Footballer of the Year award was generally considered to be the most prestigious of its type at the time.

Hedvig Lindahl: Rut Hedvig Lindahl (born 29 April 1983) is a Swedish professional football goalkeeper who plays for Chelsea Ladies.  She previously played club football in Sweden for Damallsvenskan clubs including Malmö FF, Linköpings FC, Kristianstads DFF and Kopparbergs/Göteborg FC.  Since making her international debut in 2002, Lindahl has accrued over 115 caps for the Sweden women's national football team.  On 3 August 2014 Lindahl played her 100th cap for Sweden women's national football team against England.  On 17 September 2015 Lindahl played her 113th cap and thereby broke Elisabeth Leidinge's record to become the most capped Swedish female goalkeeper.  She has kept goal for Sweden at the UEFA Women's Championship, the FIFA Women's World Cup and the Olympic Games.  Lindahl was the Swedish women's goalkeeper of the year in 2004, 2005, 2009, 2014 and 2015.  She won the 2015 Diamantbollen, after being one of three nominations for Damallsvenskan's Most Valuable Player in 2014.  In 2016, Lindahl was one of 5 nominees for Women's PFA Players' Player of the Year and was also picked for the WSL Team of the Year.

Wilson Defensive Player of the Year Award: The Wilson Defensive Player of the Year Award is awarded annually to the best defensive player at each fielding position in Major League Baseball.  One overall Defensive Player of the Year is also selected each year.  Unlike the Rawlings Gold Glove Awards, which are voted on by major league managers and coaches, the Wilson Defensive Player of the Year Award winners are determined by statistics using sabermetrics.  In 2012, the baseball glove manufacturer Wilson created the Defensive Player of the Year Award to honor the best defensive player on each team in Major League Baseball.  One award winner was selected from each league as that league's overall Defensive Player of the Year.  Starting in 2014, the awards are given to the best defensive player at each position, regardless of league, and the overall award is given to only one player, regardless of league.  Also in 2014, a new award was created for the best Defensive Team of the Year, regardless of league.

PFA Players' Player of the Year: The Professional Footballers' Association Players' Player of the Year (often called the PFA Players' Player of the Year, the Players' Player of the Year, or simply the Player of the Year) is an annual award given to the player who is adjudged to have been the best of the year in English football.  The award has been presented since the 1973–74 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).  The current holder is N'Golo Kanté, who won the award on 23 April 2017 for his displays throughout the 2016–17 season, representing Chelsea.

Question: What is the position of the footballer that won the PFA Players' Player of the Year award in 2017?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_name": {
      "type": "string",
      "description": "The name of the award."
    },
    "award_year": {
      "type": "integer",
      "description": "The year the award was won."
    },
    "winner_details": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The name of the player who won the award."
        },
        "player_position": {
          "type": "string",
          "description": "The playing position of the award winner."
        },
        "club": {
          "type": "string",
          "description": "The club the player represented when winning the award."
        }
      },
      "required": [
        "player_name",
        "player_position",
        "club"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "award_name",
    "award_year",
    "winner_details"
  ],
  "additionalProperties": false
}
