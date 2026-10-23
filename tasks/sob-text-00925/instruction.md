{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHello Mr. Monkey: \"Hello Mr. Monkey\" is a disco song by the all-girl trio, Arabesque.  Initially released only in Germany in 1977, it was released worldwide in 1978.\n\nCracked (magazine): Cracked was an American humor magazine.  Founded in 1958, \"Cracked\" proved to be the most durable of the many publications to be launched in the wake of \"Mad\" magazine.\n\nHeliocybe: Heliocybe is an agaric genus closely allied to \"Neolentinus\" and the bracket fungus, \"Gloeophyllum\", all of which cause brown rot of wood.  Heliocybe sulcata, the type and sole species, is characterized by thumb-sized, tough, revivable, often dried, mushroom fruitbodies, with a tanned symmetric pileus that is radially cracked into a cartoon sun-like pattern of arranged scales and ridges, distant serrated lamellae, and a scaly central stipe.  Microscopically it differs from \"Neolentinus\" by the absence of clamp connections. Like \"Neolentinus\", it produces abundant, conspicuous pleurocystidia.  \"Heliocybe sulcata\" typically fruits on decorticated, sun-dried and cracked wood, such as fence posts and rails, vineyard trellises in Europe, branches in slash areas, and semi-arid areas such on sagebrush or on naio branches in rain shadow areas of Hawaii, or in open pine forests.\n\nPeter Raymont: Peter Raymont (born February 28, 1950 in Ottawa, Ontario) is a Canadian filmmaker and producer and the president of White Pine Pictures, an independent film, television and new media production company based in Toronto.  Among his films are \"\" (2005), \"A Promise to the Dead: The Exile Journey of Ariel Dorfman\" (2007), \"The World Stopped Watching\" (2003) and \"The World Is Watching\" (1988).  The 2011 feature documentary \"West Wind: The Vision of Tom Thomson\" and 2009's \"Genius Within: The Inner Life of Glenn Gould\", were co-directed with Michèle Hozer.  Raymont is Executive Producer of the television drama series, The Border, which he co-created with Lindalee Tracey, Janet MacLean and Jeremy Hole.  The Border's 3 seasons have been broadcast in more than 25 countries.  He is also the Executive Producer of the CBC drama series, Cracked, a Toronto-based police procedural which explores the intersection of the law and mental illness. [ Cracked's 2 seasons are also broadcast in France, Germany, USA and elsewhere.\n\nHello Pappy scandal: The \"Hello Pappy\" scandal, alluding to the nickname of involved host Willie Revillame and the Hello Garci scandal, was a scandal surrounding an incident during the August 20, 2007 episode of the Filipino variety show \"Wowowee\", broadcast by ABS-CBN.  During the episode, a technical error occurred during the final jackpot round of the show's \"Wilyonaryo\" segment which raised allegations within the media that the segment was, or could be, rigged by the producers.  The incident prompted an investigation by the country's Department of Trade and Industry, and was also the catalyst of an on-air feud between Revillame and Joey de Leon, a personality from the rival GMA Network.\n\nMedia type: A media type (also MIME type and content type) is a two-part identifier for file formats and format contents transmitted on the Internet.  The Internet Assigned Numbers Authority (IANA) is the official authority for the standardization and publication of these classifications.  Media types were originally defined in Request for Comments 2045 in November 1996 as a part of \"MIME (Multipurpose Internet Mail Extensions)\" specification, for denoting type of email message content and attachments; hence the name \"MIME type\".  Media types are also used by other internet protocols such as HTTP and document file formats such as HTML, for similar purpose.\n\nHello Mr.: Hello Mr., stylized as hello mr., is a biannual American lifestyle magazine focused on topics of interest to gay men.  The magazine describes itself as being \"about men who date men,\" though the magazine tackles both queer and queer-adjacent topics.  Each issue, between 150 and 200 pages in length, features fiction, personal essays, interviews, art, and photography and photo essays.\n\nWrite strategy: In DVD authoring, a write strategy is a set of low-level parameters that enables an optical disc drive to write on a specific type of blank media according to its optimum specifications.  The media type is identified by the manufacturer and media ID, which is often unrelated to the brand of the media due to rebadging.  Write strategies are essential for compatibility with various types of blank media, and are typically stored in the drive's firmware.  If a drive lacks a write strategy for a media type, it will only be able to write using minimum speed.  Drive manufacturers typically include new or improved write strategies as part of a firmware upgrade, in order to extend or improve compatibility with blank media.  In cases where official support for a drive has been discontinued or is deemed unsatisfactory, users have come up with ways to patch the write strategies by modding the drive's firmware.\n\nAló Presidente: Aló Presidente (English: \"Hello Mr. President\") was a largely unscripted talk show that was hosted by Venezuelan President Hugo Chávez.  It was broadcast on Venezuelan state television and radio stations every Sunday at 11:00 AM.  The program did not have a fixed ending time, but usually ended by 5:00 PM, or as the program dynamics permitted.  The show promoted the \"Bolivarian Revolution\" and blamed Venezuelan economic problems on its northern neighbor, the United States.  Many Venezuelans tuned in because Chávez was known for unveiling new financial assistance packages every weekend.  Beginning in 1999, Chávez spent an average of 40 hours a week on television promoting his \"Bolivarian Revolution\" policies.\n\nLee In-sung: Lee In-sung (born July 28, 1996) is a South Korean actor.  He began his entertainment career as a child actor, notably in the comedy film \"Cracked Eggs and Noodles\" and the third season of sitcom \"Hello Franceska\" (both in 2005).\n\nQuestion: Hello Mr. and Cracked and what type of media?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entities\": {\n      \"type\": \"array\",\n      \"description\": \"List of entities mentioned in the question and their attributes.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity.\"\n          },\n          \"media_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of media for the entity.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"media_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_media_type\": {\n      \"type\": \"string\",\n      \"description\": \"The common media type shared by all entities, if applicable.\"\n    },\n    \"media_type_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of distinct media types identified.\"\n    }\n  },\n  \"required\": [\n    \"entities\",\n    \"common_media_type\",\n    \"media_type_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entities": {
        "type": "array",
        "description": "List of entities mentioned in the question and their attributes.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the entity."
            },
            "media_type": {
              "type": "string",
              "description": "The type of media for the entity."
            }
          },
          "required": [
            "name",
            "media_type"
          ],
          "additionalProperties": false
        }
      },
      "common_media_type": {
        "type": "string",
        "description": "The common media type shared by all entities, if applicable."
      },
      "media_type_count": {
        "type": "integer",
        "description": "The number of distinct media types identified."
      }
    },
    "required": [
      "entities",
      "common_media_type",
      "media_type_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
