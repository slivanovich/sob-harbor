{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRegulation NMS: Regulation National Market System (or Reg NMS) is a US financial regulation promulgated and described by the United States Securities and Exchange Commission (SEC) as \"a series of initiatives designed to modernize and strengthen the National Market System for equity securities.\"  The Reg NMS is intended to assure that investors receive the best price executions for their orders by encouraging competition in the marketplace.\n\nNational market system plan: A national market system plan (or NMS plan) is a structured method of transmitting securities transactions in real-time.  In the United States, national market systems are governed by section 11A of the Securities Exchange Act of 1934.\n\nShameless (U.S. TV series): Shameless is an American comedy-drama television series which airs on Showtime.  It is the remake of the British series of the same name.  Set in Chicago, the series is filmed in Los Angeles, with the exterior scenes shot in Chicago.\n\nSecurities Acts Amendments of 1975: The Securities Acts Amendments of 1975 is an act of Congress.  It was passed as a United States Public Law (Pub.L.  94–29 ) on June 4, 1975, and amended the Securities Act of 1933 ( \"et seq.\") and the Securities Exchange Act of 1934 ( \"et seq.\").  The Securities Acts Amendments imposed an obligation on the Securities Exchange Commission to consider the impacts that any new regulation would have on competition.  The law also empowered the Securities Exchange Commission (SEC) to establish a national market system and a system for nationwide clearing and settlement of securities transactions, enabling the SEC to enact Regulation NMS, and created the Municipal Securities Rulemaking Board (MSRB), a self-regulatory organization that writes investor protection rules and other rules regulating broker-dealers and banks in the United States municipal securities market.\n\nEmmy Rossum: Emmanuelle Grey \"Emmy\" Rossum (born September 12, 1986) is an American actress and singer-songwriter.  She is known for the Phantom of the Opera (2004), and her portrayal of Fiona Gallagher in the television series \"Shameless\".  Rossum has starred in movies including \"Songcatcher\" (2000), \"An American Rhapsody\", (2001) and \"Passionada\" (2002).  Her role in \"Mystic River\" (2003) garnered her wider recognition.  She starred in the science fiction film \"The Day After Tomorrow\" (2004) and received critical acclaim for her performance in the leading role of Christine Daaé in \"The Phantom of the Opera\" (2004).  She has since starred in \"Poseidon\" (2006), \"Dragonball Evolution\" (2009), \"Dare\" (2009), \"Beautiful Creatures\" (2013), \"Before I Disappear\" (2014), \"You're Not You\" (2014) and \"Comet\" (2014).\n\nPattison Outdoor Advertising: Pattison Outdoor Advertising is Canada's largest Out-of-home advertising company, holding more than 55% of the national market share in horizontal posters and a 43% market share of all traditional Out-of-Home media.\n\nList of Mexican Football Transfers Winter 2011: This is a list of Mexican football transfers in the Mexican Primera Division during the winter 2011 transfer window, grouped by club.  The 2011 winter transfer window for Mexican football opened on December 1 and will close at 23:00 on December 21, 2011 for the national market and on December 31, 2011 for the international one.  Football has been played professionally in Mexico since the early 1900s.  Since 1996, the country has played two split seasons instead of a traditional long season.  There are two separate playoff and league divisions.  After many years of calling the regular seasons as \"Verano\" (Summer) and \"Invierno\" (Winter); the Primera División de México (Mexican First League Division) have changed the names of the competition, and has opted for \"Apertura\" (opening) and \"Clausura\" (closing) events.  The Apertura division begins in the middle of Mexico's summer and ends before the official start of winter.  The Clausura division begins during the New Year, and concludes in the spring season.\n\nMulti-domestic strategy: A multi-domestic strategy is a strategy by which companies try to achieve maximum local responsiveness by customizing both their product offering and marketing strategy to match different national conditions.  Production, marketing and R&D activities tend to be established in each major national market where business is done.\n\nBill Lupien: William A. Lupien (born October 6, 1941) is an American business executive in the financial industry.  He traded actively in the financial markets throughout his career.  He was a Specialist and later Exchange Governor on the Pacific Stock Exchange (PSE), a Nasdaq market maker, the Chairman and CEO of Instinet, the Chairman and CEO of OptiMark Corporation, and the Managing Director of the General Partner of a hedge fund, Kudu Partners LP.  He helped develop the world's first electronic trading system.  He also served on the Advisory Committee on the National Market System.  In 1999 he was featured in a CNBC television series as one of five people who had changed the course of the securities industry in the 20th century.\n\nPhilip Danforth Armour: Philip Danforth Armour Sr. (16 May 1832 – 6 January 1901) was an American meatpacking industrialist who founded the Chicago-based firm of Armour & Company.  Born on an upstate New York farm, he made $8000 in the California gold rush, 1852–56.  He opened a wholesale grocery business in Cincinnati, then moved it to Milwaukee.  He made millions selling meat to the United States Army during the Civil War.  In 1875, he moved his base to Chicago.  Armour's innovations including bringing live hogs to the metropolis for slaughter, inventing an assembly line system for the dis-assembly of hogs, canning the product, economy of scale and efficiency in detail.  He systematically utilized waste products, boasting that he made use of \"everything but the squeal\".  The introduction of refrigerated rail cars opened a national market for him and competitors such as Gustavus Swift.  Armour expanded into banking and speculation on the futures market for pork and wheat by 1900, his plants employed 15,000 workers; his own wealth was in the range of $50 million.  The urgent Army need for meat during the Spanish–American War of 1898 led to highly publicized complaints about \"embalmed beef.\"  Armour retired from business in 1899, and devoted himself to philanthropy in the Chicago area, including local cost housing for industrial workers, and the major institution of higher education, the Armour Institute of Technology.\n\nQuestion: Emily Rossum start in Shameless a remake of a series from what national market?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"remake_series_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the television series that is a remake.\"\n    },\n    \"original_series_origin_country\": {\n      \"type\": \"string\",\n      \"description\": \"The national market or country of origin for the original series.\"\n    },\n    \"actress_involved\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress mentioned in the question.\"\n        },\n        \"role_in_remake\": {\n          \"type\": \"string\",\n          \"description\": \"The character portrayed by the actress in the remake series.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_remake\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"remake_series_title\",\n    \"original_series_origin_country\",\n    \"actress_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "remake_series_title": {
        "type": "string",
        "description": "The title of the television series that is a remake."
      },
      "original_series_origin_country": {
        "type": "string",
        "description": "The national market or country of origin for the original series."
      },
      "actress_involved": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress mentioned in the question."
          },
          "role_in_remake": {
            "type": "string",
            "description": "The character portrayed by the actress in the remake series."
          }
        },
        "required": [
          "name",
          "role_in_remake"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "remake_series_title",
      "original_series_origin_country",
      "actress_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
