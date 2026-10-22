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
Castle of Castro Laboreiro: The Castle of Castro Laboreiro (Portuguese: "Castelo de Castro Laboreiro" ) is a Portuguese castle in civil parish of Castro Laboreiro, in the municipality of Melgaço.  It is the ruins of a Romanesque castle with a belt of walls around a central keep with a cistern.

Panteón Nacional Román Baldorioty de Castro: The Panteón Nacional Román Baldorioty de Castro (English: Román Baldorioty de Castro National Pantheon) is a tract of land in Barrio Segundo of the city of Ponce, Puerto Rico, originally designed as the city's cemetery, but later converted into what has come to be a famous burial place.  Established in 1842, it is Puerto Rico's first (and only) national pantheon.  It is the only cemetery dedicated as a museum in Puerto Rico and the Caribbean.  Prior to being dedicated as a Panteon Nacional, it was known as Cementerio Viejo or as Cementerio Antiguo de Ponce, and is listed under that name on the U.S. National Register of Historic Places.  The Pantheon is named after Román Baldorioty de Castro, a prolific Puerto Rican politician, and firm believer of Puerto Rican autonomy and independence.  His remains are located here.  The Pantheon also houses a small museum about the history of autonomism in the Island, and it is currently used both as a park and a venue for the expression of culture and the arts.  It is called the Museo del Autonomismo Puertorriqueño.

Cão de Castro Laboreiro: The Cão de Castro Laboreiro, or Dog from Castro Laboreiro, or Portuguese Cattle Dog or Portuguese Watch Dog, is a dog breed of the livestock guardian dog type, originating from Castro Laboreiro in the northern mountains of Portugal.

Gutierre Rodríguez de Castro: Gutierre Rodríguez de Castro also known as Gutierre Ruiz de Castro and nicknamed el Escalabrado (died  1195 ) was a Castilian nobleman, member of the House of Castro as the son of Rodrigo Fernández de Castro and his wife Elo Álvarez, daughter of Álvar Fáñez and his wife Mayor Pérez, daughter of Count Pedro Ansúrez.

Pointer (dog breed): The Pointer, often called the English Pointer, is a medium to large-sized breed of dog developed in England as a gun dog.  It is one of several pointing breeds.

Castro Laboreiro: Castro Laboreiro is a village and a former civil parish in the municipality of Melgaço in the Viana do Castelo District, Portugal.  In 2013, the parish merged into the new parish Castro Laboreiro e Lamas de Mouro.  It is in the mountain range of the Laboreiro.  As of 2001 the area had 726 inhabitants.  The name derives from "Castro", a hill fort, and "Lepporariu", "of hares", a Latin name from Roman times.

Machado de Castro National Museum: The National Museum Machado de Castro (Museu Nacional de Machado de Castro) is an art museum in Coimbra, Portugal, named after the renowned Portuguese sculptor Joaquim Machado de Castro.  It first opened in 1913 and its latest renovation (2004-2012), which included the addition of a new building, was awarded the Piranesi/Prix de Rome Prize 2014.

Adélia Josefina de Castro Fonseca: Adélia Josefina de Castro Fonseca (Salvador, Bahia, 24 November 1827 — Rio de Janeiro, 9 December 1920) was a Brazilian poet.  Her parents were Justiniano de Castro Rebello and Adriana de Castro Rebello.  She married Inácio Joaquim da Fonseca.  She published her poems in newspapers and books, and was a constant collaborator with the Almanaque de lembranças luso-brasileiro.  Towards the end of her life, she entered the Convent of Santa Teresa, in Rio de Janeiro, adopting the name of Mother Maria José de Jesús.

Castro Laboreiro e Lamas de Mouro: Castro Laboreiro e Lamas de Mouro is a civil parish in the municipality of Melgaço, Portugal.  It was formed in 2013 by the merger of the former parishes Castro Laboreiro and Lamas de Mouro.  The population in 2011 was 657, in an area of 106.09 km².

Fernando Rodríguez de Castro (died 1304): Fernando Rodríguez de Castro (died 1304), was a Galician noble and a member of the House of Castro.  He was the son of Esteban Fernández de Castro, Lord of Lemos and Sarria, and Alzonza Rodríguez de León.  His paternal grandparents were Fernando Gutiérrez de Castro and Emilia Iniguez de Mendoza.  His maternal grandparents were Rodrigo Alfonso de León, son of Alfonso IX of León, and Ines Rodríguez Cabrera.

Question: Cão de Castro Laboreiro and Pointer, are a breed of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_animal_type": {
      "type": "string",
      "description": "The common animal type that both mentioned breeds belong to."
    },
    "breeds_mentioned": {
      "type": "array",
      "description": "Details about each specific breed mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The primary name of the breed."
          },
          "is_a_dog_breed": {
            "type": "boolean",
            "description": "Indicates if the breed is explicitly stated to be a dog breed."
          },
          "origin_location": {
            "type": "string",
            "description": "The geographical origin of the breed, if specified."
          },
          "other_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other names or aliases for the breed, if available."
          }
        },
        "required": [
          "name",
          "is_a_dog_breed"
        ],
        "additionalProperties": false
      }
    },
    "number_of_breeds_identified": {
      "type": "integer",
      "description": "The total count of distinct breeds identified in the question."
    }
  },
  "required": [
    "common_animal_type",
    "breeds_mentioned",
    "number_of_breeds_identified"
  ],
  "additionalProperties": false
}
