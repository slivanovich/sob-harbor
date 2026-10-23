{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMark McNeill: Mark McNeill (born February 22, 1993) a Canadian ice hockey player who is currently playing for the Texas Stars of the American Hockey League as a prospect for the Dallas Stars of the National Hockey League.  He was selected 18th overall in the 2011 NHL Entry Draft by the Chicago Blackhawks, and he was also selected by Vityaz Chekhov in the fifth round (112th overall) of the 2011 KHL Junior Draft.\n\nAlex Stalock: Alexander Dezmund \"Alex\" Stalock (born July 28, 1987) is an American professional ice hockey goaltender currently playing for the Minnesota Wild in the National Hockey League (NHL).  Stalock was originally drafted 112th overall in the 2005 NHL Entry Draft by the San Jose Sharks.\n\nMatt Pelech: Matt Pelech (born September 4, 1987) is a Canadian professional ice hockey forward who is currently playing for ERC Ingolstadt in the Deutsche Eishockey Liga (DEL).  He formerly played with the Calgary Flames and the San Jose Sharks of the National Hockey League (NHL).  Pelech was a draft pick of the Flames, selected in the first round, 26th overall in the 2005 NHL Entry Draft and made his NHL debut in 2009 as a defenceman with the Flames.  He has since switched to right wing and become known as an enforcer.  His brother, Michael Pelech, also plays professionally.\n\nRyan Duthie: Ryan Duthie (born September 2, 1974) is a Canadian former professional ice hockey player.  He was twice selected in the NHL Entry Draft.  At the 1992 NHL Entry Draft he was selected 105th overall by the New York Islanders, and at the 1994 NHL Entry Draft he was selected 91st overall by the Calgary Flames.\n\nAnže Kopitar: Anže Kopitar (] ) (born 24 August 1987) is a Slovenian professional ice hockey centre currently serving as captain of the Los Angeles Kings of the National Hockey League (NHL).  The 11th overall pick in the 2005 NHL Entry Draft, Kopitar became the first Slovenian to play in the NHL upon making his debut in 2006.  Kopitar has spent his entire NHL career with the Kings, leading them in scoring every year except his rookie season.  Following the 2015–16 season, he was named the Kings' captain.  Noted for both his offensive and defensive play, Kopitar was awarded the Frank J. Selke Trophy as the best defensive forward in the NHL in 2016, as well as the Lady Byng Memorial Trophy for gentlemanly play the same year.\n\nAdam Wilcox (ice hockey): Adam Wilcox (born November 26, 1992) is an American professional ice hockey goaltender.  He is currently playing under contract to the Buffalo Sabres of the National Hockey League (NHL).  He was selected by the Lightning in the 6th round (178th overall) of the 2011 NHL Entry Draft.  Wilcox is cousins with Minnesota Wild goaltender, Alex Stalock.  Both Wilcox and Stalock played goaltender for the same high school, South St. Paul.\n\nT. J. Oshie: Timothy Leif \"T. J.\" Oshie (born December 23, 1986) is an American professional ice hockey right winger for the Washington Capitals of the National Hockey League (NHL).  He was selected by the St. Louis Blues in the first round of the 2005 NHL Entry Draft, as the 24th overall pick.  He attended Everett High School before transferring after his freshman year.  He then spent the first seven years of his NHL career with the St. Louis Blues before being traded to the Washington Capitals in 2015.\n\n2000 NHL Entry Draft: The 2000 NHL Entry Draft was held from June 24 to 25 at the Pengrowth (now Scotiabank) Saddledome in Calgary, Alberta, following the 2000 NHL Expansion Draft on June 23 for the Columbus Blue Jackets and Minnesota Wild.  This was the second NHL Entry Draft in which a goaltender was taken first overall (at that point), when the New York Islanders selected Rick DiPietro with the first overall pick.  Previously, Michel Plasse was selected 1st overall in the 1968 NHL Amateur Draft.\n\n2008 NHL Entry Draft: The 2008 NHL Entry Draft was the 46th NHL Entry Draft.  It was hosted by the Ottawa Senators at Scotiabank Place in the city of Ottawa, Ontario, Canada, on June 20–21, 2008.  The Senators were originally awarded the 2005 NHL Entry Draft, but because of the lockout, that draft was scaled back significantly from its usual format of being open to the public and having many draft-eligible players in attendance.  The actual 2005 drafting was held in Ottawa's Westin Hotel instead of the Corel Centre, as Canadian Tire Centre was then known.  As a result of 2005's abridged draft, Ottawa was compensated with the 2008 draft.\n\nPaul Houck: Paul Houck (born August 12, 1963 in Vancouver, British Columbia) is a former ice hockey player.  He had a successful college career with the University of Wisconsin between 1981 and 1985, and was named a Western Collegiate Hockey Association Second Team All-Star in 1983, as well as earning a spot on the National Collegiate Athletic Association Championship All-Tournament team.  He was selected 71st overall by the Edmonton Oilers in the 1981 NHL Entry Draft, and traded to the Minnesota North Stars in 1985.  Houck played 16 National Hockey League games for the North Stars between 1985 and 1988, scoring one goal and two assists while spending most of his career in the minor leagues.  He played two seasons in the Nederlands between 1989 and 1991 before retiring.  His son, Jackson Houck, was drafted 94th overall by the Edmonton Oilers in the 2013 NHL Entry Draft.  Paul, of the 1981 NHL Entry Draft, and his son, of the 2013 NHL Entry Draft, become the first father-and-son tandem drafted by the Edmonton Oilers in the team's history.\n\nQuestion: Adam Wilcox is cousins with which 112th overall pick in the 2005 NHL Entry Draft?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the ice hockey player.\"\n    },\n    \"relationship_to_adam_wilcox\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the player to Adam Wilcox.\"\n    },\n    \"draft_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"draft_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year of the NHL Entry Draft.\"\n        },\n        \"overall_pick_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The overall pick number in the draft.\"\n        },\n        \"drafting_team\": {\n          \"type\": \"string\",\n          \"description\": \"The team that drafted the player.\"\n        }\n      },\n      \"required\": [\n        \"draft_year\",\n        \"overall_pick_number\",\n        \"drafting_team\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"relationship_to_adam_wilcox\",\n    \"draft_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the ice hockey player."
      },
      "relationship_to_adam_wilcox": {
        "type": "string",
        "description": "The relationship of the player to Adam Wilcox."
      },
      "draft_information": {
        "type": "object",
        "properties": {
          "draft_year": {
            "type": "integer",
            "description": "The year of the NHL Entry Draft."
          },
          "overall_pick_number": {
            "type": "integer",
            "description": "The overall pick number in the draft."
          },
          "drafting_team": {
            "type": "string",
            "description": "The team that drafted the player."
          }
        },
        "required": [
          "draft_year",
          "overall_pick_number",
          "drafting_team"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "relationship_to_adam_wilcox",
      "draft_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
