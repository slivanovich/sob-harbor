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
Pleiacanthus: Pleiacanthus is a monotypic genus of flowering plants in the aster family containing the single species Pleiacanthus spinosus (formerly "Stephanomeria spinosa"), which is known by the common name thorn skeletonweed, or thorny skeletonweed.  It is native to the western United States from Montana and Idaho to southern California and Arizona, where it grows in many types of mostly dry habitat from deserts to mountains.  It is a spindly subshrub producing several slender stems up to 40 or 50 centimeters tall from a woody caudex.  The stems divide many times into short, rigid branches which narrow to sharp thorn-tips.  The plant is mostly hairless except for brownish woolly tufts at the base and below the basal leaves.  The leaves are small and linear on the lower stem, and reduced to scale-like growths on the upper branches.  Flower heads occur near the ends of the branches.  Each has a cylindrical base wrapped in one layer of phyllaries.  The head contains 3 to 5 ray florets, each with an elongated tube and a pale to bright pink ligule.  The fruit is an achene tipped with a cluster of pappus bristles which are not plumelike as are those of the "Stephanomeria" species with which this plant was once classified.

Tuberaria: Tuberaria is a genus of about 12 species of annual or perennial plants in the rockrose family Cistaceae, native to western and southern Europe.  They occur on dry, stony sites, often close to the sea.

Carphalea: Carphalea is a genus of flowering plants in the Rubiaceae family.  It is endemic to Madagascar.

Self-pollination: Self-pollination is when pollen from the same plant arrives at the stigma of a flower (in flowering plants) or at the ovule (in Gymnosperms).  There are two types of self-pollination: In autogamy, pollen is transferred to the stigma of the same flower.  In geitonogamy, pollen is transferred from the anther of one flower to the stigma of another flower on the same flowering plant, or from microsporangium to ovule within a single (monoecious) Gymnosperm.  Some plants have mechanisms that ensure autogamy, such as flowers that do not open (cleistogamy), or stamens that move to come into contact with the stigma.  The term selfing that is often used as a synonym, is not limited to self-pollination, but also applies to other types of self fertilization.

Exochorda: Exochorda is a small genus of flowering plants in the family Rosaceae, native to China and central Asia (Turkestan).  They are used as ornamental plants with the common name pearl bush, or pearlbush.  Numerous species have been described on the basis of differing appearance and geographical separation, but a systematic study revealed that the different types are closely related and probably all descended from a single species that formerly had a wide distribution that has been fragmented by habitat loss.  As a single species the correct name is "E. racemosa".

Tessmannianthus: Tessmannianthus is a genus of flowering plants in the family Melastomataceae.  There are seven species distributed in Central and South America.  They are medium to large trees up to 40 meters tall.  The flowers are heterantherous, bearing two types of stamens.  These plants are rare, and some are narrow endemics known from only one location.

Vigna: Vigna is a genus of flowering plants in the legume family, Fabaceae, with a pantropical distribution.  It includes some well-known cultivated species, including many types of beans.  Some are former members of the genus "Phaseolus".  According to "Hortus Third", "Vigna" differs from "Phaseolus" in biochemistry and pollen structure, and in details of the style and stipules.

Mentzelia affinis: Mentzelia affinis is a species of flowering plants in the family Loasaceae known by the common name yellowcomet.  It is native to the southern half of California, Arizona, and adjacent sections of Nevada and Baja California, where it is known from scrub, woodland, desert sands, and other habitat types.

Vessel element: A vessel element or vessel member (trachea) is one of the cell types found in xylem, the water conducting tissue of plants.  Vessel elements (tracheae) are typically found in flowering plants (angiosperms) but absent from most gymnosperms such as conifers.  Vessel elements are the main feature distinguishing the "hardwood" of angiosperms from the "softwood" of conifers.

Gonochorism: In biology, gonochorism ("Greek" offspring + disperse) or unisexualism or gonochory describes the state of having just one of at least two distinct sexes in any one individual organism.  The term is most often used with animals, in which the individual organisms are often gonochorous.  Gonochory is less common in plants.  For example, in flowering plants, individual flowers may be hermaphrodite (i.e. with both stamens and ovaries) or gonochorous (unisexual), having either no stamens (i.e. no male parts) or no ovaries (i.e. no female parts).  Among flowering plant species that have unisexual flowers, some also produce hermaphrodite flowers, and the three types occur in different arrangements on separate plants; the plants can be monoecious, dioecious, polygamomonoecious, polygamodioecious, andromonoecious, or gynomonoecious.

Question: Tuberaria and Carphalea, are both types of flowering plants?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_flowering_plants": {
      "type": "boolean",
      "description": "True if both Tuberaria and Carphalea are described as flowering plants in the context, otherwise false."
    },
    "carphalea_details": {
      "type": "object",
      "properties": {
        "is_flowering_plant": {
          "type": "boolean",
          "description": "True if Carphalea is explicitly stated to be a flowering plant."
        },
        "family": {
          "type": "string",
          "description": "The plant family Carphalea belongs to."
        }
      },
      "required": [
        "is_flowering_plant",
        "family"
      ],
      "additionalProperties": false
    },
    "tuberaria_details": {
      "type": "object",
      "properties": {
        "is_flowering_plant": {
          "type": "boolean",
          "description": "True if Tuberaria is explicitly stated to be a flowering plant."
        },
        "family": {
          "type": "string",
          "description": "The plant family Tuberaria belongs to."
        }
      },
      "required": [
        "is_flowering_plant",
        "family"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "is_both_flowering_plants",
    "carphalea_details",
    "tuberaria_details"
  ],
  "additionalProperties": false
}
