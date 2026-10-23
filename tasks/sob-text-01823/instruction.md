{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLavandula: Lavandula (common name lavender) is a genus of 47 known species of flowering plants in the mint family, Lamiaceae.  It is native to the Old World and is found from Cape Verde and the Canary Islands, Europe across to northern and eastern Africa, the Mediterranean, southwest Asia to southeast India.  Many members of the genus are cultivated extensively in temperate climates as ornamental plants for garden and landscape use, for use as culinary herbs, and also commercially for the extraction of essential oils.  The most widely cultivated species, \"Lavandula angustifolia\", is often referred to as lavender, and there is a color named for the shade of the flowers of this species.\n\nTaro: Taro ( ) commonly refers to the plant \"Colocasia esculenta\", the most widely cultivated species of several plants in the Araceae family which are used as vegetables for their corms, leaves, and petioles.  Thus, this article describes the \"dasheen\" form of taro; another variety of taro is known as eddoe or \"Colocasia antiquorum\".  Other species of taro include giant taro (\"Alocasia macrorrhizos\"), swamp taro (\"Cyrtosperma merkusii\"), and arrowleaf elephant's ear (\"Xanthosoma sagittifolium\").\n\nXanthosoma: Xanthosoma is a genus of flowering plants in the arum family, Araceae.  The genus is native to tropical America but widely cultivated and naturalized in other tropical regions.  Several are grown for their starchy corms, an important food staple of tropical regions, known variously as \"malanga\", \"otoy\", \"otoe\", cocoyam (or new cocoyam), \"tannia\", \"tannier\", \"yautía\", \"macabo\", \"ocumo\", \"macal\", \"taioba\", \"dasheen\", \"quequisque\", \"ʻ ape\" and (in Papua New Guinea) as Singapore taro (\"taro kongkong\").  Many other species (including especially \"X. roseum\") are used as ornamental plants, and in popular horticultural literature are known as ‘ape or elephant ear (from the purported resemblance of the leaf to an elephant's ear), although the latter name is sometimes also applied to members with similar appearance and uses in the closely related genera \"Caladium\", \"Colocasia\" (i.e., taro), and \"Alocasia\".\n\nMoringa oleifera: Moringa oleifera is the most widely cultivated species of the genus \"Moringa\", which is the only genus in the family Moringaceae.  English common names include: moringa, drumstick tree (from the appearance of the long, slender, triangular seed-pods), horseradish tree (from the taste of the roots, which resembles horseradish), ben oil tree, or benzoil tree (from the oil which is derived from the seeds).  It is a fast-growing, drought-resistant tree, native to the southern foothills of the Himalayas in northwestern India, and widely cultivated in tropical and subtropical areas where its young seed pods and leaves are used as vegetables.  It can also be used for water purification and hand washing, and is sometimes used in herbal medicine.\n\nJasarum: Jasarum is a monotypic genus of flowering plants in the Araceae family.  The single species that makes up the genus is Jasarum steyermarkii.  It was discovered in 1960, but wasn't described until 1977 due to classification difficulties with regards to understanding this species.  \"Jasarum\" is now believed to be closely related to \"Caladium\"s and it may have evolved from \"Caladium\"s that once grew in seasonal swamps. \"Jasarum steyermarkii\" is an aquatic species that is native to two river systems in Venezuela and Guyana.  It is found growing in acidic blackwater and is unique in that it is the only submerged aquatic species in Araceae endemic to South America.  \"Jasarum steyermarkii\" has thin ribbon-like leaves that can get as long as 30 cm.  Running down the length of the leaf is a clear midrib that has veins moving at right angles to the edge of the leaf.  The spathes produced open above the surface of the water and are about 15 cm long.\n\nColocasia: Colocasia is a genus of flowering plants in the family Araceae, native to southeastern Asia and the Indian subcontinent.  Some species are widely cultivated and naturalized in other tropical and subtropical regions.  Common names include tarul, karkala ko ganu, elephant-ear, taro, cocoyam, dasheen, chembu, champadhumpa, shavige gadde, and eddoe.  Elephant-ear and cocoyam are also used for some other large-leaved genera in the Araceae, notably \"Xanthosoma\" and \"Caladium\".  The generic name is derived from the ancient Greek word \"kolokasion\", which in the Greek botanist Dioscorides (1st century AD) meant the edible roots of both \"Colocasia esculenta\" and \"Nelumbo nucifera\".  It is thought that the edible roots of \"Colocasia esculenta\" have been cultivated in Asia for more than ten thousand years.  The species \"Colocasia esculenta\" is an invasive species in wetlands along the American Gulf coast, where it threatens to displace native wetland plants.\n\nPhilodendron: Philodendron is a large genus of flowering plants in the Araceae family.  s of September 2015 , the World Checklist of Selected Plant Families accepted 489 species; other sources accept different numbers.  Regardless of number of species, the genus is the second-largest member of the Araceae family.  Taxonomically, the genus \"Philodendron\" is still poorly known, with many undescribed species.  Many are grown as ornamental and indoor plants.  The name derives from the Greek words \"philo-\" or \"love, affection\" and \"dendron\" or \"tree\".  They are commonly called by their generic name.\n\nKahakuloa, Hawaii: Kahakuloa is an area on the north side of West Maui, Hawaii.  It is home to the isolated picturesque community of Kahakuloa Village, two churches, Lorraine's Banana Bread and Banana Cream Pie, Julia's Banana Bread, Kaukini Gallery, Bruce Turnbull Studio and Sculpture Garden, and a few small businesses.  Taro is grown nearby.\n\nPhilodendron melanochrysum: Philodendron melanochrysum is a species of flowering plant in the Araceae family, endemic to Colombia but widely cultivated elsewhere as an ornamental.\n\nList of onion cultivars: There are dozens of cultivars of the onion (\"Allium cepa\"), one of the most widely cultivated species of the genus \"Allium\", But there are also other species cultivated as 'onions'.  Many are named after the first person to breed them, or the locality they came from.  Different localities often use their own common names for cultivars that are genetically almost identical.  Sometimes different cultivars are known by the same common name (for example the name 'Chinese chives' could be referring to \"Allium odorum\" or \"Allium tuberosum\").\n\nQuestion: What Hawaiian island is home to Taro, the most widely cultivated species of plants in the Araceae family, and the Kaukini Gallery?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"island_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Hawaiian island.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"area_name\": {\n          \"type\": \"string\",\n          \"description\": \"The specific area or community on the island.\"\n        },\n        \"island_part\": {\n          \"type\": \"string\",\n          \"description\": \"The part of the island where the area is located.\"\n        }\n      },\n      \"required\": [\n        \"area_name\",\n        \"island_part\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"found_items\": {\n      \"type\": \"array\",\n      \"description\": \"A list of items or entities found at the specified location that are relevant to the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"item_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of item, e.g., 'plant', 'gallery'.\"\n          },\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The common name or specific name of the item.\"\n          },\n          \"scientific_name\": {\n            \"type\": \"string\",\n            \"description\": \"The scientific name of the plant, if applicable.\"\n          },\n          \"plant_family\": {\n            \"type\": \"string\",\n            \"description\": \"The botanical family of the plant, if applicable.\"\n          },\n          \"description\": {\n            \"type\": \"string\",\n            \"description\": \"Additional descriptive information about the item from the context.\"\n          }\n        },\n        \"required\": [\n          \"item_type\",\n          \"name\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"island_name\",\n    \"location_details\",\n    \"found_items\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "island_name": {
        "type": "string",
        "description": "The name of the Hawaiian island."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "area_name": {
            "type": "string",
            "description": "The specific area or community on the island."
          },
          "island_part": {
            "type": "string",
            "description": "The part of the island where the area is located."
          }
        },
        "required": [
          "area_name",
          "island_part"
        ],
        "additionalProperties": false
      },
      "found_items": {
        "type": "array",
        "description": "A list of items or entities found at the specified location that are relevant to the question.",
        "items": {
          "type": "object",
          "properties": {
            "item_type": {
              "type": "string",
              "description": "The type of item, e.g., 'plant', 'gallery'."
            },
            "name": {
              "type": "string",
              "description": "The common name or specific name of the item."
            },
            "scientific_name": {
              "type": "string",
              "description": "The scientific name of the plant, if applicable."
            },
            "plant_family": {
              "type": "string",
              "description": "The botanical family of the plant, if applicable."
            },
            "description": {
              "type": "string",
              "description": "Additional descriptive information about the item from the context."
            }
          },
          "required": [
            "item_type",
            "name"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "island_name",
      "location_details",
      "found_items"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
