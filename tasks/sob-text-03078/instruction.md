{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShikha Sharma: Shikha Sharma (born November 19, 1958) is the Managing Director & CEO of Axis Bank, the third largest private sector bank in India.  Sharma joined Axis Bank in 2009 and as a leader adept at managing change, she has focused on transforming Axis Bank into a Bank with strengths across a wide range of Corporate and Retail Banking products.  At Axis Bank, she has focused on strengthening its retail lending franchise, enlarged its investment banking & advisory capabilities and developed a comprehensive portfolio of products in the payments space.\n\nRanjana Kumar: Ranjana Kumar, was (from 2005) Vigilance Commissioner in Central Vigilance Commission, after her retirement as Chairperson of National Bank for Agriculture and Rural Development (NABARD) is a prominent Indian banker.  When the Government of India appointed her as the Chairperson and managing Director of the Indian Bank, she became the first woman to become head of a public sector bank in India.  At the time of her appointment, the Indian Bank was saddled with huge losses, and during her tenure she ensured the turnaround of the Indian Bank.\n\nUday Kotak: Uday Kotak (born 15 March 1959) is an Indian banker; the executive vice chairman and managing director of Kotak Mahindra Bank.\n\nAditya Puri: Aditya Puri is the Managing Director of HDFC Bank, India's largest private sector bank.  He assumed this position in September 1994, making him the longest-serving head of any private bank in the country.  India Today magazine ranked him #24th in India's 50 Most powerful people of 2017 list.\n\nCenturion Bank of Punjab: The Centurion Bank of Punjab (formerly Centurion Bank) was an Indian private sector bank that provided retail and corporate banking services.  It operated on a strong nationwide franchise of 403 branches and had over 5,000 employees.  The bank listed its shares on the major Indian stock exchanges and on the Luxembourg Stock Exchange.  On 23 May 2008 HDFC Bank acquired Centurion Bank of Punjab.\n\nAB Bank: AB Bank (formerly Arab Bangladesh Bank) is a leading private sector bank in Bangladesh established in 31 December 1981.  This was the first joint venture private bank in Bangladesh.  On 14 November 2007 Bangladesh bank approved the name change to AB Bank from Arab Bangladesh Bank.  A former deputy managing director was charged with embezzling 3.25 billion taka from the bank.  In 2014 AB bank completed its acquisition of Cashlink Bangladesh Limited.  A former vice president and his wife were sentenced to prison terms for embezzlement from the bank in 2016.\n\nCitibank India: Citibank India is an Indian private sector bank headquartered in Mumbai, Maharashtra.  It is a subsidiary of Citigroup, a multinational financial services corporation headquartered in New York City, United States.  The Indian Headquarters are at Bandra Kurla Complex, a hub for multinational corporations in Mumbai.\n\nCatholic Syrian Bank: The Catholic Syrian Bank Limited (CSB) is an Indian private sector bank with its headquarters at Thrissur, Kerala, India.  It is one of the oldest banks in India.  The bank has a network of over 420 branches and more than 240 ATMs across India.\n\nV. P. Shetty: Vaddarse Prabhankar Shetty, better known as V.P. Shetty, is an Indian banker who is the Chairman of JM Financial Asset Reconstruction Co.  Pvt. Ltd., JM Financial Asset Management Co.  Pvt. Ltd. and JM Financial Products Ltd.  He retired as Chairman and Managing Director of IDBI Bank in 2007.  Before joining IDBI, he was also Chairman and Managing Director of UCO Bank and Canara Bank.  He began his career with Vijaya Bank.  Currently, he is a member of the Banking Codes and Standards Board of India.\n\nKotak Mahindra Bank: Kotak Mahindra Bank is an Indian private sector bank headquartered in Mumbai, Maharashtra, India.  In February 2003, Reserve Bank of India (RBI) gave the licence to Kotak Mahindra Finance Ltd., the group's flagship company, to carry on banking business.\n\nQuestion: Uday Kotak in an Indian banker and managing director of an Indian private sector bank headquarted where?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"banker_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the banker.\"\n    },\n    \"bank_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the bank associated with the banker.\"\n    },\n    \"headquarters_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the bank is headquartered.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the bank is headquartered.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the bank is headquartered.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"banker_name\",\n    \"bank_name\",\n    \"headquarters_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "banker_name": {
        "type": "string",
        "description": "The name of the banker."
      },
      "bank_name": {
        "type": "string",
        "description": "The name of the bank associated with the banker."
      },
      "headquarters_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the bank is headquartered."
          },
          "state": {
            "type": "string",
            "description": "The state where the bank is headquartered."
          },
          "country": {
            "type": "string",
            "description": "The country where the bank is headquartered."
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "banker_name",
      "bank_name",
      "headquarters_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
