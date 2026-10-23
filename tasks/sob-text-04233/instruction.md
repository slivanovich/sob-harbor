{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKemah Boardwalk: The Kemah Boardwalk is a 60-acre Texas Gulf Coast theme park in Kemah, Texas, approximately 30 miles southeast of Downtown Houston, Texas.  The Boardwalk is built entirely along the shores of Galveston Bay and Clear Lake, and is considered among the premier boardwalks in the United States.  The complex is owned and operated by Landry’s, Inc. , and is home to more than 10 restaurants, a collection of rides, midway games, attractions, a boutique hotel, a charter yacht, a 400-slip marina and multiple shops.  There is no charge to walk around on the boardwalk.  Tickets for rides can be purchased individually or all-day ride passes are available.  Restaurants on the boardwalk include Landry’s Seafood, Bubba Gump Shrimp Co. , Saltgrass Steak House, Cadillac Bar and many others.\n\nMcCormick &amp; Schmick's: McCormick & Schmick's Seafood Restaurants Inc. is an American seafood restaurant chain, based in Portland, Oregon.  As of October 2016, the company operates 72 locations in North America under various brands, including 60 restaurants across 22 U.S. states, as well as 12 Canadian locations that operate under the Boathouse name.  A sale to the parent company, Landry's, Inc., was completed in January 2012.\n\nHarmon Corner: Harmon Corner is a 110,184-square-foot enclosed shopping mall on the Las Vegas Strip in Las Vegas, Nevada with a giant LED sign as a standout feature that is home to many dining options.  Its tenants include Bubba Gump Shrimp Company, Krispy Kreme, McDonald's, Panda Express, Popeyes, Rainforest Cafe, Subway, Taco Bell Cantina, Twin Peaks Restaurant, and Walgreens.\n\nWhataburger: Whataburger is an American privately held regional fast food restaurant chain, based in San Antonio, Texas, that specializes in hamburgers.  The company, founded by Harmon Dobson and Paul Burton, opened its first restaurant in Corpus Christi, Texas, in 1950.  The chain is owned and operated by the Dobson family, along with 25 franchisers.  s of 2017 , there are currently 809 Whataburger stores across the Southeastern and Southwestern United States regions.\n\nSaltgrass Steak House: Saltgrass Steak House is an American restaurant concept with more than 50 locations across the country.  The company is based in Houston, Texas, and is wholly owned by Landry’s, Inc.\n\nLandry's Seafood: Landry’s Seafood is a chain of American casual seafood restaurants owned by Landry's, Inc. It currently operates in 20 locations in eight U.S. states, with many situated near tourist landmarks and attractions.\n\nRainforest Cafe: Rainforest Cafe is a themed restaurant chain owned by Landry's, Inc. of Houston.  It was founded by entrepreneur Steven Schussler.  The first location opened in the Mall of America in Bloomington, Minnesota, on February 3, 1994.  By 1997, the chain consisted of six restaurants, all in the United States.  In 1998, it was planned to build 12 additional restaurants in the United States, seven in Mexico, and five in the UK, for a total of 22 restaurants by 2008.\n\nClaim Jumper: Claim Jumper Restaurant and Saloon is an American restaurant chain with more than 40 locations.  The company is based in Houston, Texas.  Claim Jumper is wholly owned by Landry's, Inc.\n\nLandry's, Inc.: Landry's, Inc., is an American, privately owned, multi-brand dining/hospitality/entertainment/gaming corporation.  Headquartered in Houston, Texas, Landry's, Inc. owns and operates more than 600 restaurant/hotel/casino/entertainment destinations in 37 states and the District of Columbia.  The company also owns and operates numerous international locations.\n\nVic &amp; Anthony's Steakhouse: Vic & Anthony’s is an American steakhouse restaurant chain with locations in Downtown Houston, ]and inside the Golden Nugget Casinos in Las Vegas and Atlantic City.  A fourth location is scheduled to open inside the new Golden Nugget Lake Charles in late 2014.  Vic & Anthony’s is owned and operated by Landry’s, Inc.\n\nQuestion: Who founded the restaurant in Harmon Corner that is owned by Landry's, Inc. \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"restaurant_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the restaurant.\"\n    },\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who founded the restaurant.\"\n    },\n    \"owner_company\": {\n      \"type\": \"string\",\n      \"description\": \"The company that owns the restaurant.\"\n    },\n    \"location_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the location where the restaurant is situated.\"\n    }\n  },\n  \"required\": [\n    \"restaurant_name\",\n    \"founder_name\",\n    \"owner_company\",\n    \"location_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "restaurant_name": {
        "type": "string",
        "description": "The name of the restaurant."
      },
      "founder_name": {
        "type": "string",
        "description": "The name of the person who founded the restaurant."
      },
      "owner_company": {
        "type": "string",
        "description": "The company that owns the restaurant."
      },
      "location_name": {
        "type": "string",
        "description": "The name of the location where the restaurant is situated."
      }
    },
    "required": [
      "restaurant_name",
      "founder_name",
      "owner_company",
      "location_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
