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
Ornithogalum narbonense: Ornithogalum narbonense, common names Narbonne star-of-Bethlehem, pyramidal star-of-Bethlehem and southern star-of-Bethlehem, is a herbaceous perennial flowering plant with underground bulbs, belonging to the genus Ornithogalum of the Asparagaceae family.  The Latin name "Ornithogalum" of the Genus, meaning "bird's milk", derives from the Greek, while the species name "narbonense" refers to the French town of Narbonne.

Rhodiola rosea: Rhodiola rosea (commonly golden root, rose root, roseroot, Aaron's rod, Arctic root, king's crown, lignum rhodium, orpin rose) is a perennial flowering plant in the family Crassulaceae.  It grows naturally in wild Arctic regions of Europe, including Britain, Asia and North America, and can be propagated as a groundcover.  Although it has long been used in traditional medicine for several disorders, notably including treatment of anxiety and depression, there is little scientific evidence to verify any benefit.

Lomatium macrocarpum: Lomatium macrocarpum is a perennial flowering plant in the carrot family known by the common names bigseed lomatium, biscuit root or even bigseed biscuitroot.  It is native to much of western North America, where it can be found in various types of habitat, including the grasslands of the Great Plains.  It is spreading or erect perennial herb growing up to about half a meter long with hairy, gray-green herbage.  The leaves are up to about 24 centimeters long and are intricately divided into many small, narrow segments.  The inflorescence bears an umbel of yellowish, purplish, or white flowers.  The fruit is a compressed, winged, round or oval disc up to about 2 centimeters long.

Valeria (given name): Valeria or Valéria is a female given name dating back to the Latin verb "valere", meaning "to be strong".  The male version is Valerius, Valerio or Valery.  Valeria is also connected to the same root with the name, "Valentine," and "Valerian," or "Valeriana officinalis," the herb.

Valerian (herb): Valerian ("Valeriana officinalis", Caprifoliaceae) is a perennial flowering plant, with heads of sweetly scented pink or white flowers that bloom in the summer and can reach a height of 1.5 m .  Valerian flower extracts were used as a perfume in the 16th century.

Valeriana edulis: Valeriana edulis (tobacco root, edible valerian), a species in the Caprifoliaceae family, is a dioecious perennial flowering plant native to western and central North America.  Despite its common name, tobacco root is not closely related to tobacco, but is instead more closely related to elderberry, honeysuckle, and teasel (Caprifoliaceae s.l.).

Chrysanthemum japonense: Chrysanthemum japonense (also known as "ashizuri noji-giku Ashizuri" (Japanese) meaning ""Point wild roadside daisy"" or gold / silver chrysanthemum in English) is a flowering plant within the Asteraceae family and "Chrysanthemum" genus and has a 27 pairs of chromosomes.  It is a perennial flowering plant with leaves between 3–5 cm in length and flower heads that are 3-4.5 cm with white petals.  Typically, flowering occurs in October to December annually.  It the floral emblem of Hyōgo Prefecture.

Dendranthema boreale: Chrysanthemum boreale (or "Dendranthema boreale") is a flowering plant within the Asteraceae family and "Chrysanthemum" genus.  It used to be in the compositae family and many books still contain as such.  It is a perennial flowering plant that is often noted because of its yellow flowers.  It has 18 chromosomes at the diploid stage.

Saxifraga stolonifera: Saxifraga stolonifera is a perennial flowering plant known by several common names, including creeping saxifrage, strawberry saxifrage, creeping rockfoil, as well as the quite ambiguous "Aaron's beard", mother of thousands, roving sailor, wandering Jew, and strawberry begonia or strawberry geranium (it is neither a begonia nor a geranium).  It is native to Asia but has been introduced to other continents, mainly for use as an ornamental.  A popular garden flower, it has attractive white blossoms with distinctive pointed petals and bright yellow ovary.  "S. stolonifera" also sees use as a houseplant.  Its creeping green foliage makes a good groundcover.  The plant spreads via threadlike stolon (runners), with plantlets taking root in the vicinity of the mother plant.  It is hardy to USDA zone 5.

Aconitum carmichaelii: Aconitum carmichaelii syn.  "A. fischeri", is a species of flowering plant of the genus "Aconitum", family Ranunculaceae.  It is native to East Asia and eastern Russia.  It is commonly known as Chinese aconite, Carmichael's monkshood or Chinese wolfsbane () (Japanese: 鳥兜 or トリカブト, Torikabuto ).  It is known in Mandarin as Fu Zi (meaning daughter root, or lateral root) and as Wu Tou (meaning tuberous mother root, or root tuber).

Question: What's the name of a perennial flowering plant who's female root name Valeria, meaning "to be strong"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_name": {
      "type": "string",
      "description": "The common name of the perennial flowering plant."
    },
    "scientific_name": {
      "type": "string",
      "description": "The scientific name of the plant."
    },
    "family": {
      "type": "string",
      "description": "The botanical family the plant belongs to."
    },
    "name_origin_details": {
      "type": "object",
      "properties": {
        "related_given_name": {
          "type": "string",
          "description": "The female given name connected to the plant's name."
        },
        "given_name_meaning": {
          "type": "string",
          "description": "The meaning of the related given name."
        },
        "latin_root": {
          "type": "string",
          "description": "The Latin verb from which the name derives."
        }
      },
      "required": [
        "related_given_name",
        "given_name_meaning",
        "latin_root"
      ],
      "additionalProperties": false
    },
    "is_perennial_flowering_plant": {
      "type": "boolean",
      "description": "Indicates if the plant is a perennial flowering plant."
    }
  },
  "required": [
    "plant_name",
    "scientific_name",
    "family",
    "name_origin_details",
    "is_perennial_flowering_plant"
  ],
  "additionalProperties": false
}
