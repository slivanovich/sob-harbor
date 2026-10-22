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
Jon Patricof: Jon Patricof (born 1973) is an American businessman and current president of New York City FC.  Before joining New York City FC, Patricof was President and Chief Operating Officer of Tribeca Enterprises which oversees the popular Tribeca Film Festival, Tribeca Film, and Tribeca Cinemas.

New York City FC Stadium: The New York City FC Stadium is a proposed soccer-specific stadium to be built in New York City for the expansion franchise New York City FC of Major League Soccer.  The team currently plays their home games at Yankee Stadium.

2015 New York City FC season: The 2015 New York City FC season is the club's first season of existence, their first season in the top tier of American soccer, and their first season in Major League Soccer.  New York City FC plays their home games at Yankee Stadium in the New York City borough of The Bronx.

Patrick Vieira: Patrick Vieira (born 23 June 1976) is a former footballer and current head coach of New York City FC.  A former midfielder, Vieira began his career with French club Cannes in 1994.  He moved to Italian side Milan the following season, but was unable to break into the starting line-up, and was subsequently sold.  He rose to prominence during a hugely successful spell at Arsenal from 1996 to 2005, where he eventually became club captain, and won three Premier League titles – one unbeaten – and four FA Cups.  He transferred from Arsenal in 2005 and spent one season at Juventus, helping the team to the Serie A championship.  Following Juventus' relegation for their part in a match-fixing scandal, Vieira moved to Internazionale and won three Serie A titles, before moving to Manchester City for two seasons, where he retired in 2011 after adding another FA Cup winners' medal to his personal honours.

An Sung-hun: An Sung-hun (; born 11 September 1982) is a South Korean footballer who played as a Midfielder for FC Seoul (then known as Anyang LG Cheetahs) and Incheon United in the K League.  When he was in FC Seoul, He appeared on friendly match with France national football team during 2002 FIFA World Cup in GS Champions Park (France team training camp).  He was played as temporary France national team player for Patrick Vieira.

Sports in New York (state): New York has two Major League Baseball teams, the New York Yankees (based in the Bronx) and the New York Mets (based in Queens).  New York is home to three National Hockey League franchises: the New York Rangers in Manhattan, the New York Islanders in Brooklyn and the Buffalo Sabres in Buffalo.  New York has two National Basketball Association teams, the New York Knicks in Manhattan, and the Brooklyn Nets in Brooklyn.  New York has one Major League Soccer team: New York City FC.  Although the New York Red Bulls represent the New York metropolitan area they play in Red Bull Arena, located in Harrison, New Jersey.

2016 New York City FC season: The 2016 New York City FC season is the club's second season of competition and their second in the top tier of American soccer, Major League Soccer.  New York City FC plays their home games at Yankee Stadium in the New York City borough of The Bronx.

Win!: Win!  is an all-access, vérité film about a former player turned sporting director, a coach and a team of diverse football players given the mission to create a professional soccer team from scratch in New York City.  Manchester City FC, an English club with ambitions to spread a style of “beautiful” football around the globe, joined up with the New York Yankees and handed the job of Sporting Director of New York City FC to Claudio Reyna, former captain of the US National team.  When Reyna selected Jason Kreis as the team’s first coach, a race began to find players in the months before the inaugural season.  Global soccer stars like David Villa and Frank Lampard join a growing squad of American rising stars, to face the highs and lows, joys and sacrifices, disappointments and triumphs of the first season.  Playing in front of their home fans in Yankee Stadium, at a time when soccer has never been more popular in the US, they fight to win the hearts of New Yorkers.

City FC: City FC or just City is usually used as short-hand to refer to one of Manchester City F.C., New York City FC or Melbourne City FC, which are all association football clubs owned by the City Football Group, an organisation which bases it's identity around the cognomen "City".

2017 New York City FC season: The 2017 New York City FC season is the club's third season of competition and their third in the top tier of American soccer, Major League Soccer.  New York City FC plays their home games at Yankee Stadium in the New York City borough of The Bronx.

Question: For what current head coach of New York City FC did An Sung-hun play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the coach."
        },
        "current_role": {
          "type": "string",
          "description": "The current role of the coach."
        },
        "current_team": {
          "type": "string",
          "description": "The team the coach currently manages."
        }
      },
      "required": [
        "name",
        "current_role",
        "current_team"
      ],
      "additionalProperties": false
    },
    "player_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the player."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "playing_interaction": {
      "type": "object",
      "properties": {
        "played_for_coach": {
          "type": "boolean",
          "description": "Indicates if the player played for the specified coach."
        },
        "capacity": {
          "type": "string",
          "description": "The capacity in which the player played for the coach."
        },
        "team_played_for": {
          "type": "string",
          "description": "The team for which the player played for the coach."
        }
      },
      "required": [
        "played_for_coach",
        "capacity",
        "team_played_for"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_details",
    "player_details",
    "playing_interaction"
  ],
  "additionalProperties": false
}
