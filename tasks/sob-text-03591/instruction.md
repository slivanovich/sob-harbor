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
Jatropha: Jatropha is a genus of flowering plants in the spurge family, Euphorbiaceae.  The name is derived from the Greek words ἰατρός ("iatros"), meaning "physician", and τροφή ("trophe"), meaning "nutrition", hence the common name physic nut.  Another common name is nettlespurge.  It contains approximately 170 species of succulent plants, shrubs and trees (some are deciduous, like "Jatropha curcas").  Most of these are native to the Americas, with 66 species found in the Old World.  Plants produce separate male and female flowers.  As with many members of the family Euphorbiaceae, "Jatropha" contains compounds that are highly toxic.  Jatropha species have traditionally been used in basketmaking, tanning and dye production.  In the 2000s, one species, "Jatropha curcas", generated interest as an oil crop for biodiesel production.

Psychotria: Psychotria is a genus of flowering plants in the Rubiaceae family.  It contains around 1,850 species and is therefore one of the largest genera of flowering plants.  The genus has a pantropical distribution and members of the genus are small understorey trees in tropical forests.  Some species are endangered or facing extinction due to deforestation, especially species of central Africa and the Pacific.

Hydnophytum: Hydnophytum is a genus of epiphytic myrmecophytes (ant plants) native to Southeast Asia, the Pacific region and also extending into Queensland in northern Australia.  The name is derived from the Ancient Greek "hydnon" "tuber", and "phyton" "plant", after their appearance with their swollen succulent stems.  The species grow in tree branches and on trunks.  Like the related genus "Myrmecodia", they are known as antplants or ant-house plants.  The type species is "Hydnophytum formicarum" from the Philippines.  The genus contains 55 species, of which 44 are found in and around the island of New Guinea.  Many are poorly known, with 11 known only from the holotype.

Rubieae: Rubieae is a tribe of flowering plants in the Rubiaceae family and contains 969 species in 14 genera.  The genus "Galium" is responsible for more than two thirds of the species in the tribe.  The second largest genus is "Asperula", which contains about 200 species.  Unlike the rest of the Rubiaceae family, the tribe contains predominantly perennial and annual herbs with pseudowhorls of leaves and leaflike stipules and is centered in temperate and tropical-mountain regions.

Stenotus (plant): Stenotus is a genus of flowering plants in the daisy family, Asteraceae.  There are four species, all native to western North America.  They are known commonly as mock goldenweeds.

Aneurophyton: Aneurophyton is a genus of extinct vascular plants that belong to the Aneurophytales, a class of progymnosperms.  The genus is primarily known from records of two well-known species found in mostly Middle Devonian and Upper Devonian (late Eifelian to Famennian) outcrops in Belgium, China (West Junggar), Germany, and the United States (New York).  Some uncertain species within the genus are also recorded from Middle Devonian outcrops in Kazakhstan, Russia (Timan and Siberia), and the Ukraine.  While a number of species have been described in the paleobotanical literature, the genus likely only contains two well-circumscribed species, "A. germanicum" and "A. doui", and possibly a third species, "A. olnense", from Fammenian outcrops in Belgium.  If the ages of the Early Devonian (Emsian) records of "A. germanicum" reported from Siberia are confirmed, these would constitute the oldest records of this genus.

Frond dimorphism: Frond dimorphism refers to a difference in ferns between the fertile and sterile fronds.  Since ferns, unlike flowering plants, bear spores on the leaf blade itself, this may affect the form of the frond itself.  In some species of ferns, there is virtually no difference between the fertile and sterile fronds, such as in the genus "Dryopteris", other than the mere presence of the sori, or fruit-dots, on the back of the fronds.  Some other species, such as "Polystichum acrostichoides" (Christmas fern), or some ferns of the genus "Osmunda", feature dimorphism on a portion of the frond only.  Others, such as some species of "Blechnum" and "Woodwardia", have fertile fronds that are markedly taller than the sterile.  Still others, such as "Osmunda cinnamomea" (Cinnamon fern), or plants of the family Onocleaceae, have fertile fronds that are completely different from the sterile.

Polystichum: Polystichum is a genus of about 260 species of ferns with a cosmopolitan distribution.  The highest diversity is in eastern Asia, with about 120 species in China alone; the region from Mexico to Brazil has nearly 100 additional species; Africa (17 species), North America (15 species), and Europe (5 species) have much lower diversity.  Polystichum species are terrestrial or rock-dwelling ferns of warm-temperate and montane-tropical regions (a few species grow in alpine regions).

Zeltnera: Zeltnera is a genus of flowering plants in the gentian family.  It was erected in 2004 when the genus "Centaurium" (the centauries) was split.  Genetic analysis revealed that "Centaurium" was polyphyletic, made up of plants that could be grouped into four clades. Each became a genus.  "Centaurium" remained, but it is now limited to the Eurasian species.  The Mexican species now belong to genus "Gyrandra", and the Mediterranean and Australian plants are in genus "Schenkia".  The new name "Zeltnera" was given to this genus, which contains most of the North American centauries.  There are about 25 species.

Heliamphora: The genus Heliamphora ( or ; Greek: "helos" "marsh" and "amphoreus" "amphora") contains 23 species of pitcher plants endemic to South America.  The species are collectively known as sun pitchers, based on the mistaken notion that the "heli" of "Heliamphora" is from the Greek "helios", meaning "sun".  In fact, the name derives from "helos", meaning marsh, so a more accurate translation of their scientific name would be marsh pitcher plants.  Species in the genus "Heliamphora" are carnivorous plants that consist of a modified leaf form that is fused into a tubular shape.  They have evolved mechanisms to attract, trap, and kill insects; and control the amount of water in the pitcher.  At least one species ("H. tatei") produces its own proteolytic enzymes that allows it to digest its prey without the help of symbiotic bacteria.

Question: Which genus of plants contains more species, Polystichum or Stenotus?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement indicating which genus has more species."
    },
    "genera_details": {
      "type": "array",
      "description": "Details for each genus compared, including its name and species count.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the plant genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The number of species in the genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "genus_with_most_species": {
      "type": "string",
      "description": "The name of the genus identified as having the most species."
    },
    "species_count_of_most_species_genus": {
      "type": "integer",
      "description": "The number of species in the genus with the most species."
    },
    "species_count_difference": {
      "type": "integer",
      "description": "The numerical difference in species count between the two compared genera."
    }
  },
  "required": [
    "comparison_summary",
    "genera_details",
    "genus_with_most_species",
    "species_count_of_most_species_genus",
    "species_count_difference"
  ],
  "additionalProperties": false
}
