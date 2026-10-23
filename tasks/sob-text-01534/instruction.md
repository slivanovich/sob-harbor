{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFlag of the Czech Republic: The national flag of the Czech Republic (Czech: \"státní vlajka České republiky\" ) is the same as the flag of the former Czechoslovakia.  Upon the dissolution of Czechoslovakia, the Czech Republic kept the Czechoslovak flag while Slovakia adopted its own flag.  The first flag of Czechoslovakia was based on the flag of Bohemia, and was white over red.  This was almost identical to the flag of Poland (only the proportion was different), so a blue triangle was added at the hoist in 1920.  The flag was banned by the Nazis in 1939, and a horizontal tricolor of white, red, and blue was enforced.  The 1920 flag was restored in 1945.\n\nOrder of Tomáš Garrigue Masaryk: The Order of Tomáš Garrigue Masaryk () is an Order of the Czech Republic and the former Czechoslovakia.  It was established in 1990 after the Velvet Revolution, and re-established in 1994 (following the dissolution of Czechoslovakia).  The President of the Czech Republic awards it to individuals who have made outstanding contributions to the development of democracy, humanity and human rights.  The order has five classes, of which class I is the highest.  The order is named in honor of Tomáš Garrigue Masaryk, an advocate of Czechoslovak independence and the first President of Czechoslovakia.\n\nJiří Louda: Jiří Louda (October 3, 1920 – September 1, 2015) was a Czech heraldist and veteran of World War II.  Louda was considered among the leading coats of arms designers in the Czech Republic and the former Czechoslovakia.  He designed the current coat of arms of the Czech Republic, adopted in 1992, which incorporates the displays of the three historic Czech lands.  Louda also designed the standard (official presidential flag) of President of the Czech Republic, which was adopted in 1993 following the country's independence.  Additionally, Louda created coat of arms of the Olomouc Region, as well as the municipal coats of arms for more than 200 towns and cities throughout the Czech Republic.\n\nJohann Joseph Abert: Johann Joseph Abert (20 September 1832 – 1 April 1915 in Stuttgart) was a German composer.  An ethnic German from the Sudetenland, he is also known by his Czech name Jan Josef Abert.\n\nCzech Republic–Greece relations: Czech Republic–Greece relations are foreign relations between the Czech Republic and Greece.  The diplomatic relations between Greece and former Czechoslovakia were established in 1920 - after Czechoslovakia’s foundation.  Czech Republic and Greece established diplomatic relations on January 1, 1993.  Each country has an embassy in the other's capital.  Both countries are members of European Union and NATO.\n\nSudetenland: The Sudetenland ( ; ] ; Czech and Slovak: \"Sudety\" ; Polish: \"Kraj Sudecki\" ) is the name for the northern, southern, and western areas of former Czechoslovakia which were inhabited primarily by Sudeten Germans.  These German speakers had predominated in the border districts of Bohemia, Moravia, and Czech Silesia from the time of the Austrian Empire.\n\nJohann Joseph Thalherr: Johann Joseph Thalherr (or Talherr), also known as Czech: Jan Josef Talherr or Hungarian: József Talherr (1730 – 16 October 1801), was an Austrian architect.\n\nJan Josef Ignác Brentner: Jan Josef Ignác Brentner (\"Johann Joseph Ignaz\", surname also spelled Brenntner, Brendner, Brendtner, or Prentner) (November 3, 1689 – June 28, 1742), was a Czech composer of the Baroque era.\n\nKarel Gott: Karel Gott (born 14 July 1939, in Plzeň) is a Czech singer, and an amateur painter.  He is considered the most successful male singer in the former Czechoslovakia and the Czech Republic, and has been voted the country's best male singer in the annual \"Český slavík\" (Czech Nightingale) national poll 41 times, most recently in 2016.  He has also achieved considerable success in the German-speaking countries, where he is known as \"the Golden Voice of Prague\", winning the Goldene Stimmgabel award three times (1982, 1984, and 1995).  Over the course of his career he has released over 100 albums and 100 compilation albums, and has sold an estimated 50–100 million records worldwide, 23 million of them in the German-speaking market, and about 15 million in Czechoslovakia and its successor states (Czech Republic and Slovakia).\n\nCzechoslovak Hussite Church: The Czechoslovak Hussite Church (Czech: \"Církev československá husitská\" , \"CČSH\" or \"CČH\") is a Christian church that separated from the Roman Catholic Church after World War I in former Czechoslovakia.  It traces its tradition back to the Hussite reformers and acknowledges Jan Hus (John Huss) as its predecessor.  It was well-supported by Czechoslovakia's first president, Tomáš Garrigue Masaryk, who himself belonged to the Evangelical Church of Czech Brethren—the main Protestant denomination in what is now the Czech Republic.\n\nQuestion: What was the name of the inhabitants for the northern, southern, and western areas of former Czechoslovakia where  a German composerknown by his Czech name Jan Josef Abert  is from? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"region_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the geographical region in former Czechoslovakia.\"\n    },\n    \"inhabitant_group_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the primary inhabitants of the specified region.\"\n    },\n    \"composer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the composer.\"\n        },\n        \"czech_name\": {\n          \"type\": \"string\",\n          \"description\": \"The Czech name of the composer.\"\n        },\n        \"origin_region\": {\n          \"type\": \"string\",\n          \"description\": \"The region the composer was from.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"czech_name\",\n        \"origin_region\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"region_name\",\n    \"inhabitant_group_name\",\n    \"composer_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "region_name": {
        "type": "string",
        "description": "The name of the geographical region in former Czechoslovakia."
      },
      "inhabitant_group_name": {
        "type": "string",
        "description": "The name of the primary inhabitants of the specified region."
      },
      "composer_details": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the composer."
          },
          "czech_name": {
            "type": "string",
            "description": "The Czech name of the composer."
          },
          "origin_region": {
            "type": "string",
            "description": "The region the composer was from."
          }
        },
        "required": [
          "full_name",
          "czech_name",
          "origin_region"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "region_name",
      "inhabitant_group_name",
      "composer_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
