{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouth Kalgoorlie Gold Mine: The South Kalgoorlie Gold Mine is a gold mine located south-west of Kalgoorlie, Western Australia.  The mine is sometimes also referred to as \"South Kal Mines - New Celebration\", being a merger of the former \"New Celebration Gold Mine\" and the \"Jubilee Gold Mine\", which were combined in 2002.\n\nHill 50 Gold Mine: The Hill 50 Gold Mine is a gold mine located 4 km north-west of Mount Magnet, Western Australia.  The mine was, until July 2010, owned by Harmony Gold and had been placed in care and maintenance since 2007.  In July 2010, Harmony sold the mine to Ramelius Resources, owner of the Wattle Dam Gold Mine, for A$40 million.\n\nSalmita Mine: The Salmita Mine was a gold producer in the Northwest Territories, Canada during 1983 to 1987.  The deposit was first discovered in 1945 and underground exploration was carried out in 1951-1952.  It was reactivated for exploration by Giant Yellowknife Mines Limited in 1975 and entered production in 1983.  They used the old camp and milling plant of the abandoned Tundra Mine, located a few kilometres to the south.  The mine produced 179,906 troy ounces (5596 kg) of gold from the milling of 238,177 tons of ore.\n\nCrisson Mine: Crisson Mine was a gold mine in Lumpkin County, Georgia, USA, located just east of Dahlonega.  Like many mines in the area, the property probably started as a placer mine during the Georgia Gold Rush.  Once the placer deposits had been exhausted, an open pit gold mine was established in 1847 and commercial operations continued until the early 1980s.  A small stamp mill was also established here.  Much of the gold used for the gold leaf dome of the Georgia State Capitol was mined at this mine, which was among the most productive mine in the Georgia Gold Belt.  The mine is located just north of the site of the Consolidated Mine, which is itself north of and the Calhoun Mine.\n\nMeadowbank Gold Mine: The Meadowbank Gold Mine is an open pit gold mine operated by Agnico-Eagle Mines in the Kivalliq district of Nunavut, Canada.\n\nSamira Hill Gold Mine: The Samira Hill Gold Mine (fr.  \"Mine d'Or du Mont Samira\") is a Gold mine in Téra Department of the Tillabéri Region in Niger.  Opened in late 2004, it is the first industrial scale gold mine in the nation, and while operated by a Canadian/Moroccan consortia, the government of Niger owns both a 20% stake in its operation, and functions under government concession.  The mine, and the possibility that other gold concessions will follow, is projected to be an important component of future export revenue for the West African state.\n\nSukari mine: The Sukari mine or Alsukari mine (Arabic: السكري \"Al-Sukkari\", Egyptian pronunciation: \"El-Sokkari\") is a Gold Mine located in the Nubian Desert/Eastern Desert near the Red Sea in Egypt in the south-east of the country in the Red Sea Governorate, 30 km south of Marsa Alam.  It is exploited jointly by the Egyptian Ministry of Mineral Resources and Centamin.  It is Egypt's first modern gold mine, an industry considered to have scope for expansion in the country.  Egypt was known in the ancient world as being a source of gold, and one of the earliest available maps shows a gold mine at this location.\n\nMining in Mongolia: Mining is important to the national economy of Mongolia.  Coal, copper, and gold are the principal reserves mined in Mongolia.  Several gold mines are located about 110 km north of Ulaanbaatar, such as Boroo Gold Mine and Gatsuurt Gold Mine.  Khotgor Coal Mine is an open-pit coal mining site about 120 km west of Ulaangom.  Ömnögovi Province in the south of Mongolia is home to large scale mining projects such as the Tavan Tolgoi coal mine and the Oyu Tolgoi copper mine.  Oyu Tolgoi mine is reported to have the potential to boost the national economy by a third but is subject to dispute over how the profits should be shared.  The International Monetary Fund (IMF) has estimated that 71 percent of the income from the mine would go to Mongolia.\n\nDvoinoye Gold Mine: The Dvoinoye Gold Mine is an underground gold mine in the Bilibinsky District of the Chukotka Autonomous Okrug of Russia.  The mine is owned by Canadian mining company Kinross Gold and is approximately 100 km from their Kupol Gold Mine.  Originally the site of a surface mine, Kinross acquired the property in 2010, and built the underground mine at a cost of US$360-million.  The mine began production in 2013.\n\nMeadowbank Aerodrome: Meadowbank Aerodrome (TC LID: CMB2) is an aerodrome located 1 NM northeast of Meadowbank Gold Mine, Nunavut, Canada.\n\nQuestion: Which is still operational, the Meadowbank Gold Mine or the Salmita Mine?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"operational_mine_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the gold mine that is currently operational.\"\n    },\n    \"operational_status_details\": {\n      \"type\": \"string\",\n      \"description\": \"Details from the context indicating the operational status of the mine.\"\n    },\n    \"non_operational_mine_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the gold mine that is no longer operational.\"\n    },\n    \"non_operational_status_details\": {\n      \"type\": \"string\",\n      \"description\": \"Details from the context indicating the non-operational status and period of the mine.\"\n    },\n    \"comparison_result\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the mine that is still operational based on the comparison.\"\n    }\n  },\n  \"required\": [\n    \"operational_mine_name\",\n    \"operational_status_details\",\n    \"non_operational_mine_name\",\n    \"non_operational_status_details\",\n    \"comparison_result\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "operational_mine_name": {
        "type": "string",
        "description": "The name of the gold mine that is currently operational."
      },
      "operational_status_details": {
        "type": "string",
        "description": "Details from the context indicating the operational status of the mine."
      },
      "non_operational_mine_name": {
        "type": "string",
        "description": "The name of the gold mine that is no longer operational."
      },
      "non_operational_status_details": {
        "type": "string",
        "description": "Details from the context indicating the non-operational status and period of the mine."
      },
      "comparison_result": {
        "type": "string",
        "description": "The name of the mine that is still operational based on the comparison."
      }
    },
    "required": [
      "operational_mine_name",
      "operational_status_details",
      "non_operational_mine_name",
      "non_operational_status_details",
      "comparison_result"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
