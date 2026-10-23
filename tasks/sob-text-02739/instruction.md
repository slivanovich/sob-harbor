{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nS.P.I.D.E.R.: S.P.I.D.E.R. was a fictional terrorist organization which appeared in DC Comics.  Their first and only appearances were in \"Catwoman\" #48 and #49.  The group was created by Doug Moench and Jim Balent.\n\nXenobrood: Xenobrood is a fictional comic book superhero team in the DC Comics universe.  They first appeared in \"Xenobrood\" #0 (October 1994).  The series was created by Doug Moench and Tomm Coker.\n\nBlack Spectre: Black Spectre has two meanings in the Marvel Universe.  The first Black Spectre is the name of a fictional organization which first appeared in \"Daredevil\" #108 (March 1974) and was created by writer Steve Gerber and penciller Bob Brown.  It was a league of costumed female commandos, entranced by the Mandrill into doing his bidding, and led by Nekra.  The second Black Spectre is a fictional supervillain who first appeared in \"Moon Knight\" #25 (November 1982) and was created by writer Doug Moench and penciller Bill Sienkiewicz.  The character is one of the greatest enemies of the vigilante Moon Knight.\n\nMorning Star (comics): Morning Star is the alias of Schuyler Belial, a fictional Marvel Comics villain and Satanist who was an enemy of Moon Knight and the Werewolf by Night.  He first appeared in \"Moon Knight\", Volume 1 #29.  He was created by Doug Moench and Bill Sienkiewicz.\n\nStained Glass Scarlet: Stained Glass Scarlet (real name Scarlet Fasinera) is a fictional character appearing in the Marvel Comics universe created by Doug Moench, Bill Sienkiewicz, and Jim Shooter.\n\nBlack Mask (comics): Black Mask (Roman Sionis) is a fictional supervillain appearing in comic books published by DC Comics.  Created by Doug Moench and Tom Mandrake, he first appeared in \"Batman\" #386 (Aug. 1985).  The character is a brutally sadistic kingpin in Gotham City's criminal underworld who has a fixation with masks.  Black Mask is an adversary of the superhero Batman and belongs to the collective of enemies that make up his rogues gallery.\n\nMoon Knight: Moon Knight is a fictional superhero appearing in American comic books published by Marvel Comics.  Created by Doug Moench and Don Perlin, the character first appeared in \"Werewolf by Night\" #32 (August 1975).\n\nDeathlok: Deathlok (also referred to as \"Deathlok the Demolisher\") is a fictional character appearing in American comic books published by Marvel Comics.  He first appeared in \"Astonishing Tales\" #25 (Aug.  1974), created by Rich Buckler and Doug Moench.  At least three subsequent Marvel characters have used the \"Deathlok\" identity since then.  A recurring theme among these characters is that a dead human has been reanimated with cybernetic technology.  \"Deathlok technology\" has also been used thematically by Marvel writers in other stories.  The character has also appeared on television in animation and live action.\n\nBane (comics): Bane is a fictional supervillain appearing in American comic books published by DC Comics, commonly as an adversary of the superhero Batman.  The character first appeared in \"Batman: Vengeance of Bane\" #1 (January 1993) and was created by Chuck Dixon, Doug Moench, and Graham Nolan.\n\nBallistic (DC Comics): Ballistic is a fictional superhero published by DC Comics.  He first appeared in \"Batman Annual\" #17 (1993), and was created by Doug Moench and Michael Manley.\n\nQuestion: What fictional superhero created by Doug Moench and Don Perlin was the mortal enemy of Black Spectrel\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"superhero_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fictional superhero.\"\n    },\n    \"superhero_publisher\": {\n      \"type\": \"string\",\n      \"description\": \"The publisher of the superhero's comics.\"\n    },\n    \"superhero_creators\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of creators of the superhero.\"\n    },\n    \"enemy_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the enemy.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the enemy (e.g., 'supervillain', 'organization').\"\n        },\n        \"relationship\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the adversarial relationship with the superhero.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"relationship\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"superhero_name\",\n    \"superhero_publisher\",\n    \"superhero_creators\",\n    \"enemy_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "superhero_name": {
        "type": "string",
        "description": "The name of the fictional superhero."
      },
      "superhero_publisher": {
        "type": "string",
        "description": "The publisher of the superhero's comics."
      },
      "superhero_creators": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of creators of the superhero."
      },
      "enemy_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the enemy."
          },
          "type": {
            "type": "string",
            "description": "The type of the enemy (e.g., 'supervillain', 'organization')."
          },
          "relationship": {
            "type": "string",
            "description": "Description of the adversarial relationship with the superhero."
          }
        },
        "required": [
          "name",
          "type",
          "relationship"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "superhero_name",
      "superhero_publisher",
      "superhero_creators",
      "enemy_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
