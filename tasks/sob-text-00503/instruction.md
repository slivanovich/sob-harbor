{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nYakel House and Union Brewery: The Yakel House and Union Brewery are a historic house and brewery complex located at 1421-1431 Pearl St. in Alton, Illinois.  Philip Yakel, a German immigrant, built the brewery soon after coming to America in 1836.  The brewery was the first in Alton and one of the city's earliest successful industries.  Yakel's son George, who eventually ran the brewery alongside his father, built the house in 1863; it was the family's second home at the site.  The brick home features a vernacular design influenced by German architectural tradition.  William Netzhammer, a brewer from St. Louis, purchased the brewery in 1882.  The Netzhammer family ran the brewery until it closed in 1952;, notably, the brewery continued production during Prohibition by making near beer.\n\nFürstenberg Brewery: The Fürstenberg Brewery (\"Fürstlich Fürstenbergische Brauerei\") is brewery located in Donaueschingen, Germany.  It has been a subsidiary of Brau Holding International since 2005, before which it was owned by the House of Fürstenberg, a German noble family.  Among other offerings, the brewery produces pilsner, export, and wheat beer, primarily serving southern Germany.\n\nArchipelago Brewery: The Archipelago Brewery is a Singapore brewery owned by Heineken Asia Pacific, which produces a range of signature craft beers.\n\nPaderborner Brauerei: Brauerei Paderborner is a brewery in the German city of Paderborn.  The traditional Westphalian brewery was purchased by the German brewery-major Warsteiner in 1990.\n\nBrau und Brunnen: Brau und Brunnen AG (\"Brew and Spring\") was a German brewing and beverage group which was formed as \"Dortmunder Union-Schultheiss Brauerei AG\" in 1972 through a merger between Schultheiss-Brauerei and Dortmunder Union-Brauerei.  It was renamed \"Brau und Brunnen\" in 1988.  It owned a number of formerly independent breweries, including Einbecker Brewery.  Until the early 1990s, Brau und Brunnen was the largest beverage company in Germany, but its market share steadily declined throughout the 1990s.  An additional cause for the decline was the company's purchase of Bavaria – St. Pauli Brewery and Jever for an estimated 800 million DM, although these purchases were later estimated to only be worth closer to 250 million DM.  Other companies engaged in a series of mergers and acquisitions, and by 1999, it had sank to the fourth-largest beverage company and was continually losing money.  After unsuccessful internal reorganizations, the company was purchased by Dr. August Oetker KG and integrated into its subsidiary Radeberger Gruppe.\n\nWarsteiner: Warsteiner beer is brewed in the Arnsberg Forest Nature Park outside of Warstein, North-Rhine Westphalia, Germany.  Warsteiner has been owned by the Cramer family since 1753.  Warsteiner is Germany's largest privately owned brewery; its most popular beer is Warsteiner Premium Verum.\n\nErnst Barre Private Brewery: The Ernst Barre Private Brewery (German: \"Privatbrauerei Ernst Barre GmbH\" ) is a brewery in the East Westphalian town of Lübbecke in the north-western German district of Minden-Lübbecke.  It was founded by Ernst Johann Barre in 1842.  Along with its immediate competitor, the Herforder Brauerei, it is one of the largest breweries in East Westphalia (based on beer production), and is thus of regional importance.  The brewery is located at the southern end of the pass over the Wiehen Hills (Bundesstrasse 239) between Lübbecke and Hüllhorst, at the base of the Reineberg hill, and has been in the same family for generations.\n\nMalt Shovel Brewery: The Malt Shovel Brewery is an Australian brewery owned by Lion and located in Camperdown, New South Wales.  It is best known for the James Squire range of beers.  The beer is named after the convict turned Australia's first brewer James Squire, who also went on the grow Australia's first hops and is said to have created Australia's first commercial brewery.\n\nOriental Brewery: Oriental Brewery or OB (Hangul: 오비맥주) is a South Korean brewery owned by AB InBev.  (was started by Doosan group)\n\nSchwaben Bräu: Schwaben Bräu (also Schwabenbräu ) is a brewery owned by Dinkelacker-Schwaben Bräu GmbH und Co.  KG and located in Stuttgart, Germany.  The company owns the largest brewery in the German state of Baden-Württemberg .\n\nQuestion: In 1990 the brewery Brauerei Paderborner was purchased by a brewery owned by what family?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"purchased_brewery_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the brewery that was purchased.\"\n    },\n    \"purchasing_brewery_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the brewery that made the purchase.\"\n    },\n    \"purchasing_brewery_owner_family\": {\n      \"type\": \"string\",\n      \"description\": \"The family that owns the purchasing brewery.\"\n    },\n    \"purchase_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the purchase took place.\"\n    }\n  },\n  \"required\": [\n    \"purchased_brewery_name\",\n    \"purchasing_brewery_name\",\n    \"purchasing_brewery_owner_family\",\n    \"purchase_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "purchased_brewery_name": {
        "type": "string",
        "description": "The name of the brewery that was purchased."
      },
      "purchasing_brewery_name": {
        "type": "string",
        "description": "The name of the brewery that made the purchase."
      },
      "purchasing_brewery_owner_family": {
        "type": "string",
        "description": "The family that owns the purchasing brewery."
      },
      "purchase_year": {
        "type": "integer",
        "description": "The year the purchase took place."
      }
    },
    "required": [
      "purchased_brewery_name",
      "purchasing_brewery_name",
      "purchasing_brewery_owner_family",
      "purchase_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
