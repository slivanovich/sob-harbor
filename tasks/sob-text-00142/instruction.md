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
Indian country: Indian country is any of the many self-governing Native American communities throughout the United States.  As a legal category, it includes "all land within the limits of any Indian reservation", "all dependent Indian communities within the borders of the United States", and "all Indian allotments, the Indian titles to which have not been extinguished."  This legal classification defines American Indian tribal and individual land holdings as part of a reservation, an allotment, or a public domain allotment.  All federal trust lands held for Native American tribes is Indian country.  Federal, state, and local governments use this category in their legal processes.  Today, however, according to the U.S. Census of 2010, over 78% of all Native Americans live off reservations.  Indian country now spans thousands of rural areas, towns and cities where Indian people live.

Lechenaultia biloba: Lechenaultia biloba, commonly known as the blue leschenaultia, is a plant in the family Goodeniaceae native to Western Australia.  It was described in 1839 by John Lindley.  The species name refers to the two corolla lobes of the flowers.  It is a very variable species.

Indigenous languages of Arizona: Arizona, a state in the southwestern region of the United States of America, is known for its high population of Native Americans.  Arizona has the third highest number (and the sixth highest percentage) of Native Americans of any state in the Union (See Demographics of Arizona).  Out of the entire US population of 2.9 million Native Americans, roughly 286,680 live in Arizona, representing 10% of the country's total Native American population.  Only California and Oklahoma have more Native Americans than Arizona by number.  Arizona also has the highest proportion of land allocated to Native American reservations, at 28%.  Arizona has five of the twelve largest Indian reservations in the United States, including the largest, the Navajo Nation, and the third-largest, the Tohono O'odham Nation.  Also, Arizona has the largest number of Native American language speakers in the United States.

List of endemic birds of New Zealand: Many of New Zealand's birds are endemic to the country, that is, they are not found in any other country.  Endemic species differ from native or indigenous species in that native or indigenous species have generally and historically, migrated to a region or country and become established over a long period of time, whereas endemic species, have only ever inhabited the region or country where they were first discovered.  Approximately 71% of the bird species breeding in New Zealand before humans arrived are widely accepted as being endemic.

Lechenaultia formosa: Lechenaultia formosa, commonly known as the red leschenaultia, is a plant in the family Goodeniaceae native to Western Australia.  It was described in 1810 by Robert Brown.

Corokia: Corokia is a genus in the Argophyllaceae family comprising about ten species native to New Zealand and one native to Australia.  "Corokia" species are shrubs or small trees with zigzagging (divaricating) branches.  In fact, "Corokia cotoneaster" is commonly known as "wire-netting bush".  The stems of the shrubs are dark when mature, covered with downy or silky hairs (tomentum) when young.  In spring, they produce clusters of small, star shaped yellow blossoms.  Berries are red or yellow.  The shrubs prefer forests and rocky areas, sun or light shade, reasonably well drained soil, and moderate watering.

Exploitation colonialism: Exploitation colonialism is the national economic policy of conquering a country to exploit its natural resources and its native population.  The practice of exploitation colonialism contrasts with settler colonialism, the policy of conquering a country to establish a branch of the metropole (Motherland), and for the exploitation of its natural resources and native population.  A colonialist power pursues settler colonialism to relieve the pressures of over-population upon the economy and the national territory of the motherland, and to extend its territory and culture by reproducing its society in other parts of the world.  A reason for which a country might practice exploitation colonialism is the immediate financial gain produced by the low-cost extraction of raw materials by means of a native people, usually administered by a colonial government.

Argophyllaceae: Argophyllaceae is a family of shrubs or small trees belonging to the order Asterales.  The family includes two genera "Argophyllum" and "Corokia".  Members of the family are native to eastern Australia, New Zealand, Lord Howe Island, New Caledonia, and Rapa Iti.

Lady Bird Johnson Wildflower Center: The Lady Bird Johnson Wildflower Center is a public botanical garden dedicated to creating a more sustainable earth through research and education.  Situated 10 miles southwest of downtown Austin, Texas and just inside the edge of the distinctive Texas hill country, the 279-acre Wildflower Center attracts 100,000 annual visitors.  The center is a self-supporting research unit of The University of Texas at Austin devoted entirely to native plants, with more than 700 species native to central Texas, and the environmental benefits of native-plant landscaping.  (see Native Plant Information Network).  The Wildflower Center also hosts changing exhibits of visual art and photography and features outdoor sculptures, walking trails, formal and research plantings, educational exhibits, and an annual sale of native plants.  In 2013, the syndicated television series, "Texas Country Reporter", hosted by Bob Phillips, declared the center the No. 1 site from which to view wildflowers within Texas.

Lechenaultia: Lechenaultia is a genus of plants in the Goodeniaceae family.  Some species of this genus are used like ornamental plants. "Lechenaultia" species are diverse in form: they may be woody or herbaceous, upright or prostrate with leaves flat, needle-like or virtually absent in mature plants.  The genus differs from other Goodeniaceae in the structure of the stigma and the fertilization mechanism.  They are found in Australia and New Guinea (one species).

Question: Lechenaultia and Corokia, are native to which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genera_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the plant genera mentioned in the question."
    },
    "common_native_country_found": {
      "type": "boolean",
      "description": "Indicates if a common native country was found for all specified genera."
    },
    "native_countries": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The countries where all specified genera are native."
    }
  },
  "required": [
    "genera_names",
    "common_native_country_found",
    "native_countries"
  ],
  "additionalProperties": false
}
