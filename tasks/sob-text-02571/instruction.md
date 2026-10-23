{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nVishweshwaraiah Prakash: Vishweshwaraiah Prakash is an Indian structural biologist, food technologist and a former director-general designate of the Council of Scientific and Industrial Research (CSIR).  He is a former director of the Central Food Technological Research Institute (CFTRI), Mysore and was involved with the International Union of Food Science and Technology as the chairman of its International Academy during 2008-10.  He received the Shanti Swarup Bhatnagar Prize, the highest Indian award in the science and technology category in 1996.  The Government of India awarded him the fourth highest civilian honour of the Padma Shri in 2004,\n\nArunachala Sreenivasan: Arunachala Sreenivasan (1909–1996) was an Indian food technologist, nutritional scientist and the director of Cancer Research Institute of the Tata Memorial Centre, Mumbai.  Born on 13 July 1909 in Tamil Nadu and after receiving the degree of Doctor of Science from the University of Madras in 1936, he served in various positions such as Deputy Director of Central Food Technological Research Institute, (1959–64), Head of Biochemistry and Food Technology Division of Bhabha Atomic Research Centre, (1964–71), Adviser at the Department of Atomic Energy, and as the Emeritus Scientist of BARC (1971–73), before superannuating from Tata Memorial Centre in 1975.  He was an elected Fellow of the Indian National Science Academy and his research findings have been documented by way of several articles.  The Government of India awarded him the third highest civilian honour of the Padma Bhushan, in 1974, for his contributions to science.  Sreenivasan died on 20 July 1996 at the age of 87.\n\nMysore: Mysore ( ), officially renamed as Mysuru, is the third most populous and the third largest city after Hubli in the state of Karnataka, India.  Located in the foothills of the Chamundi Hills about 146 km southwest of the state capital Bangalore, it is spread across an area of 128.42 km2 .  According to the provisional results of the 2011 national census of India, the population is 887,446.  Mysore City Corporation is responsible for the civic administration of the city, which is also the headquarters of the Mysore district and the Mysore division.\n\nWilliam Harrison Cook: William Harrison Cook, {'1': \", '2': \", '3': \", '4': \"} (September 2, 1903 – May 19, 1998) was an English Canadian food technologist and biochemist.  He was Executive Director of the National Research Council.\n\nMaría Orosa: María Orosa e Ylagan (1893–1945) was a Filipino food technologist, pharmaceutical chemist, humanitarian and war heroine.  She experimented with foods native to the Philippines and formulated food products like calamansi nip, a desiccated and powdered form of calamansi that could be used to make calamansi juice, banana ketchup, and a powdered preparation of soybeans called Soyalac, a \"magic food\" preparation which helped save the lives of thousands of Filipinos, Americans, and other nationals who were held prisoner in different Japanese concentration camps during World War II.\n\nSpace Food Sticks: Space Food Sticks are snacks created for the Pillsbury Company in the late 1960s by the company's chief food technologist, Howard Bauman.  Bauman was instrumental later in establishing the Hazard Analysis and Critical Control Points regulations used for food safety.\n\nJoseph H. Hulse: Joseph H. Hulse (1923–2013) was a Canadian biochemist, food technologist, writer, and the president of the International Union of Food Science and Technology.  He chaired the Committee of the Canadian chapter of the Freedom From Hunger, presided over the Canadian Institute of Food Science and Technology and was the assistant director of nutrition at the Food and Agriculture Organization, besides serving as the vice president of the International Development Research Centre (IDRC).  He was the author of several texts and monographs on nutrition and allied sciences, including a 991-page treatise, \"Sorghum and the Millets: Their Composition and Nutritive Value\".  The Government of India awarded him the fourth highest civilian honour of the Padma Shri, in 2008, for his contributions to Science and for his humanitarian activities in India.\n\nCyril P. Callister: Cyril Percy Callister (16 February 1893 – 5 October 1949) was an Australian chemist and food technologist who developed the Vegemite yeast spread.\n\nToronto Western Research Institute: The Krembil Research Institute formerly known as \"Toronto Western Research Institute\" (Krembil) is a non-profit academic medical research institute located in Canada’s largest city, Toronto.  The Krembil is one the principal research institutes of the University Health Network of academic teaching hospitals associated with the University of Toronto; the Krembil is also one of the largest research institutes in Canada focusing on human neurological disease from both a basic science and clinical research perspective.  Research within the Krembil is directed at the development of treatments for neurodegenerative diseases (Alzheimer's disease, Parkinson's disease), epilepsy, stroke, brain tumours, concussions, spinal cord injuries, neurophthalmologic and other ocular disorders, multiple sclerosis and autoimmune disorders.\n\nNicolas Appert (study association): Nicolas Appert is a Dutch study association for Food Technology students at Wageningen University.  The association is named after the French inventor Nicolas Appert, who can be seen as the first food technologist.  The chef Nicolas Appert was researching ways to preserve food for a longer period of time and discovered that heating food products in a closed glass jar would greatly increase its shelflife.  A process, nowadays called appertisation.\n\nQuestion: Where is the institute formerly directed by food technologist Vishweshwaraiah Prakash located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the food technologist.\"\n    },\n    \"institute_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the institute formerly directed by the person.\"\n    },\n    \"institute_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the institute is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the institute's city is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the institute's city is located.\"\n        },\n        \"geographical_feature\": {\n          \"type\": \"string\",\n          \"description\": \"A specific geographical feature near the institute's location.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\",\n        \"country\",\n        \"geographical_feature\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"institute_name\",\n    \"institute_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the food technologist."
      },
      "institute_name": {
        "type": "string",
        "description": "The name of the institute formerly directed by the person."
      },
      "institute_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the institute is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the institute's city is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the institute's city is located."
          },
          "geographical_feature": {
            "type": "string",
            "description": "A specific geographical feature near the institute's location."
          }
        },
        "required": [
          "city",
          "state",
          "country",
          "geographical_feature"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "institute_name",
      "institute_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
