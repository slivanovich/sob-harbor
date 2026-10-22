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
Magaliesberg Biosphere Reserve: The Magaliesberg Biosphere Reserve is located in South Africa between the cities of Pretoria and Johannesburg to the east and Rustenburg to the west.  The reserve lies at the interface of two great African biomes — the Central Grassland Plateaux and the sub-Saharan savannah — and the remnants of a third biome, the Afro‐montane forest.  The rich biodiversity includes floral species such as Aloe peglerae and Frithia pulchra, and faunal species such as the forest shrew (Myosorex varius), sable antelope (Hippotragus niger) and 443 bird species representing 46.6% of total bird species in the southern African sub-region.

Hakgala Strict Nature Reserve: Hakgala Strict Nature Reserve is one of the three strict nature reserves in Sri Lanka, the only one in the wet zone.  The reserve is an important although isolated cloud forest which supports a number of faunal species including some endemics.  The area was designated a strict nature reserve on 25 February 1938.  The reserve is adjacent to and contiguous with the Hakgala Botanical Garden which was founded in 1860.

Australian Faunal Directory: The Australian Faunal Directory (AFD) is an online catalogue of taxonomic and biological information on all animal species known to occur within Australia.  It is a program of the Department of Sustainability, Environment, Water, Population and Communities of the Government of Australia.  By September 20, 2016, the Australian Faunal Directory has collected information about 122,898 species and subspecies.  It includes the data from the discontinued "Zoological Catalogue of Australia" and is regularly updated.  Started in the 1980s, it set a goal to compile a "list of all Australian fauna including terrestrial vertebrates, ants and marine fauna" and create an "Australian biotaxonomic information system".

Wildlife of Zanzibar: The wildlife of Zanzibar consists of terrestrial and marine flora and fauna in the archipelago of Zanzibar, an autonomous region of Tanzania.  Its floral vegetation is categorized among the coastal forests of eastern Africa as the Southern Zanzibar-Inhambane coastal forest mosaic and the Northern Zanzibar-Inhambane coastal forest mosaic.  Its faunal species are mostly small animals, birds, and butterflies.

Rupa Lake: Rupa Lake or Rupa Tal is a freshwater lake in Nepal located in the pokhara-lekhnath metropolitian municipality.  It is the third biggest lake in Pokhara valley of Nepal and at an altitude of 600 m covering area about 1.35 km2 with an average water depth 3 m and maximum depth 6 m.  The lake is elongated north to south and is fed by perennial streams.  Its watershed area is 30 km², where The main inflow of water is from Talbesi stream, whereas Dhovan khola is the feeder stream with its outlet Tal khola at Sistani ghat.  It supports a number of floral and faunal species.  A total of 36 species of waterbirds have been recorded in the lake which represents about 19 percent of the total 193 wetland-dependent birds found in Nepal.

Golden jackal: The golden jackal ("Canis aureus"), also known as the Eurasian golden jackal, common jackal, or Asiatic jackal is a canine native to southeastern and central Europe, Asia Minor, the Middle East and South Asia.  It is listed as Least Concern on the IUCN Red List, due to its widespread range in areas with optimum food and shelter.  It is a social species, the basic social unit of which consists of a breeding pair and any offspring it might have.  The golden jackal is very adaptable, being able to exploit many foodstuffs, from fruit and insects to small ungulates.  As of 2005, MSW3 recognises 13 subspecies, though genetic studies published in 2015 revealed that six supposed golden jackal subspecies living in Africa were members of a separate species, "Canis anthus", reducing the number of actual golden jackal subspecies to seven.

Anatolian leopard: The Anatolian leopard ("Panthera pardus tulliana"), also called the Asia Minor leopard, was proposed in the 19th century as a distinct leopard subspecies native to south-western Turkey.  Based on morphological analysis, it was proposed to retain the name 'Anatolian leopard' for the population that lived in south-western Turkey, where leopards are considered extinct since the mid-1970s.  To date, no leopard has been recorded in this area.

Devetashka cave: Devetàshka cave (Bulgarian: Деветашката пещера ) is a large karst cave around 7 km east of Letnitsa and 15 km northeast of Lovech, near the village of Devetaki on the east bank of the river Osam, in Bulgaria.  The site has been continuously occupied by Paleo humans for tens of thousands of years, served as a shelter for various faunal species during extensive periods and is now home to nearly 30,000 bats.

Tusheti National Park: The Tusheti National Park in East Georgia is one of the eight new Protected Areas approved by Parliament of Georgia on 22 April 2003.  Global Environment Facility (GEF) and the World Bank were part of this approval process under the "Georgia – Protected Areas Development Project."  Plants conserved in the park are pine groves ("Pinus sosnovkji") and birch groves ("Betula litvinovii", "Betula raddeana").  The key faunal species in the park are Anatolian leopard ("Panthera pardus ambornii"), bear, chamois, falcon, Golden Eagle, lammergeier, lynx, mountain goat, wild goat, and wolf.  The park was named one of the "12 best places you’ve never heard of" by BudgetTravel in 2011 not only for its rich biodiversity but also for its aesthetic terrain, hamlets, old defense towers, cuisine, and folk culture.

Kiwengwa/Pongwe Forest Reserve: The Kiwengwa/Pongwe Forest Reserve is located on the north east coast of Unguja, 20 km from Zanzibar Town.  The reserve is an important biodiversity spot in the coral rag zone.  The forest reserve is rich both in faunal and floral species.  The faunal species reported from the reserve are: Endemic species of red colobus monkey, Aders's duiker, sykes, blue monkeys, sunni antelope and several species of snakes.  The avifauna species consist of 47 bird species, which includes Fischer's turaco, Zanzibar sombre greenbul, crowned hornbill and white-browed coucal.  There are 100 plant species which includes many medicinal species.  There are also coral caves within the reserve where stalactites and stalagmites can be seen.  There is also a spice plantation near the reserve.  Coral rag forest, a sensitive ecosystem, is under threat due to timber extraction since the 1970s.  Conservation measures have been undertaken to preserve the rich biodiversity of the reserve.

Question: In which Georgia park is a subspecies of the Asia Minor leopard a key faunal species?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "park_name": {
      "type": "string",
      "description": "The name of the national park."
    },
    "location_country": {
      "type": "string",
      "description": "The country where the park is located."
    },
    "key_faunal_species_count": {
      "type": "integer",
      "description": "The total number of key faunal species listed for the park."
    },
    "leopard_species_details": {
      "type": "object",
      "properties": {
        "common_name": {
          "type": "string",
          "description": "The common name of the leopard species."
        },
        "subspecies_scientific_name": {
          "type": "string",
          "description": "The scientific name of the specific leopard subspecies found in the park."
        }
      },
      "required": [
        "common_name",
        "subspecies_scientific_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "park_name",
    "location_country",
    "key_faunal_species_count",
    "leopard_species_details"
  ],
  "additionalProperties": false
}
