{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMadhabdi: Madhabdi (Bengali: মাধবদী ) is a \"pourashava\" (municipal corporation) in Narsingdi District, Dhaka division, Bangladesh.  It's an A grade municipality.  Madhabdi is a densely textile commarcial and industrial area, where a number of automatic and hand-made loom weaving and manufacturing mills (about 3000/4500) are situated.  There are about 45,000 people employed directly and indirectly in these mills.  It's also one of the richest area in Narsingdi District.\n\nChempark: With its three sites in Leverkusen, Dormagen and Krefeld-Uerdingen, Chempark is the biggest chemical park in Germany.  Some 50,000 people employed by the 60 plus companies and service providers located there work on an area measuring 13.3 square kilometers.  Around one third of North Rhine-Westphalia’s chemical output is produced at these three sites.  Manager and operator of CHEMPARK is CURRENTA GmbH & CO.  OHG (until 2007 known as Bayer Industry Services GmbH & Co.  OHG).\n\nQueen of Peace, Bray: The Queen of Peace is a Catholic church situated at the junction of the Putland Road and the Vevay Road in Bray, Co.  Wicklow, Ireland.  The present church was built in 1946 by T & J Macken of St Patrick’s Street, Dún Laoghaire, with many local people employed on the construction.  The plot of land used was donated by the Presentation Brothers who were running Presentation College, Bray.\n\nYugoslavian parliamentary election, 1963: Parliamentary elections were held in Yugoslavia in June 1963.  They were the first held under the 1963 constitution which created a five-chamber Parliament.  Only one chamber, the 120-seat Federal Council, was directly elected, with its election taking place on 16 June.  The other four chambers, the Economic Council, the Educational-Cultural Council, the Social and Heath Council and the Organisational-Political Council were elected between 3 and 16 June by people employed or specialising in those industries.\n\nList of astronauts by name: This is an alphabetical list of astronauts, people employed and trained by a manned spaceflight program to command, fly as a pilot, or serve as a crew member of a manned spacecraft.  More than 560 people have been trained as astronauts.  Until 2004, astronauts were sponsored and trained exclusively by governments, either by military agencies or by civilian space agencies.  However, with the first sub-orbital flight of the privately funded SpaceShipOne, a new category of astronaut was created – the commercial astronaut.\n\nCoxHealth: CoxHealth is a five-hospital, 860 bed health system headquartered in Springfield, Missouri.  It serves a 25 county region of Southwest Missouri and Northwest Arkansas.  CoxHealth is one of Springfield's largest employers, with more than 10,000 people employed throughout the system.\n\nClive Farahar: Clive Farahar (born 1950) is a British dealer and expert on books and manuscripts.  He is best known as an expert on the BBC's \"Antiques Roadshow\", which he joined in 1986.\n\nBBC: The British Broadcasting Corporation (BBC) is a British public service broadcaster with its headquarters at Broadcasting House in London.  The BBC is the world's oldest national broadcasting organisation and the largest broadcaster in the world by number of employees.  It employs over 20,950 staff in total, 16,672 of whom are in public sector broadcasting.  The total number of staff is 35,402 when part-time, flexible, and fixed contract staff are included.\n\nCinema of Ireland: The Irish film industry has grown somewhat in recent years thanks partly to the promotion of the sector by \"Bord Scannán na hÉireann\" (Irish Film Board) and the introduction of heavy tax breaks.  According to the Irish Audiovisual Content Production Sector Review carried out by the Irish Film Board and PricewaterhouseCoopers in 2008 this sector, has gone from 1,000 people employed six or seven years ago, to well over 6,000 people in that sector now and is valued at over €557.3 million and represents 0.3% of GDP.\n\nJewel of Muscat: The Jewel of Muscat is a ship based on the design of the Belitung shipwreck, an Arabian dhow that was found off the coast of Belitung Island, Indonesia, in 1998 and subsequently salvaged.  It was built in a joint effort by the governments of Oman and Singapore and Mike Flecker, one of the people employed by the salvage company Seabed Explorations at the time of the original recovery.\n\nQuestion: Clive Farahar is one of approximately how many people employed by BBC?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the organization.\"\n    },\n    \"employee_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of people employed by the organization.\"\n    },\n    \"employee_category\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the category of employees counted.\"\n    }\n  },\n  \"required\": [\n    \"organization_name\",\n    \"employee_count\",\n    \"employee_category\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "organization_name": {
        "type": "string",
        "description": "The name of the organization."
      },
      "employee_count": {
        "type": "integer",
        "description": "The number of people employed by the organization."
      },
      "employee_category": {
        "type": "string",
        "description": "A description of the category of employees counted."
      }
    },
    "required": [
      "organization_name",
      "employee_count",
      "employee_category"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
