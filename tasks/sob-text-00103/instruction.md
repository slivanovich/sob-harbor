{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnother Kind of Blues: Another Kind of Blues is the first studio album released by English punk band, the U.K. Subs.  It was released in the UK on 14 September 1979 on GEM Records, a subsidiary of RCA.  It is considered as a classic from the punk era.\n\nJarvis (album): Jarvis (also known as \"The Jarvis Cocker Record\") is the debut solo album by Pulp vocalist and musician Jarvis Cocker, released in the UK on 13 November 2006.\n\nMac Cocker: Mac Cocker (1941 – 3 June 2016) was an English-born Australian radio announcer, who worked for the Australian Broadcasting Corporation radio network for 33 years, with stints on Radio Australia, Triple J, Radio National and 105.7 ABC Darwin.  He was also known for being the father of Jarvis Cocker, the lead singer of the English rock band Pulp.\n\nU.K. Subs: The U.K. Subs are an English punk band, among the earliest in the first wave of British punk.  Formed in 1976, the mainstay of the band has been vocalist Charlie Harper, originally a singer in Britain's R&B scene.  They were also one of the first street punk bands.\n\nBattalion of Saints: Battalion of Saints is a hardcore punk rock band from San Diego, California that was founded in 1980.  The band went through numerous lineup changes before touring the United States and Canada from 1984-1985 with George Anthony, Chris Smith, James Cooper and Joey Wrecked (Maya).  Half-way through the 55-city summer 1985 tour, the road manager, Captain Scarlett(David Lloyd) replaced James Cooper on bass.  The band officially broke up in 1985.  Singer George Anthony re-formed the band in 1995 with Terry \"Tezz\" Roberts (veteran of British punk bands Discharge, Broken Bones, and U.K. Subs), and signed to Taang!  Records, which reissued most of their material on the \"Death-R-Us\" CD.\n\nBrand New Age: Brand New Age is the second studio album released by English punk band the U.K. Subs.  It was released in 1980 on RCA/GEM Records.  It is the U.K. Subs' most successful studio recording, reaching number 18 in the UK album charts and staying in the chart for nine weeks.\n\nThe Visitors (American punk band): The Visitors were a Dallas, TX based punk band formed in early 1998 by the members of Fallout and a former member of the U.K. Subs.\n\nCareer Soldiers (band): Career Soldiers was a street punk band based in San Diego.  The band have toured America and Canada with bands like The Casualties, Lower Class Brats, Monster Squad, Clit 45, U.K. Subs, Funeral Dress among others.\n\nJarvis Cocker: Jarvis Branson Cocker (born 19 September 1963) is an English musician, actor and presenter.  As the frontman of the band Pulp, he became a figurehead of the Britpop genre of the mid-1990s.  Following Pulp's hiatus, Cocker has pursued a solo career, and presents a BBC Radio 6 Music show called \"Jarvis Cocker's Sunday Service\".\n\nCharlie Harper (singer): Charlie Harper (born David Charles Perez, 25 May 1944, Hackney, London) is a British singer and songwriter.  He is best known as the lead singer from the punk band U.K. Subs.\n\nQuestion: Which musician, Jarvis Cocker or Charlie Harper, is best known as the lead singer from the punk band U.K. Subs?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"target_band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band in question.\"\n    },\n    \"musicians_compared\": {\n      \"type\": \"array\",\n      \"description\": \"A list of musicians evaluated for their association with the target band.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"musician_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the musician.\"\n          },\n          \"is_lead_singer_of_target_band\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the musician is identified as the lead singer of the target band, false otherwise.\"\n          },\n          \"primary_band_affiliation\": {\n            \"type\": \"string\",\n            \"description\": \"The primary band the musician is known for being affiliated with, according to the context.\"\n          }\n        },\n        \"required\": [\n          \"musician_name\",\n          \"is_lead_singer_of_target_band\",\n          \"primary_band_affiliation\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"identified_lead_singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the musician identified as the lead singer of the target band.\"\n    }\n  },\n  \"required\": [\n    \"target_band_name\",\n    \"musicians_compared\",\n    \"identified_lead_singer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "target_band_name": {
        "type": "string",
        "description": "The name of the band in question."
      },
      "musicians_compared": {
        "type": "array",
        "description": "A list of musicians evaluated for their association with the target band.",
        "items": {
          "type": "object",
          "properties": {
            "musician_name": {
              "type": "string",
              "description": "The name of the musician."
            },
            "is_lead_singer_of_target_band": {
              "type": "boolean",
              "description": "True if the musician is identified as the lead singer of the target band, false otherwise."
            },
            "primary_band_affiliation": {
              "type": "string",
              "description": "The primary band the musician is known for being affiliated with, according to the context."
            }
          },
          "required": [
            "musician_name",
            "is_lead_singer_of_target_band",
            "primary_band_affiliation"
          ],
          "additionalProperties": false
        }
      },
      "identified_lead_singer_name": {
        "type": "string",
        "description": "The name of the musician identified as the lead singer of the target band."
      }
    },
    "required": [
      "target_band_name",
      "musicians_compared",
      "identified_lead_singer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
