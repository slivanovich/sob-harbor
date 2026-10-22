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
List of Solanum species: This is a list of species in the plant genus "Solanum".  There may be up to approximately 1500 species worldwide.  With some 800 accepted specific and infra-specific taxa of the more than 4,000 described, the genus "Solanum" contains more species than any other genus in the Solanaceae family and it is one of the largest among the angiosperms.

List of Amanita species: The following is a list of some notable species of the agaric genus "Amanita".  This genus contains over 500 named species and varieties, but the list is far from exhaustive.  The list follows the classification of subgenera and sections of "Amanita" outline by Corner and Bas; Bas, as used by Tulloss (2007) and modified by Redhead & al. (2016) for "Amanita" subgenus "Amanitina" and Singer for "Amanita" section "Roanokenses".  Bolding of the species name and an asterisk (*) following indicates the species is the type species of that section, with a double asterisk (**) indicating the type species of the entire genus.  Use of common names follows Tulloss (2007), Holden (2003), Arora (1986), and Lincoff (1981).

Banksiamyces: Banksiamyces is a genus of fungi in the order Helotiales, with a tentative placement in the family Helotiaceae.  The genus contains four species, which grow on the seed follicles of the dead infructescences or "cones" of various species of "Banksia", a genus in the plant family Proteaceae endemic to Australia.  Fruit bodies of the fungus appear as small (typically less than 10 mm diameter), shallow dark cups on the follicles of the "Banksia" fruit.  The edges of dry fruit bodies fold inwards, appearing like narrow slits.  The first specimens of "Banksiamyces", known then as "Tympanis toomansis", were described in 1887.  Specimens continued to be collected occasionally for almost 100 years before becoming examined more critically in the early 1980s, leading to the creation of a new genus to contain what was determined to be three distinct species, "B. katerinae", "B. macrocarpus", and "B. toomansis".  A fourth species, "B. maccannii", was added in 1984.

Megalurus: Megalurus is a genus of passerine bird in the family Locustellidae.  The genus was once placed in the Old World warbler "wastebin" family Sylviidae.  The genus contains six species also known as the typical grassbirds.  The genus is distributed from northern China and Japan, to India in the west, and Australia in the south, with most species being located wholly or partly in the tropics.  The genus is also sometimes considered to include the genus "Bowdleria", which holds the fernbirds of New Zealand.  The most widespread species, the tawny grassbird, ranges from the Philippines to southern New South Wales, whereas the Fly River grassbird is restricted to swampland in the southern part of New Guinea.  The natural habitat of the typical grassbirds is, as the name suggests, wet grasslands, swamps and other marshlands.  Some species exist away from water in tall grasslands, heathlands, and forest clearings.  Some species have adapted to the margins of rice fields and gardens.

Lycopersicon: Lycopersicon was a genus in the flowering plant family Solanaceae (the nightshades and relatives).  It contains 13 confirmed species in the tomato group of nightshades; a few others might also belong here.  First removed from the genus "Solanum" by Philip Miller in 1754, its removal leaves the latter genus paraphyletic, so modern botanists generally accept the names in "Solanum".  The name "Lycopersicon" (from Greek "λύκοπερσικων" meaning "wolf peach") is still used by gardeners, farmers, and seed companies.  Collectively, the species in this group apart from the common cultivated plant are called wild tomatoes.

Lophodermium: Lophodermium is a genus of fungi within the family Rhytismataceae.  The genus contains 145 species and has a global distribution.  Species of this genus are usually observed producing zone lines, conidiomata and ascomata on dead fallen leaves, but at least some are known to colonize living leaves.  In many cases they then live inside the colonized leaf as a symptomless endobiont, where they are regarded as detritivores utilising dead plant matter.  In a few cases they may kill all or part of the leaf prematurely, and there is a substantial literature dealing with those species as plant pathogens.  The genus infects many different plant families but with a notable concentration in the family Pinaceae; many "Lophodermium" species are restricted to a single host genus (or even species), but some, particularly those infecting grasses, may infect several genera.  Some are economically important plant pathogens, such as those that cause needlecast disease in European Black Pine, Scots Pine and Red Pine in forestry and christmas tree plantations.  In these species, notably "L. pinastri" and "L. seditiosum", the fungal spores disperse and infect the pine needles in late summer, which turn brown by the following spring and then fall off.

Coelia: Coelia is a genus of orchids (family Orchidaceae, tribe Epidendreae, subtribe Coeliinae).  It contains 5 species, native to Mexico, Central America and the West Indies.

Pachyornis: Pachyornis is an extinct genus of ratites from New Zealand which belonged to the moa family.  Like all ratites it was a member of the order Struthioniformes.  The Struthioniformes are flightless birds with a sternum without a keel.  They also have a distinctive palate.  This genus contains three species, and are part of the Anomalopteryginae or lesser moa subfamily.  "Pachyornis" moa were the stoutest and most heavy-legged genus of the family.  The most notable species being "Pachyornis elephantopus" - the Heavy-Footed Moa.  They were generally similar to the Eastern Moa or the Broad-billed moa of the genus "Euryapteryx", but differed in having a pointed bill and being more heavyset in general.  At least one species ("P. australis") is assumed to have had a crest of long feathers on its head.  The species became rapidly extinct following human colonization of New Zealand, with the possible exception of "P. australis", which may have already been extinct by then.

Solanum: Solanum is a large and diverse genus of flowering plants, which include two food crops of high economic importance, the potato and the tomato.  It also contains the nightshades and horse nettles, as well as numerous plants cultivated for their ornamental flowers and fruit.

Calyptocephalellidae: The Calyptocephalellidae are a family of toads found in Chile containing two genera, "Calyptocephalella" and "Telmatobufo".  The "Calyptocephalella" genus contains one species, "C. gayi", the helmeted water toad, which is a large aquatic toad weighing up to 0.5 kg .  The "Telmatobufo" genus contains four species, "T. australis", "T. bullocki", "T. ignotus", and "T. venustus".  All species within the family are considered threatened, with "T. bullocki" and "T. venustus" being classified as critically endangered.

Question: Which genus contains more species, Solanum or Coelia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement indicating which genus contains more species."
    },
    "genus_with_more_species": {
      "type": "string",
      "description": "The name of the genus that contains more species."
    },
    "genera_details": {
      "type": "array",
      "description": "Details for each genus involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The number of accepted species in the genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "solanum_has_more_species_than_coelia": {
      "type": "boolean",
      "description": "True if Solanum contains more species than Coelia, false otherwise."
    }
  },
  "required": [
    "comparison_summary",
    "genus_with_more_species",
    "genera_details",
    "solanum_has_more_species_than_coelia"
  ],
  "additionalProperties": false
}
