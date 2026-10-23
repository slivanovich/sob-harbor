{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2012 Trophée des Alpilles – Doubles: Pierre-Hugues Herbert and Édouard Roger-Vasselin were the defending champions but Roger-Vasselin decided not to participate. <br>\n\n2015 French Open – Men's Doubles: Julien Benneteau and Édouard Roger-Vasselin were the defending champions, but Benneteau withdrew from the tournament because of a sports hernia.  Roger-Vasselin played alongside Guillermo García-López, but lost in the third round to Ivan Dodig and Marcelo Melo.\n\n2013 Moselle Open – Doubles: Nicolas Mahut and Édouard Roger-Vasselin were the defending champions, but chose not to participate together.  Roger-Vasselin teamed up with Rohan Bopanna, but lost in the semifinals to Johan Brunström and Raven Klaasen. <br>\n\n2016 Western &amp; Southern Open – Men's Doubles: Daniel Nestor and Édouard Roger-Vasselin were the defending champions, but chose not to compete together.  Nestor played alongside Vasek Pospisil, but lost in the semifinals to Ivan Dodig and Marcelo Melo.  Roger-Vasselin teamed up with Julien Benneteau, but lost in the first round to Milos Raonic and Nenad Zimonjić.\n\nSergi Bruguera: Sergi Bruguera i Torner (] ; born 16 January 1971) is a former professional tennis player from Catalonia, Spain.  He won consecutive men's singles titles at the French Open in 1993 and 1994.  As of 2016, he has won the most Grand Slam titles for someone not inducted to the International Tennis Hall of Fame.\n\n2016 Moselle Open – Doubles: Łukasz Kubot and Édouard Roger-Vasselin were the defending champions, but Kubot chose not to participate this year.  Roger-Vasselin played alongside Julien Benneteau, but lost in the first round to Marcus Daniell and Marcelo Demoliner.\n\n2014 Hall of Fame Tennis Championships – Doubles: Nicolas Mahut and Édouard Roger-Vasselin were the defending champions, but Roger-Vasselin chose not to participate.  Mahut played alongside Sergiy Stakhovsky, but lost in the semifinals to Jonathan Erlich and Rajeev Ram. <br>\n\nÉdouard Roger-Vasselin: Édouard Roger-Vasselin (] ; born 28 November 1983) is a male tennis player from France.  He won the men's doubles title at Roland Garros in 2014, partnering Julien Benneteau.  He is the son of 1983 French Open semifinalist Christophe Roger-Vasselin.\n\n2010 Challenger DCNS de Cherbourg – Doubles: Arnaud Clément and Édouard Roger-Vasselin were the defending champions, but they elected to defend their title with different partners.Clément partnered up with David Guez, but they withdrew before their quarterfinal match against Harsh Mankad and Adil Shamasdin. Roger-Vasselin partnered up with Nicolas Mahut and they won in the final 6–2, 6–4, over Mankad and Shamasdin.\n\n2011 BNP Paribas Primrose Bordeaux – Doubles: Nicolas Mahut and Édouard Roger-Vasselin were the defending champions; however, Roger-Vasselin chose not to compete this year.\n\nQuestion: Édouard Roger-Vasselin and Sergi Bruguera, has which occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"individuals\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"occupation\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"occupation\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"shared_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The common occupation shared by all individuals mentioned.\"\n    },\n    \"occupation_category\": {\n      \"type\": \"string\",\n      \"description\": \"A broader category for the occupation.\"\n    }\n  },\n  \"required\": [\n    \"individuals\",\n    \"shared_occupation\",\n    \"occupation_category\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "individuals": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "occupation": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "occupation"
          ],
          "additionalProperties": false
        }
      },
      "shared_occupation": {
        "type": "string",
        "description": "The common occupation shared by all individuals mentioned."
      },
      "occupation_category": {
        "type": "string",
        "description": "A broader category for the occupation."
      }
    },
    "required": [
      "individuals",
      "shared_occupation",
      "occupation_category"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
