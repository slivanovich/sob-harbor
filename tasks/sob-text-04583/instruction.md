{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAuvergne horse: The Auvergne horse (French cheval d'Auvergne) is a breed of light draft horse from the Auvergne region of south central France.  It stands 143 to at the withers, and weighs 450 – .  Coat colours are bay or seal brown.  It is used mainly for trekking.  It was recognised as a breed by the Haras Nationaux, the French association of horse breeders in December 2012.  The standard is published by a breeders' association, the \"Association Nationale du Cheval de Race Auvergne.\"\n\nBraque d'Auvergne: The Braque d'Auvergne is a breed of dog originating in the mountain area of Cantal, in the historic Auvergne province in the mid-south of France.  It is a pointer and versatile gundog.  The breed descends from ancient regional types of hunting dogs.\n\nSokoke: The Sokoke (or Sokoke Forest Cat in long form, and formerly the African Shorthair) is natural breed of domestic cat, developed and standardised, beginning in the late 1970s, from the feral khadzonzo landrace of eastern, coastal Kenya.  The Sokoke is recognized by four major cat pedigree registry organizations as a standardised cat breed.  It is named after the Arabuko Sokoke National Forest, the environment from which the foundation stock was obtained, for breed development primarily in Denmark and the United States.  The cat is long-legged, with short, coarse hair, and typically a tabby coat, though specific lineages have produced different appearances.  Although one rumored to be a domestic × wildcat hybrid, genetic study has not borne out this belief.  Another idea, that the variety is unusually ancient, remains unproven either way.  The native population is closely related to an island-dwelling group, the Lamu cat, further north.\n\nDomestic short-haired cat: A domestic short-haired cat is a cat of mixed ancestry – thus not belonging to any particular recognized cat breed – possessing a coat of short fur.  In British English, they are often referred to as moggies.  Domestic short-haired cats should not be confused with the British Shorthair, American Shorthair or other standardized breeds with \"Shorthair\" names, which are breeds recognized by various registries.  Domestic short-haireds are the most common cat in the United States, accounting for around 90–95% of their number.  Other generic terms include house cat and alley cat (the latter may be used more specifically to refer to feral specimens).  The term tabby cat technically refers to a coat pattern, but is also often used as a general term for cats of this sort.\n\nDonskoy cat: The Donskoy is a hairless cat breed of Russian origin.  This breed started in 1987 with the discovery of a hairless cat in the Russian city of Rostov-on-Don by cat breeder Elena Kovaleva.  It is not related to the better known hairless breed of cat the Sphynx, also known as the Canadian hairless, whose characteristic hairlessness is caused by a recessive gene, whereas the Don hairlessness is caused by a dominant gene.\n\nDomestic long-haired cat: A domestic long-haired cat, or fluffy cat, is a cat of mixed ancestry – thus not belonging to any particular recognised cat breed – possessing a coat of semi-long to long fur.  Domestic long-haired cats should not be confused with the British Longhair, American Longhair, or other breeds with \"Longhair\" names, which are standardized breeds defined by various registries.  Domestic long-haireds are the second most popular cat in the United States after the domestic short-haired; one in ten of the ninety million cats in the US is a domestic long-hair.  Other generic terms are long-haired house cat and, in British English, long-haired moggie.\n\nCat registry: A cat registry or cat breed registry, also known as a cat fancier organisation, cattery federation, or cat breeders' association, is an organisation that registers domestic cats (usually purebred) of many breeds, for exhibition and for breeding lineage tracking purposes.  A cat registry stores the pedigrees (genealogies) of cats, cattery names, and other details of cats; studbooks (lists of authorised studs of recognised breeds), breed descriptions, and the formal breed standards (a.k.a. standards of points or SoP); lists of judges qualified to judge at shows run by or affiliated with that registry; and sometimes other information.  A cat registry is not the same as a breed club or breed society (these are specific-breed organisations that may be affiliated with one or more registries with whom they have lodged breed standards in order to be able to exhibit under the auspices of that registry).  Cat registries each have their own rules and usually also organise or license (sanction) cat shows.  The show procedures vary widely, and awards won in one registry are not normally recognised by another.  Some registries only serve breeders, while others are oriented toward pet owners and provide individual as well as cattery memberships, while yet others are federations only deal with breed clubs or even other registries as intermediaries between the organisation and breeders.\n\nKuchi (dog): The Kuchi or Afghan Shepherd dog is an Afghan livestock guardian dog, taking its name from the Kuchi people of Afghanistan.  It is a working dog following the nomads, protecting caravans and flocks of sheep, goats, camels and other livestock from wolves, big cats and thieves.  It is sometimes known as just a local variant of the Central Asian Shepherd Dog and its status as a distinct breed is disputable.\n\nManx cat: The Manx cat ( , in earlier times often spelled Manks), is a breed of domestic cat (\"Felis catus\") originating on the Isle of Man, with a naturally occurring mutation that shortens the tail.  Many Manx have a small stub of a tail, but Manx cats are best known as being entirely tailless; this is the most distinguishing characteristic of the breed, along with elongated hind legs and a rounded head.  Manx cats come in all coat colours and patterns, though all-white specimens are rare, and the coat range of the original stock was more limited.  Long-haired variants are sometimes considered a separate breed, the Cymric.  Manx are prized as skilled hunters, and thus have often been sought by farmers with rodent problems, and been a preferred ship's cat breed.  They are said to be social, tame and active.  An old local term for the cats on their home island is stubbin.  Manx have been exhibited in cat shows since the 1800s, with the first known breed standard published in 1903.\n\nThai cat: The Thai cat or Wichien Maat (Thai: วิเชียรมาศ ,  ] , rtgs: wichianmat , meaning 'moon diamond') is a newly renamed but old cat breed, related to but distinct from the Western, modern Siamese cat.  This natural breed is descended from the landrace of \"wichianmat \" cats of Thailand, and as a standardised breed has also been variously called the Old-style, Old-type, Traditional, or Classic Siamese; the Whichian Mat (anglicised from the Thai name); and the Applehead, a nickname that originated as a pejorative used by breeders of the modern-style Siamese.  According to The International Cat Association: \"The Thai is the breed dedicated to preserving the native pointed cat of Thailand in as close to its original form as possible.\"\n\nQuestion: Are The Braque d'Auvergne and The Kuchi cat breed names?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"is_cat_breed_names\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if all listed names are cat breed names, false otherwise.\"\n    },\n    \"names_checked\": {\n      \"type\": \"array\",\n      \"description\": \"List of names that were checked.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the breed or animal.\"\n          },\n          \"animal_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of animal associated with the name (e.g., 'dog', 'cat', 'horse').\"\n          },\n          \"is_cat_breed\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if this specific name is a cat breed name.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"animal_type\",\n          \"is_cat_breed\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"summary_conclusion\": {\n      \"type\": \"string\",\n      \"description\": \"A brief summary of why the overall answer is true or false.\"\n    }\n  },\n  \"required\": [\n    \"is_cat_breed_names\",\n    \"names_checked\",\n    \"summary_conclusion\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "is_cat_breed_names": {
        "type": "boolean",
        "description": "True if all listed names are cat breed names, false otherwise."
      },
      "names_checked": {
        "type": "array",
        "description": "List of names that were checked.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the breed or animal."
            },
            "animal_type": {
              "type": "string",
              "description": "The type of animal associated with the name (e.g., 'dog', 'cat', 'horse')."
            },
            "is_cat_breed": {
              "type": "boolean",
              "description": "True if this specific name is a cat breed name."
            }
          },
          "required": [
            "name",
            "animal_type",
            "is_cat_breed"
          ],
          "additionalProperties": false
        }
      },
      "summary_conclusion": {
        "type": "string",
        "description": "A brief summary of why the overall answer is true or false."
      }
    },
    "required": [
      "is_cat_breed_names",
      "names_checked",
      "summary_conclusion"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
