{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoseph Huber Brewing Company: The Joseph Huber Brewing Company was founded in 1845 in Monroe, Wisconsin.  Originally called The Blumer Brewery, it adopted the Huber name in 1947.  It is the oldest continually operating brewery in the Midwest and second oldest in the United States.\n\nJamie Merisotis: Jamie Merisotis is president and CEO of Lumina Foundation, one of the largest private foundations in the United States whose mission is to increase the proportion of Americans with degrees, certificates and other high-quality credentials to 60 percent by 2025.  Merisotis leads the Foundation's $1.3 billion endowment.  He is the author of \"America Needs Talent,\" published in September 2015 by RosettaBooks and named a Top 10 business book of 2016 by Booklist.\n\nPacific Tarn: Pacific Tarn is a small lake located in the Colorado Rocky Mountains in the United States.  It is notable for its 13,420 foot (4,090 m) elevation, making it the highest lake in the United States whose name is recognized by the United States Board on Geographic Names.\n\nMinhas Craft Brewery: The Minhas Craft Brewery is located in Monroe, Wisconsin, owned by brother and sister, Ravinder and Manjit Minhas.  It is the Midwest's oldest brewery and the second oldest in the United States.  It survived the Great Depression, Prohibition and a fire.  It is currently the 9th largest craft brewery in America.\n\nPori Brewery: Pori Brewery (Finnish: \"Porin Oluttehdas\" ) was a brewery in Pori, Finland established 1853.  It was last owned by Danish brewing company Carlsberg and closed in 2009.  Pori Brewery was the second oldest brewery in Finland and one of the oldest in Nordic countries.\n\nLynn Korwatch: Lynn Korwatch is the executive director of Marine Exchange of the San Francisco Bay Region.  This is a nonprofit membership organization that was established in the year 1849 and is the second oldest organization in California.  It is the second oldest corporation in California.  Lynn Korwatch joined the California Maritime Academy in 1972, and she was one of the few first class women to join.  In 1988, she was the first woman ever to command a United States commercial vessel.  As a general manager at Matson Navigation Company, she held many responsibilities.  Some of these responsibilities included managing the operation of fourteen ships that were owned by this company.  Another achievement she was responsible for was helping to create the \"Zero Garbage Discharge Program\".  This was helpful in not being able to throw away waste over board that contained any solid materials.  This is seen as monumental because it was seen as the first of its kind and was exceeding all of the government regulations at the time.\n\nManjit Minhas: Manjit Minhas (born May 31, 1980) is a Canadian entrepreneur, television personality and venture capitalist.  She is co-founder and CEO of Minhas Breweries & Distillery, manufacturer of beer brands such as Boxer Lager, Lazy Mutt Ale and Huber Bock.  Minhas was announced as one of the new dragons on Season 10 of the Canadian reality television series \"Dragons' Den\" in 2015 for its tenth season.\n\nŠvyturys: The Švyturys Brewery \"(English: Lighthouse)\" is Lithuania’s second oldest brewery located in Klaipėda, Lithuania.  It was founded in 1784 by the Reincke family of merchant seamen.  The brewery is a part of Švyturys-Utenos alus and currently is owned by the Carlsberg Group, which controls Švyturys-Utenos alus through Baltic Beverages Holding.\n\nWilliam Mason (locomotive): William Mason is a 4-4-0 steam locomotive currently in operation at the Baltimore and Ohio Railroad Museum in Baltimore, Maryland, United States.  It was built for the Baltimore and Ohio Railroad, carrying that railroad's number 25.  The locomotive is named in honor of its builder, William Mason, who built around 754 steam locomotives at his Mason Machine Works firm in Taunton, Massachusetts, from 1853 until his death in 1883.  The engine is one of the oldest operable examples of the American Standard design, and the fourth oldest Baltimore and Ohio locomotive in existence, the oldest being the 0-4-0 no. 2, the \"Andrew Jackson\" from 1836, second oldest is the no. 8 0-4-0, \"John Hancock\" built later that same year, and the third being the 0-8-0 no. 57, \"Memnon\" of 1848 (the preserved \"Tom Thumb\" and \"Lafayette\" engines are replicas built by the road for exhibition purposes in 1926 and 1927, respectively).  The \"William Mason\" had been the second oldest operational locomotive in the world, and the oldest in the western hemisphere.  Only the Indian locomotive \"Fairy Queen\", built one year prior to the \"William Mason\" is older.\n\nAmericans for Peace Now: Americans for Peace Now (APN) is a nonprofit organization based in the United States whose stated aim is to help achieve a comprehensive political settlement to the Israeli–Palestinian conflict.  Founded in 1981 as the sister organization to Israel's \"Shalom Achshav\" (Peace Now), APN describes itself as a non-partisan, non-profit, pro-Israel, pro-peace, American Jewish organization.  The current President and CEO of APN is Debra DeLee.\n\nQuestion: What is the name of the second oldest brewery in the United States whose CEO is Manjit Minhas?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"brewery_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the brewery.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the brewery is located.\"\n    },\n    \"ceo\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the CEO of the brewery.\"\n    },\n    \"oldest_ranking_us\": {\n      \"type\": \"integer\",\n      \"description\": \"The ranking of the brewery by age in the United States.\"\n    },\n    \"additional_facts\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other notable facts about the brewery.\"\n    }\n  },\n  \"required\": [\n    \"brewery_name\",\n    \"location\",\n    \"ceo\",\n    \"oldest_ranking_us\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "brewery_name": {
        "type": "string",
        "description": "The name of the brewery."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the brewery is located."
      },
      "ceo": {
        "type": "string",
        "description": "The name of the CEO of the brewery."
      },
      "oldest_ranking_us": {
        "type": "integer",
        "description": "The ranking of the brewery by age in the United States."
      },
      "additional_facts": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other notable facts about the brewery."
      }
    },
    "required": [
      "brewery_name",
      "location",
      "ceo",
      "oldest_ranking_us"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
