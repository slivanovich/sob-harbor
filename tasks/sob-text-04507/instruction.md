{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIndian Institute of Spices Research: The Indian Institute of Spices Research (IISR) is an autonomous organization engaged in agricultural research related to spices in India.  The institute has its headquarters in Moozhikkal, Silver Hills, Kozhikode, Kerala and is a subsidiary of Indian Council of Agricultural Research (ICAR), New Delhi, under the Ministry of Agriculture, India.\n\nCentral Sheep and Wool Research Institute: The ICAR-Central Sheep and Wool Research Institute (ICAR-CSWRI) is an Indian Council of Agricultural Research subsidiary commissioned for research, training and extension activities related to sheep and rabbits.  The Institute is an autonomous body and is sponsored by the Department of Agricultural Research and Education (DARE), Ministry of Agriculture, Government of India.  It is situated in Avikanagar, Malpura, in Rajasthan, India.  It works in close liaison with the other ICAR institutes, Central Wool Development Board, Sheep and Wool Marketing Federation, Department of Biotechnology (GOI), Small Entrepreneurs, NGOs, State Animal Husbandry and Khadi gram and Cottage industries.\n\nIndian Veterinary Research Institute: Indian Veterinary Research Institute (IVRI) is located at Izatnagar, Bareilly in Uttar Pradesh state.  It is India's premier advanced research facility in the field of veterinary medicine and allied branches.  It has regional campuses at Mukteshwar, Bangalore, Palampur, Bhopal, Kolkata and Srinagar.  Formerly known as Imperial Bacteriological Laboratory, it was renamed in 1925 as Imperial Veterinary Research Institute.  The name of the Institute was changed following independence to Indian Veterinary Research Institute.  Administrative control of the Institute is currently under Indian Council of Agricultural Research (ICAR), New Delhi.  The Ministry of Education, Govt.  of India on the recommendation of University Grants Commission conferred the status of the Deemed to be University on 16 November 1983 under Section 3 of UGC Act 1956.\n\nCentral Soil Salinity Research Institute: The Central Soil Salinity Research Institute (acronym CSSRI) is an autonomous institute of higher learning, established under the umbrella of Indian Council of Agricultural Research (ICAR) by the Ministry of Agriculture, Government of India for advanced research in the field of soil sciences.  The Institute is located on Kachawa Road in Karnal, in the state of Haryana, 125 km from the Indian capital of New Delhi.\n\nIndian Institute of Millets Research: The Indian Institute of Millets Research (IIMR), located at Rajendranagar (Hyderabad, Telangana, India) is an agricultural research institute engaged in basic and strategic research on sorghum and other millets. IIMR operates under the aegis of Indian Council of Agricultural Research (ICAR).  It conducts agricultural research on Millets breeding, improvement, pathology and value addition.  IIMR coordinates and facilitates sorghum research at national level through the All India Coordinated Research Projects on Sorghum (AICRP on Sorghum) and provides linkages with various national and international agencies.\n\nIndian Institute of Soil Science: The Indian Institute of Soil Science (acronym IISS) is an autonomous institute for higher learning, established under the umbrella of Indian Council of Agricultural Research (ICAR) by the Ministry of Agriculture, Government of India for advanced research in the field of soil sciences.\n\nIndian Institute of Natural Resins and Gums: The Indian Institute of Natural Resins and Gums (acronym IINRG), formerly known as the Indian Lac Research Institute, is an autonomous institute, established under the umbrella of Indian Council of Agricultural Research (ICAR) by the Ministry of Agriculture, Government of India for advanced research on lac and other natural resins and gums.  The Institute is located at Namkum, Ranchi in Jharkhand, India.\n\nDirectorate of Groundnut Research: ICAR - Directorate of Groundnut Research (ICAR-DGR) formerly known as National Research Centre for Groundnut is a premier national level institute set up by the Indian Council of Agricultural Research, Ministry of Agriculture of India to cater to the needs of agricultural science research in the field of groundnut (peanut) crop in India.  ICAR-DGR was established in 1979 at Junagadh, Gujarat to give a fillip to research for enhancing productivity of groundnut in keeping with its importance among the oilseed crops of India.  The research centre came into being as the first crop commodity research unit under the category of NRC's (National Research Centres) of the Indian Council of Agricultural Research, as an autonomous body set up as a registered society.  The National Research Centre on Groundnut (NRCG) was elevated to the level of a Directorate in the year 2009 and rechristened as the Directorate of Groundnut Research.\n\nIndian Institute of Sugarcane Research: The Indian Institute of Sugarcane Research (acronym IISR) is an autonomous institute of higher learning, under the umbrella of Indian Council of Agricultural Research (ICAR) by the Ministry of Agriculture, Government of India for advanced research in sugar cane agriculture.  The Institute is located on Raibareli Road, Dilkusha (Post Office) in Lucknow, Uttar Pradesh, India.\n\nGum arabic: Gum arabic, also known as acacia gum, is a natural gum consisting of the hardened sap of various species of the acacia tree.  Originally, gum arabic was collected from \"Acacia nilotica\" which was called the \"gum arabic tree\"; in the present day, gum arabic is predominantly collected from two related species, namely \"Acacia senegal\" and \"Vachellia (Acacia) seyal\".  Producers harvest the gum commercially from wild trees, mostly in Sudan (80%) and throughout the Sahel, from Senegal to Somalia—though it is historically cultivated in Arabia and West Asia.\n\nQuestion: The Indian Institute of Natural Resins and Gums (acronym IINRG), formerly known as the Indian Lac Research Institute, is an autonomous institute, established under the umbrella of Indian Council of Agricultural Research (ICAR) by the Ministry of Agriculture, Government of India, for advanced research on what, and other natural resins and Gum arabic?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"institute_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the research institute.\"\n    },\n    \"acronym\": {\n      \"type\": \"string\",\n      \"description\": \"The acronym of the research institute.\"\n    },\n    \"former_name\": {\n      \"type\": \"string\",\n      \"description\": \"The previous name of the institute.\"\n    },\n    \"research_areas\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of specific materials or subjects the institute conducts advanced research on.\"\n    },\n    \"parent_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The main organization under which the institute operates.\"\n    },\n    \"sponsoring_ministry\": {\n      \"type\": \"string\",\n      \"description\": \"The government ministry that established or sponsors the institute.\"\n    }\n  },\n  \"required\": [\n    \"institute_name\",\n    \"acronym\",\n    \"former_name\",\n    \"research_areas\",\n    \"parent_organization\",\n    \"sponsoring_ministry\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "institute_name": {
        "type": "string",
        "description": "The full name of the research institute."
      },
      "acronym": {
        "type": "string",
        "description": "The acronym of the research institute."
      },
      "former_name": {
        "type": "string",
        "description": "The previous name of the institute."
      },
      "research_areas": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of specific materials or subjects the institute conducts advanced research on."
      },
      "parent_organization": {
        "type": "string",
        "description": "The main organization under which the institute operates."
      },
      "sponsoring_ministry": {
        "type": "string",
        "description": "The government ministry that established or sponsors the institute."
      }
    },
    "required": [
      "institute_name",
      "acronym",
      "former_name",
      "research_areas",
      "parent_organization",
      "sponsoring_ministry"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
