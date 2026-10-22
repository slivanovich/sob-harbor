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
Sierra Nevada National Park (Venezuela): The Sierra Nevada National Park (PNSN) is an important National Park of Venezuela located between Mérida and Barinas states in the west of the country.  It was created on May 2, 1952, by decree of President Germán Suárez Flamerich, in order to protect the Sierra Nevada de Mérida in the Andes.

Pagué District: Pagué is the single district of Príncipe Province.  Out of the seven districts that make up the equatorial Atlantic islands of São Tomé and Príncipe, its population is one of the smallest: 7,542 (2012).  Its capital, Santo António, is also the provincial capital of Príncipe.  This district as well as the province includes several small islands around the island of Príncipe.  The Obo National Park covers the southern part of the island and since 2012, Island of Príncipe Biosphere Reserve which covers the area of parts of the island and the islets.

Atlantic Islands of Galicia National Park: The Atlantic Islands of Galicia National Park (Galician: "Parque Nacional das Illas Atlánticas de Galicia" , Spanish: "Parque Nacional de las Islas Atlánticas de Galicia" ) is the only national park located in the autonomous community of Galicia, Spain.  It comprises the archipelagos of Cíes, Ons, Sálvora and Cortegada.  The park covers a land area of 1200 ha and a sea area of 7200 ha .  It is the tenth most visited national park in Spain.  It was the thirteenth national park to be established in Spain.

Sálvora: Sálvora is a small island located on the Ría de Arousa, coast of Galicia, Spain.  It belongs to the municipality of Santa Uxía de Ribeira and is integrated in the Atlantic Islands of Galicia National Park.  It is separated from the mainland by a distance of about 3 kilometers to the north.  It occupies about 190 hectares and has a maximum height of 71 meters ("As Gralleiras").  Almost the entire perimeter of the island is rocky but has three beaches of fine white sand.  Since 2001 it has been integrated into the Atlantic Islands of Galicia National Park.

Sierra Nevada National Park (Spain): The Parque Nacional de Sierra Nevada (known as the Sierra Nevada National Park in English) is a national park located in the provinces of Granada, Almería, and Málaga in Andalusia, Spain.  It was declared a national park on 14 January 1999.  It stretches from the Alpujarra to El Marquesado and the Lecrin Valley, covering a total area of 85,883 hectares, making it the largest national park in Spain.  It incorporates the municipalities of Abla, Abrucena, Alboloduy, Alsodux, Bayárcal, Beires, Canjáyar, Fiñana, Fondón, Laujar de Andarax, Nacimiento, Ohanes, Paterna del Río, Rágol, Las Tres Villas, Aldeire, Alpujarra de La Sierra, Bérchules, Bubión, Busquístar, Cáñar, Capileira, Dílar, Dólar, Dúrcal, Ferreira, Güéjar Sierra, Huéneja, Jerez del Marquesado, Juviles, Lanjarón, Lanteira, Lecrín, Lugros, Monachil, Nevada, Nigüelas, Pampaneira, Pórtugos, Soportújar, La Taha, Trevélez, Valor and La Zubia.

Pico Bonpland: Pico Bonpland is Venezuela's third highest peak, at 4,883 metres above sea level.  It is located in the Sierra Nevada de Merida, in the Venezuelan Andes of (Mérida State).  The peak with its sister peak Pico Humboldt, and the surrounding páramos are protected by the Sierra Nevada National Park.  The name of the peak is in honor to Aimé Bonpland, although he never visited the Venezuelan Andes.

Sierra Nevada del Cocuy: The Sierra Nevada del Cocuy Chita o Guican National Natural Park (or Sierra Nevada de Chita or Sierra Nevada de Güicán, Spanish: "Parque Natural Sierra Nevada del Cocuy Chita o Guican" is a national park and a set of highlands within the Cordillera Oriental mountain range in the Andes Mountains of Colombia.

Cortegada Island: Cortegada is an almost tidal island (it is possible to go walking when the lowest tides happen, but a small amount of water flow does not disappear) in a coastal inlet near Pontevedra in Galicia, Spain.  It is part of the Atlantic Islands of Galicia National Park.

Pico Humboldt: Pico Humboldt is Venezuela's second highest peak, at 4,940 metres above sea level.  It is located in the Sierra Nevada de Merida, in the Venezuelan Andes of (Mérida State).  The peak with its sister peak Pico Bonpland, and the surrounding páramos are protected by the Sierra Nevada National Park.

Cíes Islands: The Cíes Islands are an archipelago off the coast of Pontevedra in Galicia (Spain), in the mouth of the Ria de Vigo.  They belong to the parish of San Francisco de Afora, in the municipality of Vigo.  They were declared a Nature Reserve in 1980 and are included in the Atlantic Islands of Galicia National Park ("Parque Nacional Marítimo-Terrestre das Illas Atlánticas de Galicia") created in 2002.

Question: Which park covers more land area, Sierra Nevada National Park or Atlantic Islands of Galicia National Park?

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
          "location_country": {
            "type": "string",
            "description": "The country where the park is located."
          },
          "land_area_hectares": {
            "type": "integer",
            "description": "The land area of the park in hectares."
          }
        },
        "required": [
          "park_name",
          "location_country",
          "land_area_hectares"
        ],
        "additionalProperties": false
      },
      "description": "Details of the national parks being compared."
    },
    "park_with_larger_land_area": {
      "type": "string",
      "description": "The name of the park that covers more land area."
    },
    "land_area_difference_hectares": {
      "type": "integer",
      "description": "The difference in land area between the two parks in hectares."
    }
  },
  "required": [
    "park_comparison",
    "park_with_larger_land_area",
    "land_area_difference_hectares"
  ],
  "additionalProperties": false
}
