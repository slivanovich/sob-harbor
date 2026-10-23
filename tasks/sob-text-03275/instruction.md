{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCharlie McCarthy (Gaelic footballer): Charlie McCarthy (born in Gneeveguilla, County Kerry, Ireland) played Gaelic football with his local club Gneeveguilla.  At the age of 19 he was a member of the Kerry senior inter-county team during the 1996 Championship campaign.  That year Kerry won their first Munster Championship since 1991.  McCarthy was part of the Kerry team that won the 1995 and 1996 All Ireland Under 21 titles.  He also won an All Ireland Minor Medal with Kerry in 1994, the last time Kerry won the All Ireland minor competition.  McCarthy played centre back and won the “man of the match award” in that game.  He won three consecutive Kerry Senior County Championship medals with East Kerry in 1997, 1998 and 1999.\n\nSteve McCarthy (ice hockey): Steve McCarthy (born February 3, 1981) is a Canadian former professional ice hockey defenceman.  McCarthy played in the National Hockey League with the Chicago Blackhawks, Vancouver Canucks and the Atlanta Thrashers.\n\nJoe McCarthy (catcher): Joseph Nicodemus McCarthy (December 25, 1881 – January 12, 1937) was a Major League Baseball catcher.  McCarthy played for the New York Highlanders in and the St. Louis Cardinals in .  In 16 career games, he had 9 hits in 39 at-bats.  He batted and threw right-handed.\n\nRichard D. McCarthy: Richard Dean McCarthy (September 24, 1927 in Buffalo, Erie County, New York – May 5, 1995 in Arlington County, Virginia) was a Democratic member of the United States House of Representatives from New York, also known as Richard Max McCarthy or Max McCarthy.\n\nSandy McCarthy: Sandy McCarthy was selected by the Calgary Flames in the third round (52nd overall) of the 1991 NHL Entry Draft.  He began playing hockey in the Georgian Bay Junior C Hockey League with the Midland Centennials and the Central Junior A Hockey League for the Hawkesbury Hawks.  As a power forward, McCarthy played for the QMJHL Laval Titan in the 1989–90 season before being drafted by the Calgary Flames.  He played one last season with the Titan.  His next stop was during the 1992–93 season for the IHL's Salt Lake Golden Eagles.  Sandy throughout his career with the Flames played the role as the enforcer, with many major fights.\n\nBob McCarthy (footballer): Robert Zepp \"Bob\" McCarthy (born 21 November 1948) is an English retired footballer.  Originally from Lyndhurst, Hampshire, McCarthy played the majority of his professional career with Football League club Southampton, before finishing his short career with brief spells at Poole Town, Cowes Sports, and Andover.  McCarthy played primarily as a right-back.\n\nBilly Elliot: Billy Elliot is a 2000 British dance drama film about a boy becoming a professional ballet dancer, set in north-eastern England during the 1984–85 coal miners' strike.  It was produced by Greg Brenman and Jon Finn, music composed by Stephen Warbeck, co-produced by BBC Films, Tiger Aspect Pictures and Working Title Films, distributed by Universal Pictures and Focus Features, written by Lee Hall and directed by Stephen Daldry.\n\nBrendan McCarthy (American football): Brendan B. McCarthy (born August 6, 1945 – August 26, 1997) was an American football running back in the National Football League and American Football League.  He was drafted by the Green Bay Packers in the fourth round of the 1968 Common Draft.  In August of that year he was traded to the Detroit Lions for undisclosed future draft pick.  McCarthy then moved on to the Atlanta Falcons, where he played in 7 games before being released by coach Norm Van Brocklin.  McCarthy played 9 games over two seasons with the Denver Broncos before eventually moving on to real estate.\n\nShawn McCarthy: Shawn Michael McCarthy (born February 22, 1968) is a former American football punter in the National Football League.  He was drafted by the Atlanta Falcons in the 12th round of the 1990 NFL Draft and later played for the New England Patriots.  McCarthy played college football at Purdue, where he was also a quarterback.  He attended Fremont Ross High School and was the football teams' starting quarterback, punter and placekicker.\n\nDean McCarthy (actor): Dean McCarthy (born 25 January 1992) is an Irish actor, dancer and model best known for his performance as Billy in \"Billy Elliot the Musical\", based on the film \"Billy Elliot\".\n\nQuestion: Dean McCarthy played a boy becoming what in an adaptation of Billy Elliott? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"role_played\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"production_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of production (e.g., musical, film).\"\n    },\n    \"character_aspiration\": {\n      \"type\": \"string\",\n      \"description\": \"What the character was aspiring to become.\"\n    },\n    \"original_work_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the original work the adaptation is based on.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_played\",\n    \"production_type\",\n    \"character_aspiration\",\n    \"original_work_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "role_played": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "production_type": {
        "type": "string",
        "description": "The type of production (e.g., musical, film)."
      },
      "character_aspiration": {
        "type": "string",
        "description": "What the character was aspiring to become."
      },
      "original_work_title": {
        "type": "string",
        "description": "The title of the original work the adaptation is based on."
      }
    },
    "required": [
      "actor_name",
      "role_played",
      "production_type",
      "character_aspiration",
      "original_work_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
