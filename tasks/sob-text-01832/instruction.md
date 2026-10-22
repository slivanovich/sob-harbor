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
Calabarzon: CALABARZON (), formally known as Southern Tagalog Mainland and designated as Region IV-A, is an administrative region in the Philippines.  The region comprises five provinces: Cavite, Laguna, Batangas, Rizal, and Quezon, and one Highly Urbanized City, Lucena.  The name of the region is an acronym of its five component provinces.  Its regional center is Calamba City in Laguna.  CALABARZON is the most populous region in the Philippines, having inhabitants in ?  , and is also the country's second most densely populated after NCR.

Shenzhou City: Shenzhou () is city of Hengshui, Hebei province, China.

Nyabarongo River: The Nyabarongo (or Nyawarungu) is a major river in Rwanda, part of the upper headwaters of the Nile.  At 297 km (184 miles), it is the longest river entirely in Rwanda.  The river begins its course at the confluence of the rivers Mbirurume and Mwogo in the South West of the country.  These two rivers themselves begin in Nyungwe Forest, and are considered by some to be the most distant source of the Nile.  From its start, Nyabarongo flows northward for 85 km (53 miles), and forms the border between the Western and Southern Provinces.  At the confluence with the river Mukungwa, the river changes course and flows eastward for 12 km (7.5 miles), then to a more South Eastern course for the last 200 km (124 miles).  For the longest stretch of this course, the river serves as the boundary between the Northern and Southern Provinces, then between the City of Kigali and the Southern Province, and lastly between the City of Kigali and the Eastern Province.  The river then before enters the Eastern Province and ends its course close to the border with Burundi.  The Nyabarongo River empties both in Lake Rweru and Akagera river in a small but complicated Delta.  The Akagera river outflows from Lake Rweru, a mere 1 km from the Nyabarongo delta.  Almost all the branches of the Nyabarongo delta empty in the lake, however, one branch of the delta empties directly in the just formed Akagera river.  The Akagera River eventually flows into Lake Victoria and forms the Nile.

Herat Province: Herat (Pashto/Dari: هرات) is one of the thirty-four provinces of Afghanistan, located in the western part of the country.  Together with Badghis, Farah, and Ghor provinces, it makes up the south-western region of Afghanistan.  Its primary city and administrative capital is Herat City.  The province of Herat is divided into about 17 districts and contains over 1,000 villages.  It has a population of about 1,780,000, making it the second most populated province in Afghanistan behind Kabul Province.  The population is multi-ethnic but largely Persian-speaking.

Badghis Province: Bādghīs (Pashto/Persian: بادغیس‎ ‎ ) is one of the thirty-four provinces of Afghanistan, located in the northwest of the country next to Turkmenistan.  The name is a corruption of the Persian compound, bâd-khiz, meaning "wind source", referring to the steppe winds that blow into the province from the north and northwest.  Badghis is irrigated by the Murghab .  The extension of the area into Turkmenistan still sports the old version, and serves as the "Bâdkhiz Nature Preserve."  Its northern border extends to the edge of the desert of Sarakhs.  Badghis includes the Chul formations through which the Turkmen-Afghan boundary runs.  The province was carved out of portions of Herat Province and Meymaneh Province in 1964 and has a total area of 20,591 km.  It is counted as one of the most underdeveloped of the country's 34 provinces.  Qala i Naw, a small town halfway between Maimana and Herat, serves as the provincial center.

Province: A province is almost always an administrative division, within a country or state.  The term derives from the ancient Roman "provincia", which was the major territorial and administrative unit of the Roman Empire's territorial possessions outside Italy.  The term province has since been adopted by many countries, and in those with no actual provinces, it has come to mean "outside the capital city".  While some provinces were produced artificially by colonial powers, others were formed around local groups with their own ethnic identities.  Many have their own powers independent of federal authority, especially in Canada.  In other countries, like China, provinces are the creation of central government, with very little autonomy.

Longchang: Longchang(） is a county-level city of Sichuan Province, China.  It is under the administration of Neijiang city.  Longchang has a population of nearly 760,000, covering 794.41 square kilometer.

Shenzhou Railway Station: Shenzhou Railway Station is a railway station of Hainan East Ring Intercity Rail, serving the county-level city of Wanning, located in Hainan, People's Republic of China.

Kandal Province: Kandal (Khmer: កណ្ដាល , ) is a province ("khaet") of Cambodia located in the southeast portion of the country.  It borders the provinces of Kampong Speu and Takeo to the west, Kampong Chhnang and Kampong Cham to the north, Prey Veng to the east, and shares an international border with Vietnam to the south.  Its capital and largest city is Ta Khmao, which is 20 km south of Phnom Penh.  Kandal is one of the wealthier provinces in the country.

West Azerbaijan Province: West Azerbaijan Province is one of the 31 provinces of Iran.  It is in the northwest of the country, bordering Turkey, Iraq and Azerbaijan's Nakhchivan Autonomous Republic, as well as the provinces of East Azerbaijan, Zanjan and Kurdistan.  The province is part of Region 3.  It is separated from Armenia by Turkey's short border with the Azerbaijan Republic.  The province of West Azerbaijan covers an area of 39,487 km², or 43,660 km² including Lake Urmia.  In 2012 the province had a population of about 3 million (estimate).  The capital city and largest city of the province is Urmia.

Question: Shenzhou City and Longchang are located in provinces in what country? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country where both cities are located."
    },
    "located_cities": {
      "type": "array",
      "description": "A list of cities mentioned in the question, along with their respective provinces.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city."
          },
          "province_name": {
            "type": "string",
            "description": "The name of the province the city is located in."
          }
        },
        "required": [
          "city_name",
          "province_name"
        ],
        "additionalProperties": false
      }
    },
    "number_of_cities_found": {
      "type": "integer",
      "description": "The total number of cities found in the context that are relevant to the question."
    }
  },
  "required": [
    "country_name",
    "located_cities",
    "number_of_cities_found"
  ],
  "additionalProperties": false
}
