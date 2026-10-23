{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nModitlo Private Game Reserve: Moditlo Private Game Reserve (3,500 hectares, approximately 7,500 acres) forms an integral part of the 17,000 hectare (approximately 36,000 acres) Blue Canyon Conservancy, located near Hoedspruit, Limpopo Province, South Africa.  The reserve borders Kapama Game Reserve to the eastern side, the Drakensberg Mountains forms the backdrop to the west, and falls into the southern/central region of the Greater Kruger Park biosphere.  The size of the Blue Canyon Conservancy has now reached 36,000 acres in total, and is home to typical African game such as lions, elephants, leopards, rhinos, cheetahs, hippos and several hundreds of bird species typical to the lowveld in South Africa.  The reserve is also home to a pack of wild dogs, which is the second rarest carnivore species in Africa with only an estimated 2000 remaining specimen in existence.\n\nJavan warty pig: The Javan warty pig or Javan pig (\"Sus verrucosus\") is a species of even-toed ungulate in the family Suidae.  It was originally endemic to the Indonesian islands Java, Bawean, and Madura, but has recently been found extinct in Madura.  \"Sus verrucosus\" lives in fragmented teak forest regions ranging in altitudes from sea level to 800 m above sea level.\n\nGiraffa jumae: Giraffa jumae is an extinct species of even-toed ungulate in the Giraffidae family.  The species ranged from Malawi to Chad with a possible occurrence of the species or a closely related species found in Turkey.  The type specimen was discovered during trenching excavations on the upper member of the Rawi Formation by Louis Leakey in the 1930s.  The specimen was found with \"Ceratotherium simum\", Suidae such as \"Metridiochoerus andrewsi\", a \"Hippopotamus gorgops\", and a nearly complete pygmy hippopotamus mandible.\n\nAntelope: An antelope is a member of a number of even-toed ungulate species indigenous to various regions in Africa and Eurasia.  Antelopes comprise a wastebasket taxon (miscellaneous group) within the family Bovidae, encompassing those Old World species that are not cattle, sheep, buffalo, bison, or goats; even so, antelope are generally more deer-like than other bovids.  A group of antelope is called a herd.\n\nFalgore Game Reserve: Falgore Game Reserve is protected ecosystem designated mainly for games protection in southern Kano State of northern Nigeria.  This game reserve is located about 150 kilometers away from Kano city.  It lies in Tudun Wada, Doguwa and Sumaila local government areas.  It extends to the boundary line between Kano, Kaduna and Bauchi states respectively.  It covers an area of about 1000 square kilometers and is traversed by the River Kano.  Falgore game reserve lies on northern guinea savanna ecological belt.  This ecosystem is bisected by River Kano.  Falgore game reserve started as Kogin Kano forest reserve which was developed since the British colonial period in 1940s.  The forest reserve was only upgraded into a game reserve in the 1960s and subsequently called Falgore game reserve.\n\nIndian spotted chevrotain: The Indian spotted chevrotain (\"Moschiola indica\") is a species of even-toed ungulate in the family Tragulidae found in India and possibly Nepal.  It has a body length of 23 in (57.5 cm), with a tail length of 1 in (2.5 cm); it weighs around 7 lb (3 kg).  It lives in rainforests and is nocturnal.  This was earlier included under the name of \"Tragulus meminna\" but studies on the systematics of the group have led to that name being restricted to the Sri Lankan spotted chevrotain.\n\nGiraffe: The giraffe (\"Giraffa\") is a genus of African even-toed ungulate mammals, the tallest living terrestrial animals and the largest ruminants.  The genus currently consists of one species, \"Giraffa camelopardalis\", the type species.  Seven other species are extinct, prehistoric species known from fossils.  Taxonomic classifications of one to eight extant giraffe species have been described, based upon research into the mitochondrial and nuclear DNA, as well as morphological measurements of \"Giraffa,\" but the IUCN currently recognizes only one species with nine subspecies.\n\nMavuradona, Zimbabwe: Mavuradona (\"Mvuradona\") is a wilderness area in Northern Zimbabwe.  The name is Shona, roughly translating as 'Land of Falling Water' or simply 'water falls'.  The area, lying north of Centenary on the Zambezi Escarpment, is relatively unknown.  Characterised by rugged mountainous hills and miombo woodland, the wild landscape was a main theatre of conflict during the war.  Declared a game reserve in 1988, its protected status has lured wildlife back.  Antelope include sable, eland, kudu, waterbuck and impala.  Elephant roam the area, baboon, warthog, zebra and leopard are common and lion are occasionally seen.  The 290 species of birds include several types of eagles that inhabit the water-berry, mhobohobo, msasa and other brachystegia trees.\n\nList of even-toed ungulates by population: This is a list of even-toed ungulate species by estimated global population.  This list is not comprehensive, as not all ungulates have had their numbers quantified.\n\nDomestic pig: The domestic pig (Sus scrofa domesticus or only Sus domesticus), often called swine, hog, or pig when there is no need to distinguish it from other pigs, is a large, even-toed ungulate.  It is variously considered a subspecies of the wild boar or a distinct species.  The domestic pig's head-plus-body-length ranges from 0.9 to , and the adult can weigh between 50 to .  Compared to other artiodactyls, its head is relatively long, pointed, and free of warts.  Even-toed ungulates are generally herbivorous, but the domestic pig is an omnivore, like its wild relative.\n\nQuestion: What member of even-toed ungulate species lives in an African game reserve?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"species_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the even-toed ungulate species.\"\n    },\n    \"is_even_toed_ungulate\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the species is classified as an even-toed ungulate.\"\n    },\n    \"habitat_continent\": {\n      \"type\": \"string\",\n      \"description\": \"The continent where the species is indigenous.\"\n    },\n    \"game_reserve_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the African game reserve where the species lives.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the game reserve is located.\"\n        },\n        \"status_declared_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the area was declared a game reserve.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country\",\n        \"status_declared_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"species_name\",\n    \"is_even_toed_ungulate\",\n    \"habitat_continent\",\n    \"game_reserve_info\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "species_name": {
        "type": "string",
        "description": "The name of the even-toed ungulate species."
      },
      "is_even_toed_ungulate": {
        "type": "boolean",
        "description": "Indicates if the species is classified as an even-toed ungulate."
      },
      "habitat_continent": {
        "type": "string",
        "description": "The continent where the species is indigenous."
      },
      "game_reserve_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the African game reserve where the species lives."
          },
          "country": {
            "type": "string",
            "description": "The country where the game reserve is located."
          },
          "status_declared_year": {
            "type": "integer",
            "description": "The year the area was declared a game reserve."
          }
        },
        "required": [
          "name",
          "country",
          "status_declared_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "species_name",
      "is_even_toed_ungulate",
      "habitat_continent",
      "game_reserve_info"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
