{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHey, Let's Twist!: Hey, Let's Twist!  is a 1961 American musical film directed by Greg Garrison and written by Hal Hackady.  The film stars Joey Dee, Jo Ann Campbell, Teddy Randazzo, Kay Armen, Zohra Lampert and Dino Di Luca.  The film was released on December 31, 1961, by Paramount Pictures.\n\nCJK Unified Ideographs: The Chinese, Japanese and Korean (CJK) scripts share a common background, collectively known as CJK characters.  In the process called Han unification, the common (shared) characters were identified and named \"CJK Unified Ideographs.\"  As of Unicode 10.0, Unicode defines a total of 87,882 CJK Unified Ideographs.\n\nPseudochromis fuscus: Pseudochromis fuscus is a species of saltwater fish in the Dottyback family.  Dottybacks are generally very bright in color and relatively small, factors which have made them popular among aquarium enthusiasts.  Besides their coloration and size, they are probably best known for their aggressive temperament.  While many of the more common dottybacks are in the Pseudochromis genus, there are also species in other genera.  Common names for this particular species include the brown dottyback, the golden dottyback, and the musky dottyback.  The common name “Golden dottyback” is shared with another species of dottyback, the \"Pseudochromis pseudoplesiopinae\".  The species name, \"fuscus\", means dark or dusky in Latin.\n\nRakotomalala: Rakotomalala is a common Malagasy last name.  Malagasy are citizens of Madagascar, the largest island in the Indian Ocean.  Rakoto is a common root for many Malagasy last names.  Malala means \"beloved\".  The name is so common that it is shared by a former prime minister, a UN representative and a singer who are not related.  There are Rakotomalala present in 14 different countries, which is a large number for a total Malagasy population of only 15 million people.\n\nKardashian: Kardashian (Armenian: Քարտաշեան ) is an Armenian surname (from the Armenian քարտաշ meaning \"stone carver\").\n\nBrick (soundtrack): Brick: Original Motion Picture Soundtrack is the soundtrack to the 2005 film of the same name.  It was released on March 21, 2006 by Lakeshore Records.  The soundtrack features the original score for the film composed by Nathan Johnson, lead of The Cinematic Underground as well as music by The Velvet Underground, Bunny Berigan, Anton Karas and Kay Armen and a song from the Gilbert and Sullivan operetta \"The Mikado\" recited by Nora Zehetner that was featured in the film.\n\nNational consciousness: A national consciousness is a shared sense of national identity; that is, a shared understanding that a people group shares a common ethnic/linguistic/cultural background.  Historically, a rise in national consciousness has been the first step towards the creation of a nation.  National consciousness, at a glance, is one's level of awareness, of the collective, and one's understanding that without \"them\" there is no \"us\".  It is the mere awareness of the many shared attitudes and beliefs towards things like family, customs, societal and gender roles, etc.  This awareness allows one to have a \"collective identity\" which allows them to be knowledgeable of not only where they are, but how those places and people around them are so significant in that they ultimately make the collective, a nation.  In short, national consciousness can be defined as a specific core of attitudes that provide habitual modes for regarding life's phenomena.\n\nKay Armen: Armenuhi Manoogian (Armenian: Արմենուհի Մանուկյան ); November 2, 1915 – October 3, 2011), better known by her stage name Kay Armen (Armenian: Քեյ Արմեն ), was an American Armenian singer popular during the 1940s and 1950s.  Her career in show business spanned almost six decades, as she worked in radio, television, onstage and in film.  She also wrote many songs, performed in nightclubs and recorded many records.\n\nEthnoreligious group: An ethnoreligious group (or ethno-religious group) is an ethnic group whose members are also unified by a common religious background.  Ethnoreligious communities define their ethnic identity neither by ancestral heritage nor simply by religious affiliation but often through a combination of both.  An ethnoreligious group has a shared history and a cultural tradition of its own.  In many cases ethnoreligious groups are ethno-cultural groups with a traditional ethnic religion; in other cases ethnoreligious groups begin as communities united by a common faith which through endogamy developed cultural and ancestral ties.  Some ethnoreligious groups' identities are reinforced by the experience of living within a larger community as a distinct minority.\n\nLove and Marriage (1959 TV series): Love and Marriage is an American situation comedy which aired on NBC from September 21, 1959, to January 25, 1960, starring William Demarest as William Harris, Jeanne Bal as Pat Baker, Murray Hamilton as Steve Baker, Kay Armen as Sophie, Stubby Kaye as Stubby Wilson, Susan Reilly as Susan Baker, Jennie Lynn as Jennie Baker.\n\nQuestion: What shared background do the names \"Kardashian\" and \"Kay Armen\" have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"shared_origin_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of shared origin (e.g., ethnic, linguistic, national).\"\n    },\n    \"origin_name\": {\n      \"type\": \"string\",\n      \"description\": \"The specific name of the shared origin.\"\n    },\n    \"entities_with_shared_origin\": {\n      \"type\": \"array\",\n      \"description\": \"A list of entities that share this origin, with details from the context.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"entity_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity.\"\n          },\n          \"context_confirmation\": {\n            \"type\": \"string\",\n            \"description\": \"A phrase from the context confirming the entity's origin.\"\n          }\n        },\n        \"required\": [\n          \"entity_name\",\n          \"context_confirmation\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"shared_origin_type\",\n    \"origin_name\",\n    \"entities_with_shared_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "shared_origin_type": {
        "type": "string",
        "description": "The type of shared origin (e.g., ethnic, linguistic, national)."
      },
      "origin_name": {
        "type": "string",
        "description": "The specific name of the shared origin."
      },
      "entities_with_shared_origin": {
        "type": "array",
        "description": "A list of entities that share this origin, with details from the context.",
        "items": {
          "type": "object",
          "properties": {
            "entity_name": {
              "type": "string",
              "description": "The name of the entity."
            },
            "context_confirmation": {
              "type": "string",
              "description": "A phrase from the context confirming the entity's origin."
            }
          },
          "required": [
            "entity_name",
            "context_confirmation"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "shared_origin_type",
      "origin_name",
      "entities_with_shared_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
