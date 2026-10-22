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
PFAI Young Player of the Year: The Professional Footballers' Association of Ireland Players' Young Player of the Year (often called the PFAI Players' Young Player of the Year, the PFAI Young Player of the Year, or simply the Young Player of the Year) award is given to the footballer in the top-flight of Irish football, the League of Ireland, who is seen to have been the best player of the previous season and is under 23 years of age.

Ligue 1 Young player of the year: The Ligue 1 Young Player of the Year is an award given to the player aged 23 years or under at the start of the season whose performances are considered to be the best, playing in Ligue 1.  The award has been presented since the 1993–94 season and the first winner of the award was Bordeaux midfielder Zinedine Zidane.  The current holder is Ousmane Dembélé, who won the award for his performances throughout the 2015–16 campaign for Rennes scoring 12 goals and assisting 5.  Eden Hazard is the only player to have won this award twice

Ousmane Dembélé: Ousmane Dembélé (born 15 May 1997) is a French professional footballer who plays as a forward for Spanish club FC Barcelona and the France national team.

Ligue 2: Ligue 2 (] ), also known as Domino's Ligue 2 due to sponsorship by Domino's Pizza, is a French professional football league.  The league serves as the second division of French football and is one of two divisions making up the Ligue de Football Professionnel (LFP), the other being Ligue 1, the country's top football division.  Contested by 20 clubs, it operates on a system of promotion and relegation with both Ligue 1 and the third division Championnat National.  Seasons run from August to May, with teams playing 38 games each totaling 380 games in the season.  Most games are played on Fridays and Mondays, with a few games played during weekday and weekend evenings.  Play is regularly suspended the last weekend before Christmas for two weeks before returning in the second week of January.

PFA Young Player of the Year: The Professional Footballers' Association Young Player of the Year (often called the PFA Young Player of the Year, or simply the Young Player of the Year) is an annual award given to the player aged 23 or under at the start of the season who is adjudged to have been the best of the season in English football.  The award has been presented since the 1973–74 season and the winner is chosen by a vote amongst the members of the players' trade union, the Professional Footballers' Association (PFA).  The first winner of the award was Ipswich Town defender Kevin Beattie.  The current holder is Dele Alli, who won the award for his performances throughout the 2016–17 campaign for Tottenham Hotspur.

2009–10 Ligue 1: The 2009–10 Ligue 1 season was the 72nd since its establishment.  Bordeaux were the defending champions.  The fixtures were announced on 5 June 2009, and play commenced on 8 August and ended on 15 May 2010.  There were three promoted teams from Ligue 2, replacing the three teams that were relegated from Ligue 1 following the 2008–09 season.  A total of 20 teams competed in the league with three clubs suffering relegation to the second division, Ligue 2.  All clubs that secured Ligue 1 status for this season were subject to approval by the DNCG before becoming eligible to participate.  In addition, German sportswear company Puma became the official provider of match balls for the season after agreeing to a long term partnership with the Ligue de Football Professionnel.

SFWA Young Player of the Year: The Scottish Football Writers' Association Young Player of the Year (often called the SFWA Young Player of the Year, or simply the Scottish Young Player of the Year) award is given to the footballer in the Scottish football league system, who is seen to have been the best young (under 23) player of the previous season.  The shortlist is compiled by the members of the Scottish Football Writers' Association (the SFWA), who also vote for the winner.  The prize is seen as the highest awarded to a young player as it names the "Young Player of the Year"; the footballer who is seen to have been "the" best young player over the previous season.  The award was first made in 2002, and was won by Motherwell forward James McFadden.

Ligue 1 Player of the Year: The Ligue 1 Player of the Year, is an award given to the player whose performances are considered to be the best, playing in Ligue 1.  The award has been presented since the 1993–94 season and the first winner of the award was Paris Saint-Germain Winger David Ginola.  The current holder is Edinson Cavani, who won the award for his performances throughout the 2016–17 campaign for Paris Saint-Germain scoring 35 goals.

Vietnamese Golden Ball: Vietnamese Golden Ball (Vietnamese: Quả bóng vàng Việt Nam ) also referred to as "Vietnamese Footballer of the Year", is an annual association football award for the best performances of Vietnamese footballer over the previous year.  Presented since 1995 by Sài Gòn Giải Phóng Newspaper.  The first winner was striker Le Huynh Duc.  Since 2001, It also awards Young Player of the Year, Best Woman Player of the year and Best Foreign Player of the year.  The current holder of the award, as selected in 2016, is Hà Nội T&T's midfielder Phạm Thành Lương.

List of Ligue 1 players: This is a "'list of Ligue 1 players" who have made 300 or more appearances in Ligue 1.  Current Ligue 1 players are shown in bold

Question: What position does the current holder of the Ligue 1 Young player of the year play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_name": {
      "type": "string",
      "description": "The name of the young player award."
    },
    "current_holder": {
      "type": "string",
      "description": "The name of the player who currently holds the award."
    },
    "holder_details": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The name of the player."
        },
        "playing_position": {
          "type": "string",
          "description": "The primary playing position of the player."
        },
        "award_season": {
          "type": "string",
          "description": "The season for which the player won the award."
        },
        "club_at_award": {
          "type": "string",
          "description": "The club the player was playing for when they won the award."
        }
      },
      "required": [
        "player_name",
        "playing_position",
        "award_season",
        "club_at_award"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "award_name",
    "current_holder",
    "holder_details"
  ],
  "additionalProperties": false
}
