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
E. Thomas: E. Thomas is an Italian fabric mill established in Brusimpiano in 1922 by Ernesto Thomas.  The mill's fabrics include a range of blends combining wool with silk, Chinese and Mongolian cashmere, mohair and linen.  The mill is located on the Italian shore of Lake Lugano.

Drago (fabric mill): Drago is a wool mill founded in 1973 by Umberto and Laura Drago in Biella, Italy.  Their son, Paolo Drago, is the current President and CEO.  The mill produces 1,750,000 meters of fabrics per year.  Drago fabrics are exported all over the world.  Drago sells some fabric under its own brand, but sells mainly under other brand labels.

Holland &amp; Sherry: Holland & Sherry is a fabric mill founded in London in 1836 by Stephen George Holland and Frederick Sherry.  Its head office is still on Savile Row.  Holland & Sherry provide fabrics to tailors and couture designers throughout the world.  It is owned by Individualized Apparel Group as of March 2003.

Vitale Barberis Canonico: Vitale Barberis Canonico is an Italian fabric mill established in 1663, located about 50 miles north of Milan in the northern Biella region.  Francesco Vitale Barberis is the current creative director.

Savile Row: Savile Row (pronounced ) is a street in Mayfair, central London.  Known principally for its traditional bespoke tailoring for men, the street has had a varied history that has included accommodating the headquarters of the Royal Geographical Society at 1 Savile Row, where significant British explorations to Africa and the South Pole were planned; and more recently, the Apple office of the Beatles at 3 Savile Row, where the band's final live performance was held on the roof of the building.

Woodside Cotton Mill Village Historic District: Woodside Cotton Mill Village Historic District is a national historic district located in Greenville County, South Carolina.  The district encompasses 278 contributing buildings and 2 contributing sites in an early 20th century urban South Carolina textile mill village.  Centered on a mill founded by John T. Woodside in 1902, the district is located just west of the city limits of Greenville and is largely intact despite modernizations made by a succession of mill and home owners.  The mill itself is a rectangular, brick, four-story building designed by J.E. Sirrine and built between 1902 and 1912.  Eventually the mill became the largest cotton mill under one roof in the United States and one of the largest in the world.

Heap's Rice Mill: Heap's Rice Mill was a rice mill founded by Joseph Heap with Joseph Heap & Sons Ltd. in either 1778 or 1780 on Pownall Street in Liverpool, Merseyside.  It originated as a rice mill, with warehouses added and later combined into a single building.  The rice in Kellogg's Rice Krispies was once ground at Heap's.  It is constructed in brick with some sandstone dressings, and has roofs of slate, tiles and corrugated sheeting and a frame of timber and cast iron.  The whole building has a square plan, and is mainly in seven storeys.

Bloomsbury Publishing: Bloomsbury Publishing plc (formerly M.B.N.1 Limited and Bloomsbury Publishing Company Limited) is a British independent, worldwide publishing house of fiction and non-fiction.  It is a constituent of the FTSE SmallCap Index.  Bloomsbury's head office is located in Bloomsbury, an area of the London Borough of Camden and it has a US publishing office located in New York City, an India publishing office in New Delhi and an Australia sales office in Sydney CBD.  The company's growth over the past two decades is primarily attributable to the "Harry Potter" series by J. K. Rowling and, from 2008, to the development of its academic and professional publishing division.  The Bloomsbury Academic & Professional division won the Bookseller Industry Award for Academic, Educational & Professional Publisher of the Year in both 2013 and 2014.

Piccadilly: Piccadilly ( ) is a road in the City of Westminster, London to the south of Mayfair, between Hyde Park Corner in the west and Piccadilly Circus in the east.  It is part of the A4 road that connects central London to Hammersmith, Earl's Court, Heathrow Airport and the M4 motorway westward.  St James's is to the south of the eastern section, while the western section is built up only on the northern side.  At just under 1 mi in length, Piccadilly is one of the widest and straightest streets in central London.

Shepherd Market: Shepherd Market is a small square in the Mayfair area of central London, developed in 1735-46 by Edward Shepherd on the open ground then used for the annual May fair from which Mayfair gets its name.  It is located between Piccadilly and Curzon Street and has a village-like atmosphere.  It has been associated with prostitutes since the Eighteenth century; in the 1980s, Jeffrey Archer met the prostitute Monica Coghlan in Shepherd Market.  In the 1920s it was a popular residential area for writers and artists, such as Anthony Powell, Michael Arlen and Sophie Fedorovitch.

Question: Holland & Sherry is a fabric mill founded in London in 1836, on which street it the head office located, in Mayfair, central London?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fabric_mill_name": {
      "type": "string",
      "description": "The name of the fabric mill."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the fabric mill was founded."
    },
    "head_office_location": {
      "type": "object",
      "properties": {
        "street_name": {
          "type": "string",
          "description": "The name of the street where the head office is located."
        },
        "city": {
          "type": "string",
          "description": "The city where the head office is located."
        },
        "area": {
          "type": "string",
          "description": "The specific area or district within the city."
        }
      },
      "required": [
        "street_name",
        "city",
        "area"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fabric_mill_name",
    "founding_year",
    "head_office_location"
  ],
  "additionalProperties": false
}
