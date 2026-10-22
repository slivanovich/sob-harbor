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
Acadia National Park: Acadia National Park is a United States National Park located in the state of Maine, near Bar Harbor.  It reserves much of Mount Desert Island, and associated smaller islands, off the Atlantic coast.  Initially created as the Sieur de Monts National Monument in 1916, the park was renamed Lafayette National Park in 1919, and was given its current name of Acadia in 1929.  Over three million people visited the park in 2016.  Acadia is the oldest designated national park area east of the Mississippi River.

Cortegada Island: Cortegada is an almost tidal island (it is possible to go walking when the lowest tides happen, but a small amount of water flow does not disappear) in a coastal inlet near Pontevedra in Galicia, Spain.  It is part of the Atlantic Islands of Galicia National Park.

Atlantic Islands of Galicia National Park: The Atlantic Islands of Galicia National Park (Galician: "Parque Nacional das Illas Atlánticas de Galicia" , Spanish: "Parque Nacional de las Islas Atlánticas de Galicia" ) is the only national park located in the autonomous community of Galicia, Spain.  It comprises the archipelagos of Cíes, Ons, Sálvora and Cortegada.  The park covers a land area of 1200 ha and a sea area of 7200 ha .  It is the tenth most visited national park in Spain.  It was the thirteenth national park to be established in Spain.

Cíes Islands: The Cíes Islands are an archipelago off the coast of Pontevedra in Galicia (Spain), in the mouth of the Ria de Vigo.  They belong to the parish of San Francisco de Afora, in the municipality of Vigo.  They were declared a Nature Reserve in 1980 and are included in the Atlantic Islands of Galicia National Park ("Parque Nacional Marítimo-Terrestre das Illas Atlánticas de Galicia") created in 2002.

Ria de Vigo: Vigo Ria (Galician: "" and Spanish: "Ría de Vigo" ) is an estuary in Galicia, Spain.  It is the southern most ria of the Rías Baixas.  It is located south of the province of Pontevedra, and extends in northeast direction over a length of 35 km from its mouth at Cape Silleiro to the deepest point in Arcade, with a maximum width of 7 km, and is narrowest in the Strait of Rande at 700 m. Its western entrance is protected by the Cies Islands, which are part of the National Park of the Atlantic Islands, within the islands of Toralla and San Simon.  Its borders the north with Morrazo Peninsula.  In the extreme south lies the Bay of Baiona.  Its easy access, deep draft and calm waters make the Vigo estuary an ideal retreat for sailing and water sports.

Brook Islands National Park: The Brook Islands National Park is a national park in Cassowary Coast Region, Queensland, Australia, 1246 km northwest of Brisbane, with an area of 0.9 km.  It was established in 1994 and comprises three islands - North, Tween and Middle - which lie off the coast 7 km north-east of Cape Richards on Hinchinbrook Island and 30 km east of the nearest mainland town of Cardwell.  The fourth island of the Brooks group, South Island, is not part of the national park but is protected by the Great Barrier Reef Marine Park Authority.  Public access to the three islands in the national park is prohibited in order to protect breeding birds, especially the Torresian imperial-pigeon.  The islands have no roads, walking tracks or other facilities.  Popular activities in the waters around the islands are boating, snorkelling and fishing.  The islands are managed by the Queensland Parks and Wildlife Service.  The Park's IUCN category is II.

Guadarrama National Park: Sierra de Guadarrama National Park (in Spanish: "Parque Nacional de la Sierra de Guadarrama") is a national park in Spain, covering nearly 34,000 hectares, the fifth largest in Spain's national parks system.  The Guadarrama mountain range ("Sistema Central") contains some ecologically valuable areas, located in the Community of Madrid and Castile and León (provinces of Segovia and Ávila).  The law that regulates the recently approved national park was published in the BOE in  26, 2013 (2013--) .

Galicia national basketball team: The Galicia national basketball team is the basketball team of Galicia (Spain).  The team is not affiliated to FIBA, so only plays friendly games.

Pagué District: Pagué is the single district of Príncipe Province.  Out of the seven districts that make up the equatorial Atlantic islands of São Tomé and Príncipe, its population is one of the smallest: 7,542 (2012).  Its capital, Santo António, is also the provincial capital of Príncipe.  This district as well as the province includes several small islands around the island of Príncipe.  The Obo National Park covers the southern part of the island and since 2012, Island of Príncipe Biosphere Reserve which covers the area of parts of the island and the islets.

Sálvora: Sálvora is a small island located on the Ría de Arousa, coast of Galicia, Spain.  It belongs to the municipality of Santa Uxía de Ribeira and is integrated in the Atlantic Islands of Galicia National Park.  It is separated from the mainland by a distance of about 3 kilometers to the north.  It occupies about 190 hectares and has a maximum height of 71 meters ("As Gralleiras").  Almost the entire perimeter of the island is rocky but has three beaches of fine white sand.  Since 2001 it has been integrated into the Atlantic Islands of Galicia National Park.

Question: Which park in Spain is bigger Guadarrama National Park or Atlantic Islands of Galicia National Park?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "park_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "park_name": {
            "type": "string",
            "description": "The name of the national park."
          },
          "area_hectares": {
            "type": "integer",
            "description": "The total area of the park in hectares."
          }
        },
        "required": [
          "park_name",
          "area_hectares"
        ],
        "additionalProperties": false
      },
      "description": "Details of the national parks being compared."
    },
    "larger_park_name": {
      "type": "string",
      "description": "The name of the national park that is larger."
    },
    "unit_of_measurement": {
      "type": "string",
      "description": "The unit of measurement used for the park areas."
    }
  },
  "required": [
    "park_comparison",
    "larger_park_name",
    "unit_of_measurement"
  ],
  "additionalProperties": false
}
