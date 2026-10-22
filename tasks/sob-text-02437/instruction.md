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
Spice Boys (footballers): The Spice Boys was a media pejorative used to described a group of high-profile Liverpool F.C. footballers in the mid-late 1990s, typically Jamie Redknapp, David James, Steve McManaman, Robbie Fowler and Jason McAteer, but occasionally team-mates such as Stan Collymore and Paul Ince.  The name was a play on the Spice Girls, who were extremely popular at the same time and famed for their 'Girl Power' persona.

Neutral zone trap: The neutral zone trap (often referred to as simply the trap) is a defensive strategy used in ice hockey to prevent an opposing team from proceeding through the neutral zone (the area between the blue lines) to force turnovers.  The strategy is generally used to level the playing field for teams that are not as offensively talented as their opponents, although the trap can also be used by teams simply looking to protect a lead late in the game.  The trap was innovated by the Toronto Maple Leafs in the 1920s and 1930s but became the defensive scheme for most coaches during the late 90s early 2000s—known as the "Dead Puck era"—as a direct result of the success seen by the New Jersey Devils under the coaching of Jacques Lemaire, who perfected the trap defense to 3 Stanley cups in 1995, 2000 , and 2003 for the New Jersey Devils.

Mykola Yurchenko: Mykola Mykolayovych Yurchenko (Ukrainian: Микола Миколайович Юрченко ; born 31 March 1966 in Ivano-Frankivsk) is the Soviet and Ukrainian professional footballer known for his performance in the Ukrainian club Prykarpattia Ivano-Frankivsk.  Mykola has an older brother Ihor Yurchenko whose name is also tightly intertwined with the fate of the western Ukrainian club.

Kevin Young (baseball): Kevin Stacey Young (born June 16, 1969) is a former professional baseball player.  He played twelve seasons in Major League Baseball for the Pittsburgh Pirates (1992–95, 1997–2003) and Kansas City Royals (1996), primarily as a first baseman.  He batted and threw right-handed.  As a union rep Young helped end the most recent baseball players strike in MLB along with resolving labor negotiations in the late 90's representing the Pittsburgh Pirates.

Alberto Malesani: Alberto Malesani (] ; born 5 June 1954) is an Italian association football manager and former footballer.  As a manager, he is mostly remembered for his successful spell with Parma during the late 90s, where he managed to win the Coppa Italia, the UEFA Cup, and the Supercoppa Italiana.

Juniper Shuey: Juniper Shuey (born 1974) is a Seattle-based visual artist, known for his video installations and sculptural performance.  He is the Co-Artistic Director of zoe|juniper and is the Head Carpenter at the University of Washington Meany Hall.  Since establishing himself in the late 90's he has continued to gain a professional reputation for his works.

Pete Yorn: Peter Joseph Yorn (born July 27, 1974) is an American singer, songwriter, and musician.  He first gained international recognition after his debut record, "Musicforthemorningafter", was released to critical and commercial acclaim in 2001.  He is known for playing the bulk of the instruments on his records and is often credited with helping to usher in the singer-songwriter resurgence of the late 90's and early 2000's.

Ihor Yurchenko: Ihor Mykolayovych Yurchenko (Ukrainian: Ігор Миколайович Юрченко ; born in 1960) is the Soviet and Ukrainian professional footballer known for his performance in the Ukrainian club Prykarpattia Ivano-Frankivsk.  Ihor has a younger brother Mykola Yurchenko whose name is also tightly intertwined with the fate of the western Ukrainian club.

The Billy's: The Billy's are an American rock band from the Twin Cities.  They recorded 3 studio albums in the mid to late 90's which were released by the OarFin Records label.  Their sound generally falling under the Alternative country label, they were often compared to the Gear Daddies.  The band built a sizable following, particularly in the Mid-West.  In addition to their own material, live shows were well known for wide ranging covers.

Robbie Fowler: Robert Bernard Fowler (born 9 April 1975) is an English former professional footballer and manager who played as a striker from 1993 to 2012.  Fowler was known for being a natural scorer with an instinctive goal-poaching ability.

Question: What former professional footballer known for his goal-poaching abilities was often described as a Spice Boy in the late 90s?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "footballer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the professional footballer."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the footballer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the footballer."
        },
        "primary_position": {
          "type": "string",
          "description": "The primary playing position of the footballer."
        },
        "notable_skill_description": {
          "type": "string",
          "description": "A description of the footballer's notable skill or ability."
        }
      },
      "required": [
        "name",
        "birth_year",
        "nationality",
        "primary_position",
        "notable_skill_description"
      ],
      "additionalProperties": false
    },
    "group_association": {
      "type": "object",
      "properties": {
        "group_name": {
          "type": "string",
          "description": "The name of the group the footballer was associated with."
        },
        "group_type": {
          "type": "string",
          "description": "The type or nature of the group (e.g., media pejorative)."
        },
        "association_period": {
          "type": "string",
          "description": "The time period during which the association occurred."
        }
      },
      "required": [
        "group_name",
        "group_type",
        "association_period"
      ],
      "additionalProperties": false
    },
    "answer_summary": {
      "type": "string",
      "description": "A concise summary of the answer."
    }
  },
  "required": [
    "footballer_details",
    "group_association",
    "answer_summary"
  ],
  "additionalProperties": false
}
