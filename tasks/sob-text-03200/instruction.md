{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLeonard Andrews: Leonard Edward Bryant Andrews (March 31, 1925 – January 2, 2009) was an American publisher and art collector best known for his purchase of some 240 previously unknown Andrew Wyeth works of a woman known as Helga, including several nudes.\n\nJacqueline Kennedy Onassis: Jacqueline Lee \"Jackie\" Kennedy Onassis (née Bouvier; ; July 28, 1929 – May 19, 1994) was the wife of the 35th President of the United States, John F. Kennedy, and First Lady of the United States from 1961 until his assassination in 1963.\n\nJackie O (disambiguation): Jackie O often refers to Jacqueline Onassis.  It may also refer to:\n\nBarbara Erni: Barbara Erni (15 February 1743 – 26 February 1785) was a Liechtenstein woman known for stealing from inns throughout western Europe using a confidence trick.  Known in Liechtenstein legend as Golden Boos, Erni was the last person to be executed by Liechtenstein.\n\nDaniels County Courthouse: The Daniels County Courthouse, located at 213 Main Street in Scobey, is the county courthouse serving Daniels County, Montana.  The building was built in 1913, the same year Scobey was relocated to a site on the Great Northern Railway, and originally functioned as a hotel.  The two-story building, which had a false front, was the largest in the city at the time.  Over the next seven years, the hotel passed through several hands; it became known as \"One-eyed Molly's House of Pleasure\" after its most notorious proprietor, a glass-eyed woman known as One-Eyed Molly who supposedly ran a brothel from the hotel.  When Daniels County was established in 1920, the newly formed county purchased the hotel to use as its courthouse.\n\nFlorence Tullis: Florence \"Rusty\" Tullis (née Steinberg; May 29, 1936 – November 11, 2006), also known as Rusty Dennis, Rusty Mason and Rusty Dennis Mason was an American woman known for being the mother of Rocky Dennis, who was diagnosed with craniodiaphyseal dysplasia.  Their story was depicted in the 1985 film, \"Mask\", in which Tullis was portrayed by Cher.\n\nMayra Rosales: Mayra Lizbeth Rosales (born 1980) is a Mexican American woman known for being, at one point, the heaviest living woman.  At her heaviest, she weighed 470 kg (1,036 lb) but currently weighs an estimated 91 kg (200 lb).  She came to prominence in March 2008 when her sister was jailed for murdering her two-year-old nephew.  She decided to get her life back in order to get custody of her sister's children, who had no parents to take care of them at that time.\n\nEva Merthen: Eva Merthen (1723–15 October 1811), known as \"\"The Duchess of Finland\"\", was a Finnish woman known for her relationship with the General James Keith during the Russian occupation of the Swedish province of Finland during the Russo-Swedish War (1741–1743).  She is the subject of the novel \"Hertiginnan av Finland\" (1850) by Zacharias Topelius.\n\nMochou Lake: Mochou Lake (莫愁湖, Mò Chóu Hú, literally No Worry Lake or No Unhappieness Lake) is located west to Qinhuai River and Hanzhongmen Gate in Nanjing, China, inside Mochou Lake Park.  The lake is named after Mochou, a legendary woman known for her beauty, versatility, virtue and loyalty.  It was named Hengtang in ancient times, and also known as Stone City Lake.  The lake park was owned by Zhu Yuanzhang, the first emperor of Ming Dynasty, and bestowed to his general Xu Da.  Since then, it has become a famous garden best known for its two-storied Shenggi Pavilion.  Within the park are other pavilions, gardens, pools and a stunning rock display.  It is noted for its architecture, collection of carved antique rosewood furniture and calligraphies.  Visitors can take boats allow through the lotus blossomed lake.\n\nJudy Hoback Miller: Judith \"Judy\" Hoback Miller (born May 10, 1937) is an American woman known for her involvement in the Watergate scandal in 1972 during the presidency of Richard Nixon.  She served as the bookkeeper for the Committee to Re-elect the President, also known as CREEP.\n\nQuestion: Who was married to the woman known as Jackie O until his assassination in 1963?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was married to Jackie O.\"\n    },\n    \"relationship_to_jackie_o\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the person to Jackie O.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of event that ended the marriage.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the event occurred.\"\n        }\n      },\n      \"required\": [\n        \"event_type\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"jackie_o_full_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the woman known as Jackie O.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"relationship_to_jackie_o\",\n    \"event_details\",\n    \"jackie_o_full_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who was married to Jackie O."
      },
      "relationship_to_jackie_o": {
        "type": "string",
        "description": "The relationship of the person to Jackie O."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_type": {
            "type": "string",
            "description": "The type of event that ended the marriage."
          },
          "year": {
            "type": "integer",
            "description": "The year the event occurred."
          }
        },
        "required": [
          "event_type",
          "year"
        ],
        "additionalProperties": false
      },
      "jackie_o_full_name": {
        "type": "string",
        "description": "The full name of the woman known as Jackie O."
      }
    },
    "required": [
      "person_name",
      "relationship_to_jackie_o",
      "event_details",
      "jackie_o_full_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
