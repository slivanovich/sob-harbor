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
Formica rufa species group: The "Formica rufa" group is a subgeneric group within the genus "Formica", first proposed by William Morton Wheeler.  This group contains the mound-building species of "Formica" commonly termed "wood ants" or "thatch-mound ants", which build prominent nests consisting of a mound of grass, litter, or conifer needles.  The species "Formica rufa" or the red wood ant is the type species of this sub group.

Chrysidinae: The subfamily Chrysidinae contains those species that are most commonly recognized as cuckoo wasps, being by far the largest and most familiar subfamily.  The group contains some 3000 species in 48 genera in four tribes worldwide.  They are highly sculptured, with brilliantly metallic-coloredbodies, and capable of folding their bodies over (or, more commonly, rolling into a ball) as a defensive mechanism.  They are most diverse in desert regions of the world, as they are typically associated with solitary bee and wasp species, which are also most diverse in such areas.

Willow: Willows, also called sallows, and osiers, form the genus Salix, around 400 species of deciduous trees and shrubs, found primarily on moist soils in cold and temperate regions of the Northern Hemisphere.  Most species are known as willow, but some narrow-leaved shrub species are called osier, and some broader-leaved species are referred to as sallow (from Old English "sealh", related to the Latin word "salix", willow).  Some willows (particularly arctic and alpine species) are low-growing or creeping shrubs; for example, the dwarf willow ("Salix herbacea") rarely exceeds 6 cm in height, though it spreads widely across the ground.

List of cotingas: The cotingas (Cotingidae) are a clade of suboscines bird species of neotropical distribution in South America and Central America.  The group contains more than 60 living species and is in the clade Tyrannides (along with Pipridae, Oxyruncidae, Onychorhynchidae, Tityridae, Pipritidae, Platyrinchidae, Tachurididae, Rhynchocyclidae, Tyrannidae, Melanopareiidae, Conopophagidae, Thamnophilidae, Grallariidae, Rhinocryptidae, Formicariidae, and Furnariidae).

Piperaceae: The Piperaceae, also known as the pepper family, are a large family of flowering plants.  The group contains roughly 3,600 currently accepted species in 13 genera.  The vast majority of peppers can be found within the two main genera: "Piper" (2000 species) and "Peperomia" (1600 species).

Swiftlet: Swiftlets are birds contained within the four genera "Aerodramus", "Hydrochous", "Schoutedenapus" and "Collocalia".  They form the Collocaliini tribe within the swift family Apodidae.  The group contains around thirty species mostly confined to southern Asia, south Pacific islands, and northeastern Australia, all within the tropical and subtropical regions.  They are in many respects typical members of the Apodidae, having narrow wings for fast flight, with a wide gape and small reduced beak surrounded by bristles for catching insects in flight.  What distinguishes many but not all species from other swifts and indeed almost all other birds is their ability to use a simple but effective form of echolocation to navigate in total darkness through the chasms and shafts of the caves where they roost at night and breed.  The nests of some species are built entirely from threads of their saliva, and are collected for the famous Chinese delicacy bird's nest soup.

Salix sepulcralis group: The "Salix sepulcralis" group is a cultivar group containing all cultivars of hybrids between "Salix alba" and "Salix babylonica".  The "sepulcralis" or × "sepulcralis" trees are sometimes referred to as white weeping willow or glaucous weeping willow in reference to the mixed appearance from the parent species.  It was first described by L. Simonkai in 1890 from trees growing in Romania.  The group contains both weeping and nonweeping cultivars, though the best-known of its cultivars is 'Chrysocoma', the most widely grown weeping tree. .

Cuckoo paper wasp: The name cuckoo paper wasp refers to a monophyletic species group of brood-parasitic paper wasps in the genus "Polistes".  This species group contains only three species; "Polistes atrimandibularis", "P. semenowi", and "P. sulcifer", all of them obligate social parasites on other "Polistes" species.

Ostariophysi: Ostariophysi is the second-largest superorder of fish.  Members of this superorder are called ostariophysians.  This diverse group contains almost 8,000 species, about 28% of known fish species in the world and 68% of freshwater species, and are present on all major continents except Antarctica.  They have a number of common characteristics such as an alarm substance and a Weberian apparatus.  Members of this group include fish important to people for food, sport, the aquarium industry, and research.

Stipa: Stipa is a genus of around 300 large perennial hermaphroditic grasses collectively known as feather grass, needle grass, and spear grass.  They are placed in the subfamily Pooideae and the tribe Stipeae.

Question: Which group contains more species, Willow or Stipa?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "compared_groups": {
      "type": "array",
      "description": "Details of the groups being compared, including their species count.",
      "items": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the group."
          },
          "species_count": {
            "type": "integer",
            "description": "The approximate number of species in the group."
          }
        },
        "required": [
          "group_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "group_with_more_species": {
      "type": "string",
      "description": "The name of the group that contains more species."
    },
    "species_difference": {
      "type": "integer",
      "description": "The numerical difference in species count between the two groups."
    }
  },
  "required": [
    "compared_groups",
    "group_with_more_species",
    "species_difference"
  ],
  "additionalProperties": false
}
