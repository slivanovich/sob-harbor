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
Danny Ings: Daniel William John Ings (born 23 July 1992) is an English professional footballer who plays as a forward for Premier League club Liverpool and the England national team.

Jon Flanagan: Jonathon Patrick Flanagan (born 1 January 1993) is an English professional footballer who plays as a full back for Premier League club Liverpool, and the England national team.  He made his debut for Liverpool in a 3–0 win against Manchester City on 11 April 2011 at age 18.

Daniel Sturridge: Daniel Andre Sturridge ( ; born 1 September 1989) is an English professional footballer who plays for Premier League club Liverpool and the England national team.  He plays as a striker, but he has also been used as a winger on occasion.

Trent Alexander-Arnold: Trent John Alexander-Arnold (born 7 October 1998) is an English professional footballer who plays as a right-back for Premier League club Liverpool.  He is an academy graduate of Liverpool and made his senior debut for the club in 2016, aged 18.  The following year, he won the club's Young Player of the Season award.  He has also represented England at all youth levels from under-16 through to under-19.  Due to the length of his name, his surname is shortened to Alexander for Premier League fixtures.

Alex Oxlade-Chamberlain: Alexander Mark David Oxlade-Chamberlain (born 15 August 1993) is an English professional footballer who plays as a midfielder for Premier League club Liverpool and the England national team.

Joe Hart: Charles Joseph John "Joe" Hart (born 19 April 1987) is an English professional footballer who plays as a goalkeeper for West Ham United, on loan from fellow Premier League club Manchester City, and the England national team.  With over 100 Premier League clean sheets, Hart holds the joint record for the most Premier League Golden Glove awards (four) and has amassed 73 international caps since his debut in 2008.

Nathaniel Clyne: Nathaniel Edwin Clyne (born 5 April 1991) is an English professional footballer who plays as a right back for Premier League club Liverpool and the England national team.

Jessica Clarke: Jessica Anne "Jess" Clarke (born 5 May 1989) is an English footballer who plays as a winger or forward for FA WSL club Liverpool and the England national team.  After beginning her career with hometown team Leeds United (known as Leeds Carnegie between 2008 and 2010), Clarke joined Lincoln Ladies in 2010 and remained with the club when it re-branded as Notts County four years later.  After six seasons at Notts County, Clarke signed for league rivals Liverpool in April 2017.  Since making her senior England debut in 2009, Clarke has won over 40 caps.  She has represented her country at two editions of the UEFA Women's Championship and at the 2011 FIFA Women's World Cup.

Jordan Henderson: Jordan Brian Henderson (born 17 June 1990) is an English professional footballer who captains Premier League club Liverpool and plays for the England national team.  He is usually deployed as a central midfielder for both club and country.

Jim Cassell: Jim Cassell is a former Youth Academy Director at Manchester City.  He has been responsible for the development of players such as Shaun Wright-Phillips, Joey Barton, Stephen Ireland, Nedum Onuoha, Daniel Sturridge, Michael Johnson and Micah Richards and many others.

Question: Which person Jim Cassell has been responsible for the development of plays for Premier League club Liverpool and the England national team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "developed_player": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the player developed by Jim Cassell."
        },
        "club": {
          "type": "string",
          "description": "The Premier League club the player plays for."
        },
        "national_team": {
          "type": "string",
          "description": "The national team the player represents."
        },
        "position": {
          "type": "string",
          "description": "The primary playing position of the player."
        }
      },
      "required": [
        "name",
        "club",
        "national_team",
        "position"
      ],
      "additionalProperties": false
    },
    "developer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person responsible for development."
        },
        "role": {
          "type": "string",
          "description": "The role of the developer."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "Describes the relationship between the developer and the player."
    }
  },
  "required": [
    "developed_player",
    "developer",
    "relationship_type"
  ],
  "additionalProperties": false
}
