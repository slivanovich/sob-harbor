{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStandard Oil: Standard Oil Co.  Inc. was an American oil producing, transporting, refining, and marketing company.  Established in 1870 by John D. Rockefeller as a corporation in Ohio, it was the largest oil refinery in the world of its time.  Its controversial history as one of the world's first and largest multinational corporations ended in 1911, when the United States Supreme Court ruled that Standard Oil was an illegal monopoly.\n\nJ. Paul Getty: Jean Paul Getty (December 15, 1892 – June 6, 1976) was an American industrialist.  He founded the Getty Oil Company, and in 1957 \"Fortune\" magazine named him the richest living American, while the 1966 Guinness Book of Records named him as the world's richest private citizen, worth an estimated $1.2 billion (approximately $ billion in 2016).  At his death, he was worth more than $2 billion (approximately $ billion in 2016).  A book published in 1996 ranked him as the 67th richest American who ever lived, based on his wealth as a percentage of the gross national product.\n\nMOGAS Group: Maestro Oil and Gas Solutions (MOGAS) is a multinational integrated downstream oil marketing company.  As of 2015, its business operations include international oil trading, fuels and lubrication services and retail networks.  The company is registered in the UAE and has its head office in Kampala, Uganda but is operational in Uganda, Kenya, Tanzania, DRC, U.A.E, Rwanda and Burundi.\n\nAstral Oil Works: Astral Oil Works was an American oil company specializing in illuminating oil, and based in Brooklyn, New York.  Astral Oil was a high-quality kerosene used in lamps and noted for being relatively safe.  It was founded by Charles Pratt.  Charles Pratt and Company (including Astral Oil) became part of John D. Rockefeller’s Standard Oil Trust in 1874, although the fact that Astral Oil was a New York branch of Standard Oil in Ohio was not made public until 1892.\n\nPan American Petroleum and Transport Company: The Pan American Petroleum and Transport Company (PAT) was an oil company founded in 1916 by the American oil tycoon Edward L. Doheny after he had made a huge oil strike in Mexico.  Pan American profited from fuel demand during World War I, and from the subsequent growth in use of automobiles.  For several years Pan American was the largest American oil company, with holdings in the United States, Mexico, Colombia and Venezuela.  In 1924 Pan American was involved in the Teapot Dome scandal over irregularities in the award of a U.S. government oil concession.  Standard Oil of Indiana obtained a majority stake in 1925.  The company sold its foreign properties to Standard Oil of New Jersey in 1932.  What was left of Pan American was merged with Standard Oil of Indiana in 1954 to form Amoco.\n\nThe Trump Network: The Trump Network was a multi-level marketing company named after businessman Donald Trump.  The company, which sold vitamins and health products, was initially founded as Ideal Health in 1997, before being renamed in 2009 as part of a licensing agreement between Trump and the owners.  The licensing agreement expired at the end of 2011, and the company's remaining assets were sold to Bioceutica the following year.\n\nStandard Oil of Iowa: Standard Oil Company of Iowa was created in 1885 as a subsidiary of the Standard Oil Trust to handle marketing along the Pacific Coast states of Idaho, Oregon, Washington, California, and Arizona.  Though named for the midwestern state, it never included Iowa as one of its primary marketing areas.  A prior company named Standard Oil of California had been formed in 1877, and was not associated with the Standard Oil Trust.  In 1906, Standard Oil of Iowa was dissolved and its assets handed over to a new Standard Oil of California, later Chevron Oil Company, and now the Chevron Corporation.  Standard Oil Company of Iowa is thus the original company that is now Chevron.\n\nGetty Oil: Getty Oil is an American oil marketing company with its origins as part of the large integrated oil company founded by the father of J. Paul Getty.\n\nOman Oil Marketing Company: Oman Oil Marketing Company SAOG (omanoil) was launched in October 2003, along with its new brand identity, when Oman Oil Company acquired shares of what was formally known as BP Oman in December 2003.  Today, it is the only 100 percent Omani owned fuels marketing company, 49% of which is owned by Oman Oil Company.  Other shareholders include Oman Cement Company, BankMuscat and Dhofar International Development and Investment Holding Company.  The Chairman of the Board of directors is Salim Abdullah Al Rawas and the Chief Executive Officer is Omar Ahmad Salim Qatan.\n\nCharles Millard Pratt: Charles Millard Pratt (November 2, 1855 – November 27, 1935) was an American oil industrialist, educator, and philanthropist.  As the eldest son of industrialist Charles Pratt, In 1875 he began working at Charles Pratt and Company, soon becoming president.  He was a director of the Standard Oil Company and later a president of the Pratt Institute in Brooklyn.  He donated large sums to Vassar College and Amherst College, among other institutions.\n\nQuestion: What was the American industrialist that founded an American oil marketing company named by a 1957 \"Fortune\" magazine?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"industrialist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American industrialist.\"\n    },\n    \"company_founded\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the oil marketing company founded by the industrialist.\"\n    },\n    \"fortune_magazine_designation\": {\n      \"type\": \"string\",\n      \"description\": \"The designation or title given to the industrialist by Fortune magazine in 1957.\"\n    },\n    \"fortune_magazine_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year Fortune magazine made the designation.\"\n    }\n  },\n  \"required\": [\n    \"industrialist_name\",\n    \"company_founded\",\n    \"fortune_magazine_designation\",\n    \"fortune_magazine_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "industrialist_name": {
        "type": "string",
        "description": "The name of the American industrialist."
      },
      "company_founded": {
        "type": "string",
        "description": "The name of the oil marketing company founded by the industrialist."
      },
      "fortune_magazine_designation": {
        "type": "string",
        "description": "The designation or title given to the industrialist by Fortune magazine in 1957."
      },
      "fortune_magazine_year": {
        "type": "integer",
        "description": "The year Fortune magazine made the designation."
      }
    },
    "required": [
      "industrialist_name",
      "company_founded",
      "fortune_magazine_designation",
      "fortune_magazine_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
