{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFlora of the Sonoran Desert: Flora of the Sonoran Desert includes six subdivisions based on vegetation types. Two are north of the boundary between the United States and Mexico, and four are south of the boundary.  The flora of the Colorado Desert are influenced by the environment of the very dry and hot lower areas of the Colorado River valley, which may be barren, treeless, and generally have no large cacti.  Flora of the Arizona Upland are comparatively lush, with trees and large columnar cacti that can withstand winter frosts.  South of the border subdivisions are characterized by plants that cannot withstand frost.\n\nFlora of Scotland: The flora of Scotland is an assemblage of native plant species including over 1,600 vascular plants, more than 1,500 lichens and nearly 1,000 bryophytes.  The total number of vascular species is low by world standard but lichens and bryophytes are abundant and the latter form a population of global importance.  Various populations of rare fern exist, although the impact of 19th-century collectors threatened the existence of several species.  The flora is generally typical of the north west European part of the Palearctic ecozone and prominent features of the Scottish flora include boreal Caledonian forest (much reduced from its natural extent), heather moorland and coastal machair.  In addition to the native varieties of vascular plants there are numerous non-native introductions, now believed to make up some 43% of the species in the country.\n\nLatania: Latania commonly known as Latan palm or Latania palm is a genus of flowering plant in the palm tree family, native to islands in the western Indian Ocean.\n\nFlora of the South Sandwich Islands: This is a list of the flora of the South Sandwich Islands, a group of islands in the subantarctic Atlantic Ocean, part of the British overseas territory of South Georgia and the South Sandwich Islands.  The list contains flora in the strict sense; that is, plants only.  It comprises a single species of vascular plant, 38 mosses, and 11 liverworts. Unusually, not a single species is known to have naturalised on the islands; all are presumed native.\n\nThreatened Species Protection Act 1995: The Threatened Species Protection Act 1995, is an act of the Parliament of Tasmania that provides the statute relating to conservation of flora and fauna.  Its long title is An Act to provide for the protection and management of threatened native flora and fauna and to enable and promote the conservation of native flora and fauna.  It received the royal assent on 14 November 1995.\n\nStingray Swamp Flora Reserve: Stingray Swamp Flora Reserve (SWFR) is located immediately north of Penrose township in the south-western region of Wingecarribee Shire.  The reserve is primarily surrounded by the Penrose State Forest, which is a commercially active plantation forest administered by the Forest Corporation NSW.  Pine species dominate the state forest with a mix of native vegetation types in isolated pockets and adjacent areas.  Stingray Swamp Flora Reserve belongs to a larger wetland complex known as the Paddy’s River Wetland Complex (PRWC).  These wetlands also form part of the Paddy’s River sub-catchment, which belong to the larger Hawkesbury-Nepean catchment.  Historic use of this area has mainly been that of pine plantation, agriculture and mining activities.  The forest is publicly accessible and therefore is a site of mixed recreational activities.\n\nRhynchophorus cruentatus: The palmetto weevil (\"Rhynchophorus cruentatus\") is an insect native to Florida, but has been found as far as southern Texas to the west and South Carolina to the north.  It is the largest weevil in North America and the only kind of palm weevil in the continental United States.  It infests palms and is considered a pest.  Its main target is the Canary Island date palm, but date palms (a different species than the Canary Island date palm), sabal palms (the palmetto weevil's traditional target), saw palmetto (the palmetto weevil's traditional alternative target), \"Washingtonia\", \"Pritchardia\", royal palms, \"Latania\", coconut palms, \"Caryota\", and \"Bismarckia\" are also susceptible.  Distressed palm trees are usually attacked, which makes transplanted trees a frequent target.  The Palmetto Weevils mate at the base of the palm branches where the females deposit their eggs.  The grubs then eat into the palm tree, killing it.  After the larvae have turned into adult weevils, the damage can be seen, but by then, it is considered to be too late for the tree.  The life cycle from egg to adult for a palmetto weevil is about 84 days.  For prevention, it is recommended an appropriate insecticidal crown drench is done twice a year for high value palms.\n\nArundina: The bamboo orchid, Arundina graminifolia, is a species of orchid and the sole accepted species of the genus Arundina.  This tropical Asiatic genus extends from India, Sri Lanka, Nepal, Thailand, Vietnam, the Ryukyu Islands, Malaysia, Singapore, China to Indonesia, the Philippines and New Guinea.  It has become naturalized in Réunion, Fiji, French Polynesia, Micronesia, the West Indies, Costa Rica, Panama and Hawaii.\n\nFlora: Flora is the plant life occurring in a particular region or time, generally the naturally occurring or indigenous—native plant life.  The corresponding term for animal life is fauna.  \"Flora\", \"fauna\" and other forms of life such as fungi are collectively referred to as biota.  Sometimes bacteria and fungi are also referred to as flora, as in the terms gut flora or skin flora.\n\nFlora of Madhya Pradesh: The Flora of Madhya Pradesh province in India, is very rich and diverse.  Central, eastern and southern parts of the state are forested, whereas northern and western parts are deficient in forest.  Variability in climatic and edaphic conditions brings about significant difference in the forest types and flora of the state.  There are four important forest types: Tropical Moist, Tropical Dry, Tropical Thorn, and Subtropical broadleaved Hill forests.  Based on composition, there are three important forest formations namely Teak forest, Sal forest and Miscellaneous Forests.  Bamboo bearing areas are widely distributed in the state.\n\nQuestion: Latania and Arundina are types of flora that are native to which ocean?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"flora_names\": {\n      \"type\": \"array\",\n      \"description\": \"The names of the flora mentioned in the question.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"native_ocean\": {\n      \"type\": \"string\",\n      \"description\": \"The ocean to which both flora are native.\"\n    },\n    \"flora_details\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each flora's native location as described in the context.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the flora.\"\n          },\n          \"native_location_description\": {\n            \"type\": \"string\",\n            \"description\": \"Description of the flora's native location from the context.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"native_location_description\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"flora_names\",\n    \"native_ocean\",\n    \"flora_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "flora_names": {
        "type": "array",
        "description": "The names of the flora mentioned in the question.",
        "items": {
          "type": "string"
        }
      },
      "native_ocean": {
        "type": "string",
        "description": "The ocean to which both flora are native."
      },
      "flora_details": {
        "type": "array",
        "description": "Details about each flora's native location as described in the context.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the flora."
            },
            "native_location_description": {
              "type": "string",
              "description": "Description of the flora's native location from the context."
            }
          },
          "required": [
            "name",
            "native_location_description"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "flora_names",
      "native_ocean",
      "flora_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
