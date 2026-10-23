{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMaruti Suzuki: Maruti Suzuki India Limited, formerly known as Maruti Udyog Limited, is an automobile manufacturer in India.  It is a 56.21%-owned subsidiary of Japanese automobile and motorcycle manufacturer Suzuki Motor Corporation.  s of 2017 , it had a market share of 51% of the Indian passenger car market.  Maruti Suzuki manufactures and sells popular cars such as the Ciaz, Ertiga, Wagon R, Alto, Swift, Celerio, Swift Dzire, Omni, Baleno and Baleno RS.  The company is headquartered at New Delhi.  In February 2012, the company sold its ten millionth vehicle in India.\n\nTobermory distillery: Tobermory distillery is a Scotch whisky distillery situated on the Hebridean island of Mull, Scotland in the village of Tobermory.  The distillery, which was formerly known as Ledaig, was founded in 1798 and has changed hands several times, having undergone a number of periods of closure.  The only distillery on Mull, it is currently owned by Burn Stewart Distillers, a subsidiary of Distell Group Limited of South Africa.  Its main product, Tobermory single malt, is used in the blends Scottish Leader and Black Bottle.  The distillery also produces a smaller amount of peated whisky, which remains known under the former name, Ledaig.\n\nLindsay Manufacturing: Lindsay Corporation (), formerly known as Lindsay Manufacturing Co., is a manufacturer of \"Zimmatic\" brand center pivot irrigation systems, based in the U.S. state of Nebraska.  It also manufactures farm and construction machinery, as well as road and railroad infrastructure equipment.  The company states that it has a market capitalization of $547,584,000.  At August 31, 2008, the company had 1,239 employees.\n\nBrown-Forman: The Brown-Forman Corporation is one of the largest American-owned companies in the spirits and wine business.  Based in Louisville, Kentucky, it manufactures several well known brands throughout the world, including Jack Daniel's, Early Times, Old Forester, Woodford Reserve, Canadian Mist, GlenDronach, BenRiach, Glenglassaugh, Finlandia, Herradura, Korbel, and Chambord.  Brown-Forman formerly owned Southern Comfort and Tuaca before selling them off in 2016.\n\nClear Creek Distillery: Clear Creek Distillery is a distillery based in Portland, Oregon.  Founded in 1985, it has been owned by Hood River Distillers since 2014.  It is most well known for its \"eau de vie\" produced from Bartlett pears, though today it also makes a variety of other fruit brandies, aged spirits, and liqueurs.\n\nAuchenblae: Auchenblae (Scottish Gaelic: \"Achadh nam Blàth\" ) is a village in the Kincardine and Mearns area of Aberdeenshire, formerly in Kincardineshire, Scotland.  It is featured in Lewis Grassic Gibbon's novel, Sunset Song.  The name is a derivation from the Gaelic for \"Field of Flowers\" possibly due to the growing of flax in bygone times.  The village was known for its weavers, a whisky distillery and the annual Paldie's Fair horse market.  The current parish church, on the opposite side of the Luther Water was built next to an older chapel dedicated to St. Palladius and was formerly known as Fordoun Parish Church.  This location, known as at Kirkton of Fordoun was the birthplace of the chronicler John of Fordun (before 1360 – c. 1384) and has been a religious site since the 7th century.  St Palladius died and was reputedly buried here.  There is a Pictish cross slab, the Fordoun Stone, in the kirk's vestibule.  In the graveyard is the ancient ruin of St Palladius' Chapel and there is a memorial to Scotland's first Protestant martyr George Wishart, born at Mains of Pittarrow in the old parish of Fordoun and burnt at the stake under the orders of Cardinal Beaton in St Andrews.\n\nTalisker distillery: Talisker distillery is an Island single malt Scotch whisky distillery based in Carbost, Scotland on the Isle of Skye.  The distillery is operated by Diageo, and is marketed as part of their \"Classic Malts\" series.  The brand is sold as a premium whisky.\n\nWoodford Reserve: The Woodford Reserve Distillery, formerly known as the Old Oscar Pepper Distillery and later the Labrot & Graham Distillery, is approximately eight miles from the town of Versailles in north-central Kentucky, off U.S. Route 60 between Interstate 64 and Versailles.\n\nThe London Distillery Company: The London Distillery Company, also known as TLDC, is a distillery based in a former Victorian dairy cold room in Battersea, London.  TLDC produce English Whisky, London Gin and British spirits, compounds and cordials.  TLDC also creates experimental spirits under the TESTBED brand; named after the art space of similar ethos by architect Will Alsop.\n\nBuffalo Trace Distillery: Buffalo Trace Distillery is a distillery located in Frankfort, Kentucky.  It has historically been known by several names, including most notably, the George T. Stagg Distillery and the O.F.C. Distillery.  Its namesake bourbon brand, \"Buffalo Trace\" Kentucky Straight Bourbon whiskey, was introduced in August 1999.  The company claims the distillery is the oldest continuously-operating distillery in the United States.  Located on what the company claims was once an ancient buffalo crossing on the banks of the Kentucky River in Franklin County, the distillery is named after the American bison.  The Sazerac Company, an American family-owned producer and importer based in New Orleans, Louisiana, purchased the distillery in 1992 and is now the parent company of Buffalo Trace Distillery.\n\nQuestion: Where is the manufacturer who manufactures the brand formerly known as the Old Oscar Pepper Distillery based?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"manufacturer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company that manufactures the brand.\"\n    },\n    \"brand_name\": {\n      \"type\": \"string\",\n      \"description\": \"The current name of the brand.\"\n    },\n    \"former_brand_name\": {\n      \"type\": \"string\",\n      \"description\": \"The former name of the brand or distillery.\"\n    },\n    \"manufacturer_headquarters_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the manufacturer is based.\"\n    },\n    \"manufacturer_headquarters_state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the manufacturer is based.\"\n    }\n  },\n  \"required\": [\n    \"manufacturer_name\",\n    \"brand_name\",\n    \"former_brand_name\",\n    \"manufacturer_headquarters_city\",\n    \"manufacturer_headquarters_state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "manufacturer_name": {
        "type": "string",
        "description": "The name of the company that manufactures the brand."
      },
      "brand_name": {
        "type": "string",
        "description": "The current name of the brand."
      },
      "former_brand_name": {
        "type": "string",
        "description": "The former name of the brand or distillery."
      },
      "manufacturer_headquarters_city": {
        "type": "string",
        "description": "The city where the manufacturer is based."
      },
      "manufacturer_headquarters_state": {
        "type": "string",
        "description": "The state where the manufacturer is based."
      }
    },
    "required": [
      "manufacturer_name",
      "brand_name",
      "former_brand_name",
      "manufacturer_headquarters_city",
      "manufacturer_headquarters_state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
