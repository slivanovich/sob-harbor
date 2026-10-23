{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Route of the K-Money: The Route of the K-Money (Spanish: \"La ruta del dinero K\" ; \"K\" stands for \"\"Kirchnerism\"\") was a 2013 political scandal in Argentina.  It began with reports on the \"Periodismo Para Todos\" television program on the results of it investigation, led by journalist Jorge Lanata.  Embezzlement and an associated money trail involved Argentine presidents Néstor Kirchner, Cristina de Kirchner and their employee, businessman Lázaro Báez.  The investigation concluded that Báez diverted money intended for public infrastructure to tax havens.  The scandal led to an official investigation.  To date no judicial investigation ever found any proof of wrongdoing by Néstor Kirchner or Cristina de Kirchner.  However, in April 2016 Lázaro Baez was awaiting trial on corruption charges in an Argentinian federal prison.\n\nArgentine general election, 2011: Argentina held national presidential and legislative elections on Sunday, 23 October 2011.  Incumbent president Cristina Fernández de Kirchner secured a second term in office after the Front for Victory won just over half of the seats in the National Congress.\n\nFront for Victory: The Front for Victory (Spanish: \"Frente para la Victoria\" , FPV) is a center-left Peronist electoral alliance in Argentina, and it is formally a faction of the Justicialist Party.  Both the former President Néstor Kirchner (2003-2007) and the former President Cristina Fernández de Kirchner (2007–2015) belong to this party, located on the center-left of the mainstream Argentine political spectrum.  The party was led by Néstor Kirchner until his death in 2010.  The Front for Victory is ideologically identified with what has been called \"Kirchnerism\".  Legally, the Front should not be confused with the Party for Victory, which is just one of the political parties in it.\n\nKirchner's viscacha rat: Kirchner's viscacha rat or Kirchner's vizcacha rat (\"Tympanoctomys kirchnerorum\") is a species of rodents in the family Octodontidae described in 2014.  It is one of two species in the genus \"Tympanoctomys\".  That species is endemic to Chubut Province in the central western Argentina, where it has a fragmented range.  Its natural habitat is desert scrubland, dunes and salt flats, where it eats halophyte plants.  It is a solitary, nocturnal rodent that constructs large mounds with complex burrows.  The species was named in honor if both Cristina Fernández de Kirchner and Néstor Kirchner, presidents of Argentina.\n\nNéstor Kirchner Dam: The Néstor Kirchner Dam, formerly known as Condor Cliffs Dam, is a concrete-face rock-fill dam being built on the Santa Cruz River about 180 km west of Puerto Santa Cruz in Santa Cruz Province, Argentina.  It is named after the former president Néstor Kirchner, born in Santa Cruz.  A consortium led by China's Gezhouba Group was awarded the contract to build the Néstor Kirchner Dam and Jorge Cepernic Dam downstream in August 2013.  The consortium will also fund the construction.  Both dams are expected to cost nearly US$4.8 billion.  It will be built by the firm \"Electroingeniería\", led by Osvaldo Acosta and Gerardo Ferreyra.  The primary purpose of the dam is hydroelectric power generation and its power station will have an installed capacity of 1140 MW .\n\nDeath and state funeral of Néstor Kirchner: Argentina’s former President and 1st Secretary General of the Union of South American Nations, Néstor Kirchner, died of heart failure on the morning of 27 October 2010 at the Jose Formenti hospital in El Calafate, Santa Cruz Province at the age of 60.  Efforts to revive him were unsuccessful.  His wife, President Cristina Fernández de Kirchner, was present with him when he died.  He was also expected to run for president in 2011.\n\nAníbal Fernández: Aníbal Domingo Fernández (born January 9, 1957) is an Argentine Justicialist Party politician, lawyer, and certified public accountant who has been a close ally, loyal to both, the late President Néstor Kirchner and the former President Cristina Fernández de Kirchner.  He has held several cabinet positions under three presidents, serving in these offices for a total of over nine years.  He served as Minister of Production under Eduardo Duhalde, as Interior Minister under Néstor Kirchner, as Minister of Justice under Cristina Fernández de Kirchner, and as the President's Cabinet Chief from 2009 to 2011.\n\nLa Cámpora: La Cámpora is an Argentine political youth organization supporting the governments of Néstor Kirchner and Cristina Fernández de Kirchner.  It is named after former peronist president Héctor José Cámpora.  Although it was established in 2003, it became politically notorious after the death of former president Néstor Kirchner.\n\nLa audacia y el cálculo: La audacia y el cálculo (Spanish: \"The boldness and the strategy\" ) is a 2011 Argentine book by Beatriz Sarlo.  It is focused in the history of Argentina from 2003 to 2010, the presidency of Néstor Kirchner and part of the first presidency of Cristina Fernández de Kirchner (still influenced by Néstor Kirchner).  Sarlo details the plots used by Néstor Kirchner to increase his political power.\n\nMartin Báez: Martin Antonio Báez is an Argentinian businessman and the son of Lázaro Báez.  The younger Báez, who is a director of Austral Construcciones, a construction firm founded by his father, is, like the elder Báez, a central figure in the corruption scandal known variously as “Lázarogate” and “The Route of the K Money,” the letter K being a reference to the ties enjoyed by Báez and other suspects to the presidencies of the late Néstor Kirchner and his wife, the incumbent, Cristina Fernández de Kirchner.\n\nQuestion: Who was the incumbent president who was the wife of Néstor Kirchner?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"president_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the president.\"\n    },\n    \"relationship_to_nestor_kirchner\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of the president to N\\u00e9stor Kirchner.\"\n    },\n    \"presidency_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"was_incumbent\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the president was incumbent at a specific time.\"\n        },\n        \"term_secured_in_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year in which the president secured a term in office.\"\n        },\n        \"political_party\": {\n          \"type\": \"string\",\n          \"description\": \"The political party or alliance the president belongs to.\"\n        }\n      },\n      \"required\": [\n        \"was_incumbent\",\n        \"term_secured_in_year\",\n        \"political_party\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"president_name\",\n    \"relationship_to_nestor_kirchner\",\n    \"presidency_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "president_name": {
        "type": "string",
        "description": "The name of the president."
      },
      "relationship_to_nestor_kirchner": {
        "type": "string",
        "description": "The relationship of the president to Néstor Kirchner."
      },
      "presidency_details": {
        "type": "object",
        "properties": {
          "was_incumbent": {
            "type": "boolean",
            "description": "Indicates if the president was incumbent at a specific time."
          },
          "term_secured_in_year": {
            "type": "integer",
            "description": "The year in which the president secured a term in office."
          },
          "political_party": {
            "type": "string",
            "description": "The political party or alliance the president belongs to."
          }
        },
        "required": [
          "was_incumbent",
          "term_secured_in_year",
          "political_party"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "president_name",
      "relationship_to_nestor_kirchner",
      "presidency_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
