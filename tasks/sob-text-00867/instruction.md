{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRich, Young and Pretty: Rich, Young and Pretty is a 1951 musical film produced by Joe Pasternak for Metro-Goldwyn-Mayer and directed by Norman Taurog.  Written by Dorothy Cooper and adapted as a screenplay by Sidney Sheldon, the film starred Jane Powell, Danielle Darrieux, Wendell Corey, and Fernando Lamas, The Four Freshmen, and introduced Vic Damone.  This was Darrieux's first Hollywood film since \"The Rage of Paris\" (1938).\n\nCara Quici: Cara Elizabeth Quici (born May 30) is an American singer, songwriter, and actress born and raised in Corpus Christi, Texas now living in New York City and Los Angeles.\n\nGertrude Maesmore Morris: Gertrude Maesmore Morris (née Wilmot; 1872–1952), often known as Mrs Maesmore Morris, was an English actress born in London who rose to fame in Australia.  Her marriage to Maesmore Morris ended in divorce in 1905.\n\nBiyouna: Baya Bouzar (Arabic: باية بوزار‎ ‎ ), known by the stagename Biyouna (بيونة ) is an Algerian singer, dancer, actress born on September 13, 1952 in Belcourt, now known as Belouizdad, Algiers, Algeria.\n\nIrene Gorovaia: Irene Gorovaia (Russian: Ирина Горовая ; born June 13, 1989), also credited as Irina Gorovaia, is an American actress born in Russia and raised in Brooklyn, New York.  She has been a ballet dancer for many years, training with the School of American Ballet.\n\nYasmeen Sulieman: Yasmeen Sulieman (born May 19, 1982) is an American singer, songwriter and Broadway actress born in Oakland, California and raised in Hawaii.  She is best known for her 2002 R&B single \"Blue Jeans\" in addition to her ensemble work in the Tony Award-winning Broadway musical \"\" which she joined in 2014.\n\nGeorgia Carroll: Georgia Carroll (November 18, 1919 – January 14, 2011) was an American singer, fashion model, and actress, best known for her work with Kay Kyser's big band orchestra in the mid-1940s.\n\nLouisa Lytton: Louisa Claire Lytton (born 7 February 1989) is an English actress born in Camden and living in Islington.  She rose to fame in 2005 when joining \"EastEnders\" as Ruby Allen.  After leaving \"EastEnders\" in November 2006, Lytton joined \"The Bill\" as PC Beth Green, a role she played from May 2007 to March 2009.  She also appeared on \"Strictly Come Dancing\" in 2006.  Lytton also represented the UK at the Eurovision Dance Contest 2008 in Glasgow and finished in 9th place out of 14 with 47 points.\n\nJane Powell: Jane Powell (born Suzanne Lorraine Burce; April 1, 1929) is an American singer, dancer and actress who rose to fame in the mid-1940s with roles in various musicals as a contract player for Metro-Goldwyn-Mayer pictures.\n\nTiffany Evans: Tiffany Evans (born August 4, 1992) is an American singer, songwriter, actress, dancer and entrepreneur.  Evans rose to fame in 2003 as a contestant on \"Star Search,\" hosted by Arsenio Hall.  The pint-sized singer, with a magnificent voice, snagged the title of Grand Champion in the junior singer division.  She became the first contestant in \"Star Search\" history to earn a perfect score on all of her performances.  Following Evans' victory, she signed a record deal with Columbia Records in the same year.  Her self-titled debut album was released in 2008 and included her hit singles \"Promise Ring\" featuring Ciara and \"I'm Grown\" featuring Bow Wow.\n\nQuestion: When was the American singer, dancer and actress born who rose to fame in the mid-1940s and was a star in Rich, Young and Pretty?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person identified.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the person.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of the person's professions.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\",\n        \"professions\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film the person starred in.\"\n        }\n      },\n      \"required\": [\n        \"title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"fame_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"period_of_rise_to_fame\": {\n          \"type\": \"string\",\n          \"description\": \"The period when the person rose to fame.\"\n        }\n      },\n      \"required\": [\n        \"period_of_rise_to_fame\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_details\",\n    \"film_details\",\n    \"fame_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person identified."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the person."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of the person's professions."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the person."
          }
        },
        "required": [
          "name",
          "birth_date",
          "professions",
          "nationality"
        ],
        "additionalProperties": false
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film the person starred in."
          }
        },
        "required": [
          "title"
        ],
        "additionalProperties": false
      },
      "fame_details": {
        "type": "object",
        "properties": {
          "period_of_rise_to_fame": {
            "type": "string",
            "description": "The period when the person rose to fame."
          }
        },
        "required": [
          "period_of_rise_to_fame"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_details",
      "film_details",
      "fame_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
