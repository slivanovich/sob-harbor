{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBurchardia: Burchardia is a genus of herbs that are endemic to Australia.  The genus is named for Johann Heinrich Burkhardt, a German botanist.\n\nIncarvillea sinensis: Incarvillea sinensis is a species of the genus \"Incarvillea\".  The plant has been used in traditional Chinese medicine as an analgesic and as a treatment for rheumatism.  Incarvillateine isolated from \"Incarvillea sinensis\" has demonstrated significant analgesic activity when compared to the opiate alkaloid morphine.\n\nKunai: A kunai (苦無 , \"kunai\" ) is a Japanese tool originally meant for farming in the Tensho Era of Japan (1573 - 1592).  The two widely recognized variations of the kunai are short kunai (小苦無 , \"shō-kunai\" ) and the big kunai (大苦無 , \"dai-kunai\" ) .  Although a basic tool, in the hands of a martial arts expert, the kunai could be used as a multi-functional weapon, popular before the widely spread of firearms.  The kunai is commonly associated with the ninja, who used it to gouge holes in walls.  By attaching a rope to the ring, the user could easily climb walls or trees, which required great accuracy when thrown.  The kunai blade was unsharpened, soft iron, and was used for digging, prying, and smashing wood, plaster, and the like -- which would like have destroyed a tool which was sharpened or heat-treated.  Many popular manga and \"ninjutsu\" characters use kunai as both their primary and secondary weapons.\n\nAngonisaurus: Angonisaurus is an extinct genus of kannemeyeriiform dicynodont from the Late Triassic of Africa somewhere between 251 million years ago and 199 million years ago.  Only one species, \"Angonisaurus cruickshanki\" has been assigned to this genus.  This genus is thought to have been widely spread but rare in southern Gondwana.  Though few in number, the fossil record of Angonisaurus cruickshanki contains multiple specimens giving it a measurable stratigraphic range.  Sexually dimorphic features are found in Angonisaurs which include presence or absence of tusks and difference is size and robustness of the temporal arch and the rostral.\n\nIncarvillea: Incarvillea is a genus of about 16 species of flowering plants in the family Bignoniaceae, native to central and eastern Asia, with most of the species growing at high altitudes in the Himalaya and Tibet.  The most familiar species is \"Incarvillea delavayi\", a garden plant commonly known as hardy gloxinia or Chinese trumpet flower.  Unlike most other members of Bignoniaceae, which are mainly tropical woody plants, species of \"Incarvillea\" are herbs from temperate regions.\n\nNosopsyllus fasciatus: Nosopsyllus fasciatus, the northern rat flea, is a species of flea found on domestic rats and house mice.  Northern rat fleas are external parasites, living by hematophagy off the blood of rodents.  It is the most widely spread of its genus, having originated in Europe, but has been transported to temperate regions all over the world.\n\nHypericum calycinum: Hypericum calycinum is a species of prostrate or low-growing shrub in the flowering plant family Hypericaceae.  Widely cultivated for its large yellow flowers, its names as a garden plant include Rose-of-Sharon in Britain and Australia, and Aaron's beard, Great St-John's wort, and Jerusalem star.  Grown in Mediterranean climates, widely spread in the Strandja Mountains along the Bulgarian and Turkish Black Sea coast.\n\nVaniyan: Vanniyars are said to be born from flame in a mythological period.  The origin of this caste states that a Rishi or Saint known as Jambu Maharishi is the father of the group in Tamil Nadu and spread across south India.  Their main job during ancient times was safe guarding the country, forming the Army and other groups.  They broadly fall in the group of Kshatriyar.  They are widely spread groups all over Tamil Nadu, Andhra, Kerala and Karnataka(Joshua Project).\n\nSana gurban: \"Sana gurban\" is an Azerbaijani composition by Alekper Taghiyev with lyrics by Mikayil Mushfig.  It was released first in 1968 in the performance of Zeynab Khanlarova.  Due to the fact that Zeynab Khanlarova, a prominent Soviet and Azerbaijani singer, the public artist of USSR, Azerbaijani SSR, Armenian SSR and Uzbekistan SSR, enjoyed a big fame in the entire Soviet Union, the middle east and Central Asia, the songs performed by her used to become widely spread right after their release dates.  Regarding the art song \"Sana gurban\", it is believed that after the song was performed by Khanlarova in her concert in Turkey, it became spread from there over the Arab world and Greece.\n\nWild boar: The wild boar (\"Sus scrofa\"), also known as the wild swine or Eurasian wild pig, is a suid native to much of Eurasia, North Africa, and the Greater Sunda Islands.  Human intervention has spread its distribution further, making the species one of the widest-ranging mammals in the world, as well as the most widely spread suiform.  Its wide range, high numbers, and adaptability mean that it is classed as least concern by the IUCN and it has become an invasive species in part of its introduced range.  The animal probably originated in Southeast Asia during the Early Pleistocene, and outcompeted other suid species as it spread throughout the Old World.\n\nQuestion: Between Burchardia and Incarvillea which genus is more widely spread?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comparison_result\": {\n      \"type\": \"string\",\n      \"description\": \"The genus that is more widely spread.\"\n    },\n    \"compared_genera\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The two genera being compared for their spread.\"\n    },\n    \"burchardia_distribution\": {\n      \"type\": \"string\",\n      \"description\": \"Description of Burchardia's geographical distribution.\"\n    },\n    \"incarvillea_distribution\": {\n      \"type\": \"string\",\n      \"description\": \"Description of Incarvillea's geographical distribution.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for why one genus is considered more widely spread than the other.\"\n    }\n  },\n  \"required\": [\n    \"comparison_result\",\n    \"compared_genera\",\n    \"burchardia_distribution\",\n    \"incarvillea_distribution\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comparison_result": {
        "type": "string",
        "description": "The genus that is more widely spread."
      },
      "compared_genera": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The two genera being compared for their spread."
      },
      "burchardia_distribution": {
        "type": "string",
        "description": "Description of Burchardia's geographical distribution."
      },
      "incarvillea_distribution": {
        "type": "string",
        "description": "Description of Incarvillea's geographical distribution."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for why one genus is considered more widely spread than the other."
      }
    },
    "required": [
      "comparison_result",
      "compared_genera",
      "burchardia_distribution",
      "incarvillea_distribution",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
