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
Oberliga Baden-Württemberg: The Oberliga Baden-Württemberg is the highest association football league in the state of Baden-Württemberg and the Baden-Württemberg football league system.  It is one of fourteen Oberligas in German football, the fifth tier of the German football league system.  Until the introduction of the 3.  Liga in 2008 it was the fourth tier of the league system, until the introduction of the Regionalligas in 1994 the third tier.

List of Bristol Rovers F.C. players: Bristol Rovers Football Club is an English professional association football club based in Bristol, who play in Football League One, the Third tier of the English football league system, as of the 2016–17 season.  The club was formed in 1883 under the name Black Arabs F.C. playing their home games at Purdown in Bristol, but they used the name for only a single season, becoming Eastville Rovers and moving to a site known as Three Acres in 1884.  Eastville Rovers were somewhat nomadic, moving home in 1891 to the Schoolmaster's Cricket Ground, in 1892 to Durdham Down, and in 1894 to Ridgeway, before finally settling at Eastville Stadium and changing their name to Bristol Eastville Rovers in 1897.  Two years later they adopted their current name of Bristol Rovers when they became founder members of the Southern League.  They remained at Eastville Stadium for 99 years, before leaving in 1986 when financial pressures meant that they could no longer afford to pay the rent, whereupon they moved to Bath City's Twerton Park, a move that saved the club £30,000 a year.  After playing for ten years in Bath, the club returned to Bristol in 1997 when they agreed to share Bristol Rugby's Memorial Stadium.  Since joining The Football League in 1920, when the top division of the Southern League effectively became the Football League Third Division, Rovers have spent most of their time in the second and third tiers of the English football league system; the team has never played in the top flight and spent six years, 2001 to 2007, in the fourth tier.

Neuchâtel Xamax: After many financial crises, the club declared bankruptcy on 26 January 2012 and was consequently excluded from Swiss Super League.  The club was reformed, but had to restart in the Swiss amateur leagues, entering the 2.  Liga Interregional, the fifth tier of the Swiss football league system, for the 2012–13 season.  The club finished first in 2013 and was promoted to the 1.  Liga Classic for 2013–14.  Once again, Xamax finished first, winning the play-off to secure a second successive promotion.  Xamax won 1.  Liga Promotion, the third tier of Swiss league system and promoted to Challenge League after making third successive promotion in 2014–15 season.

Hessenliga: The Hessenliga (until 2008 "Oberliga Hessen") is the highest football league in the state of Hesse and the Hessian football league system.  It is one of fourteen Oberligas in German football, the fifth tier of the German football league system.  Until the introduction of the 3.  Liga in 2008 it was the fourth tier of the league system, until the introduction of the Regionalligas in 1994 the third tier.

List of clubs in the Bayernliga: This is a List of clubs in the Bayernliga, including all clubs and their final placings from 1945–46 to the current one.  The league, commonly referred to as the "Bayernliga", is the highest football league in the state of Bavaria (German: "Bayern" ) and the Bavarian football league system.  It is one of fourteen Oberligas in German football, the fifth tier of the German football league system.  Until the introduction of the 3.  Liga in 2008 it was the fourth tier of the league system, until the introduction of the Regionalligas in 1994 the third tier.

Bayernliga: The Bayernliga (English: Bavarian league) is the highest amateur football league and the second highest football league (under the Regionalliga Bayern) in the state of Bavaria (German: "Bayern" ) and the Bavarian football league system.  It is one of fourteen Oberligas in German football, the fifth tier of the German football league system.  Until the introduction of the 3.  Liga in 2008 it was the fourth tier of the league system, until the introduction of the Regionalligas in 1994 the third tier.

Swiss Promotion League: Promotion League is the third tier of the Swiss football league system, below the Swiss Challenge League and above the 1.  Liga Classic.  Introduced in 2012 the division has 16 teams.

Oberliga Rheinland-Pfalz/Saar: The Oberliga Rheinland-Pfalz/Saar, formerly the "Oberliga Südwest", is the highest regional football league for the Rhineland-Palatinate and Saarland states of Germany.  It is the fifth tier of the German football league system.  It is one of fourteen Oberligas in German football, the fifth tier of the German football league system.  Until the introduction of the 3.  Liga in 2008 it was the fourth tier of the league system, until the introduction of the Regionalligas in 1994 the third tier.

1993–94 Bayernliga: The 1993–94 season of the Bayernliga, the third tier of the German football league system in the state of Bavaria at the time, was the 49th season of the league.  It was the last season of the league at the third tier of the league system as, from 1994 onward, it slipped to the fourth tier because of the introduction of the Regionalliga as a new tier between 2.  Bundesliga and Oberliga.

Rinjala Raherinaivo: Rinjala Raherinaivo (born 25 May 1998) is a Malagasy international footballer who plays as a midfielder or forward for Swiss Promotion League side FC Sion and the Madagascar national football team.

Question: Which of the football league with which Rinjala Raherinaivo plays is the third tier of the Swiss football league system?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the football player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the player plays for."
    },
    "league_info": {
      "type": "object",
      "properties": {
        "league_name": {
          "type": "string",
          "description": "The name of the football league."
        },
        "national_system": {
          "type": "string",
          "description": "The national football league system this league belongs to."
        },
        "tier_level": {
          "type": "integer",
          "description": "The tier level of the league within its national system."
        },
        "is_third_tier": {
          "type": "boolean",
          "description": "Indicates if the league is the third tier of its national system."
        }
      },
      "required": [
        "league_name",
        "national_system",
        "tier_level",
        "is_third_tier"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "team_name",
    "league_info"
  ],
  "additionalProperties": false
}
