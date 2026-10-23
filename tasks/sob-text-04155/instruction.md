{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDedication and Everlasting Love to Animals Rescue: Dedication and Everlasting Love to Animals Rescue (D.E.L.T.A. Rescue) is an animal welfare organization based in Acton, California, USA.  With two hospitals and 150 acre of sanctuaries, it is the largest no-kill, care-for-life sanctuary in the United States.  With more than 1,500 animals on the property, it is the largest animal rescue of its type in the world.  Actor/producer/animal welfare activist Leo Grillo is its national president and founder.  As of 2007, the organization is funded solely on private donations of more than $5.5 million per year.\n\nNeutering: Neutering, from the Latin \"neuter\" (\"of neither sex\"), is the removal of an animal's reproductive organ, either all of it or a considerably large part.  \"Neutering\" is often used incorrectly to refer only to male animals, but the term actually applies to both sexes.  The male-specific term is castration, while spaying is usually reserved for female animals.  Colloquially, both terms are often referred to as fixing.  In male horses, castrating is referred to as \"gelding\".  Modern veterinary practice tends to use the term de-sexing.\n\nDogs Trust: Dogs Trust, formerly known as the National Canine Defence League, is an animal welfare charity and humane society in the United Kingdom which specialises in the well-being of dogs.  The charity rehabilitates and finds new homes for dogs which have been abandoned or given up by their owners.  People are encouraged to sponsor a dog for at least £1 a week, even if they are not able to rehome the dog.  It also runs microchipping and neutering schemes in the United Kingdom and abroad, in order to reduce the number of unwanted litters of puppies and stray dogs euthanized by other organisations.\n\nAnimal shelter: An animal shelter or pound is a place where stray, lost, abandoned or surrendered animals, mostly dogs and cats, and sometimes sick or wounded wildlife are kept and rehabilitated.  While no-kill shelters exist, it is sometimes policy to euthanize sick animals, and any animal that is not claimed quickly enough by a previous or new owner.  In Europe, of 30 countries included in a survey, all but four (Czech republic, Germany, Greece, and Italy) permitted the killing of healthy stray dogs.  Critics believe the new term \"animal shelter\" is generally a euphemism for the older term \"pound\".  The word \"pound\" had its origins in the animal pounds of agricultural communities, where stray livestock would be penned or impounded until claimed by their owners.  Some shelters even have sick tropical animals.\n\nAnimal welfare in Nazi Germany: There was widespread support for animal welfare in Nazi Germany among the country's leadership.  Adolf Hitler and his top officials took a variety of measures to ensure animals were protected.  Many Nazi leaders, including Hitler and Hermann Göring, were supporters of animal rights and conservation.  Several Nazis were environmentalists, and species protection and animal welfare were significant issues in the Nazi regime.  Heinrich Himmler made an effort to ban the hunting of animals.  Göring was a professed animal lover and conservationist, who, on instructions from Hitler, committed Germans who violated Nazi animal welfare laws to concentration camps.  In his private diaries, Nazi Propaganda Minister Joseph Goebbels described Hitler as a vegetarian whose hatred of the Jewish and Christian religions in large part stemmed from the ethical distinction these faiths drew between the value of humans and the value of other animals; Goebbels also mentions that Hitler planned to ban slaughterhouses in the German Reich following the conclusion of World War II.\n\nInternational Animal Rescue: International Animal Rescue, also known as IAR, is an animal welfare non-profit organization based in the United Kingdom that comes to the aid of wild and domestic animals with hands-on rescue and rehabilitation.  International Animal Rescue returns rehabilitated animals to the wild while also providing permanent sanctuary for those that cannot be released.  International Animal Rescue specializes in comprehensive sterilization and vaccination programs for stray dogs and cats, particularly in developing countries.  They also work to educate the public in the humane treatment of all animals.  International Animal Rescue has offices in the United Kingdom, United States, India, Indonesia, Malta and the Netherlands.\n\nAnimal House: A Dog's Life: Animal House: A Dog's Life is a United States of America documentary television series about shelter, rescue, and stray dogs. Each half-hour episode consists of two to three segments on individual dogs from the New York animal rescue group, North Shore Animal League.  The family-friendly series has featured many different breeds and dogs who arrived at the rescue for different reasons and circumstances.  Segments show footage of dogs being adopted, and also include stories of their rescue, training, and rehabilitation.\n\nPetSmart Charities: PetSmart Charities and PetSmart Charities of Canada are non-profit organizations dedicated to saving the lives of homeless pets.  In the United States, PetSmart Charities is the largest financial supporter of animal welfare and among the 400 largest philanthropic organizations working on any issue.  PetSmart Charities was formed in 1994 by PetSmart founders Jim and Janice Dougherty, who chose never to sell dogs and cats within their stores.  Their primary goal is to save the lives of homeless pets through programs such as their In-Store Adoption Centers in many PetSmart locations, Rescue Waggin' distaser relief program, grant program for animal welfare agencies across North America, and community adoption events.  Another focus of the organization is increasing spay/neuter services to help communities solve the problem of pet overpopulation.\n\nAnimal Rescue League of Western Pennsylvania: The Animal Rescue League of Western Pennsylvania, known commonly as Animal Rescue League Shelter & Wildlife Center (ARL), is an animal welfare organization founded in Pittsburgh, Pennsylvania in 1909.  The ARL is a non-profit organization that offers various services to support both animals and pet owners alike.  It is the only animal shelter in the Pittsburgh area that accepts both domestic animals and wildlife.  The agency's shelter and clinic are located in Pittsburgh's East Liberty neighborhood, while its wildlife rehabilitation center and boarding kennels are a few miles away in Verona, Pennsylvania.  The organization maintains a contract with the city of Pittsburgh and accepts all stray pets that are apprehended by the Animal Control unit.\n\nStreet dogs in Sofia: In Sofia, Bulgaria, there are many stray dogs (Bulgarian: безстопанствени кучета, romanized to \"bezstoˈpanstveni ˈkucheta\" or \"unowned dogs.\"  Also called, colloquially ,бездомни кучета, \"bezˈdomni ˈkucheta, or homeless dogs\" or улични кучета, \"ˈulichni ˈkucheta, or\" \"street dogs\").  It was estimated that that there were in 2013 about 6,635 stray dogs in the city, a large decrease from previous years.  The population of stray dogs in Sofia, the capital city of Bulgaria, was acknowledged in 2012 by the government to be a major local community problem, if not the primary problem.  The government has, in response, launched several programs to combat the problem.\n\nQuestion: International Animal Rescue, also known as IAR, is an animal welfare non-profit organization based in the United Kingdom, it specializes in comprehensive sterilization and vaccination programs, and which is the removal of an animal's reproductive organ, either all of it or a considerably large part, for stray dogs and cats, particularly in developing countries?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"identified_term\": {\n      \"type\": \"string\",\n      \"description\": \"The specific term identified as the answer to the question.\"\n    },\n    \"term_definition\": {\n      \"type\": \"string\",\n      \"description\": \"The definition of the identified term.\"\n    },\n    \"etymology\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"language\": {\n          \"type\": \"string\",\n          \"description\": \"The language of origin for the term.\"\n        },\n        \"root_word\": {\n          \"type\": \"string\",\n          \"description\": \"The root word from which the term is derived.\"\n        },\n        \"root_meaning\": {\n          \"type\": \"string\",\n          \"description\": \"The meaning of the root word.\"\n        }\n      },\n      \"required\": [\n        \"language\",\n        \"root_word\",\n        \"root_meaning\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"gender_applicability\": {\n      \"type\": \"string\",\n      \"description\": \"Describes to which sexes the term applies.\"\n    },\n    \"related_terminology\": {\n      \"type\": \"array\",\n      \"description\": \"A list of related terms, their specific uses, and applicability.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"term\": {\n            \"type\": \"string\",\n            \"description\": \"A related term.\"\n          },\n          \"applies_to\": {\n            \"type\": \"string\",\n            \"description\": \"The gender or animal type to which the related term applies.\"\n          },\n          \"colloquial_use\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the term is used colloquially.\"\n          },\n          \"specific_animal\": {\n            \"type\": \"string\",\n            \"description\": \"Specifies if the term is used for a particular animal.\"\n          },\n          \"modern_veterinary_term\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if it is a modern veterinary term.\"\n          }\n        },\n        \"required\": [\n          \"term\",\n          \"applies_to\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"specializing_organization\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the organization specializing in this practice.\"\n        },\n        \"program_focus\": {\n          \"type\": \"string\",\n          \"description\": \"The specific program focus of the organization related to the term.\"\n        },\n        \"target_animals\": {\n          \"type\": \"string\",\n          \"description\": \"The types of animals targeted by the organization's programs.\"\n        },\n        \"target_regions\": {\n          \"type\": \"string\",\n          \"description\": \"The regions where the organization primarily conducts these programs.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"program_focus\",\n        \"target_animals\",\n        \"target_regions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"identified_term\",\n    \"term_definition\",\n    \"etymology\",\n    \"gender_applicability\",\n    \"related_terminology\",\n    \"specializing_organization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "identified_term": {
        "type": "string",
        "description": "The specific term identified as the answer to the question."
      },
      "term_definition": {
        "type": "string",
        "description": "The definition of the identified term."
      },
      "etymology": {
        "type": "object",
        "properties": {
          "language": {
            "type": "string",
            "description": "The language of origin for the term."
          },
          "root_word": {
            "type": "string",
            "description": "The root word from which the term is derived."
          },
          "root_meaning": {
            "type": "string",
            "description": "The meaning of the root word."
          }
        },
        "required": [
          "language",
          "root_word",
          "root_meaning"
        ],
        "additionalProperties": false
      },
      "gender_applicability": {
        "type": "string",
        "description": "Describes to which sexes the term applies."
      },
      "related_terminology": {
        "type": "array",
        "description": "A list of related terms, their specific uses, and applicability.",
        "items": {
          "type": "object",
          "properties": {
            "term": {
              "type": "string",
              "description": "A related term."
            },
            "applies_to": {
              "type": "string",
              "description": "The gender or animal type to which the related term applies."
            },
            "colloquial_use": {
              "type": "boolean",
              "description": "Indicates if the term is used colloquially."
            },
            "specific_animal": {
              "type": "string",
              "description": "Specifies if the term is used for a particular animal."
            },
            "modern_veterinary_term": {
              "type": "boolean",
              "description": "Indicates if it is a modern veterinary term."
            }
          },
          "required": [
            "term",
            "applies_to"
          ],
          "additionalProperties": false
        }
      },
      "specializing_organization": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the organization specializing in this practice."
          },
          "program_focus": {
            "type": "string",
            "description": "The specific program focus of the organization related to the term."
          },
          "target_animals": {
            "type": "string",
            "description": "The types of animals targeted by the organization's programs."
          },
          "target_regions": {
            "type": "string",
            "description": "The regions where the organization primarily conducts these programs."
          }
        },
        "required": [
          "name",
          "program_focus",
          "target_animals",
          "target_regions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "identified_term",
      "term_definition",
      "etymology",
      "gender_applicability",
      "related_terminology",
      "specializing_organization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
