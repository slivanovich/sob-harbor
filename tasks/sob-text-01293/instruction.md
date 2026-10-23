{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEtruscan civilization: The Etruscan civilization ( ) is the modern name given to a powerful and wealthy civilization of ancient Italy in the area corresponding roughly to Tuscany, western Umbria, and northern Lazio.  As distinguished by its unique language, this civilization endured from before the time of the earliest Etruscan inscriptions ( 700 BC) until its assimilation into the Roman Republic, beginning in the late 4th century BC with the Roman–Etruscan Wars.\n\nBattle of Alalia: The naval Battle of Alalia took place between 540 BC and 535 BC off the coast of Corsica between Greeks and the allied Etruscans and Carthaginians.  A Punic-Etruscan fleet of 120 ships defeated a Greek force of Phocean ships while emigrating to the western Mediterranean and the nearby colony of Alalia (now Aléria).\n\nPorta Collina: The Colline Gate (Latin Porta Collina) was a landmark in ancient Rome, supposed to have been built by Servius Tullius, semi-legendary king of Rome 578–535 BC.  The gate stood at the north end of the Servian Wall, and past it were two important streets, the Via Salaria and Via Nomentana.  Within this area the Alta Semita linked the Quirinal with the Porta Carmentalis.  Several temples were located near the gate, including temples of Venus Erycina and Fortuna.  To a person facing the gate in the 3rd century AD, the Gardens of Sallust would have been on the left, with the Baths of Diocletian on the right.\n\nEtruscan mythology: Etruscan mythology comprises a set of stories, beliefs, and religious practices of the Etruscan civilization, originating in the 7th century BC from the preceding Iron Age Villanovan culture, with its influences in the mythology of ancient Greece and Phoenicia, and sharing similarities with concurrent Roman mythology.  As the Etruscan civilization was assimilated into the Roman Republic in the 4th century BC, the Etruscan religion and mythology were partially incorporated into classical Roman culture, following the Roman tendency to absorb some of the local gods and customs of conquered lands.\n\nVulca: Vulca was an Etruscan artist from the town of Veii.  The only Etruscan artist mentioned by ancient writers, he worked for the last of the Roman kings, Tarquinius Superbus.  He is responsible for creating a terracotta statue of Jupiter that was inside the Temple of Jupiter Optimus Maximus on the Capitoline Hill, and possibly the Apollo of Veii.  His statue of Jupiter, which being made of terracotta had a red face, was so famous that victorious Roman generals would paint their faces red during their triumphal marches through Rome.  Pliny the Elder wrote that his works were \"the finest images of deities of that era...more admired than gold.\"\n\n535 BC: The year 535 BC was a year of the pre-Julian Roman calendar.  In the Roman Empire, it was known as year 219 \" Ab urbe condita\".  The denomination 535 BC for this year has been used since the early medieval period, when the Anno Domini calendar era became the prevalent method in Europe for naming years.\n\nLucius Tarquinius Superbus: Lucius Tarquinius Superbus (died 495 BC) was the legendary seventh and final king of Rome, reigning from 535 BC until the popular uprising in 509 that led to the establishment of the Roman Republic.  He is commonly known as Tarquin the Proud, from his cognomen \"Superbus\" (Latin for \"proud, arrogant, lofty\").\n\nServius Tullius: Servius Tullius was the legendary sixth king of Rome, and the second of its Etruscan dynasty.  He reigned 575–535 BC.  Roman and Greek sources describe his servile origins and later marriage to a daughter of Lucius Tarquinius Priscus, Rome's first Etruscan king, who was assassinated in 579 BC.  Servius is said to have been the first Roman king to accede without election by the Senate, having gained the throne by popular support; and the first to be elected by the Senate alone, without reference to the people.\n\nCapitoline Brutus: The Capitoline Brutus is an ancient Roman bronze bust commonly thought to depict the Roman consul Lucius Junius Brutus (d. 509 BC), usually dated to the late 4th to early 3rd centuries BC, but perhaps as late as the 2nd century BC, or early 1st century BC.  The bust is 69 cm (27 in) in height and is currently located in the Hall of the Triumphs within the Capitoline Museums, Rome.  Traditionally taken to be an early example of Roman portraiture and perhaps by an Etruscan artist influenced by Hellenistic art and contemporary Greek styles of portraiture, it may be \"an archaizing work of the first century BC\".  The Roman head was provided with a toga-clad bronze bust during the Renaissance.\n\nVelia: Velia was the Roman name of an ancient city of Magna Graecia on the coast of the Tyrrhenian Sea.  It was founded by Greeks from Phocaea as Hyele (Ancient Greek: Ὑέλη ) around 538–535 BC.  The name later changed to Ele and then Elea ( ; Ancient Greek: Ἐλέα ) before it became known by its current Latin and Italian name during the Roman era.  Its ruins are located in the Cilento region near the modern village Velia, which was named after the ancient city.  The village is a \"frazione\" of the \"comune\" Ascea in the Province of Salerno, Campania, Italy.\n\nQuestion: Who was the etruscan artist that worked for the last of the Roman Kings that reigned during 535 BC?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Etruscan artist.\"\n        },\n        \"origin_town\": {\n          \"type\": \"string\",\n          \"description\": \"The town where the artist was from.\"\n        },\n        \"notable_works\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of notable works attributed to the artist.\"\n        },\n        \"historical_significance\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the artist's unique historical significance.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"origin_town\",\n        \"notable_works\",\n        \"historical_significance\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"roman_king_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Roman king.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title or position of the Roman king.\"\n        },\n        \"reign_start_year_bc\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the king's reign in BC.\"\n        },\n        \"reign_end_year_bc\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the king's reign in BC.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title\",\n        \"reign_start_year_bc\",\n        \"reign_end_year_bc\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"question_context_year_bc\": {\n      \"type\": \"integer\",\n      \"description\": \"The specific year mentioned in the question's context for the king's reign.\"\n    },\n    \"final_answer_artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Etruscan artist who worked for the specified Roman king.\"\n    }\n  },\n  \"required\": [\n    \"artist_details\",\n    \"roman_king_details\",\n    \"question_context_year_bc\",\n    \"final_answer_artist_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Etruscan artist."
          },
          "origin_town": {
            "type": "string",
            "description": "The town where the artist was from."
          },
          "notable_works": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of notable works attributed to the artist."
          },
          "historical_significance": {
            "type": "string",
            "description": "A description of the artist's unique historical significance."
          }
        },
        "required": [
          "name",
          "origin_town",
          "notable_works",
          "historical_significance"
        ],
        "additionalProperties": false
      },
      "roman_king_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Roman king."
          },
          "title": {
            "type": "string",
            "description": "The title or position of the Roman king."
          },
          "reign_start_year_bc": {
            "type": "integer",
            "description": "The start year of the king's reign in BC."
          },
          "reign_end_year_bc": {
            "type": "integer",
            "description": "The end year of the king's reign in BC."
          }
        },
        "required": [
          "name",
          "title",
          "reign_start_year_bc",
          "reign_end_year_bc"
        ],
        "additionalProperties": false
      },
      "question_context_year_bc": {
        "type": "integer",
        "description": "The specific year mentioned in the question's context for the king's reign."
      },
      "final_answer_artist_name": {
        "type": "string",
        "description": "The name of the Etruscan artist who worked for the specified Roman king."
      }
    },
    "required": [
      "artist_details",
      "roman_king_details",
      "question_context_year_bc",
      "final_answer_artist_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
