{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMike Pilbeam: Mike Pilbeam (born 1937) is a British motorsport designer and engineer known for his work with BRM, Lotus, Surtees and his own company, Pilbeam Racing Designs.  An early design was the experimental four wheel drive Formula One BRM P67 of 1964.  s of 2014 , Pilbeam's company continued to produce hillclimb cars and sports prototype chassis for endurance racing.\n\nForrestburn Hillclimb: Forrestburn Speed Hill Climb is a 1030 m hillclimb track near Kirk o' Shotts in North Lanarkshire, central Scotland.  The track opened in 1993, and was the first purpose-built hillclimb track in the United Kingdom to be completed since Brooklands in the 1930s.  Forrestburn Hillclimb is operated by Monklands Sporting Car Club, and all speed hillclimbs at Forrestburn are rounds of the Scottish Hillclimb Championship.  The site was designed by Willie Miller Urban Design as part of a projected Scottish motor racing circuit which was never taken forward.\n\nBrooklands: Brooklands was a 2.75 mi motor racing circuit and aerodrome built near Weybridge in Surrey, England, United Kingdom.  It opened in 1907 and was the world's first purpose-built motor racing circuit as well as one of Britain's first airfields, which also became Britain's largest aircraft manufacturing centre by 1918, producing military aircraft such as the Wellington and civil airliners like the VC-10.\n\nQuestion: What did Brooklands produce that Forrestburn Hillclimb did not?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"producing_entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity that produced the item.\"\n    },\n    \"non_producing_entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity that did not produce the item.\"\n    },\n    \"item_produced_by_first_entity\": {\n      \"type\": \"string\",\n      \"description\": \"The specific item produced by the first entity but not the second.\"\n    },\n    \"item_category\": {\n      \"type\": \"string\",\n      \"description\": \"The general category of the item produced.\"\n    },\n    \"first_entity_primary_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role or function of the first entity related to production.\"\n    },\n    \"second_entity_primary_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role or function of the second entity.\"\n    }\n  },\n  \"required\": [\n    \"producing_entity_name\",\n    \"non_producing_entity_name\",\n    \"item_produced_by_first_entity\",\n    \"item_category\",\n    \"first_entity_primary_role\",\n    \"second_entity_primary_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "producing_entity_name": {
        "type": "string",
        "description": "The name of the entity that produced the item."
      },
      "non_producing_entity_name": {
        "type": "string",
        "description": "The name of the entity that did not produce the item."
      },
      "item_produced_by_first_entity": {
        "type": "string",
        "description": "The specific item produced by the first entity but not the second."
      },
      "item_category": {
        "type": "string",
        "description": "The general category of the item produced."
      },
      "first_entity_primary_role": {
        "type": "string",
        "description": "The primary role or function of the first entity related to production."
      },
      "second_entity_primary_role": {
        "type": "string",
        "description": "The primary role or function of the second entity."
      }
    },
    "required": [
      "producing_entity_name",
      "non_producing_entity_name",
      "item_produced_by_first_entity",
      "item_category",
      "first_entity_primary_role",
      "second_entity_primary_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
