{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRat: Rats are various medium-sized, long-tailed rodents of the superfamily Muroidea.\n\nSpalacidae: The Spalacidae, or spalacids, are a family of rodents in the large and complex superfamily Muroidea.  They are native to eastern Asia, the Horn of Africa, the Middle East, and southeastern Europe.  It includes the blind mole-rats, bamboo rats, mole-rats, and zokors.  This family represents the oldest split (excluding perhaps the Platacanthomyinae) in the muroid superfamily, and comprises animals adapted to a subterranean way of life.  These rodents were thought to have evolved adaptations to living underground independently until recent genetic studies demonstrated they form a monophyletic group.  Members of the Spalacidae are often placed in the family Muridae along with all other members of the Muroidea.\n\nPearls Before Swine (comics): Pearls Before Swine is an American comic strip written and illustrated by Stephan Pastis.  It chronicles the daily lives of five anthropomorphic animals: a Pig, a Rat, a Zebra, a Goat, and a fraternity of crocodiles, as well as a number of supporting characters.  Each character represents an aspect of Pastis' own personality and world view.  The daily and Sunday comic strip is distributed by Universal Uclick (by United Media's United Feature Syndicate before 2011).\n\nPouched rat: Pouched rats are a group of African rodents in the subfamily Cricetomyinae.  They are members of the family Nesomyidae, which contains other African muroids such as climbing mice, Malagasy mice, and the white-tailed rat.  All nesomyids are in the superfamily Muroidea, a large and complex clade containing 1/4 of all mammal species.  Sometimes the pouched rats are placed in the family Muridae along with all other members of the superfamily Muroidea.\n\nSpalax: The genus Spalax contains the blind, fossorial, or subterranean mole rats, which are one of several types of rodents that are called \"mole rats\".  The hystricognath mole-rats of the family Bathyergidae are completely unrelated, but some other forms are also in the family Spalacidae.  Zokors (subfamily Myospalacinae) and root rats and bamboo rats (subfamily Rhizomyinae) are spalacids sometimes referred to as mole rats.  Blind mole rats are in the family Spalacidae, but are unique enough to be given a separate subfamily, Spalacinae.  Alternate opinions on taxonomy consider the blind mole-rats to be the only members of the family Spalacidae and rank other spalacid subfamilies as full families.  Other authors group all members of the superfamily Muroidea into a single family, Muridae.  The Spalacinae contains two genera and eight species.  Some authorities treat all species as belonging to a single genus, \"Spalax\".\n\nArvicolinae: The Arvicolinae are a subfamily of rodents that includes the voles, lemmings, and muskrats.  They are most closely related to the other subfamilies in the Cricetidae (comprising the hamsters and New World rats and mice).  Some authorities place the subfamily Arvicolinae in the family Muridae along with all other members of the superfamily Muroidea.  Some refer to the subfamily as the Microtinae or rank the taxon as a full family, the Arvicolidae.\n\nPlatacanthomyidae: The rodent family Platacanthomyidae, or Oriental dormice, includes the spiny dormice and the Chinese pygmy dormice.  In spite of their appearance, these animals are not true dormice, but are part of the large and complex superfamily Muroidea.  The platacanthomyids can be distinguished from the true dormice, because they have no premolars, giving them three cheek teeth, like their relatives, the Muroidea.\n\nLemming: A lemming is a small rodent usually found in or near the Arctic in tundra biomes. Lemmings are subnivean animals.  They make up the subfamily Arvicolinae (also known as Microtinae) together with voles and muskrats, which forms part of the superfamily Muroidea, which also includes rats, mice, hamsters, and gerbils.\n\nMarsh rat: Marsh rat can refer to several not closely related types of semiaquatic rodents of superfamily Muroidea:\n\nDendromurinae: Dendromurinae is a subfamily of rodents in the family Nesomyidae and superfamily Muroidea.  The dendromurines are currently restricted to Africa, as is the case for all extant members of the family Nesomyidae.  The authorship of the subfamily has been attributed to both Alston, 1876, and (incorrectly) to G. M. Allen, 1939.\n\nQuestion: What character from Pearls Before Swine came from the superfamily Muroidea?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character from the comic strip.\"\n    },\n    \"source_comic_strip\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the comic strip the character appears in.\"\n    },\n    \"superfamily\": {\n      \"type\": \"string\",\n      \"description\": \"The biological superfamily the character belongs to.\"\n    },\n    \"character_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general biological classification of the character.\"\n    },\n    \"superfamily_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the superfamily.\"\n    }\n  },\n  \"required\": [\n    \"character_name\",\n    \"source_comic_strip\",\n    \"superfamily\",\n    \"character_type\",\n    \"superfamily_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "character_name": {
        "type": "string",
        "description": "The name of the character from the comic strip."
      },
      "source_comic_strip": {
        "type": "string",
        "description": "The name of the comic strip the character appears in."
      },
      "superfamily": {
        "type": "string",
        "description": "The biological superfamily the character belongs to."
      },
      "character_type": {
        "type": "string",
        "description": "The general biological classification of the character."
      },
      "superfamily_description": {
        "type": "string",
        "description": "A brief description of the superfamily."
      }
    },
    "required": [
      "character_name",
      "source_comic_strip",
      "superfamily",
      "character_type",
      "superfamily_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
