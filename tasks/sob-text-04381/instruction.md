{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPiperWai: PiperWai is an American deodorant brand.  It was featured on \"Shark Tank\" in December 2015 and received an offer from Barbara Corcoran, which has been considered one of her most notable deals to date.  The product experienced the \"\"Shark Tank\" effect\" and sold out within five minutes of airing, with more than $1 million in sales over the next month.  PiperWai was co-founded by Sarah Ribner and Jess Edelstein in March 2014.\n\nBarbara Corcoran: Barbara Ann Corcoran (born March 10, 1949 in Edgewater, New Jersey) is an American businesswoman, investor, speaker, consultant, syndicated columnist, author, and television personality.  As a television personality, she is a \"Shark\" investor on ABC's \"Shark Tank\".\n\nMark Cuban: Mark Cuban (born July 31, 1958) is an American businessman, investor, author, television personality, and philanthropist.  He is the owner of the NBA's Dallas Mavericks, co-owner of 2929 Entertainment and chairman of the AXS TV.  He is also one of the main \"shark\" investors on the ABC reality television series, \"Shark Tank\".  In 2011, Cuban wrote an e-book, \"How to Win at the Sport of Business\", in which he chronicles his experiences in business and sports.\n\nChris Sacca: Christopher Sacca (born May 12, 1975) is a former American venture investor, company advisor and entrepreneur as well as a former lawyer.  He is the proprietor of Lowercase Capital, a venture capital fund in the United States that has invested in seed and early-stage technology companies such as Twitter, Uber, Instagram, Twilio, and Kickstarter.  As of 2017, he has appeared as a \"Guest Shark\" on ABC's Shark Tank.\n\nSimple Sugars: Simple Sugars is a Pittsburgh-based cosmetics company run by entrepreneur Lani Lazzari.  In 2013, Lani Lazzari appeared in Season 4 of the American reality television series \"Shark Tank\" where the business received a $100,000 investment from Dallas Mavericks owner Mark Cuban for a 33 percent stake.  A year later, Lazzari appeared again on \"Shark Tank\".\n\nPlated (meal kits): Plated is an American ingredient-and-recipe meal kit service that has been acquired by Albertsons.  The company was founded in 2012, but rose to notability through its selection for Techstars in 2013, \"Shark Tank\" in 2014 and \"Beyond the Tank\" in 2015.  Plated's founders, Nick Taranto and Josh Hix, earned a deal on \"Shark Tank\" that fell through, but negotiated a deal with another investor after the show was filmed.  The company accepted several rounds of venture capital investments and remained private until it was acquired by Albertsons in September 2017.\n\nCinnaholic: Cinnaholic is a vegan bakery franchise that started in 2010 and currently operates in eight states.  The company's owners appeared on the television show Shark Tank in 2014, which ended with them ultimately turning down a $200,000 investment offer from Robert Herjavec.  The company has adopted a franchise business model and has plans to open 100 locations by 2020.\n\nShark Tank: Shark Tank is an American reality television series that premiered on August 9, 2009, on ABC.  The show is a franchise of the international format \"Dragons' Den\", which originated in Japan in 2001.  \"Shark Tank\" shows aspiring entrepreneur-contestants as they make business presentations to a panel of \"shark\" investors, who then choose whether or not to invest.\n\nShark Tank (Australian TV series): Shark Tank is an Australian reality competition television series that premiered 8 February 2015, on Network Ten.  Based on the international \"Dragons' Den\" and \"Shark Tank\" format, it has aspiring entrepreneur-contestants make business presentations to a panel of \"shark\" investors.\n\nRobert Herjavec: Robert Herjavec ( ; ] ; born September 14, 1962) is a Croatian-Canadian businessman, investor, and television personality.  A native of Varaždin, Croatia, he moved to Halifax, Canada after living and working on a farm with his family.  After spending his youth in the relative middle class, he gained admission to the University of Toronto where he graduated with a double degree in political science and English.\n\nQuestion: The Shark Tank investor that Cinnaholic rejected an offer from is originally from what country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"investor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"origin_country\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"origin_country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"company_name\": {\n      \"type\": \"string\"\n    },\n    \"deal_status\": {\n      \"type\": \"string\",\n      \"description\": \"The outcome of the deal between the company and the investor.\"\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin of the specified investor.\"\n    }\n  },\n  \"required\": [\n    \"investor\",\n    \"company_name\",\n    \"deal_status\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "investor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "origin_country": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "origin_country"
        ],
        "additionalProperties": false
      },
      "company_name": {
        "type": "string"
      },
      "deal_status": {
        "type": "string",
        "description": "The outcome of the deal between the company and the investor."
      },
      "answer": {
        "type": "string",
        "description": "The country of origin of the specified investor."
      }
    },
    "required": [
      "investor",
      "company_name",
      "deal_status",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
