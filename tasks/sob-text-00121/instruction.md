{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTimasius: Flavius Timasius (died 396) was a general of the Roman Empire, a relative of the Empress Aelia Flaccilla, wife of Emperor Theodosius I (r. 379–395).\n\nDe Viris Illustribus (Jerome): De Viris Illustribus (\"On Illustrious Men\") is a collection of short biographies of 135 authors, written in Latin, by the 4th-century Latin Church Father Jerome.  He completed this work at Bethlehem in 392-3 CE.  The work consists of a prologue plus 135 chapters, each consisting of a brief biography.  Jerome himself is the subject of the final chapter.  A Greek version of the book, possibly by the same Sophronius who is the subject of Chapter 134, also survives.  Many biographies take as their subject figures important in Christian Church history and pay especial attention to their careers as writers.  It \"was written as an apologetic work to prove that the Church had produced learned men.\"  The book was dedicated to Flavius Dexter, who served as high chamberlain to Theodosius I and as praetorian prefect to Honorius.  Dexter was the son of Saint Pacianus, who is eulogized in the work.\n\nRufinus (consul): Flavius Rufinus (died November 27, 395) was a 4th-century Eastern Roman Empire statesman of Gaulish extraction who served as Praetorian prefect of the East for the emperor Theodosius I, as well as for his son Arcadius, under whom Rufinus was the actual power behind the throne.\n\nCount Theodosius: Count Theodosius (Latin: \"Comes Theodosius\" ) was a senior military officer serving in the Western Roman Empire.  He is also known as Flavius Theodosius or as Theodosius the Elder, distinguishing him from his son, the Roman emperor Theodosius I.  He was granted the title of Count of the Britains (\"Comes Britanniarum \") for his work there putting down the Great Conspiracy.  He afterwards fought against the Alemanni and in Mauretania.\n\nHonorius (emperor): Honorius (Latin: \"Flavius Honorius Augustus\" ; 9 September 384 – 15 August 423) was Western Roman Emperor from 393 to 423.  He was the younger son of emperor Theodosius I and his first wife Aelia Flaccilla, and brother of Arcadius, who was the Eastern Emperor from 395 until his death in 408.\n\nDe Viris Illustribus (Petrarch): De viris illustribus (English: On Illustrious Men ) is an unfinished collection of biographies, written in Latin, by the 14th century Italian author Francesco Petrarca.  These biographies are a set of Lives similar in idea to Plutarch's \"Parallel Lives\".  The works were unfinished however he was famous enough for these and other works to receive two invitations to be crowned poet laureate.  He received these invitations on exactly the same day, April 8, 1341, one being from the Paris University and the other from the Roman Senate.  He accepted the Roman invitation.\n\nAelia Flaccilla: Aelia Flavia Flaccilla (31 March 356 – 386), was a Roman empress and first wife of the Roman Emperor Theodosius I.  She was of Hispanian Roman descent.  During her marriage to Theodosius, she gave birth to two sons — future Emperors Arcadius and Honorius — and a daughter, Aelia Pulcheria.  She was titled \"Augusta\", as her coinage shows.\n\nAfraflacilla: Afraflacilla is a genus of the spider family Salticidae (jumping spiders).  Most species are distributed in Eastern to Northern Africa (including the Middle East) and Australia, with one species (\"A. epiblemoides\") found in Europe.  This genus was for a time included in the genus \"Pseudicius\", and the boundaries between both genera are disputed.  In 2016 Jerzy Prószyński erected the genus \"Psenuc\" for some borderline species.  The name \"Afraflacilla\" is combined from Africa, where most earlier described species were found, and \"Flacilla\" , an obsolete salticid genus now called \"Flacillula\" .  This genus name is in turn derived from Aelia Flaccilla, wife of Roman Emperor Theodosius I.  \"Afraflacilla\", \"Pseudicius\", \"Festucula\" and \"Marchena\" are close relatives and form a monophyletic group.\n\nPulcheria (daughter of Theodosius I): Aelia Pulcheria (385–386) was the daughter of Roman Emperor Theodosius I and Roman Empress Aelia Flaccilla.  This Pulcheria apparently died in childhood, and is not to be confused with her more famous niece of the same name.\n\nArcadius: Arcadius (Latin: \"Flavius Arcadius Augustus\" ; Greek: ; 1 January 377 – 1 May 408) was Byzantine Emperor from 383 to 408.  He was the eldest son of Theodosius I and his first wife Aelia Flaccilla, and brother of the Western Emperor Honorius.  A weak ruler, his reign was dominated by a series of powerful ministers and by his wife, Aelia Eudoxia.\n\nQuestion: De Viris Illustribus (\"On Illustrious Men\") is a collection of short biographies of 135 authors, written in Latin, by the 4th-century Latin Church Father Jerome, the book was dedicated to Flavius Dexter, who served as high chamberlain to Theodosius I and as praetorian prefect to which Western Roman Emperor from 393 to 423, the  younger son of emperor Theodosius I and his first wife Aelia Flaccilla, and brother of Arcadius?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"emperor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Western Roman Emperor.\"\n    },\n    \"imperial_title\": {\n      \"type\": \"string\",\n      \"description\": \"The specific imperial title held by the individual.\"\n    },\n    \"reign_period\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the emperor's reign.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the emperor's reign.\"\n        }\n      },\n      \"required\": [\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"family_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"father_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the emperor's father.\"\n        },\n        \"mother_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the emperor's mother.\"\n        },\n        \"sibling_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the emperor's sibling.\"\n        },\n        \"sibling_relationship\": {\n          \"type\": \"string\",\n          \"description\": \"The relationship to the sibling, e.g., 'brother'.\"\n        },\n        \"birth_order_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the emperor's birth order among his siblings, e.g., 'younger son'.\"\n        }\n      },\n      \"required\": [\n        \"father_name\",\n        \"mother_name\",\n        \"sibling_name\",\n        \"sibling_relationship\",\n        \"birth_order_description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"official_who_served_him\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"official_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the official who served this emperor.\"\n        },\n        \"service_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role in which the official served this emperor.\"\n        }\n      },\n      \"required\": [\n        \"official_name\",\n        \"service_role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"emperor_name\",\n    \"imperial_title\",\n    \"reign_period\",\n    \"family_details\",\n    \"official_who_served_him\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "emperor_name": {
        "type": "string",
        "description": "The name of the Western Roman Emperor."
      },
      "imperial_title": {
        "type": "string",
        "description": "The specific imperial title held by the individual."
      },
      "reign_period": {
        "type": "object",
        "properties": {
          "start_year": {
            "type": "integer",
            "description": "The start year of the emperor's reign."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the emperor's reign."
          }
        },
        "required": [
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "family_details": {
        "type": "object",
        "properties": {
          "father_name": {
            "type": "string",
            "description": "The name of the emperor's father."
          },
          "mother_name": {
            "type": "string",
            "description": "The name of the emperor's mother."
          },
          "sibling_name": {
            "type": "string",
            "description": "The name of the emperor's sibling."
          },
          "sibling_relationship": {
            "type": "string",
            "description": "The relationship to the sibling, e.g., 'brother'."
          },
          "birth_order_description": {
            "type": "string",
            "description": "A description of the emperor's birth order among his siblings, e.g., 'younger son'."
          }
        },
        "required": [
          "father_name",
          "mother_name",
          "sibling_name",
          "sibling_relationship",
          "birth_order_description"
        ],
        "additionalProperties": false
      },
      "official_who_served_him": {
        "type": "object",
        "properties": {
          "official_name": {
            "type": "string",
            "description": "The name of the official who served this emperor."
          },
          "service_role": {
            "type": "string",
            "description": "The role in which the official served this emperor."
          }
        },
        "required": [
          "official_name",
          "service_role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "emperor_name",
      "imperial_title",
      "reign_period",
      "family_details",
      "official_who_served_him"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
