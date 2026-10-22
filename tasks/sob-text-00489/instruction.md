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
Garden city movement: The garden city movement is a method of urban planning in which self-contained communities are surrounded by "greenbelts", containing proportionate areas of residences, industry, and agriculture.  The idea was initiated in 1898 by Sir Ebenezer Howard in the United Kingdom.

Ebenezer Howard: Sir Ebenezer Howard {'1': ", '2': ", '3': ", '4': "} ( ; 29 January 1850 – 1 May 1928), the English founder of the garden city movement, is known for his publication "" (1898), the description of a utopian city in which people live harmoniously together with nature.  The publication resulted in the founding of the garden city movement, and the building of the First Garden City, Letchworth Garden City, commenced in 1903.

Henry Wright (planner): Henry Wright (1878-1936), was a planner, architect, and major proponent of the garden city, an idea characterized by green belts and created by Sir Ebenezer Howard.

Park system: One of the earliest park systems, in London, came into existence by chance.  As London expanded around former royal parks in the nineteenth century, St. James's Park, Green Park and Hyde Park became part of the urban area.  This arrangement was admired in France and adopted for the nineteenth century re-planning of Paris by Baron Haussmann.  It was also admired by Frederick Law Olmsted and used to create the famous Emerald Necklace in Boston.  Another example is Ebenezer Howard's Adirondack Park concept.  These green networks were part of the nineteenth century Garden City Movement.

Milton Keynes Development Corporation: Milton Keynes Development Corporation was established on 23 January 1967 to provide the vision and execution of a "new city", Milton Keynes, that would be the modern interpretation of the Garden city movement concepts first expressed by Ebenezer Howard 60 years earlier.

Kebayoran Baru: Kebayoran Baru is a subdistrict of South Jakarta, Jakarta, Indonesia.  Kebayoran Baru was the last residential area to be developed by the Dutch colonial administration.  The urban planning was laid in a concept of the Garden city movement, consisting of a well-planned residential area, a shopping center, and a business district, supported with civic facilities e.g. schools, places of worship, hospitals, and parks.  Many important governmental institutions are located in Kebayoran Baru, such as the Indonesia Stock Exchange building, the City Hall of South Jakarta, and the ASEAN Secretariat building.

Garden Cities of To-morrow: Garden Cities of To-morrow is a book by the British urban planner Ebenezer Howard.  When it was published in 1898, the book was titled "To-morrow: A Peaceful Path to Real Reform".  In 1902 it was reprinted as "Garden Cities of To-Morrow".  The book gave rise to the garden city movement.

Frederic Osborn: Sir Frederic James Osborn (1885–1978) was a leading member of the UK Garden city movement and was chairman of the Town and Country Planning Association.  He lived in Welwyn Garden City, the garden city he helped create, and a local school (Sir Frederic Osborn School) was named after him in 1968.

Complete communities: Complete communities is an urban planning concept that aims to meet the basic needs of all residents in a community, regardless of income, culture, or political ideologies through integrated land use planning, transportation planning, and community design.  While the concept is used by many communities as part of their community plan, each plan interprets what complete community means in their own way.  The idea of the complete community has roots in early planning theory, beginning with The Garden City Movement, and is a component of contemporary planning methods including Smart Growth.

Howard Centre: The Howard Centre is a shopping centre in Welwyn Garden City.  It is named after Sir Ebenezer Howard, founder of the garden city movement.

Question:  The garden city movement is a method of urban planning in which self-contained communities are surrounded by "greenbelts", containing proportionate areas of residences, industry, and agriculture, the idea was initiated in 1898 by Sir Ebenezer Howard, (29 January 1850 – 1 May 1928), the English founder of the garden city movement, is known for his publication, in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movement_name": {
      "type": "string",
      "description": "The name of the urban planning movement."
    },
    "initiator": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who initiated the movement."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the initiator."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the initiator."
        },
        "death_date": {
          "type": "string",
          "description": "The death date of the initiator."
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_date",
        "death_date"
      ],
      "additionalProperties": false
    },
    "publication": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the publication."
        },
        "publication_year": {
          "type": "integer",
          "description": "The year the publication was released."
        }
      },
      "required": [
        "title",
        "publication_year"
      ],
      "additionalProperties": false
    },
    "movement_initiation_year": {
      "type": "integer",
      "description": "The year the movement idea was initiated."
    }
  },
  "required": [
    "movement_name",
    "initiator",
    "publication",
    "movement_initiation_year"
  ],
  "additionalProperties": false
}
