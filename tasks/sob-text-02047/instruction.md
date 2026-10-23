{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMulled wine: Mulled wine is a beverage usually made with red wine along with various mulling spices and sometimes raisins.  It is served hot or warm and is alcoholic, although there are non-alcoholic versions of mulled wine.  It is a traditional drink during winter, especially around Christmas.\n\nMartini (cocktail): The martini is a cocktail made with gin and vermouth, and garnished with an olive or a lemon twist.  Over the years, the martini has become one of the best-known mixed alcoholic beverages.  H. L. Mencken called the martini \"the only American invention as perfect as the sonnet\" and E. B. White called it \"the elixir of quietude\".\n\nSmoking Bishop: Smoking Bishop is a type of mulled wine, punch or wassail.  It was especially popular in Victorian England at Christmas time and it appears in Dickens' story \"A Christmas Carol\".\n\nJoulupöytä: Joulupöytä (translated \"Yule table\") is the traditional assortment of foods served at Christmas in Finland, similar to the Swedish julbord.  It contains many different dishes, most of them typical for the season.  The main dish is usually a large Christmas ham, which is eaten with mustard or bread along with the other dishes.  Fish is also served (often lutefisk and gravlax), and the ham is served with \"laatikko\"s, casseroles made with swede, potato and carrot, occasionally liver.  The traditional Christmas beverage is either alcoholic or non-alcoholic mulled wine (\"glögi\" in Finnish).\n\nAnti-tobacco movement in Nazi Germany: After German doctors became the first to identify the link between smoking and lung cancer, Germany initiated a strong anti-tobacco movement and led the first public anti-smoking campaign in modern history.  Anti-tobacco movements grew in many nations from the middle of the 19th century; the campaign in Germany, supported by the government after the Nazis came to power, is probably the best known, though in fact stronger laws were passed in some United States states between 1890 and 1930.  The German movement was the most powerful anti-smoking movement in the world during the 1930s and early 1940s.  The National Socialist leadership condemned smoking and several of them openly criticized tobacco consumption.  Research on smoking and its effects on health thrived under Nazi rule and was the most important of its type at that time.  Adolf Hitler's personal distaste for tobacco and the Nazi reproductive policies were among the motivating factors behind their campaign against smoking.\n\nWassail: Wassail ( , ; Old Norse \"ves heil\", Old English \"was hál\", literally: \"be hale\") is a beverage of hot mulled cider, traditionally drunk as an integral part of wassailing, a Medieval English drinking ritual intended to ensure a good cider apple harvest the following year.\n\nWine bar: A wine bar (also known as a bodega) is a tavern-like business focusing on selling wine, rather than liquor or beer.  A typical feature of many wine bars is a wide selection of wines available by the glass.  Some wine bars are profiled on wines of a certain type of origin, such as Italian wine or Champagne.  While many wine bars are private \"stand-alone\" establishments, in some cases, wine bars are associated with a specific wine retailer or other outlet of wine, to provide additional marketing for that retailer's wine portfolio.  In countries where licensing regulations allow this, some wine bars also sell the wines they serve, and effective function as a hybrid between a wine shop and a wine bar.\n\nFeuerzangenbowle: Feuerzangenbowle (] ) is a traditional German alcoholic drink for which a rum-soaked sugarloaf is set on fire and drips into mulled wine.  It is often part of a Christmas or New Year's Eve tradition.  The name translates literally to \"fire-tongs punch\".\n\nMulling spices: Mulling spices is a spice mixture used in drink recipes.  The spices are usually used to spice hot apple cider, mulled wine, wassail, and other drinks (such as juices) during the autumn or winter.  A \"mulled\" drink is a drink which has been prepared with these spices (usually through heating the drink in a pot with mulling spices and then straining).  Mulling spices may also be added to the brewing process to make spiced beer.\n\nOz and Hugh Drink to Christmas: Oz and Hugh Drink to Christmas is a BBC television programme in which wine personality Oz Clarke and comedian Hugh Dennis travel through Britain to sample a wide array of seasonal Christmas beverages, including whisky, winter ales, mulled wine, wassail, sloe gin, Buck's Fizz, Port wine and Sherry.  Upon its 20 December 2009 broadcast on BBC Two, it had a viewership of approximately 2.4 million with an audience share of 9%.\n\nQuestion: Which is a type of mulled wine, punch or wassail -- Smoking Bishop or Martini?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"query_category\": {\n      \"type\": \"string\",\n      \"description\": \"The category of beverage being queried.\"\n    },\n    \"beverage_candidates\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the candidate beverage.\"\n          },\n          \"description_from_context\": {\n            \"type\": \"string\",\n            \"description\": \"The description of the beverage as found in the context.\"\n          },\n          \"is_a_match\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the beverage matches the query category, false otherwise.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"description_from_context\",\n          \"is_a_match\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"identified_beverage\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the beverage that is a type of mulled wine, punch, or wassail.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for why the identified beverage is the correct answer.\"\n    }\n  },\n  \"required\": [\n    \"query_category\",\n    \"beverage_candidates\",\n    \"identified_beverage\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "query_category": {
        "type": "string",
        "description": "The category of beverage being queried."
      },
      "beverage_candidates": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the candidate beverage."
            },
            "description_from_context": {
              "type": "string",
              "description": "The description of the beverage as found in the context."
            },
            "is_a_match": {
              "type": "boolean",
              "description": "True if the beverage matches the query category, false otherwise."
            }
          },
          "required": [
            "name",
            "description_from_context",
            "is_a_match"
          ],
          "additionalProperties": false
        }
      },
      "identified_beverage": {
        "type": "string",
        "description": "The name of the beverage that is a type of mulled wine, punch, or wassail."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for why the identified beverage is the correct answer."
      }
    },
    "required": [
      "query_category",
      "beverage_candidates",
      "identified_beverage",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
