Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
List of companies of Burundi: Burundi, officially the Republic of Burundi, is a landlocked country in the African Great Lakes region of Southeast Africa, bordered by Rwanda to the north, Tanzania to the east and south and the Democratic Republic of the Congo to the west.  Burundi's largest industry is agriculture, which accounted for just over 30% of the GDP.  Subsistence agriculture accounts for 90% of agriculture.  The nation's largest source of revenue is coffee, which makes up 93% of Burundi's exports.  Burundi is one of the world's poorest countries, owing in part to its landlocked geography, poor legal system, lack of economic freedom, lack of access to education, and the proliferation of HIV/AIDS.  Approximately 80% of Burundi's population lives in poverty.

Democratic Republic of the Congo: The Democratic Republic of the Congo ( ; ] ; French: "République démocratique du Congo" ), also known as Zaire, DR Congo, East Congo, DRC, DROC, Congo-Kinshasa or simply the Congo, is a country located in Central Africa.  The DRC borders the Central African Republic and South Sudan to the north; Uganda, Rwanda, Burundi and Tanzania to the east; Zambia and Angola to the south; the Republic of the Congo to the west and the Atlantic Ocean to the southwest.  It is the second-largest country in Africa (largest in Sub-Saharan Africa) by area and eleventh largest in the world.  With a population of over 80 million, the Democratic Republic of the Congo is the most populated officially Francophone country, the fourth most-populated nation in Africa and the seventeenth most populated country in the world.

Pride of Africa: The Pride of Africa is a luxury train which is run by Rovos Rail.  It is billed as the "World's Most Luxurious Train".  It travels through South Africa, Zimbabwe, Zambia and Tanzania.

List of companies of Angola: Angola is a country in Southern Africa.  It is the seventh-largest country in Africa and is bordered by Namibia to the south, the Democratic Republic of the Congo to the north and east, Zambia to the east, and the Atlantic Ocean to west.  The exclave province of Cabinda has borders with the Republic of the Congo and the Democratic Republic of the Congo.  The capital and largest city of Angola is Luanda.

List of companies of Zambia: The Republic of Zambia is a landlocked country in Southern Africa, neighbouring the Democratic Republic of the Congo to the north, Tanzania to the north-east, Malawi to the east, Mozambique, Zimbabwe, Botswana and Namibia to the south, and Angola to the west.  The capital city is Lusaka, in the south-central part of Zambia.  The population is concentrated mainly around Lusaka in the south and the Copperbelt Province to the northwest, the core economic hubs of the country.

Index of Zambia-related articles: Zambia, officially known as the Republic of Zambia , is a landlocked country in Southern Africa.  The neighbouring countries are the Democratic Republic of the Congo to the north, Tanzania to the north-east, Malawi to the east, Mozambique, Zimbabwe, Botswana, and Namibia to the south, and Angola to the west.  The capital city is Lusaka, located in the southeast of the country.  The population is concentrated mainly around the capital and the Copperbelt to the northwest.

Angola: Angola , officially the Republic of Angola (Portuguese: "República de Angola" ] ; Kikongo, Kimbundu and Umbundu: "Repubilika ya Ngola"), is a country in Southern Africa.  It is the seventh-largest country in Africa and is bordered by Namibia to the south, the Democratic Republic of the Congo to the north, Zambia to the east, and the Atlantic Ocean to west.  The exclave province of Cabinda has borders with the Republic of the Congo and the Democratic Republic of the Congo.  The capital and largest city of Angola is Luanda.

List of companies of South Sudan: South Sudan, officially the Republic of South Sudan, and previously known as Southern Sudan, is a landlocked country in Middle Africa, in the area of northeast Central Africa that is part of the United Nations subregion of Eastern Africa.  South Sudan is bordered by the Republic of Sudan to the north, Kenya to the southeast, Uganda to the south, the Democratic Republic of the Congo to the southwest, the Central African Republic to the west, and Ethiopia to the east.

Zambia: Zambia ( ), officially the Republic of Zambia, is a landlocked country in Southern Africa, neighbouring the Democratic Republic of the Congo to the north, Tanzania to the north-east, Malawi to the east, Mozambique, Zimbabwe, Botswana and Namibia to the south, and Angola to the west.  The capital city is Lusaka, in the south-central part of Zambia.  The population is concentrated mainly around Lusaka in the south and the Copperbelt Province to the northwest, the core economic hubs of the country.

Lists of Zambia-related topics: Zambia, officially known as the Republic of Zambia , is a landlocked country in Southern Africa.  The neighbouring countries are the Democratic Republic of the Congo to the north, Tanzania to the north-east, Malawi to the east, Mozambique, Zimbabwe, Botswana, and Namibia to the south, and Angola to the west.  The capital city is Lusaka, located in the southeast of the country.  The population is concentrated mainly around the capital and the Copperbelt to the northwest.

Question: A luxury train ran by what company travels a landlocked country in Southern Africa, neighbouring the Democratic Republic of the Congo to the north? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that runs the luxury train."
    },
    "train_name": {
      "type": "string",
      "description": "The name of the luxury train."
    },
    "travel_route_details": {
      "type": "object",
      "properties": {
        "country_name": {
          "type": "string",
          "description": "The name of the country that matches the specified criteria."
        },
        "is_landlocked": {
          "type": "boolean",
          "description": "Indicates if the country is landlocked."
        },
        "region": {
          "type": "string",
          "description": "The geographical region of the country."
        },
        "bordering_country_to_north": {
          "type": "string",
          "description": "The country that borders the specified country to its north."
        }
      },
      "required": [
        "country_name",
        "is_landlocked",
        "region",
        "bordering_country_to_north"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "train_name",
    "travel_route_details"
  ],
  "additionalProperties": false
}
