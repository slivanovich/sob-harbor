{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKarl Kraepelin: Karl Matthias Friedrich Magnus Kraepelin (14 December 1848 Neustrelitz – 28 June 1915 Hamburg), was a German naturalist who specialised in the study of scorpions, centipedes, spiders and solfugids, and was noted for his monograph \"\"Scorpiones und Pedipalpi\"\" (Berlin) in 1899, which was an exhaustive survey of the taxonomy of the Order Scorpiones.  From 1889–1914 he was Director of the \"Naturhistorisches Museum Hamburg \", which was destroyed during World War II, and worked on myriapods from 1901–1916.\n\nAcari: Acari (or Acarina) are a taxon of arachnids that contains mites and ticks.  The diversity of the Acari is extraordinary and its fossil history goes back to at least the early Devonian period.  As a result, acarologists (the people who study mites and ticks) have proposed a complex set of taxonomic ranks to classify mites.  In most modern treatments, the Acari is considered a subclass of Arachnida and is composed of two or three superorders or orders: Acariformes (or Actinotrichida), Parasitiformes (or Anactinotrichida), and Opilioacariformes; the latter is often considered a subgroup within the Parasitiformes.  The monophyly of the Acari is open to debate, and the relationships of the acarines to other arachnids is not at all clear.  In older treatments, the subgroups of the Acarina were placed at order rank, but as their own subdivisions have become better understood, it is more usual to treat them at superorder rank.\n\nRicinulei: The order Ricinulei is a group of arachnids known as hooded tickspiders, though they are not true spiders.  Like most arachnids, they are predatory, eating small arthropods.  In older works they are sometimes referred to as Podogona.\n\nHesperornithes: Hesperornithes is an extinct and highly specialized group of aquatic avialans closely related to the ancestors of modern birds.  They inhabited both marine and freshwater habitats in the Northern Hemisphere, and include genera such as \"Hesperornis\", \"Parahesperornis\", \"Baptornis\", \"Enaliornis\", and \"Potamornis\", all strong-swimming, predatory divers.  Many of the species most specialized for swimming were completely flightless.  The largest known hesperornithean, \"Canadaga arctica\", may have reached a maximum adult length of over 1.5 m .\n\nBoiga kraepelini: Boiga kraepelini, commonly known as the square-headed cat snake, Kelung cat snake, or Taiwanese tree snake is a species is a species of mildly venomous colubrid snake found in East and Southeast Asia (Taiwan, China, Vietnam, and Laos).  Its specific name \"kraepelini\" honours Karl Kraepelin, a German naturalist.  The common name Kelung cat snake refers to its type locality, Keelung in northern Taiwan.\n\nScorpion: Scorpions are predatory arachnids of the order Scorpiones.  They have eight legs and are easily recognized by the pair of grasping pedipalps and the narrow, segmented tail, often carried in a characteristic forward curve over the back, ending with a venomous stinger.  Scorpions range in size from 9 mm / 0.3 in.  (\"Typhlochactas mitchelli\") to 23 cm / 9 in.  (\"Heterometrus swammerdami\").\n\nTaxidermy: Taxidermy is the preserving of an animal's body via stuffing or mounting for the purpose of display or study.  Animals are often, but not always, portrayed in a life-like state.  The word taxidermy refers to the process of preserving the animal, but the word is also used to describe the end product, which are often called \"mounts\".  The word taxidermy is derived from the Greek words \"taxis\" and \"derma\".  Taxis means to \"to move\", and \"derma\" means \"skin\" (the dermis).  The word taxidermy translates to \"arrangement of skin\".  Taxidermy is practiced primarily on vertebrates (mammals, birds, fish, reptiles, and less commonly on amphibians) but can also be done to larger insects and arachnids under some circumstances.  Taxidermy takes on a number of forms and purposes, including natural history museum displays, hunting trophies, study skins, and is sometimes used as a means to memorialize pets.  A person who practices taxidermy is called a taxidermist.  They may practice professionally for museums or as businesses catering to hunters and fishermen, or as amateurs, such as hobbyists, hunters, and fishermen.  A taxidermist is aided by familiarity with anatomy, sculpture, painting, and tanning.\n\nCaraboctonidae: The Caraboctonidae (hairy scorpions) make up the superfamily Iuroidea.  The family was established by Karl Kraepelin in 1905.\n\nArachnology: Arachnology is the scientific study of spiders and related animals such as scorpions, pseudoscorpions, and harvestmen, collectively called arachnids. Those who study spiders and other arachnids are arachnologists.\n\nCalcitronidae: The family Calcitronidae is an extinct group of arachnids. Its two monotypic genera are only known from Pliocene deposits of calcite in Arizona.  The family has been placed in the order Schizomida, but a review of the order concluded that \"the fossil taxa ... are so poorly known that final placement must await further study and possibly new material\", and they are not listed in the order in a 2016 catalog of fossil arachnids.\n\nQuestion: Karl Kraepelin specialized in the study of what predatory arachnids?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"naturalist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the naturalist.\"\n    },\n    \"specialized_predatory_arachnids\": {\n      \"type\": \"array\",\n      \"description\": \"List of predatory arachnid groups the naturalist specialized in, explicitly identified as such in the context.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"group_name\": {\n            \"type\": \"string\",\n            \"description\": \"The common name of the predatory arachnid group.\"\n          },\n          \"order_name\": {\n            \"type\": \"string\",\n            \"description\": \"The scientific order name of the group, if specified.\"\n          },\n          \"notable_contribution\": {\n            \"type\": \"string\",\n            \"description\": \"A specific notable contribution or work related to this group.\"\n          }\n        },\n        \"required\": [\n          \"group_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"other_specialized_groups\": {\n      \"type\": \"array\",\n      \"description\": \"List of other animal groups the naturalist specialized in, which are not explicitly identified as predatory arachnids in the context.\",\n      \"items\": {\n        \"type\": \"string\",\n        \"description\": \"The common name of the animal group.\"\n      }\n    }\n  },\n  \"required\": [\n    \"naturalist_name\",\n    \"specialized_predatory_arachnids\",\n    \"other_specialized_groups\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "naturalist_name": {
        "type": "string",
        "description": "The name of the naturalist."
      },
      "specialized_predatory_arachnids": {
        "type": "array",
        "description": "List of predatory arachnid groups the naturalist specialized in, explicitly identified as such in the context.",
        "items": {
          "type": "object",
          "properties": {
            "group_name": {
              "type": "string",
              "description": "The common name of the predatory arachnid group."
            },
            "order_name": {
              "type": "string",
              "description": "The scientific order name of the group, if specified."
            },
            "notable_contribution": {
              "type": "string",
              "description": "A specific notable contribution or work related to this group."
            }
          },
          "required": [
            "group_name"
          ],
          "additionalProperties": false
        }
      },
      "other_specialized_groups": {
        "type": "array",
        "description": "List of other animal groups the naturalist specialized in, which are not explicitly identified as predatory arachnids in the context.",
        "items": {
          "type": "string",
          "description": "The common name of the animal group."
        }
      }
    },
    "required": [
      "naturalist_name",
      "specialized_predatory_arachnids",
      "other_specialized_groups"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
