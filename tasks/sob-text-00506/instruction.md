{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMoricsala Nature Reserve: Moricsala Nature Reserve (Latvian: \"Moricsalas dabas rezervāts\" ) is a nature reserve in western Latvia (Courland).  It is situated on two islands in Lake Usma and consists of boreal, mixed broad-leaf and oak old-growth forest as well as swamps. Founded in 1912, it is the oldest nature reserve in Latvia.  Being a so-called strict nature reserve, entry into the reserve is prohibited except for scientific purposes.  The nature reserve serves as a habitat for several rare species of moss, lichen and insects; for example, 222 species of butterflies can be found here.  For some of these butterflies, the nature reserve is the only known habitat in the Baltic states.\n\nBaikal Nature Reserve: The Baikal Nature Reserve ( ; Russian: Байка́льский запове́дник , \"Baikalski Zapovednik\") is a nature reserve on the southeast shore of Lake Baikal, in southern Buryatia, Russia.  Also called Baikal Zapovednik, it was established in 1969 for preserving the nature along the lake and the neighboring central part of the Chamar-Daban Range.  The area of this nature reserve is 165,700 ha .  It hosts dark pine taiga (silver fir, cedar, spruce), thin forests, Siberian Dwarf Pine and rhododendron underbrush, subalpine meadows, and alpine tundras.  The Baikal Nature Reserve is home to 812 kinds of plants, 49 types of mammals, 272 birds, 3 reptiles, 3 amphibians, and 7 types of fish.  The reserve is also home to East Siberian brown bear, Baikal lynx, wolverine, otter, osprey, and golden eagle.  The Baikal Nature Reserve is part of the World Network of Biosphere Reserves (also see \"List of biosphere reserves in the Russian Federation\").  The reserve is also a part of the Lake Baikal World Heritage Site.  The Kabansky Nature Zakaznik, across , was transferred under the jurisdiction of the Baikal Nature Reserve in 1985.\n\nQuedlinburg: Quedlinburg (] ) is a town situated just north of the Harz mountains, in the district of Harz in the west of Saxony-Anhalt, Germany.  In 1994, the castle, church and old town were added to the UNESCO World Heritage List.\n\nFoping National Nature Reserve: Foping Nature Reserve () in Shaanxi Province, China, is a nature reserve and national park situated in the Qinling Mountains.  The Nature Reserve covers 350 km2 and is under the leadership of the Ministry of Forestry.  Foping Nature Reserve is girdled by other protected areas: It is bordered in the east by the Long-caoping Forest Farm; in the west it is flanked by the Changqing Nature Reserve; Zhouzhi Nature Reserve, the stronghold of the Golden Monkey, and Laoxiancheng Nature Reserve are situated to the north.  The Foping Reserve covers 29,240 ha of rugged mountain terrain and is home to a stable panda population.  Elevations range from 1,080 to 2,094 m with warm summers and cold winters.  950–1,200 mm of rain falls mostly from July to September, with snow at higher elevations.  Forested lands dominate the reserve with a mix of conifers and broadleaf deciduous trees.\n\nCentral Suriname Nature Reserve: The Central Suriname Nature Reserve (Dutch: \"Centraal Suriname Natuurreservaat (CSNR)\" ) is a conservation unit in Suriname.\n\nMogumber Nature Reserve: The Mogumber Nature Reserve is a nature reserve in Western Australia.  It is a refuge for the endangered Western Swamp Tortoise along with the Twin Swamps Nature Reserve and the Ellen Brook Nature Reserve.  Twin Swamps and Ellen Brook are IUCN Protected Area Management Category IV Reserves, while the Mogumber Nature Reserve is a Category Ia nature reserve.\n\nRalleigh Airstrip: Raleigh Vallen Airstrip (IATA: SMRA) is an airstrip serving the Central Suriname Nature Reserve, Suriname.  The runway is on Fungu Tabiki, an island in the Coppename River.\n\nProtected areas of Suriname: There are several Protected Areas of Suriname.  The largest of these is the Central Suriname Nature Reserve, a UNESCO World Heritage Site.  The protected areas are managed by the Suriname Forest Service.  The Forest Service has appointed STINASU (Stichting Natuurbehoud Suriname), a non-profit foundation, to develop and conduct the educational and tourist aspects in the protected areas.\n\nGibraltar Nature Reserve: The Gibraltar Nature Reserve (formerly the Upper Rock Nature Reserve) is a protected nature reserve in the British Overseas Territory of Gibraltar that covers over 40% of the country's land area.  It was established as the Upper Rock Nature Reserve in 1993 under the International Union for Conservation of Nature's category Ia (strict nature reserve) and was last extended in 2013.  It is known for its semi-wild population of Barbary macaques, and is an important resting point for migrating birds.\n\nPù Luông Nature Reserve: Pù Luông Nature Reserve is a nature reserve in northern Vietnam.  This nature reserve is situated in Quan Hóa and Bá Thước districts of Thanh Hóa Province, North Central Coast region of Vietnam.  Pu Luong Nature Reserve is bordered by Mai Châu, Tân Lạc and Lạc Sơn districts of Hòa Bình Province.  The reserve is located along two parallel mountain ridges, that run from north-west to south-east, and are divided by a central valley, which contains several human settlements and a large agricultural land area, therefore, is not included within the nature reserve.  Pù Luông is endowed with great biodiversity, its flora and fauna is closely associated with the Cúc Phương National Park 25 km south-east.\n\nQuestion: Central Suriname Nature Reserve and Quedlinburg, both have which heritage?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"nature_reserve_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the nature reserve.\"\n    },\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town.\"\n    },\n    \"shared_heritage_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of heritage shared by both entities.\"\n    },\n    \"heritage_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"central_suriname_nature_reserve_status\": {\n          \"type\": \"string\",\n          \"description\": \"The specific heritage status of the Central Suriname Nature Reserve.\"\n        },\n        \"quedlinburg_status\": {\n          \"type\": \"string\",\n          \"description\": \"The specific heritage status of Quedlinburg.\"\n        }\n      },\n      \"required\": [\n        \"central_suriname_nature_reserve_status\",\n        \"quedlinburg_status\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"nature_reserve_name\",\n    \"town_name\",\n    \"shared_heritage_type\",\n    \"heritage_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "nature_reserve_name": {
        "type": "string",
        "description": "The name of the nature reserve."
      },
      "town_name": {
        "type": "string",
        "description": "The name of the town."
      },
      "shared_heritage_type": {
        "type": "string",
        "description": "The type of heritage shared by both entities."
      },
      "heritage_details": {
        "type": "object",
        "properties": {
          "central_suriname_nature_reserve_status": {
            "type": "string",
            "description": "The specific heritage status of the Central Suriname Nature Reserve."
          },
          "quedlinburg_status": {
            "type": "string",
            "description": "The specific heritage status of Quedlinburg."
          }
        },
        "required": [
          "central_suriname_nature_reserve_status",
          "quedlinburg_status"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "nature_reserve_name",
      "town_name",
      "shared_heritage_type",
      "heritage_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
