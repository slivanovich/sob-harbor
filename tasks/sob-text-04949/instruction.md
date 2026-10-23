{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMuskrat (disambiguation): A muskrat is a type of mammal; the term normally refers to the common and widespread semiaquatic North American cricetid rodent \"Ondatra zibethicus\".  However, the term may also be applied to several other cricetid rodents as well as a shrew, including:\n\nBeaver: The beaver (genus Castor) is a large, primarily nocturnal, semiaquatic rodent.  \"Castor\" includes two extant species, the North American beaver (\"Castor canadensis\") (native to North America) and Eurasian beaver (\"Castor fiber\") (Eurasia).  Beavers are known for building dams, canals, and lodges (homes).  They are the second-largest rodent in the world (after the capybara).  Their colonies create one or more dams to provide still, deep water to protect against predators, and to float food and building material.  The North American beaver population was once more than 60 million, but as of 1988 was 6–12 million.  This population decline is the result of extensive hunting for fur, for glands used as medicine and perfume, and because the beavers' harvesting of trees and flooding of waterways may interfere with other land uses.\n\nHolochilus chacarius: Holochilus chacarius, also known as the Chacoan marsh rat or Chaco marsh rat, is a semiaquatic rodent species in the family Cricetidae.  It is found in Argentina and Paraguay within the Gran Chaco.\n\nArgentine swamp rat: The Argentine swamp rat (\"Scapteromys aquaticus\") is a semiaquatic rodent species from South America.  It is found in northeastern Argentina and Paraguay, where it lives in freshwater marshes and along the southern coast of the Río de la Plata estuary, as well as in woodland.\n\nMuskrat: The muskrat (\"Ondatra zibethicus\"), the only species in genus Ondatra and tribe Ondatrini, is a medium-sized semiaquatic rodent native to North America and is an introduced species in parts of Europe, Asia, and South America.  The muskrat is found in wetlands over a wide range of climates and habitats.  It has important effects on the ecology of wetlands, and is a resource of food and fur for humans.\n\nAquatic rat: The aquatic rat, Ecuador fish-eating rat, or fish-eating rat (\"Anotomys leander\") is a South American species of semiaquatic rodent in the family Cricetidae.  It is the only species in the genus \"Anotomys\".  The specific name \"leander\" was not explained in the original species description but probably refers to the Greek mythical figure Leander from the story of Hero and Leander.\n\nKondiaronk: Kondiaronk (c. 1649–1701) (Gaspar Soiaga, Souojas, Sastaretsi), known as \"Le Rat\" (The Muskrat) was Chief of the Hurons at Michilimackinac.  As a result of an Iroquois attack and dispersal of the Hurons in 1649 the Hurons settled in Michilimackinac.  The Michilimackinac area is near Lake Huron and Lake Michigan (area between Michigan's Upper and Lower Peninsulas).  Noted as a brilliant orator and a formidable strategist, he led the pro-French Petun and Huron refugees of Michilimackinac against their traditional Iroquois enemies.  Kondiaronk realized the only way to establish security was to maintain a war between their enemies, the Iroquois, and the French in an attempt to keep the Iroquois occupied and the Hurons safe from annihilation.  The Rat succeeded in killing the peace however, once he had secured the preservation of his people he favored a vast peace settlement.  This effort concluded in what is known as The Great Peace of Montreal (1701) between France, the Iroquois, and the other Indian tribes of the Upper Great Lakes.  This ended the Beaver Wars and helped open up the interior of North America to deeper French exploration and commerce.  Kondiaronk made them see the advantages such a peace would bring them.  The Jesuit historian, Father Pierre-Francois de Charlevoix wrote that \"it was the general opinion that no Indian had ever possessed greater merit, a finer mind, more valor, prudence or discernment in understanding those with whom he had to deal\".  Louis-Hector de Callier, the Onontio (governor) that replaced Frontenac, was \"exclusively indebted to him for...this assemblage, till then unexampled of so many nations for a general peace\".  Kondiaronk contracted a fever and died in Montreal during the negotiations for the Great Peace on August 2, 1701.  A Christian convert, his body was buried at Montreal's Notre Dame Church after a majestic funeral.  No trace of the grave remains.  The Kondiaronk Belvedere in Montreal's Mount Royal Park is named in his honor.  In 2001 he was named a Person of National Historic Significance by the Canadian government.\n\nHolochilus brasiliensis: Holochilus brasiliensis, also known as the Brazilian marsh rat or web-footed marsh rat, is a species of semiaquatic rodent from South America.  It is found in Argentina, Brazil and Uruguay.\n\nOryzomys couesi: Oryzomys couesi, also known as Coues' rice rat, is a semiaquatic rodent in the family Cricetidae occurring from southernmost Texas through Mexico and Central America into northwestern Colombia.  It is usually found in wet habitats, such as marshes, but also lives in drier forests and shrublands. Weighing about 43 to , \"O. couesi\" is a medium-sized to large rat.  The coarse fur is buff to reddish above and white to buff below.  The hindfeet show some specializations for life in the water, such as reduced ungual tufts of hair around the digits.  It has 56 chromosomes.  There is much geographic variation in size, proportions, color, and skull features.  \"Oryzomys couesi\" is active during the night and builds nests of vegetation that are suspended among reeds about 1 m above the ground.  It is an excellent swimmer and dives well, but can also climb in vegetation.  An omnivore, it eats both plant and animal food, including seeds and insects.  It breeds throughout the year; females give birth to about four young after a pregnancy of 21 to 28 days.  The species may be infected by several different parasites and by two hantaviruses.\n\nWaterhouse's swamp rat: Waterhouse's swamp rat, \"Scapteromys tumidus\", is a semiaquatic rodent species from South America.  It is found in southern Brazil, Uruguay and northern Argentina, where it lives in freshwater and salt marshes, as well as open grassland of the pampas. Its karyotype has 2n = 24, substantially lower than its closest relative \"S. aquaticus\" with 2n = 32.\n\nQuestion: Kondiaronk (c. 1649–1701) was Chief of the Hurons at Michilimackinac, he was known as \"Le Rat\" (The Muskrat), the  muskrat (\"Ondatra zibethicus\"), the only species in genus Ondatra and tribe Ondatrini, is a medium-sized semiaquatic rodent native to which location, and is an introduced species in parts of Europe, Asia, and South America? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The common name of the animal.\"\n    },\n    \"scientific_name\": {\n      \"type\": \"string\",\n      \"description\": \"The scientific name of the animal.\"\n    },\n    \"animal_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general classification of the animal, e.g., rodent, mammal.\"\n    },\n    \"native_location\": {\n      \"type\": \"string\",\n      \"description\": \"The continent or region where the species is native.\"\n    },\n    \"introduced_locations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of continents or regions where the species has been introduced.\"\n    },\n    \"habitat_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the type of habitat it lives in.\"\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"scientific_name\",\n    \"animal_type\",\n    \"native_location\",\n    \"introduced_locations\",\n    \"habitat_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The common name of the animal."
      },
      "scientific_name": {
        "type": "string",
        "description": "The scientific name of the animal."
      },
      "animal_type": {
        "type": "string",
        "description": "The general classification of the animal, e.g., rodent, mammal."
      },
      "native_location": {
        "type": "string",
        "description": "The continent or region where the species is native."
      },
      "introduced_locations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of continents or regions where the species has been introduced."
      },
      "habitat_description": {
        "type": "string",
        "description": "A brief description of the type of habitat it lives in."
      }
    },
    "required": [
      "entity_name",
      "scientific_name",
      "animal_type",
      "native_location",
      "introduced_locations",
      "habitat_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
