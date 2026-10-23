{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSrikanth Balachandran: Srikanth Balachandran is an Indian business executive.  He is the current Global CHRO of Bharti Airtel, an Indian multinational telecommunications services company with operations in 17 countries.\n\nDiplomatic Telecommunications Service: The Diplomatic Telecommunications Service (DTS) is a system of integrated telecommunications networks that supports foreign affairs agencies in Washington, D.C., and U.S. diplomatic missions abroad.  It is administered by the United States Department of State Diplomatic Telecommunications Service Program Office (DTSPO).  DTS is a global network of telecommunications sites that is charged with providing a global, reliable, and cost-effective communications network for the U.S. foreign affairs community.\n\nMahanagar Telephone Nigam Limited: Mahanagar Telephone Nigam Limited (MTNL) is a state-owned telecommunications service provider in the metro cities of Mumbai and New Delhi in India and in the island nation of Mauritius in Africa.  The company had a monopoly in Mumbai and New Delhi until 1992, when the telecom sector was opened to other service providers.  \"Transparency makes us different\" is the motto of the company.  The Government of India currently holds 100% stock in the company.\n\nTelecommunications Service Priority: Telecommunications Service Priority (TSP) is a United States program that authorizes national security and emergency preparedness organizations to receive priority treatment for vital voice and data circuits or other telecommunications services.  As a result of hurricanes, floods, earthquakes, and other natural or man-made disasters, telecommunications service vendors frequently experience a surge in requests for new services and requirements to restore existing services.  The TSP Program provides service vendors a Federal Communications Commission (FCC) mandate to prioritize requests by identifying those services critical to national security and emergency preparedness.  A TSP assignment ensures that it will receive priority attention by the service vendor before any non-TSP service.\n\nPawan Hans: Pawan Hans Limited is a helicopter service company based in New Delhi, India.  Pawan Hans is a Mini Ratna-I category PSU.  It has cumulatively flown more than 1 million hours and has had 2.5 million landings on its fleet since its formation.  The operations are based at the Juhu Aerodrome in Vile Parle (West), Mumbai.  Other than providing helicopter services to ONGC to its off-shore locations, this public sector company is often engaged for providing services to various state governments in India, particularly in North-east India, Inter-island ferry services in Andaman & Nicobar Islands, for last 26 years service to Lakshdweep Administration in ferrying people from Islands to Kochi Intl airport and inter-island services.  These are considered as backbone of Lakshadweep and Minicoy Islands which are far flung from Indian shores extending up to 400–500 km into Arabian sea, Vaishno Devi Helicopter service for devotees.  Service to BSF and Maharashtra Police for Medical and Logistics support in event of maoist attack on troops.  Rohini Heliport owned by Pawan Hans, was inaugurated by Union Civil Aviation Minister, Ashok Gajapathi Raju on February 28, 2017.  The heliport, located north west of New Delhi, is the first of its kind in the country.\n\nDalsvyaz: OJSC Dalsvyaz (Russian: ОАО «Дальсвязь» ) is a telecommunications service provider active in the Russian Far East.  It is part of Svyazinvest Holdings, which is Russia's largest telecommunications holding company, and which owns many large regional telecommunications service providers in Russia.\n\nIndian Telecommunication Service: The Indian Telecommunications Service, widely known as ITS, and earlier known as 'Telegraph Engineering Service Class I'(TES Class I)is an organised civil service of Government of India.  The appointment to this service is done through Combined Engineering Services exam held every year by Union Public Service Commission (UPSC) of India.  ITS is a Group 'A' Central Civil Service(Gazetted) post of the Union of India.  The service was created to meet the technical and managerial functions of the government in areas related to telecommunications.The Department of Telecommunications (DOT) had been run for years by this permanent cadre of technical civil servants called the Indian Telecom Service (ITS).\n\nAirtel Zero: Airtel Zero was a platform launched on 6 April 2015 in India by Bharti Airtel, a multinational telecommunications service company across South Asia and the largest cellular service provider in India, with 192.22 million subscribers.  As per reports, Airtel Zero was a platform through which Airtel would have offered users free access to certain mobile applications and services from companies who had signed up with Airtel.\n\nBharti Airtel: Bharti Airtel Limited is an Indian global telecommunications services company based in New Delhi, India.  It operates in 18 countries across South Asia and Africa.  Airtel provides GSM, 3G and 4G LTE mobile services, fixed line broadband and voice services depending upon the country of operation.  Airtel is also testing VoLTE technology across five cities in India and should roll out the technology towards the end of 2017.  It is the largest mobile network operator in India and the third largest in the world with 400 million subscribers.  Airtel was named India's second most valuable brand in the first ever Brandz ranking by Millward Brown and WPP plc.\n\nPacnet: Pacnet was a global telecommunications service provider between 2008 and 2015.  It was formed from the operational merger of Asia Netcom and Pacific Internet on 8 January 2008.  It was owned by a private investor group comprising Ashmore Investment Management Limited, Spinnaker Capital Limited and Clearwater Capital Partners.  Its acquisition by the Australian telecommunications company Telstra was announced at the end of 2014, and completed in April 2015.\n\nQuestion: Srikanth Balachandran is the Global CHRO of what Indian global telecommunications service company based in New Delhi, India?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person mentioned in the question.\"\n    },\n    \"person_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person within the company.\"\n    },\n    \"company_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the telecommunications service company.\"\n        },\n        \"headquarters_city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the company is based.\"\n        },\n        \"headquarters_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the company is based.\"\n        },\n        \"service_type\": {\n          \"type\": \"string\",\n          \"description\": \"The primary type of service the company provides.\"\n        },\n        \"is_global\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the company operates globally.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"headquarters_city\",\n        \"headquarters_country\",\n        \"service_type\",\n        \"is_global\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_role\",\n    \"company_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person mentioned in the question."
      },
      "person_role": {
        "type": "string",
        "description": "The role of the person within the company."
      },
      "company_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the telecommunications service company."
          },
          "headquarters_city": {
            "type": "string",
            "description": "The city where the company is based."
          },
          "headquarters_country": {
            "type": "string",
            "description": "The country where the company is based."
          },
          "service_type": {
            "type": "string",
            "description": "The primary type of service the company provides."
          },
          "is_global": {
            "type": "boolean",
            "description": "Indicates if the company operates globally."
          }
        },
        "required": [
          "name",
          "headquarters_city",
          "headquarters_country",
          "service_type",
          "is_global"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "person_role",
      "company_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
