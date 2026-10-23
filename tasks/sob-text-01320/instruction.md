{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIowa Alcoholic Beverages Division: The Iowa Alcoholic Beverages Division is the alcoholic beverage control authority for the U.S. state of Iowa.  Since March 8, 1934, it has regulated the traffic in, and maintained a monopoly on the wholesaling of, alcoholic beverages in the state, thus making Iowa an alcoholic beverage control state.\n\nPaulaner Brewery: Paulaner is a German brewery, established in 1634 in Munich by the Minim friars of the \"Neudeck ob der Au\" cloister.  The mendicant order and the brewery are named after Francis of Paola, the founder of the order.  Paulaner is one of the six breweries who provide beer for Oktoberfest, the German beer festival dating from 1810.\n\nBeer by region: This is a list of articles and categories dealing with beer by region, including breweries and brewing in general.  Beer is the world's most widely consumed alcoholic beverage, and is the third-most popular drink overall, after water and tea.  It is thought by some to be the oldest fermented beverage.  A brewery is a dedicated building for the making of beer, though beer can be made at home, and has been for much of beer's history.  A company that makes beer is called either a brewery or a brewing company.  The diversity of size in breweries is matched by the diversity of processes, degrees of automation, and kinds of beer produced in breweries.  A brewery is typically divided into distinct sections, with each section reserved for one part of the brewing process.\n\nVirginia Alcoholic Beverage Control Board: The Virginia Alcoholic Beverage Control Board is a three-person board that oversees the Virginia Department of Alcoholic Beverage Control.  The Board consists of a chairperson and two commissioners who direct all agency operations.  Board members are full-time state employees appointed by the Governor of Virginia.\n\nCaffeinated alcoholic drink: A caffeinated alcoholic drink, or caffeinated alcoholic beverage, is a drink that contains both alcohol (also known formally as ethanol) and caffeine.  They often include the ingredients of energy drinks as well.  In 2010 and 2011, this type of beverage faced criticism for posing health risks to their drinkers.  In some places there is a ban on caffeinated alcoholic beverages.\n\nList of cider brands: This is a list of cider brands.  Cider is an alcoholic beverage made exclusively from the juice of specially grown varieties of apples.  This list does not include perry, which is a similar alcoholic beverage made from specially grown pear varieties.  Craft cider makers claim that mass-produced ciders are mostly not actually ciders because of their production processes and additives including artificial sweeteners like aspartame.\n\nNockherberg: Nockherberg is the name of a small terrace on the slope of the eastern bank of the Isar in Munich, situated in the urban district of Au.  An annual beer festival rich in tradition takes place there in the Paulaner Brewery - the \"Salvator-Ausschank auf dem Nockherberg\" The name of the raised terrace is often used synonymously for this festival or its opening event, the tapping of the first barrel of a strong, seasonal beer (\"Starkbieranstich\").\n\nAragh Sagi: Aragh Sagi (or Araq Sagi) literally meaning \"Doggy distillate\" is a type of distilled alcoholic beverage in Iran which contains at least 65% pure ethanol.  It is usually produced at homes from raisins. Its production and possession by ordinary citizens is considered illegal in Iran (which is the case for all alcoholic beverages).  Prior to 1979 revolution in Iran this product had been produced traditionally in several cities of Iran.  Since it was outlawed after 1979, it became a black market and underground business.  Today, Aragh Sagi is widely considered a cheap alcoholic beverage that consumers choose due to lack of other available options.\n\nAlcohol congener analysis: Alcohol congener analysis of blood and urine is used to provide an indication of the type of alcoholic beverage consumed.  The analysis involves investigating compounds called congeners that give the beverage a distinctive appearance, aroma, and flavour, not including water and ethanol.  The theory of discovering one’s drinking habits has been investigated since the late 1970s, predominantly in Germany, for \"hip-flask\" defence type cases (after-drinking).  Alcohol congener analysis can play a crucial role in these cases where the driver is apprehended some time after a motor vehicle incident who, when returning a positive alcohol reading then claim that this is due to drinking an alcoholic beverage only after the incident.  This traditional methodology for congener analysis has focused solely on the detection of fermentation by-product congeners that are found in all alcoholic beverages.  By comparing the ratios of a set standard of congeners, the ingested alcoholic beverage type is proposed.\n\nArkansas Alcoholic Beverage Control Division: The Alcoholic Beverage Control Division is an Arkansas state government agency.  The duties of the Alcoholic Beverage Control - Administration Division are to receive applications for and issue, refuse to issue, suspend or revoke permits to manufacture, wholesale, retail and transport alcoholic beverages in Arkansas.\n\nQuestion: What type of alcoholic beverage is served at the brewery established in 1634 during the annual festival at Nockherberg ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"brewery_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the brewery.\"\n    },\n    \"establishment_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the brewery was established.\"\n    },\n    \"festival_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"festival_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the annual festival.\"\n        },\n        \"festival_location\": {\n          \"type\": \"string\",\n          \"description\": \"The location where the festival takes place.\"\n        }\n      },\n      \"required\": [\n        \"festival_name\",\n        \"festival_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"alcoholic_beverage_served\": {\n      \"type\": \"string\",\n      \"description\": \"The type of alcoholic beverage served at the festival.\"\n    },\n    \"beverage_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country or region of origin for the beverage.\"\n    }\n  },\n  \"required\": [\n    \"brewery_name\",\n    \"establishment_year\",\n    \"festival_details\",\n    \"alcoholic_beverage_served\",\n    \"beverage_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "brewery_name": {
        "type": "string",
        "description": "The name of the brewery."
      },
      "establishment_year": {
        "type": "integer",
        "description": "The year the brewery was established."
      },
      "festival_details": {
        "type": "object",
        "properties": {
          "festival_name": {
            "type": "string",
            "description": "The name of the annual festival."
          },
          "festival_location": {
            "type": "string",
            "description": "The location where the festival takes place."
          }
        },
        "required": [
          "festival_name",
          "festival_location"
        ],
        "additionalProperties": false
      },
      "alcoholic_beverage_served": {
        "type": "string",
        "description": "The type of alcoholic beverage served at the festival."
      },
      "beverage_origin": {
        "type": "string",
        "description": "The country or region of origin for the beverage."
      }
    },
    "required": [
      "brewery_name",
      "establishment_year",
      "festival_details",
      "alcoholic_beverage_served",
      "beverage_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
