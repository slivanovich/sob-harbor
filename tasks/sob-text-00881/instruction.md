{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSusan Gelman: Susan A. Gelman (born July 24, 1957) is currently Heinz Werner Distinguished University Professor of psychology and linguistics and the director of the Conceptual Development Laboratory at the University of Michigan.  Her research focuses on cognitive development, language acquisition, categorization, inductive reasoning, causal reasoning, and the relationship between language and thought.  Gelman subscribes to the domain specificity view of cognition, which asserts that the mind is composed of specialized modules supervising specific functions in the human and other animals.\n\nHeinz Engl: Heinz Werner Engl (born 28 March 1953) is an Austrian mathematician, the rector of the University of Vienna.\n\nUniversity of Vienna: The University of Vienna (German: \"Universität Wien\" ) is a public university located in Vienna, Austria.  It was founded by Duke Rudolph IV in 1365 and is one of the oldest universities in the German-speaking world.  With its long and rich history, the University of Vienna has developed into one of the biggest universities in Europe, and also one of the most renowned, especially in the Humanities.  It is associated with 15 Nobel prize winners and has been the academic home of a large number of figures both of historical and academic importance.\n\nUniversity of Coimbra: The University of Coimbra (UC; Portuguese: \"Universidade de Coimbra\" , ] ) is a Portuguese public university in Coimbra, Portugal.  Established in 1290 in Lisbon, it went through a number of relocations until it was moved permanently to its current city in 1537, being one of the oldest universities in continuous operation in the world, the oldest university of Portugal, and one of the country's largest higher education and research institutions.\n\nMedical University of Vienna: The Medical University of Vienna (German: \"Medizinische Universität Wien\") is a public university located in Vienna, Austria.  It is the direct successor to the faculty of medicine at the University of Vienna, founded in 1365 by Rudolf IV, Duke of Austria.  As one of the oldest medical schools in the world, it is the oldest in the German-speaking countries, and was the second medical faculty in the Holy Roman Empire, after the Charles University of Prague.\n\nHumboldt University of Berlin: The Humboldt University of Berlin (German: \"Humboldt-Universität zu Berlin\" , abbreviated HU Berlin) is one of Berlin's oldest universities, founded on 15 October 1811 as the University of Berlin (\"Berliner Universität\") by Frederick William III of Prussia, on the initiative of the liberal Prussian educational reformer and linguist Wilhelm von Humboldt.  The university is known worldwide for pioneering the Humboldtian model of higher education, which has strongly influenced other European and Western universities, and the university has been widely called \"the mother of all modern universities.\"  The university has been associated with 40 Nobel Prize winners and is considered one of the best universities in Europe as well as one of the most prestigious universities in the world for arts and humanities.  It was widely regarded as the world's preeminent university for the natural sciences during the 19th and early 20th century, and is linked to major breakthroughs in physics and other sciences by its professors such as Albert Einstein.\n\nUniversity of Bucharest: The University of Bucharest (Romanian: \"Universitatea din București\" ), commonly known after its abbreviation UB in Romania, is a public university founded in 1864 by decree of Prince Alexandru Ioan Cuza to convert the former Saint Sava Academy into the current University of Bucharest, making it the second oldest modern university in Romania.  It is one of the five members of the \"Universitaria Consortium\" (the group of elite Romanian universities).\n\nUniversity of Saint Francis Xavier: The Royal and Pontificial Major University of Saint Francis Xavier of Chuquisaca (Spanish: Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca or USFX) is a public university in Sucre, Bolivia.  It is one of the oldest universities of the new world, ranking as the second oldest university in the Americas behind Peru's National University of San Marcos.  On many historical texts it is also referred as the University of Charcas (Spanish: Universidad de Charcas ).\n\nUniversity of Aberdeen: The University of Aberdeen is a public research university in Aberdeen, Scotland.  It is an ancient university founded in 1495 when William Elphinstone, Bishop of Aberdeen, petitioned Pope Alexander VI on behalf of James IV, King of Scots to establish King's College, making it Scotland's third-oldest university and the fifth-oldest in the English-speaking world.  The university as it is today was formed in 1860 by a merger between King's College and Marischal College, a second university founded in 1593 as a Protestant alternative to the former.  Today, Aberdeen is consistently ranked among the top 200 universities in the world and is one of two universities in the city, the other being the Robert Gordon University.\n\nRashtrasant Tukadoji Maharaj Nagpur University: Rashtrasant Tukadoji Maharaj Nagpur University (RTMNU), formerly known as \"Nagpur University\", is a public University, established on 4 August 1923 in the city of Nagpur in Maharashtra state in central India.  It is one of the oldest universities in India and the second oldest in the state of Maharashtra, after the University of Mumbai.  It is named after \"Rashtrasant\" Tukdoji Maharaj, a renowned spiritual leader, orator and musician from Vidarbha.  The University is a member of the Association of Indian Universities and the Association of Commonwealth Universities.  It has been accredited with the \"A\" grade by the National Assessment and Accreditation Council (NAAC), New Delhi.  It has been consistently ranked among the top universities in India.\n\nQuestion: Heinz Werner Engl, the Austrian mathematician is rector of which public university founded by Duke Rudolph IV in 1365 and one of the oldest universities in the German-speaking world?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university.\"\n    },\n    \"is_public\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the university is a public institution.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"country\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"founding_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"founder\": {\n          \"type\": \"string\",\n          \"description\": \"The individual or entity that founded the university.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the university was founded.\"\n        }\n      },\n      \"required\": [\n        \"founder\",\n        \"founding_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"historical_attributes\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Key historical or significant attributes of the university.\"\n    },\n    \"rector_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the current rector of the university.\"\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"is_public\",\n    \"location\",\n    \"founding_details\",\n    \"historical_attributes\",\n    \"rector_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the university."
      },
      "is_public": {
        "type": "boolean",
        "description": "Indicates if the university is a public institution."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "founding_details": {
        "type": "object",
        "properties": {
          "founder": {
            "type": "string",
            "description": "The individual or entity that founded the university."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the university was founded."
          }
        },
        "required": [
          "founder",
          "founding_year"
        ],
        "additionalProperties": false
      },
      "historical_attributes": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Key historical or significant attributes of the university."
      },
      "rector_name": {
        "type": "string",
        "description": "The name of the current rector of the university."
      }
    },
    "required": [
      "university_name",
      "is_public",
      "location",
      "founding_details",
      "historical_attributes",
      "rector_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
