{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nZuma (restaurant): Zuma is a restaurant founded by chef Rainer Becker, inspired by informal \"izakaya\"-style Japanese dining in which dishes are brought to the table continuously throughout the meal.\n\nDa Marino: Da Marino Ristorante Italiano is a New York City Italian restaurant founded by chef Pasquale Marino.\n\nSoul Daddy: Soul Daddy was an American fast casual restaurant founded by Jamawn Woods, featuring soul food that is both traditional and healthy.  As a contestant on the reality television show \"America's Next Great Restaurant\", which aired in 2011, he created the concept for Soul Daddy (originally conceived of as W3, or Woods' Wings & Waffles), and was named the winner in the show's first season finale on May 1, 2011.  The restaurant chain opened on May 2, 2011, at three locations: at the Mall of America in Bloomington, Minnesota, at Hollywood and Highland in Los Angeles, and at the South Street Seaport in Manhattan at 189 Front Street.  The Manhattan and Los Angeles locations closed on June 14 and 15, 2011 in order for Woods to focus on making the Mall of America location successful, only for that location to close two weeks later on June 28.\n\nJean-Claude Vrinat: Jean-Claude Vrinat (12 April 1936 – 7 January 2008) was the owner of the Taillevent restaurant founded by his father André Vrinat in Paris.  This two star restaurant, named after the court chef to King Charles V in the fourteenth century, has long been considered the epitome of Haute Cuisine and is also known for its excellent service and its comprehensive wine list.  It held three stars from 1973 to 2007.\n\nPeter Elliot: Peter Elliot (born December 9, 1966) is an American writer, editor and media personality, best known for his biography of restaurateur Sirio Maccioni, \"Sirio: The Story of My Life and Le Cirque\" and for the development of DINE, the restaurant search engine and lifestyles portal for the global financial news and media company, Bloomberg LP.  He is currently manager of Lifestsyle Products at Bloomberg LP.\n\nLe Cirque: Le Cirque is a French restaurant located at One Beacon Court, 151 East 58th Street (between Lexington Avenue and Third Avenue) in Midtown Manhattan, New York City.  It is owned and operated by LC International LLC, and was founded by Sirio Maccioni.\n\nSirio Maccioni: Sirio Maccioni (born 1932 in Montecatini Terme, Italy) is a restaurateur and author.  Maccioni got his start at Oscar's Delmonico, Delmonico's.  Owner Oscar Tucci once stated \"Sirio and with Tony May will be some of the greatest restaurateurs, that will come out of Delmonico's.\"\n\nAlain Sailhac: Alain Sailhac, born in Millau, France is an internationally recognized French chef working in New York City, where he holds the position of Executive Vice President and Dean Emeritus at The International Culinary Center, founded as the French Culinary Institute.  Sailhac earned the first ever four star rating from \"The New York Times\" while at Le Cygne in 1977.  He went on to be a chef at Le Cirque, the 21 Club and the Plaza Hotel.\n\nInternational Culinary Center: The International Culinary Center was founded as \"The French Culinary Institute\" by Dorothy Cann Hamilton in 1984 and has campuses in New York City and the San Francisco Bay Area.  The facilities include professional kitchens for hands-on cooking and baking classes, specialized wine tasting classrooms, a library, theater, and event spaces.  ICC has several renowned chefs as its deans including Jacques Pépin, Jacques Torres, André Soltner, Alain Sailhac, David Kinch, Emily Luchetti, Cesare Casella and José Andrés.\n\nSir and Star: Sir and Star is a restaurant founded in 2012.  It is located in The Olema, a historic restaurant and inn built in 1876.  The restaurant is at the corner of Sir Francis Drake Boulevard and Star Route One in Olema, California.  Olema is located in West Marin County 1 mi from the Bear Valley portal to the Point Reyes National Seashore.  Olema is similar to a one-horse town as it only contains one other restaurant, a lodge, a few bed and breakfast inns, a recreational vehicle (RV) resort with hookups and a campground, a few shops, and the Hindui branch retreat for their Vedanta Society, all within walking distance of the inn.\n\nQuestion: Alain Sailhac worked as a chef in a restaurant founded by Sirio Maccioni in what city?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"chef_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the chef.\"\n    },\n    \"founder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the restaurant founder.\"\n    },\n    \"restaurant_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the restaurant where the chef worked for the founder.\"\n    },\n    \"city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the restaurant is located.\"\n    },\n    \"restaurant_cuisine\": {\n      \"type\": \"string\",\n      \"description\": \"The type of cuisine served at the restaurant.\"\n    }\n  },\n  \"required\": [\n    \"chef_name\",\n    \"founder_name\",\n    \"restaurant_name\",\n    \"city\",\n    \"restaurant_cuisine\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "chef_name": {
        "type": "string",
        "description": "The name of the chef."
      },
      "founder_name": {
        "type": "string",
        "description": "The name of the restaurant founder."
      },
      "restaurant_name": {
        "type": "string",
        "description": "The name of the restaurant where the chef worked for the founder."
      },
      "city": {
        "type": "string",
        "description": "The city where the restaurant is located."
      },
      "restaurant_cuisine": {
        "type": "string",
        "description": "The type of cuisine served at the restaurant."
      }
    },
    "required": [
      "chef_name",
      "founder_name",
      "restaurant_name",
      "city",
      "restaurant_cuisine"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
