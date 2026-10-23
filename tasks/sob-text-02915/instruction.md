{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1997 Asia Cup: The 1997 Asia Cup (also known as the Pepsi Asia Cup 1997), was the sixth Asia Cup tournament, and the second to be held in Sri Lanka.  The tournament took place between July 14–26, 1997.  Four teams took part in the tournament: India, Pakistan, Sri Lanka and Bangladesh.\n\n1988 Asia Cup: The 1988 Asia Cup (also known as the Wills Asia Cup) was the third Asia Cup tournament, held in Bangladesh between 26 October and 4 November 1988.  Four teams took part in the tournament: India, Pakistan, Sri Lanka and the host nation Bangladesh.  The matches were the first-ever List A-classified being played in Bangladesh, then an Associate Member of the International Cricket Council (ICC), their opponents all being Full Members.\n\nMalaysia National Hockey Stadium: Malaysia National Hockey Stadium is a multi-use stadium in National Sports Complex, Kuala Lumpur, Malaysia.  It is currently used mostly for the Malaysia national field hockey team and the Malaysia women's national field hockey team.  It was also used for the field hockey matches of national team and hosted matches for the 2002 Men's Hockey World Cup, 1999 Hockey Asia Cup, 2003 Hockey Asia Cup, 1982 Hockey Junior World Cup, 2000 Hockey Junior Asia Cup and 1998 Commonwealth Games.  The main stadium holds up to 12,000 people and was built in 1997.  There is a second pitch located adjacent to the stadium, which is used to hold smaller capacity and practice matches.\n\n2008 Asia Cup: The 2008 Asia Cup (also called STAR Cricket Asia Cup) took place in Pakistan in June 2008.  The six teams which took part in the tournament were India, Pakistan, Sri Lanka, Bangladesh and Asian associate nations UAE and Hong Kong.  This was the first Asia Cup hosted by Pakistan; previously political tensions between India and Pakistan did not permit Pakistan to host the event in 1993.  It was broadcast in India by Star Cricket and ESPN and in Pakistan by Geo Super.  Sri Lanka won the final against India by 100 runs.\n\n1995 Asia Cup: The 1995 Asia Cup (also known as the Pepsi Asia Cup), was the fifth Asia Cup tournament, and the second to be held in Sharjah, UAE.  The tournament took place between April 5–13, 1995.  Four teams took part in the tournament: India, Pakistan, Sri Lanka and Bangladesh.\n\n1986 Asia Cup: The 1986 Asia Cup (also known as the John Player Gold Leaf Trophy), was the second Asia Cup tournament, and was held in Sri Lanka between March 30 and April 6.  Three teams took part in the tournament: Pakistan, Sri Lanka and Asian leading associate member Bangladesh.  India pulled out of the tournament due to strained cricketing relations with Sri Lanka and was replaced by Asian leading associate nation Bangladesh, which had qualified by winning the 1984 South-East Asia Cup.\n\nGeo Super: Geo Super is the first 24-hour Dubai based Pakistani channel dedicated to the world of sports.  It belongs to Independent Media Corporation, owner of the Jang Group of Newspapers.\n\n2012 FIBA Asia Cup: 2012 FIBA Asia Cup was the 4th FIBA Asia Cup, the basketball tournament of FIBA Asia was held at the Ota Gymnasium, in Ota, Tokyo, Japan from September 14–22, 2012.  The winner of this year's FIBA Asia Cup automatically qualifies for the FIBA Asia Championship in 2013.\n\n2014 Asia Cup: The 2014 Asia Cup (also known as Arise Asia Cup) was the twelfth edition of the Asia Cup cricket tournament.  The tournament was held in Bangladesh from 25 February to 8 March 2014.  Pakistan were the defending champions, having won the previous tournament.  The tournament included the four Asian test-playing nations, Bangladesh, India, Pakistan and Sri Lanka; and ICC Asian Associate member Afghanistan.  This was the first 50-over tournament in which Afghanistan took part.  Ten league matches were played along with the final.  The title sponsors of the tournament were Arise India and it was powered by Cycle Agarbathis.  Sri Lanka Beat Pakistan in the final to become Asia Cup champions for the fifth time.\n\n2010 Asia Cup: The 2010 Asia Cup (also known as Micromax Asia Cup) was the tenth edition of the Asia Cup cricket tournament, which was held in Sri Lanka from 15–24 June 2010.  Only the test playing nations India, Pakistan, Sri Lanka and Bangladesh were taking part in the competition.  India defeated Sri Lanka by 81 runs in the final to win a record 5th Asia Cup title.  Pakistani captain, Shahid Afridi was declared the man of the tournament for scoring the most runs in the tournament, 265, with an average of 88.33 and a strike rate of 164.59.\n\nQuestion: The 2008 Asia Cup was broadcast on a Pakistani channel owned by what corporation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"tournament_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Asia Cup tournament.\"\n    },\n    \"broadcast_channel\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Pakistani channel that broadcasted the tournament.\"\n    },\n    \"channel_owner_corporation\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the corporation that owns the broadcast channel.\"\n    },\n    \"owner_additional_info\": {\n      \"type\": \"string\",\n      \"description\": \"Additional information about the owner corporation.\"\n    }\n  },\n  \"required\": [\n    \"tournament_name\",\n    \"broadcast_channel\",\n    \"channel_owner_corporation\",\n    \"owner_additional_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "tournament_name": {
        "type": "string",
        "description": "The name of the Asia Cup tournament."
      },
      "broadcast_channel": {
        "type": "string",
        "description": "The name of the Pakistani channel that broadcasted the tournament."
      },
      "channel_owner_corporation": {
        "type": "string",
        "description": "The name of the corporation that owns the broadcast channel."
      },
      "owner_additional_info": {
        "type": "string",
        "description": "Additional information about the owner corporation."
      }
    },
    "required": [
      "tournament_name",
      "broadcast_channel",
      "channel_owner_corporation",
      "owner_additional_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
