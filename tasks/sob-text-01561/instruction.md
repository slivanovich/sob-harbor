{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of Legend of the Seeker episodes: The following is an episode list for the American television series \"Legend of the Seeker\" that is produced by ABC Studios and distributed in domestic syndication by Disney-ABC Domestic Television.  The show is based on the fantasy novel series \"The Sword of Truth\" written by Terry Goodkind and follows a woods guide who, after being thrust into a world of magic, is charged with the responsibility to protect the world from evil.  The first season premiered with a double bill on November 1, 2008.  The series was renewed for a second season in January 2009, which premiered on November 7, 2009.  On April 26, 2010 Ausiello Files reported that the series has been cancelled and will not return for a third season.  Fans of the series have responded by launching a renewal campaign titled \"Save Our Seeker\".  Terry Goodkind has expressed his support for the campaign.\n\nAmos Oz: The Nature of Dreams: Amos Oz: The Nature of Dreams is an Israeli documentary film, written, directed and produced by Yonathan and Masha Zur (Yonathan & Masha Films).  It is a portrait of Israeli author Amos Oz, author of the memoir \"A Tale of Love and Darkness\", and his efforts toward peace in the Middle East.\n\nWarheart: Warheart is Terry Goodkind's eighteenth novel.  It's the 15th in the \"The Sword of Truth\" series and the fourth novel in Goodkind's new Richard and Kahlan series, which takes off right after the end of the original Sword of Truth series.\n\nChristopher Stasheff: Christopher Stasheff (born 1944) is an American science fiction author and fantasy author whose novels include \"The Warlock in Spite of Himself\" (1969) and \"Her Majesty's Wizard\" (1986).  He has a PhD.  in Theatre and taught radio and television at Eastern New Mexico University in Portales, New Mexico; he is now retired and living in Champaign, Illinois.  Stasheff has been noted for his blending of science fiction and fantasy, as seen in his \"Warlock\" series, which placed an \"'epic fantasy' in a science fictional frame\".  Stasheff's writing is often seen in the moral and ethical mentor style similar to Terry Goodkind, Terry Brooks or J.R.R. Tolkien.\n\nA Tale of Love and Darkness (film): A Tale of Love and Darkness is a 2015 drama film directed by Natalie Portman, based on the autobiographical novel of the same name by Israeli author Amos Oz.  It takes place in Jerusalem in the last years of Mandatory Palestine and the first years of independent Israel, and stars Amir Tessler as Oz, and Gilad Kahana and Portman as his parents.  It is Portman's directorial feature debut.  It was screened at the 2015 Cannes Film Festival and in the Special Presentations section of the 2015 Toronto International Film Festival.\n\nShroud of Eternity: Shroud of Eternity is the second installment in Terry Goodkind's \"The Nicci Chronicles\", Goodkind's new series set in the same world of his now-concluded \"Sword of Truth\".  The novel follows \"Death's Mistress\", and will be released on 9 January 2018.\n\nTerry Goodkind: Terry Goodkind (born 1948) is an American writer.  He is known for the epic fantasy series \"The Sword of Truth\" as well as the contemporary suspense novel \"The Law of Nines\" (2009), which has ties to his fantasy series.  \"The Sword of Truth\" series sold 25 million copies worldwide and was translated into more than 20 languages.  Additionally, it was adapted into a television series called \"Legend of the Seeker\", which premiered on November 1, 2008 and ran for two seasons, ending in May 2010.\n\nAmos Oz: Amos Oz (Hebrew: עמוס עוז‎ ; born Amos Klausner; May 4, 1939) is an Israeli writer, novelist, journalist and intellectual.  He is also a professor of literature at Ben-Gurion University in Beersheba.  He is regarded as Israel's most famous living author.\n\nThe First Confessor: The Legend of Magda Searus: The First Confessor: The Legend of Magda Searus is Terry Goodkind's 15th novel.  The book is set centuries prior to the main \"Sword of Truth\" series.  It is the first book that is self-published by Terry Goodkind.  Apart from 300 individually-numbered copies of a Limited Collector's Edition it was originally exclusively available as E-book and Audiobook.  As of July 2015, it was published by TOR Fantasy in hardcover format, and is now available in stores.\n\nSevered Souls: Severed Souls is Terry Goodkind's 17th novel.  It's the 14th in the Sword of Truth series and the third novel in Goodkind's new Richard and Kahlan series, which takes off right after the end of the original Sword of Truth series.\n\nQuestion: Amos Oz and Terry Goodkind, are in a similar occupation industry?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"authors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"occupation_details\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"occupation_details\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"occupation_industry_similar\": {\n      \"type\": \"boolean\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"authors\",\n    \"occupation_industry_similar\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "authors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "occupation_details": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "occupation_details"
          ],
          "additionalProperties": false
        }
      },
      "occupation_industry_similar": {
        "type": "boolean"
      },
      "reasoning": {
        "type": "string"
      }
    },
    "required": [
      "authors",
      "occupation_industry_similar",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
