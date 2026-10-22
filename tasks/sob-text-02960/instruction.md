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
Red Tarn: Red Tarn is a small lake in the eastern region of the English Lake District, in the county of Cumbria.  It is high up on the eastern flank of Helvellyn, beneath Striding Edge and Catstye Cam.  Red Tarn was formed when the glacier that carved out the eastern side of Helvellyn had melted.  The lake along with three others in Lake District is a habitat for the very rare and endangered Schelly fish.  Red Tarn was a dam in the nineteenth century that used bolders that raised the water level some eight or nine feet in order to supply power to the Greenside Mine at Glenridding.  Today the tarn is a popular rest stop for hikers and nature goers.

Gobioidei: The Gobioidei are a suborder of the Perciformes, the largest order of fish.  The suborder includes the gobies.  The suborder Gobioidei is made up of 2,211 species which are divided into seven different families.  Phylogenetic relationships of the Gobioidei have been elucidated using molecular data.  Gobioids are generally small fish and are mostly marine (saltwater) fishes, but roughly 10% of the population inhabit fresh waters.  This suborder is made up of mainly benthic or sand-burrowing fish.  Benthic fish live on the bottom of a body of water.  Like in most benthic organisms, gobioids do not have a gas bladder or swim bladder which keeps them from suspending in the water column, so they must stay on the bottom.

Schelly: The schelly ("Coregonus stigmaticus") is a freshwater fish of the salmon family, endemic to four lakes in the Lake District, England.  Alternatively it is considered either as a species or a subspecies of the widespread Eurasian whitefish species "Coregonus lavaretus".  It is present in Brothers Water, Haweswater, Red Tarn and Ullswater, and the population seems stable in all of these except for Haweswater where it seems to be declining.  The main threats it faces are seen to be water abstraction and cormorants, and the fish-eating birds are being culled from Haweswater.  The International Union for Conservation of Nature has rated the conservation status of this fish as "endangered".

Sprinkling Tarn: Sprinkling Tarn is a body of water at the foot of Great End, in the Southern Fells in Lake District, 3 km from Seathwaite, Cumbria.  Sprinkling Tarn is a popular location for wild campers.  It is also popular among anglers, being noted for its trout and an introduced rare fish, vendace.  Formerly known also as Sparkling Tarn.  It is known as the wettest place of England with an annual precipitation of over 5 metres.

Paleoflooding: The phenomenon of paleoflooding is apparent in the geologic record over various spatial and temporal scales.  It often occurred on a large scale, and was the result of either glacial ice melt causing large outbursts of freshwater, or high sea levels breaching bodies of freshwater.  If a freshwater outflow event was large enough that the water reached the ocean system, it caused changes in salinity that potentially affected ocean circulation and global climate.  Freshwater flows could also accumulate to form continental glacial lakes, and this is another indicator of large-scale flooding.  In contrast, periods of high global sea level (often during interglacials) could cause marine water to breach natural dams and flow into bodies of freshwater.  Changes in salinity of freshwater and marine bodies can be detected from the analysis of organisms that inhabited those bodies at a given time, as certain organisms are more suited to live in either fresh or saline conditions.

Perennial water: Perennial water body usually refers to mainly liquid fresh water, as opposed to sea and glaciers or other ice.  Most frequently the term refers to running water (lotic ecosystems) as in perennial streams and large rivers, but the distinction between perennial and non-perennial water is of equal importance in lentic aquatic ecosystems, those that are associated with relatively still terrestrial waters such as lakes and ponds. Simplistically a perennial water body is one that keeps full or flowing throughout the year for all or most years, but in practice there are degrees and kinds of distinction.  The definition is not precise, because most water bodies vary in fullness according to the season, and according to the heaviness of precipitation and other factors during any given year.  Also, the water level in many such water bodies as do not actually dry out, may nonetheless drop so drastically that their surface area is greatly reduced.  They even may be split into several separate water bodies with dry land between, either arid or covered with vegetation.  The internal ecology of such water may differ drastically between periods of drought and deep water.  In some cases the seasonal cycle is ecologically important, whereas in other examples exceptional water levels are too rare to be taken routinely into account.  There also may be effectively permanent changes; increasingly frequently even large rivers have lost their perennial status under the burden of the human demand for fresh water for purposes of agriculture, industry or the needs of the populations of large cities.  The Colorado River for instance has run dry for extended periods in most years since 1960 without reaching the sea.  Intermittent or ephemeral streams are those that run dry repeatedly, either seasonally or soon after rain stops.  Some definitions of perennial water bodies specifically include those that only are perennial except in years of severe or unusual drought.

Tropical fish: Tropical fish are generally those fish found in aquatic tropical environments around the world, including both freshwater and saltwater species.  Fishkeepers often keep tropical fish in freshwater and saltwater aquariums.

Saltwater intrusion: Saltwater intrusion is the movement of saline water into freshwater aquifers, which can lead to contamination of drinking water sources and other consequences.  Saltwater intrusion occurs naturally to some degree in most coastal aquifers, owing to the hydraulic connection between groundwater and seawater.  Because saline water has a higher mineral content than freshwater, it is denser and has a higher water pressure.  As a result, saltwater can push inland beneath the freshwater.  Certain human activities, especially groundwater pumping from coastal freshwater wells, have increased saltwater intrusion in many coastal areas.  Water extraction drops the level of fresh groundwater, reducing its water pressure and allowing saltwater to flow further inland.  Other contributors to saltwater intrusion include navigation channels or agricultural and drainage channels, which provide conduits for saltwater to move inland, and it can also make sea level rise.  Saltwater intrusion can also be worsened by extreme events like hurricane storm surges.

Perch: Perch is a common name for fish of the genus Perca, freshwater gamefish belonging to the family Percidae.  The perch, of which there are three species in different geographical areas, lend their name to a large order of vertebrates: the Perciformes, from the Greek "perke", simply meaning "perch", and the Latin "forma" meaning "shape".  Many species of freshwater gamefish more or less resemble perch, but belong to different genera.  In fact, the exclusively saltwater dwelling red drum is often referred to as a red perch, though by definition perch are freshwater fish.  Though many fish are referred to as perch as a common name, to be considered a true perch, the fish must be of the family Percidae.

Ictiobus: Ictiobus, also known as buffalo fish or simply buffalo, is a genus of freshwater fish common in the United States, but also found in Canada, Mexico and Guatemala.  They are the largest North American suckers, reaching up to 1.23 m in length.  They are sometimes mistaken for carp because of the flat face and large, silver scales running along the body, though they lack the whisker-like mouth appendages common to carp.  Buffalo fish live in most types of freshwater bodies where panfish are found, such as ponds, creeks, rivers, and lakes.  "Ictiobus" was caught by the Lewis and Clark Expedition.

Question: The schelly fish is found in bodies of water such as the Red Tarn, If the bodies of water like the Red Tarn are created from melted glaciers, do schelly fish live in freshwater or saltwater?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fish_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "water_preference": {
          "type": "string",
          "enum": [
            "freshwater",
            "saltwater"
          ]
        },
        "conservation_status": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "water_preference",
        "conservation_status"
      ],
      "additionalProperties": false
    },
    "habitat_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "formation_method": {
          "type": "string"
        },
        "location": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "formation_method",
        "location"
      ],
      "additionalProperties": false
    },
    "conclusion_water_type": {
      "type": "string",
      "enum": [
        "freshwater",
        "saltwater"
      ]
    }
  },
  "required": [
    "fish_details",
    "habitat_details",
    "conclusion_water_type"
  ],
  "additionalProperties": false
}
