{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKavin Bharti Mittal: Kavin Bharti Mittal is an Indian Software engineer and Internet entrepreneur known for being the founder and CEO of hike Messenger, the world's sixth largest mobile messaging application.  He is the son of Sunil Mittal, the founder and chairman of Bharti Airtel, India's largest telecom company with a user base of over 350 million.\n\nSunil Mittal: Sunil Bharti Mittal (born 23 October 1957) is an Indian Billionaire entrepreneur, philanthropist and the Founder & Chairman of Bharti Enterprises, which has diversified interests in telecom, insurance, real estate, malls, hospitality, agri and food besides other ventures.  Bharti Airtel, the group's flagship company is the world's third largest and India's largest telecom company with operations in 18 countries across Asia and Africa with a customer base of over 372 million.  Bharti Airtel clocked revenues of over USD 14.75 billion in FY2016.  He is listed as the 8th Richest person in India by Forbes with a Net worth of $7 Billion.\n\nAirtel India: Airtel India is the second largest provider of mobile telephony and second largest provider of fixed telephony in India, and is also a provider of broadband and subscription television services.  The brand is operated by several subsidiaries of Bharti Airtel, with Bharti Hexacom and Bharti Telemedia providing broadband fixed line services and Bharti Infratel providing telecom passive infrastructure service such as telecom equipment and telecom towers.  Bharti Airtel Limited is part of Bharti Enterprises and is headed by Sunil Bharti Mittal.\n\nBharti Airtel: Bharti Airtel Limited is an Indian global telecommunications services company based in New Delhi, India.  It operates in 18 countries across South Asia and Africa.  Airtel provides GSM, 3G and 4G LTE mobile services, fixed line broadband and voice services depending upon the country of operation.  Airtel is also testing VoLTE technology across five cities in India and should roll out the technology towards the end of 2017.  It is the largest mobile network operator in India and the third largest in the world with 400 million subscribers.  Airtel was named India's second most valuable brand in the first ever Brandz ranking by Millward Brown and WPP plc.\n\nAirtel Super Singer: Airtel Super Singer (subtitled \"Thamizhagathin Brahmaanda kuralukkana Thedal\" ,\"the search for the greatest voice of Tamil Nadu\") is a reality TV singing competition in the Tamil language that is sponsored by the mobile service provider Bharti Airtel.  The show is televised in India on Vijay TV, and worldwide through partner broadcasting networks.  The show, together with its spin-off editions such as Airtel Super Singer Junior, are part of Vijay TV's Super Singer TV series.\n\nAirtel Zero: Airtel Zero was a platform launched on 6 April 2015 in India by Bharti Airtel, a multinational telecommunications service company across South Asia and the largest cellular service provider in India, with 192.22 million subscribers.  As per reports, Airtel Zero was a platform through which Airtel would have offered users free access to certain mobile applications and services from companies who had signed up with Airtel.\n\nAirtel Africa: Bharti Airtel International (Netherlands) B.V., doing business as Airtel Africa, is a holding company and a subsidiary of Indian telecommunications company Bharti Airtel.  Through its subsidiaries, Airtel Africa provides telecommunication services in 15 African countries.\n\nBharti Enterprises: Bharti Enterprises is an Indian business conglomerate headquartered in New Delhi, India.  It was founded in 1976 by Sunil Bharti Mittal and it operates in 17 countries across Asia and Africa.  Bharti Enterprises owns businesses spanning across telecommunications, agri business, financial services and manufacturing.\n\nAirtel Sri Lanka: Airtel (Sinhalese: එයාටෙල්; Tamil: ஏர்டெல்) is the brand name of mobile network operator, Bharti Airtel Lanka (Pvt.) Ltd, the Sri Lankan subsidiary of Indian telecommunications company Bharti Airtel.  The company was awarded a mobile phone operator license in 2006 and was scheduled to start operations in early 2007, however the company didn't commence services until 12 January 2009.  Airtel had over 1.7 million active subscribers as of January 2013 .\n\nAirtel Uganda: Airtel Uganda is a mobile communications and information technology services provider in Uganda.  The company also offers mobile funds transfer and banking services known as \"Airtel Money\".  Airtel Uganda Limited is a subsidiary of Bharti Airtel Limited, the Indian telecommunications conglomerate operating in over 20 countries in Asia, Africa, and the Channel Islands.\n\nQuestion: How may countries does Bharti Airtel's parent company operate in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"parent_company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of Bharti Airtel's parent company.\"\n    },\n    \"number_of_countries_operated_in\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of countries the parent company operates in.\"\n    },\n    \"regions_of_operation\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The regions where the parent company operates.\"\n    }\n  },\n  \"required\": [\n    \"parent_company_name\",\n    \"number_of_countries_operated_in\",\n    \"regions_of_operation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "parent_company_name": {
        "type": "string",
        "description": "The name of Bharti Airtel's parent company."
      },
      "number_of_countries_operated_in": {
        "type": "integer",
        "description": "The total number of countries the parent company operates in."
      },
      "regions_of_operation": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The regions where the parent company operates."
      }
    },
    "required": [
      "parent_company_name",
      "number_of_countries_operated_in",
      "regions_of_operation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
