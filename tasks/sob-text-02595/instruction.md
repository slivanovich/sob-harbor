{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOrex Exploration: Orex Exploration is a Canadian advanced stage junior gold exploration company headquartered in Montreal, Quebec.  It operates in Nova Scotia, Canada with a focus on exploring former gold mines and properties in the Goldboro, Nova Scotia, and surrounding areas of Guysborough County, Nova Scotia.\n\nClarence Gillis: Clarence (Clarie) Gillis, MP (October 3, 1895 – December 17, 1960) was a Canadian social democratic politician and trade unionist from Cape Breton Island, Nova Scotia.  He was born on Nova Scotia's mainland, but grew-up in Cape Breton.  He worked in the island's underground coal mines operated by the British Empire Steel and Coal Company (BESCO).  He also served as a member of the infantry in the Canadian Corps in Flanders during the First World War.  After the war he returned to the coal mines and became an official with the mine's United Mine Workers of America (UMW) union.  In 1938, he helped bring UMW Local 26 into the Co-operative Commonwealth Federation (CCF), becoming the first labour local to affiliate with the party.  In 1940, he became the first CCF member elected to the Canadian House of Commons, east of Manitoba.  While serving in the House, he was known as its leading voice championing labour issues.  He was also a main voice for social rights during his 17-years in Parliament.  His most notable achievement was securing the funding that allowed the building of a fixed-link between Nova Scotia's mainland and Cape Breton Island at the Strait of Canso: the Canso Causeway.  After winning four-straight elections, he was defeated in 1957 and died three-years later in Glace Bay, Nova Scotia.\n\nAmBev: Ambev, formally Companhia de Bebidas das Américas (official English translation: \"Americas' Beverage Company\", hence the name \"Ambev\", formerly styled as \"AmBev\") is a Brazilian brewing company.  It is the biggest brewery in Latin America and the fifth in the world.  It was created on July 1, 1999, with the merger of two breweries, Brahma and Antarctica.  The merger was approved by the Board of Directors of the Brazilian Administrative Council for Economic Defense (CADE) on March 30, 2000.  The headquarters are in São Paulo, Brazil.\n\nAmbulance Operators Association of Nova Scotia: The Ambulance Operators Association of Nova Scotia (AOANS) was the provincial association representing ambulance company owners in Nova Scotia.  The association’s focus was negotiating with the Government of Nova Scotia over funding, service standards, and private ownership of ambulance services.  The AOANS was also contracted by the Government of Nova Scotia to provide a training program for ambulance personnel and an ambulance inspection program.  Between 1994 and 1999, after the publication of the Murphy Report, Nova Scotia transitioned to a single ambulance service provider.  This resulted in the AOANS members being bought–out and their ambulance services merged into the new system.  The AOANS was formally dissolved in 2002.\n\nInterbrew: Interbrew was a large Belgium-based brewing company which owned many internationally known beers, as well as some smaller local beers.  In 2004, Interbrew merged with Brazilian brewer AmBev to form InBev, which at the time became the largest brewer in the world by volume, with a 13% global market share.  In 2008, InBev further merged with American brewer Anheuser-Busch to form Anheuser-Busch InBev (abbreviated AB InBev).  Interbrew is now a division of Anheuser-Busch InBev SA/NV since the latter acquired SABMiller in October 2016.\n\nGorham's Rangers: Gorham's Rangers was one of the most famous and effective ranger units raised in the colonial North America.  Formed by John Gorham, the unit served as the prototype for many subsequent ranger forces, including the better known Rogers' Rangers.  The unit started out as a Massachusetts provincial auxiliary company, which means it was not part of the province's normal militia system.  Recruited in the summer of 1744 at the start of King George's War, Governor William Shirley ordered the unit raised as reinforcements for the then-besieged British garrison at Fort Anne in Annapolis Royal.  Over the next eight years the unit proved remarkably effective at suppressing Acadian and Mi'kmaq resistance to British rule in Nova Scotia and helped to both expand and secure the British sphere of influence in the region.  Initially a sixty-man all-Indian company led by British colonial officers, the original Native American members of the unit were gradually replaced by Anglo-Americans and recent Scots and Irish immigrants and were a minority in the unit by the mid-1750s.  The company were reconnaissance experts as well as renowned for their expertise at both water-borne operations and frontier guerrilla warfare.  They were known for surprise amphibious raids on Acadian and Mi'kmaq coastal or riverine settlements, using large whaleboats, which carried between ten and fifteen rangers each.  This small unit was the main British military force defending Nova Scotia from 1744 to 1749.  The company became part of the British army and was expanded during the Seven Years' War and went on to play an important role in fighting in Nova Scotia as well as participating in many of the important campaigns of the war, particularly distinguishing itself at the Siege of Quebec in 1759.\n\nMermaid Theatre of Nova Scotia: Mermaid Theatre of Nova Scotia was co-founded in 1972 in Wolfville, Nova Scotia, by the late Evelyn Garbary, Tom Miller, and Sara Lee Lewis who continues to serve as Managing Director.  The Theatre moved to Windsor, Nova Scotia in 1987, purchasing a large commercial building in the town’s center, which now houses its workshops, administration, rehearsal and performance facilities.  The company was registered under the Societies Act of Nova Scotia, and received charitable status with Revenue Canada in March 1973.\n\nInBev: InBev was a brewing company that resulted from the merger between Belgium-based company Interbrew and Brazilian brewer AmBev which took place in 2004.  It existed independently until the acquisition of Anheuser-Busch in 2008, that formed Anheuser-Busch InBev (abbreviated AB InBev).  InBev had operations in over 30 countries and sales in over 130 countries.  In 2006, it had a market capitalization of €30.6 billion and net profit of €3.2 billion on sales of €13.3 billion.\n\nOland Brewery: Oland Brewery is a brewing company in Halifax, Nova Scotia, Canada, and a unit of Labatt Brewing Company, itself a unit of InBev.\n\nMoses Delesdernier: Moses Delesdernier (c.1713-1811) was land trader and author who moved from Switzerland to Halifax, Nova Scotia (1750).  In 1754, while at Pisiquid, he was the first Protestant to farm among the Acadians.  He was also the truckmaster for trade with the Mi’kmaq (1760).  He also held office in present-day New Brunswick and Prince Edward Island.  Delesdernier met Richard John Uniacke in Philadelphia and encouraged him to settle in Nova Scotia (1774).  Delesderneir became Uniacke’s father-in-law (1775).  The following year Delesderneir's son and son-in-law Uniacke became involved in the Eddy Rebellion and, as a result, Delesdernier fell into disfavour with the government.  Delesderneir also wrote two manuscripts that were used by Andrew Brown in his history of Nova Scotia.  He is buried in the Old Burying Ground (Halifax, Nova Scotia).\n\nQuestion: What company has a brewing company is Nova Scotia and is the result of merger between Interbrew and AmBev?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company that is the result of the merger.\"\n    },\n    \"merger_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"merged_companies\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The names of the companies that merged to form the main company.\"\n        },\n        \"merger_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the merger took place.\"\n        }\n      },\n      \"required\": [\n        \"merged_companies\",\n        \"merger_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"nova_scotia_operations\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The specific location of the brewing company in Nova Scotia.\"\n        },\n        \"business_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of business operated in Nova Scotia.\"\n        },\n        \"operating_unit\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the specific brewing company operating in Nova Scotia.\"\n        }\n      },\n      \"required\": [\n        \"location\",\n        \"business_type\",\n        \"operating_unit\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"merger_details\",\n    \"nova_scotia_operations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the company that is the result of the merger."
      },
      "merger_details": {
        "type": "object",
        "properties": {
          "merged_companies": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The names of the companies that merged to form the main company."
          },
          "merger_year": {
            "type": "integer",
            "description": "The year the merger took place."
          }
        },
        "required": [
          "merged_companies",
          "merger_year"
        ],
        "additionalProperties": false
      },
      "nova_scotia_operations": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The specific location of the brewing company in Nova Scotia."
          },
          "business_type": {
            "type": "string",
            "description": "The type of business operated in Nova Scotia."
          },
          "operating_unit": {
            "type": "string",
            "description": "The name of the specific brewing company operating in Nova Scotia."
          }
        },
        "required": [
          "location",
          "business_type",
          "operating_unit"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "company_name",
      "merger_details",
      "nova_scotia_operations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
