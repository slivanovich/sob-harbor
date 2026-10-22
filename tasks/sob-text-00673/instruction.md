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
Nuphar japonica: Nuphar japonica, known as East Asian yellow water-lily, is an aquatic plant species in the genus "Nuphar" found in Japan and the Korean Peninsula.  It is endangered in Russia.  The species was not accepted by The Plant List as of November 2013 , which regarded it as an "unresolved name".

Nasturtium floridanum: Nasturtium floridanum, common names Florida yellowcress and Florida watercress, is an aquatic plant species endemic to Florida, though widely distributed within that state.  It is found in wet places at elevations less than 50 m.

Wildlife of Burkina Faso: Burkina Faso is largely wild bush country with a mixture of grass and small trees in varying proportions.  The savanna region is mainly grassland in the rainy season and semi desert during the harmattan period (defined as the period when stormy and dusty Sahara winds blow dry and hot).  Fauna, one of the most diverse in West Africa, includes the elephant, hippopotamus, buffalo, monkey, lions, crocodile, giraffe, various types of antelope, and a vast variety of bird and insect life.  The country has 147 mammal species, 330 aquatic species including 121 species of fish and 2067 different plant species.  Of the plant species, the dominant endemic species are shea tree "(Butyrospermum parkii") and the baobab, the former plant species has immense economic value to the country.

Blyxa aubertii: Blyxa aubertii, common name bamboo plant, is a plant species widespread across Asia, Europe, Africa and Australia, but known from the Western Hemisphere only from a few collections in the southwestern part of the US State of Louisiana.  This is an aquatic plant growing in shallow lakes and ponds.  This and other species in the genus are sold commercially as greenery to grow alongside fish in aquaria.

Wolffia arrhiza: Wolffia arrhiza is a species of flowering plant known by the common names spotless watermeal and rootless duckweed, belonging to the Araceae, a family rich in water-loving species, such as "Arum" and "Pistia".  It is the smallest vascular plant on Earth.  It is native to Europe, Africa, and parts of Asia, and it is present in other parts of the world as a naturalized species.  It is an aquatic plant which grows in quiet water bodies such as ponds.  The green part of the plant, the frond, is a sphere measuring about 1 mm wide, but with a flat top that floats at the water's surface.  It has a few parallel rows of stomata.  There is no root.  The plant produces a minute flower fully equipped with one stamen and one pistil.  It often multiplies by vegetative reproduction, however, with the rounded part budding off into a new individual.  In cooler conditions the plant becomes dormant and sinks to the bed of the water body to overwinter as a turion.  The plant is a mixotroph which can produce its own energy by photosynthesis or absorb it from the environment in the form of dissolved carbon.

Andira: Andira is a genus of flowering plants in the legume family, Fabaceae.  It is distributed in the tropical Americas, except for "A. inermis", which also occurs in Africa.  It was formerly assigned to the tribe Dalbergieae, but recent molecular phylogenetic evidence has placed it in a unique clade named the "Andira" clade.

Plant cover: The abundances of plant species are often measured by plant cover, i.e. the relative area covered by different plant species in a small plot.  Plant cover is not biased by the size and distributions of individuals, and is an important and often measured characteristic of the composition of plant communities.  Plant cover data may be used to classify the studied plant community into a vegetation type, to test different ecological hypothesis on plant abundance, and in gradient studies, where the effects of different environmental gradients on the abundance of specific plant species are investigated.

Aquatic weed harvester: An aquatic weed harvester, also known as a water mower, mowing boat and weed cutting boat, is an aquatic machine specifically designed for inland watercourse management to cut and harvest underwater weeds, reeds and other aquatic plant life.  The action of removing aquatic plant life in such a manner has been referred to as "aquatic harvesting".

Hydrocleys nymphoides: Hydrocleys nymphoides, the waterpoppy or water-poppy, is an aquatic plant species in the Alismataceae.  It is widespread across South America, Central America, Puerto Rico, Trinidad and the Netherlands Antilles.  It is cultivated in many places for used in decorative ponds and artificial aquatic habitats, and naturalized in Australia, New Zealand, South Africa, Fiji, New Caledonia, French Polynesia, Florida, Louisiana and Texas.

Watercress: Watercress is an aquatic plant species with the botanical name Nasturtium officinale.  This should not be confused with the profoundly different and unrelated group of plants with the common name of nasturtium, within the genus "Tropaeolum".

Question: Which plant is an aquatic plant species, Andira or Watercress?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_name": {
      "type": "string",
      "description": "The name of the plant identified as aquatic."
    },
    "is_aquatic": {
      "type": "boolean",
      "description": "Indicates whether the identified plant is an aquatic species."
    },
    "reason": {
      "type": "string",
      "description": "The reason or evidence from the text supporting the classification."
    },
    "other_plant_considered": {
      "type": "string",
      "description": "The name of the other plant mentioned in the question that was not aquatic."
    }
  },
  "required": [
    "plant_name",
    "is_aquatic",
    "reason",
    "other_plant_considered"
  ],
  "additionalProperties": false
}
