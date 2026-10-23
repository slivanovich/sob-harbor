{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAmy &amp; Isabelle: Amy & Isabelle is a 2001 made-for-television movie produced through Oprah Winfrey's Harpo Films as part of her \"Oprah Winfrey Presents\" film line.  It was directed by Lloyd Kramer, who had previously directed another film under the \"Oprah Winfrey Presents\" banner, \"\".  The book is based on the 1998 Elizabeth Strout book \"Amy and Isabelle\" and stars Elisabeth Shue and Hanna Hall as Isabelle and her daughter Amy.\n\nIsabelle Romée: Isabelle Romée, also known as Isabelle de Vouthon and Isabelle d'Arc (1377–1458) and Ysabeau Romee, was the mother of Joan of Arc.  She grew up in Vouthon-Bas and later married Jacques d'Arc.  The couple moved to Domrémy, where they owned a farm consisting of about 50 acre of land.  After their daughter's famous activities in 1429, the family was granted noble status by Charles VII in December of that year.  Isabelle moved to Orléans in 1440 after her husband's death and received a pension from the city.  She petitioned Pope Nicholas V to reopen the court case that had convicted Joan of heresy, and then, in her seventies, addressed the opening session of the appellate trial at Notre Dame cathedral in Paris.  The appeals court overturned Joan's conviction on 7 July 1456.  Isabelle died two years later, probably at Sandillon near Orléans.\n\nVilla Romée: The Villa Romée is a historic mansion in Cannes.  It was built in 1928 for Marcelle Aron, the widow of Jacques Isidore Gompel, a World War I veteran.  It was designed by architects Georges-Henri Pingusson and Paul Furiet.  The garden was built in 1929.  Aron sold the house in 1935.  It has been listed as an official historical monument since 1994.\n\nTimeline of Joan of Arc: January 6: Joan of Arc is born to Jacques d'Arc and Isabelle Romée at Domrémy, France.  The birth occurs during the Christian holiday of Epiphany.\n\nLiving Heritage Tree Museum: The Living Heritage Tree Museum is located in the city of Storm Lake, Iowa, US.  It is an open-air museum dedicated to heritage trees, situated in Sunset Park on West Lake Shore Drive.  It was founded by Stan Lemaster and Theodore Klein.  The museum collection includes descendents of trees with historical connections to Joan of Arc, Johnny Appleseed, and Henry Wadsworth Longfellow.\n\nArc fault: An arc fault is a high power discharge of electricity between two or more conductors.  This discharge translates into heat, which can break down the wire's insulation and possibly trigger an electrical fire.  These arc faults can range in power from a few amps up to thousands of amps high and are highly variable in terms of strength and duration.  Common causes of arc faults include faulty connections due to corrosion and faulty initial installation.\n\nRetrial of Joan of Arc: The Retrial of Joan of Arc, also known as the \"nullification trial\" or \"rehabilitation trial\", was a posthumous retrial of Joan of Arc authorized by Pope Callixtus III at the request of Inquisitor-General Jean Bréhal and Joan's mother Isabelle Romée.\n\nJoan of Arc: Joan of Arc (French: Jeanne d'Arc , ] ; 6 January c. 1412 – 30 May 1431), nicknamed \"The Maid of Orléans\" (French: \"La Pucelle d'Orléans\" ), is considered a heroine of France for her role during the Lancastrian phase of the Hundred Years' War and was canonized as a Roman Catholic saint.  Joan of Arc was born to Jacques d'Arc and Isabelle Romée, a peasant family, at Domrémy in north-east France.  Joan said she received visions of the Archangel Michael, Saint Margaret, and Saint Catherine of Alexandria instructing her to support Charles VII and recover France from English domination late in the Hundred Years' War.  The uncrowned King Charles VII sent Joan to the siege of Orléans as part of a relief mission.  She gained prominence after the siege was lifted only nine days later.  Several additional swift victories led to Charles VII's coronation at Reims.  This long-awaited event boosted French morale and paved the way for the final French victory.\n\nMarie Isabelle de Rohan, Duchess of Tallard: Marie Isabelle de Rohan (Marie Isabelle Gabrielle Angélique; 17 January 1699 – 5 January 1754) was a French noblewoman and grand daughter of Madame de Ventadour.  Marie Isabelle was the governess of the children of Louis XV and his consort Marie Leszczyńska.\n\nVouthon-Bas: A notable native is Isabelle Romée, the mother of Joan of Arc.\n\nQuestion: What is the name of the Museum with connections to the daughter of Jacques d'Arc and Isabelle Romée?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"museum_name\": {\n      \"type\": \"string\",\n      \"description\": \"The official name of the museum.\"\n    },\n    \"museum_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general type or classification of the museum.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"state\": {\n          \"type\": \"string\"\n        },\n        \"country\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"dedicated_to\": {\n      \"type\": \"string\",\n      \"description\": \"The specific subject or theme the museum is dedicated to.\"\n    },\n    \"founders\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The names of the individuals who founded the museum.\"\n    },\n    \"historical_connections\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Historical figures whose associated trees or descendants of trees are part of the museum's collection.\"\n    }\n  },\n  \"required\": [\n    \"museum_name\",\n    \"museum_type\",\n    \"location\",\n    \"dedicated_to\",\n    \"founders\",\n    \"historical_connections\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "museum_name": {
        "type": "string",
        "description": "The official name of the museum."
      },
      "museum_type": {
        "type": "string",
        "description": "The general type or classification of the museum."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "dedicated_to": {
        "type": "string",
        "description": "The specific subject or theme the museum is dedicated to."
      },
      "founders": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The names of the individuals who founded the museum."
      },
      "historical_connections": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Historical figures whose associated trees or descendants of trees are part of the museum's collection."
      }
    },
    "required": [
      "museum_name",
      "museum_type",
      "location",
      "dedicated_to",
      "founders",
      "historical_connections"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
