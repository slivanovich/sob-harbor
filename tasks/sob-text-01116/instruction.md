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
Calla: Calla (bog arum, marsh calla, wild calla, squaw claw, and water-arum) is a genus of flowering plant in the family Araceae, containing the single species Calla palustris.  It is native to cool temperate regions of the Northern Hemisphere, in central, eastern and northern Europe (France and Norway eastward), northern Asia and northern North America (Alaska, Canada, and northeastern contiguous United States).

Zantedeschia: Zantedeschia is a genus of 8 species of herbaceous, perennial, flowering plants in the family Araceae, native to southern Africa from South Africa north to Malawi.  The genus has been introduced on all continents except Antarctica.  Common names include arum lily for "Z. aethiopica" and calla and calla lily for "Z. elliottiana" and "Z. rehmannii", although members of the genus are neither true lilies of Liliaceae, true "Arums", or true "Callas" (related genera in Araceae).  They are also often confused with "Anthurium".  The colourful flowers and leaves of both species and cultivars are greatly valued and commonly grown as ornamental plants.

Sinningia: Sinningia is a genus of flowering plants in the family Gesneriaceae.  It is named after Wilhelm Sinning (1792-1874), a gardener of the Botanische Gärten der Friedrich-Wilhelms-Universität Bonn.  There are about 65 species of tuberous herbaceous perennials, all occurring in Central and South America, with the greatest concentration of species occurring in southern Brazil.

Anubias: Anubias is a genus of aquatic and semi-aquatic flowering plants in the family Araceae, native to tropical central and western Africa.  They primarily grow in rivers and streams, but can also be found in marshes.  They are characterized by broad, thick, dark leaves that come in many different forms.  The genus was revised in 1979 and since then its nomenclature has been stable.  Species can be determined by using mostly characteristics of the inflorescence.  Because of the often shady places where the plants grow, the genus was named after the Egyptian god Anubis, the god of the afterlife.  The genus was first described in 1857 by Heinrich Wilhelm Schott, with "A. afzelii" as its type species.

Zantedeschia rehmannii: Zantedeschia rehmanii, the pink arum lily, pink calla, or red calla lily, is a herbaceous ornamental plant in the Araceae family.

Sinningia muscicola: Sinningia muscicola, also known as Sinningia sp.  "Rio das Pedras", is a tuberous member of the flowering plant family Gesneriaceae.  The plants produce small, bright lavender flowers.  Cultural requirements are similar to African Violets except that "S. speciosa" generally requires more humid environment.

Colocasia: Colocasia is a genus of flowering plants in the family Araceae, native to southeastern Asia and the Indian subcontinent.  Some species are widely cultivated and naturalized in other tropical and subtropical regions.  Common names include tarul, karkala ko ganu, elephant-ear, taro, cocoyam, dasheen, chembu, champadhumpa, shavige gadde, and eddoe.  Elephant-ear and cocoyam are also used for some other large-leaved genera in the Araceae, notably "Xanthosoma" and "Caladium".  The generic name is derived from the ancient Greek word "kolokasion", which in the Greek botanist Dioscorides (1st century AD) meant the edible roots of both "Colocasia esculenta" and "Nelumbo nucifera".  It is thought that the edible roots of "Colocasia esculenta" have been cultivated in Asia for more than ten thousand years.  The species "Colocasia esculenta" is an invasive species in wetlands along the American Gulf coast, where it threatens to displace native wetland plants.

Zantedeschia aethiopica: Zantedeschia aethiopica (known as calla lily and arum lily) is a species in the family Araceae, native to southern Africa in Lesotho, South Africa, and Swaziland.

Calloideae: Calloideae is a monotypic subfamily of flowering plants in the Araceae family.  The single genus in the family is Calla, although in the past under Engler's description of Araceae it included four genera, namely Lysichiton, Symplocarpus, Orontium, and Calla.  The subfamily was subsequently made monotypic and given a single tribe, Callea.  Species in Calloideae are often found in marshy habitats in the northern hemisphere.  Trichosclereids are not found in the flowers.

Arum palaestinum: Arum palaestinum is a species of flowering herbaceous perennial plant in the family Araceae (also known as black calla, Solomon's lily, Priest's Hood, Noo'ah Loof and kardi) This plant is native to the Levant and other parts of the Mediterranean Basin, and has been naturalized in North America, Europe, and Australia

Question: What type of plants are Sinningia, named after Wilhelm Sinning, and Calla from the family Araceae?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_classification": {
      "type": "string",
      "description": "The general classification or type of the plants."
    },
    "number_of_genera_identified": {
      "type": "integer",
      "description": "The count of genera identified in the answer."
    },
    "genera_information": {
      "type": "array",
      "description": "Details about each specific genus mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "plant_family": {
            "type": "string",
            "description": "The family to which the genus belongs."
          },
          "named_after_person": {
            "type": "string",
            "description": "The person after whom the genus was named, if applicable."
          }
        },
        "required": [
          "genus_name",
          "plant_family"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "plant_classification",
    "number_of_genera_identified",
    "genera_information"
  ],
  "additionalProperties": false
}
