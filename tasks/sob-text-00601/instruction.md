{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSchneider Electric: Schneider Electric SE is a French multinational corporation that specialises in energy management and automation solutions, spanning hardware, software, and services.  Native of France, the company is headquartered in Rueil-Malmaison and is also based at the World Trade Center of Grenoble with offices throughout the world.  A Fortune Global 500 company, Schneider Electric is publicly traded on the Euronext Exchange and is a component of the Euro Stoxx 50 stock market index.  In FY2016, the company posted revenues of about €25 billion.\n\nInsurial: Insurial Americas, Inc or Insurial was an American multinational corporation headquartered in Manhattan, New York City, New York, United States.  The company invested in and operated the group's wholly owned subsidiaries and branches in the United Arab Emirates, China, Pakistan, Japan, and India.  Insurial Americas, Inc also participated in Asia-Pacific transactions through the group's Hong Kong-based equities arm.  The group's primary areas of operations were trade finance, trade negotiations, inspections, and logistics.  The group's estimated revenues, prior to its merger with an undisclosed entity, were in excess of $400 million.\n\nAmdocs: Amdocs is a multinational corporation headquartered in Chesterfield, Missouri, with support and development centers located worldwide.  The company specializes in software and services for communications, media and financial services providers and digital enterprises.  Its offerings include business support systems (BSS), operational support systems (OSS), open network solutions, Internet of Things, big data analytics and entertainment and media solutions.\n\nFlowserve: The Flowserve Corporation is an American multinational corporation and one of the largest suppliers of industrial and environmental machinery such as pumps, valves, end face mechanical seals, automation, and services to the power, oil, gas, chemical and other industries.  Headquartered in Irving, Texas, which is a suburb of Dallas, Texas, Flowserve has over 19,000 employees in more than 60 countries.  Flowserve sells products and offers aftermarket services to engineering and construction firms, original equipment manufacturers, distributors and end users.  The Flowserve brand name originated in 1997 with a merger of BW/IP and Durco International.\n\nEmerson Electric: The Emerson Electric Company () is an American multinational corporation headquartered in Ferguson, Missouri, United States.  This Fortune 500 company manufactures products and provides engineering services for a wide range of industrial, commercial, and consumer markets.\n\nABB Group: ABB (ASEA Brown Boveri) is a Swedish-Swiss multinational corporation headquartered in Zürich, Switzerland, operating mainly in robotics, power, heavy electrical equipments, and automation technology areas.  It is ranked 286th in The World's Most Admired companies in the Fortune 500 global list of 2016.  ABB has been a Global Fortune 500 company for 23 years.\n\nDow Corning: Dow Corning is an American multinational corporation headquartered in Midland, Michigan, United States.  Originally established as a joint venture between the Dow Chemical Company and Corning Incorporated, it is now owned by DowDuPont and specializes in silicone and silicon-based technology, and is the largest silicone product producer in the world.\n\nAPM Automation Solutions: APM Automation Solutions is an Israeli-based developer of solids volume and level measurement instrumentation established in Tel Aviv, Israel.  The APM technology is used in all the bulk solids industries such as:food and beverage, metals and mining, power, cement, coal, chemical, pulp and paper, and other industries.  The outfit recently became part of the Emerson Process Management business under Rosemount Brand.\n\nManpowerGroup: ManpowerGroup (formerly known as Manpower Inc.) is a Fortune 500 American multinational corporation headquartered in Milwaukee, Wisconsin.  Founded in 1948 by Elmer Winter and Aaron Scheinfeld, ManpowerGroup is the third-largest staffing firm in the world behind Swiss firm Adecco and Dutch firm Randstad.  The company provides administrative & support services, professional services, and business services through its four primary brands: Manpower (contingent staffing & permanent recruitment), Experis (professional resourcing and project-based solutions), Right Management (career management, workforce consulting, and training & development), and ManpowerGroup Solutions (managed services and outsourcing).\n\nDell EMC: Dell EMC (EMC Corporation until 2016) is an American multinational corporation headquartered in Hopkinton, Massachusetts, United States.  Dell EMC sells data storage, information security, virtualization, analytics, cloud computing and other products and services that enable organizations to store, manage, protect, and analyze data.  Dell EMC's target markets include large companies and small- and medium-sized businesses across various vertical markets.  The company's stock (as EMC Corporation) was added to the New York Stock Exchange on April 6, 1986, and was also listed on the S&P 500 index.\n\nQuestion: Which of the corporation to which  APM Automation Solutions recently became a part is an American multinational corporation headquartered in Ferguson, Missouri, United States?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the corporation that matches the criteria.\"\n    },\n    \"is_american_multinational\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the corporation is an American multinational corporation.\"\n    },\n    \"headquarters_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the corporation is headquartered.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the corporation is headquartered.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the corporation is headquartered.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_to_apm_automation_solutions\": {\n      \"type\": \"string\",\n      \"description\": \"Describes how this corporation is related to APM Automation Solutions.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"is_american_multinational\",\n    \"headquarters_location\",\n    \"relationship_to_apm_automation_solutions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the corporation that matches the criteria."
      },
      "is_american_multinational": {
        "type": "boolean",
        "description": "True if the corporation is an American multinational corporation."
      },
      "headquarters_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the corporation is headquartered."
          },
          "state": {
            "type": "string",
            "description": "The state where the corporation is headquartered."
          },
          "country": {
            "type": "string",
            "description": "The country where the corporation is headquartered."
          }
        },
        "required": [
          "city",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "relationship_to_apm_automation_solutions": {
        "type": "string",
        "description": "Describes how this corporation is related to APM Automation Solutions."
      }
    },
    "required": [
      "company_name",
      "is_american_multinational",
      "headquarters_location",
      "relationship_to_apm_automation_solutions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
