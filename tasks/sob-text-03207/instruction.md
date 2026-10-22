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
Soil series: Soil series as established by the National Cooperative Soil Survey of the United States Department of Agriculture (USDA) Natural Resources Conservation Service are a level of classification in the USDA Soil Taxonomy classification system hierarchy.  The actual object of classification is the so-called soil individual, or pedon.  Soil series consist of pedons that are grouped together because of their similar pedogenesis, soil chemistry, and physical properties.  More specifically, each series consists of pedons having soil horizons that are similar in soil color, soil texture, soil structure, soil pH, consistence, mineral and chemical composition, and arrangement in the soil profile.  These result in soils which perform similarly for land use purposes.

Manual Ability Classification System: The Manual Ability Classification System (MACS) is a medical classification system used to describe how children aged from 4 to 18 years old with cerebral palsy use their hands with objects during activities of daily living, with a focus on the use of both hands together.  Like the Gross Motor Function Classification System (GMFCS), there are five levels - level I being the least impaired, only finding difficulty in tasks needing speed and accuracy, and level V being the most impaired, not being able to handle objects and having severely limited abilities for even simple actions.

Taxonomy of the Cactaceae: In 1984, the International Organization for Succulent Plant Study set up a working party, now called the International Cactaceae Systematics Group, to produce a consensus classification of the cactus family, down to the level of genus.  Their classification has been used as the basis for systems published since the mid-1990s.  Treatments in the 21st century have generally divided the family into around 125–130 genera and 1,400–1,500 species, which are then arranged in a number of tribes and subfamilies.  However, subsequent molecular phylogenetic studies have shown that a very high proportion of the higher taxa (genera, tribes and subfamilies) are not monophyletic, i.e. they do not contain all of the descendants of a common ancestor.  , the internal classification of the family Cactaceae remained uncertain and subject to change.  A classification incorporating many of the insights from the molecular studies was produced by Nyffeler and Eggli in 2010.

Hierarchical classifier: A hierarchical classifier is a classifier that maps input data into defined subsumptive output categories.  The classification occurs first on a low-level with highly specific pieces of input data.  The classifications of the individual pieces of data are then combined systematically and classified on a higher level iteratively until one output is produced.  This final output is the overall classification of the data.  Depending on application-specific details, this output can be one of a set of pre-defined outputs, one of a set of on-line learned outputs, or even a new novel classification that hasn't been seen before.  Generally, such systems rely on relatively simple individual units of the hierarchy that have only one universal function to do the classification.  In a sense, these machines rely on the power of the hierarchical structure itself instead of the computational abilities of the individual components.  This makes them relatively simple, easily expandable, and very powerful.

Voice type: A voice type is a particular human singing voice identified as having certain qualities or characteristics of vocal range, vocal weight, tessitura, vocal timbre, and vocal transition points ("passaggio"), such as breaks and lifts within the voice.  Other considerations are physical characteristics, speech level, scientific testing, and vocal register.  A singer's voice type is identified by a process known as voice classification, by which the human voice is evaluated and thereby designated into a particular voice type.  The discipline of voice classification developed within European classical music and is not generally applicable to other forms of singing.  Voice classification is often used within opera to associate possible roles with potential voices.  Several different voice classification systems are available to identify voice types, including the German "Fach" system and the choral music system among many others; no system is universally applied or accepted.

Holodiscus: Holodiscus (syn.  "Sericotheca") is a genus of flowering plants in the family Rosaceae, native to the Americas, from southwestern British Columbia, Canada and the western United States south to Bolivia.

Para-archery classification: Para-archery classification is the classification system for para-archery used to create a level playing field for archers with a different range of disabilities.  Governance in the sport is through the International Archery Federation.  Early classification systems for the sport were created during the 1940s and based on medical classification.  This has subsequently changed to a functional mobility classification with the exception of blind archery.

List of NUTS regions in the European Union by GDP: The European Union uses a classification for subnational territory called "Nomenclature des Unites Territriales Statistques" (commonly abbreviated as NUTS).  The NUTS 1 classification is applied to a group of regions, NUTS 2 for regions and NUTS 3 as subdivisions of regions.  There are also two levels (NUTS 4 and 5) which relate to local administrative unit levels.  Countries agree a NUTS classification with the European Commission.  Geddes notes that NUTS level 2 is "particularly important", because they often exist as territorial-government divisions and are used for regional policies by countries.  NUTS 1 typically has a population of 3-7 million; NUTS 2 0.8-3 million; and NUTS 3 150,000-800,000.  As of 2015, there are 98 regions at NUTS 1 level, 276 regions at NUTS 2 level and 1,342 regions at NUTS 3 level "(as a result, statistics at the NUTS level 3 are found as an external link to this article)".  The EU is based on the classification of NUTS 2 regions as: less developed regions, transition regions and more developed regions.

Wachau wine: Wachau is one of Austria's most established and notable wine regions, specializing in dry wines made from Riesling and Grüner Veltliner.  Located in Lower Austria along the Danube, west of Vienna and Krems an der Donau, it is one of the westernmost wine producing regions in Austria with only a few scattered plantings in Tyrol being further west.  While most of Austria follows a wine classification systems based on ripeness and harvest must weight that parallels the German wine classification system, Wachau wines have a unique classification system.  The three classification levels for Wachau wine include "Steinfeder" for wines up to 11.5% alcohol level, "Federspiel" for wines between 11.5–12.5% and "Smaragd" that must have a minimum of 12.5% alcohol level.  Despite its renown, the Wachau is a small wine region that usually accounts for only around 3% of Austria's wine production.

Anisacanthus: Anisacanthus is a genus of flowering plants in the bear's breeches family, Acanthaceae.  The generic name is derived from the Greek words ανισος ("anisos"), meaning "unequal," and ακανθος ("acanthos"), meaning "thorn."  Members of the genus are native to tropical and subtropical regions of the Americas.  They are commonly known as desert honeysuckles, though this term is shared with the genus "Ancistranthus", and is something of a misnomer as true honeysuckles (genus "Lonicera") belong to the family Caprifoliaceae.  "Anisacanthus" species are sometimes cultivated for use in xeriscaping.

Question: Both Anisacanthus and Holodiscus are what level of classification?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "classification_level": {
      "type": "string",
      "description": "The common classification level for the entities."
    },
    "classified_entities": {
      "type": "array",
      "description": "A list of entities that share this classification level.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the classified entity."
          }
        },
        "required": [
          "entity_name"
        ],
        "additionalProperties": false
      }
    },
    "entity_count": {
      "type": "integer",
      "description": "The total number of entities identified with this classification level."
    }
  },
  "required": [
    "classification_level",
    "classified_entities",
    "entity_count"
  ],
  "additionalProperties": false
}
