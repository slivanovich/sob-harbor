{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJanssen and Bechly Brewery: Janssen & Bechly Brewery produced beer at Neubrandenburg, Germany from 1912 until the company was nationalized by East Germany in 1949.  The brewery continued to produce beer under the Neubrandenburg and Nordbräu brand names until the company ended production in 1995.  The Nordbräu brand was sold to the Mecklenburg brewery Lübzer in 1996.\n\nMayfield Brewery: The Mayfield Brewery was a brewery that operated in Mayfield, California between years 1868 and 1920.  The brewery was located at what is now the corner of California Avenue and Birch Street in Palo Alto, California.  The brewery produced Steam beer and sold it in kegs to local saloons.  The brewery was shut down by Prohibition.\n\nAC Golden Brewing Company: The AC Golden Brewing Company is a subsidiary of MillerCoors, a joint venture between SABMiller and Molson Coors Brewing Company.  Its purpose is to serve as a specialty brewing arm of MillerCoors, in the words of president Glenn Knippenberg, \"Our mission for AC Golden is to be a brand incubator for what is now MillerCoors\".  The AC Golden Brewery operates in the former pilot brewery of the Coors Brewery.  It debuted its first beer, Herman Joseph's Private Reserve, in 2008.  The company began brewing its seasonal beer, a Vienna Style lager called Winterfest, in 2009.  In April 2010, AC Golden introduced Colorado Native lager in Colorado, an amber lager made with 100% Colorado ingredients.\n\nGilroy’s Brewery: Gilroy’s Brewery is a microbrewery and restaurant in Muldersdrift, Gauteng, South Africa.  The brewery was founded in 2000 by Stephen Gilroy at his pharmaceutical printing company in Roodepoort, Gauteng.  Gilroy’s Brewery was one of the first microbreweries in South Africa, along with Mitchell's Brewery, Nottingham Road Brewery, and Drayman’s Brewery.  In 2008 the operation was relocated to the current premises at Ngwenya Glass Village in Muldersdrift, where it expanded to include the restaurant, beer garden, and a gift shop.  The brewery produces 5 styles of beer – a lager, pale ale, ruby ale, and a dark ale.  The brewery has recently introduced a ginger beer.\n\n1612er Zwickelbier: 1612er Zwickelbier, is a Zwickel (Or Zwickl) beer made in the same tradition as Kellerbiers: unfiltered, served straight from the cask or conditioning tank, and naturally cloudy in the glass.  1612er Zwickelbier has an alcohol content of 5.3% abv and was first brewed by Hofbräuhaus Traunstein in 1612, when the Bavarian Duke Maximilian I founded a brewery solely for producing Weissbier.  Today however, the brewery range also includes a Pilsner and a Dunkel.  Hops for 1612er Zwickelbier come from the brewery's own farm in the Hallertau area, whereas the malt is sourced locally.  1612er is currently only available in the brewery's restaurants and beer halls.\n\nStarobrno Brewery: Starobrno Brewery (in Czech: Pivovar Starobrno) is a Czech brewery located in the city of Brno.  It was built as a successor of the brewery founded in 1325, as a part of Cistercian convent.  The brewery was named \"Starobrno Brewery\" only in the second half of the 19th century.  In 2009, Starobrno Brewery produced more than one million hectoliters of beer.  The same year, the brewery merged with the Royal Brewery of Krušovice and became a part of the Dutch brewing company Heineken.\n\nSteam beer: Steam beer is a highly effervescent beer made by fermenting lager yeasts at warmer ale yeast fermentation temperatures.  It has two distinct but related meanings:\n\nWoodforde's Brewery: Woodforde’s Brewery is a brewery located in Slad Lane in the village of Woodbastwick, in the county of Norfolk, England.  The brewery produced its first commercial brew in 1981 from original brewery in the village of Drayton north east of Norwich.  In 1996 the brewery’s popular Wherry bitter became CAMRA Supreme Champion Beer of Britain.\n\nHeavy Seas Beer: Heavy Seas Beer is brewed by Clipper City Brewing Company, in Baltimore, Maryland.  The brewery was established by Hugh Sisson in 1995.  Previously, Sisson operated Maryland's first brewpub, Sisson's.  In 2010, the brewery rebranded.  While the name of the company remains Clipper City Brewing Company, all of its beer falls under the Heavy Seas brand.  Heavy Seas hosts tours on most weekends.  It is located at 4615 Hollins Ferry Road, Suite B, in the Halethorpe section of Baltimore.  Heavy Seas currently offers a variety of beer styles in approx. 18 states within the United States.  Several Heavy Seas beers have been awarded and include the following: Cutlass Amber Lager (a repeat medal winner at the Great American Beer Festival from 2006-2010, bronze medal winner at the 2010 World Beer Cup and silver medal winner at the 2012 World Beer Cup as Heavy Seas Märzen), Powder Monkey Pale Ale (silver medal winner at the 2008 Great American Beer Festival and bronze medal winner at the 2010 World Beer Cup as Heavy Seas Pale Ale), Small Craft Warning Uber Pils (bronze medal winner at the 2004 Great American Beer Festival), Gold Ale (gold medal winner at the 2010 World Beer Cup, bronze medal winner at the 2010 Great American Beer Festival and bronze medal winner at the 2014 Great American Beer Festival as Heavy Seas Gold Ale) and Winter Storm Imperial ESB (gold medal winner at the 2008 World Beer Cup).\n\nWrexham Lager Beer: Wrexham Lager Beer is a brewery and pilsner beer brewed in Wrexham, north-east Wales.  The brewery has existed since 1881 and is reputed to be the first successful lager brewery in the UK.  The original brewery closed in 2000, but re-opened under new owners in 2011 at a different site.  The lager is currently sold in two variants: 'Wrexham Lager' (4.2% ABV) available on draught and 'Wrexham Lager Export' (5% abv) which is only available in bottles.\n\nQuestion: The Mayfield Brewery produced a highly effervescent beer made by fermenting lager yeasts at warmer what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"brewery_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the brewery.\"\n    },\n    \"beer_produced\": {\n      \"type\": \"string\",\n      \"description\": \"The specific type of beer produced by the brewery.\"\n    },\n    \"beer_characteristics\": {\n      \"type\": \"string\",\n      \"description\": \"A key characteristic of the beer.\"\n    },\n    \"fermentation_process\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"yeast_type_used\": {\n          \"type\": \"string\",\n          \"description\": \"The type of yeast used for fermentation.\"\n        },\n        \"temperature_condition\": {\n          \"type\": \"string\",\n          \"description\": \"The condition of the fermentation temperature relative to the yeast type.\"\n        },\n        \"comparison_temperature_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of fermentation temperature used for comparison.\"\n        }\n      },\n      \"required\": [\n        \"yeast_type_used\",\n        \"temperature_condition\",\n        \"comparison_temperature_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"brewery_name\",\n    \"beer_produced\",\n    \"beer_characteristics\",\n    \"fermentation_process\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "brewery_name": {
        "type": "string",
        "description": "The name of the brewery."
      },
      "beer_produced": {
        "type": "string",
        "description": "The specific type of beer produced by the brewery."
      },
      "beer_characteristics": {
        "type": "string",
        "description": "A key characteristic of the beer."
      },
      "fermentation_process": {
        "type": "object",
        "properties": {
          "yeast_type_used": {
            "type": "string",
            "description": "The type of yeast used for fermentation."
          },
          "temperature_condition": {
            "type": "string",
            "description": "The condition of the fermentation temperature relative to the yeast type."
          },
          "comparison_temperature_type": {
            "type": "string",
            "description": "The type of fermentation temperature used for comparison."
          }
        },
        "required": [
          "yeast_type_used",
          "temperature_condition",
          "comparison_temperature_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "brewery_name",
      "beer_produced",
      "beer_characteristics",
      "fermentation_process"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
