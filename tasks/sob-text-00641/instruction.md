{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnna Katharina Schwabroh: Anna Katharina Schwabroh (October 21, 1979 in Hamburg) is a German actress.\n\nAnna Katharina Schönkopf: Anna Katharina Schönkopf (] ; also called „Käthchen“ (]) and „Annette“ (]); * 22 August 1746 Leipzig - 20 May 1810 ibidem) was the daughter of the pewterer and wine merchant Christian Gottlieb Schönkopf (]; 1716-1791) and his wife Katharina Sibylla (]), born Hauck (]; 1714-1790).  The young Johann Wolfgang Goethe, who studied in Leipzig from 1765 to 1768, fell in love with her in 1766.\n\nAnna Katharina Schmid: Anna Katharina Schmid (born December 12, 1989) is a Swiss pole vaulter.  She won the bronze medal at the 2007 European Junior Championships.\n\nAnna Katharina Block: Anna Katharina Block (1642, Nuremberg – 1719, Regensburg), was a German Baroque flower painter.\n\nAnna Wienhard: Anna Katharina Wienhard (born 1977) is a German mathematician whose research concerns differential geometry, and especially the use of higher Teichmüller spaces to study the deformation theory of symmetric geometric structures.  She is a professor at Heidelberg University.\n\nSophia of Hanover: Sophia of the Palatinate (commonly referred to as Sophia of Hanover; 14 October 1630 – 8 June 1714) was the Electress of Hanover from 1692 to 1698.  As a granddaughter of James VI and I, she became heir presumptive to the crowns of the Kingdom of England and the Kingdom of Ireland under the Act of Settlement 1701.  After the Acts of Union 1707, she became heir presumptive to the unified throne of the Kingdom of Great Britain.  She died less than two months before she would have become queen, and her claim to the throne passed on to her eldest son, George Louis, Elector of Hanover, who ascended as George I on 1 August 1714 (Old Style).\n\nAnna Katharina Kränzlein: Anna Katharina Kränzlein, also known as Anna Katharina, (born 7 November 1980 in Fürstenfeldbruck, Germany) is a German violinist.  She is most known for her quick and varied technique.  She is the youngest founding member of Medieval folk rock/folk metal band Schandmaul.\n\nKatharina von Zimmern: Katharina von Zimmern (* 1478 in Messkirch; † 17 August 1547 in Zürich), also known as the imperial abbess of Zürich and Katharina von Reischach, was the last abbess of the Fraumünster Abbey in Zürich.\n\nAnna Katharina von Offen: Anna Katharina von Offen (1624-1702), was a German courtier and royal governess.  She served as Oberhofmeisterin to Sophia of Hanover, and also served as governess to her children.\n\nEuropean Medical Students' Orchestra and Choir: European medical students' orchestra and choir began in 2009 when European medical students' orchestra (EMSO) and European medical students' choir (EMSC) joined forces to produce a spectacular series of concerts in Ljubljana and Piran, Slovenia under the direction of two highly skilled and dedicated conductors - Martina Batič and Marjan Grdadolnik.  The union of the orchestra and the choir was so successful that the cooperation of EMSO and EMSC continued with concerts in Chester Cathedral and the Royal Northern College of Music, Manchester in 2010 under the conduction of John Anderson and Daniel Parkinson, and in Giessen and Frankfurt, Germany in 2011, under the leadership of Stefan Ottersbach and Anna Katharina Kalmbach with once again spectacular concerts that astonished the local audience and media.\n\nQuestion: What did Anna Katharina von Offen serve as for Sophia of Hanover?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person whose roles are being described.\"\n    },\n    \"served_for_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person for whom the service was rendered.\"\n    },\n    \"primary_role_for_served_person\": {\n      \"type\": \"string\",\n      \"description\": \"The main role served directly for the specified person.\"\n    },\n    \"other_related_roles\": {\n      \"type\": \"array\",\n      \"description\": \"A list of other roles served by the person, potentially for other recipients.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"role_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the additional role.\"\n          },\n          \"role_recipient\": {\n            \"type\": \"string\",\n            \"description\": \"The person or group who received this specific role's service.\"\n          }\n        },\n        \"required\": [\n          \"role_name\",\n          \"role_recipient\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"served_for_person_name\",\n    \"primary_role_for_served_person\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person whose roles are being described."
      },
      "served_for_person_name": {
        "type": "string",
        "description": "The name of the person for whom the service was rendered."
      },
      "primary_role_for_served_person": {
        "type": "string",
        "description": "The main role served directly for the specified person."
      },
      "other_related_roles": {
        "type": "array",
        "description": "A list of other roles served by the person, potentially for other recipients.",
        "items": {
          "type": "object",
          "properties": {
            "role_name": {
              "type": "string",
              "description": "The name of the additional role."
            },
            "role_recipient": {
              "type": "string",
              "description": "The person or group who received this specific role's service."
            }
          },
          "required": [
            "role_name",
            "role_recipient"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "person_name",
      "served_for_person_name",
      "primary_role_for_served_person"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
