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
Connaught Village: Connaught Village is a commercial and residential area just west of Marble Arch and just north of Hyde Park within the City of Westminster, London.  As part of the Hyde Park Estate, it is owned by the Church Commissioners of England.  Numerous boutiques, designer shops and restaurants.  The couture store of famous shoemaker Jimmy Choo was previously located here.  Tony Blair, former leader of the Labour Party and Prime Minister, resides in Connaught Square.

Connaught Square (Thunder Bay): Connaught Square is a public park located in the north end of Thunder Bay, Ontario, Canada.  It is located directly east of Waverley Park across Algoma Street, formed by the conflux of Waverly Street and Red River Road.  The square was originally named Gore Park, then renamed in 1936 for Prince Arthur, Duke of Connaught, after whom the former city of Port Arthur (originally Prince Arthur's Landing) was named.  It covers a quarter of an acre, or 1,000 square metres.  Contrary to its name is actually triangular.

Statue Square: Statue Square (; lit.  "Empress' Statue Square") is a public pedestrian square in Central, Hong Kong.  Built entirely on reclaimed land at the end of the 19th century, Statue Square consists of two parts separated by Chater Road into a northern and a southern section.  It is bordered by Connaught Road Central in the north and by Des Voeux Road Central in the south.

Thomas Allason: Thomas Allason (1790–1852) was an English architect, surveyor and landscaper, noted in particular for his work at Connaught Square and the Ladbroke Estate in Kensington.

Ellerman baronets: The Ellerman Baronetcy, of Connaught Square in the Metropolitan Borough of Paddington, was a title in the Baronetage of the United Kingdom.  It was created on 11 December 1905 for the shipowner and investor John Ellerman.  His only son, the second Baronet, was a natural historian and philanthropist.  The title became extinct on the latter's death in 1973.

Hyde Park, London: Hyde Park is a Grade I-registered major park in Central London.  It is the largest of four Royal Parks that form a chain from the entrance of Kensington Palace through Kensington Gardens and Hyde Park, via Hyde Park Corner and Green Park past the main entrance to Buckingham Palace.  The park is divided by the Serpentine and the Long Water.

St. Andrew's Church, Thunder Bay: St. Andrew's Church is a Roman Catholic Parish church in Thunder Bay, Ontario.  It was founded by the Society of Jesus in the 1872 and is a centre for ministry with the Fort William First Nation.  It is situated on Connaught Square in the Port Arthur area of the city.

Connaught Square: Connaught Square in Westminster, London, England, was the first square of city houses to be built in the Bayswater area.  It is named after the Earl of Connaught who had a house nearby.  The current appearance of the square dates from the 1820s.  The square is just north of Hyde Park, and to the west of Edgware Road.  It is also within 300 m of Marble Arch, and the western end of Oxford Street.

Seward Square: Seward Square is a square and park maintained by the National Park Service located at the intersection of Pennsylvania Avenue and North Carolina Avenue in the Capitol Hill neighborhood of Southeast Washington, D.C.  The square is bounded by 4th Street to the west and 6th Street to the east.  North and south of the park are the respective westbound and eastbound lanes of Seward Square, SE.  Because Pennsylvania and North Carolina Avenues intersect in the middle of the square, it divides the square into four unique smaller parks.  The park is named after William Henry Seward, the United States Secretary of State under Presidents Abraham Lincoln and Andrew Johnson.  Seward is noted for his part in the American purchase of Alaska from the Russian Empire in 1867.  The purchase was ridiculed at the time and was colloquially known as "Seward's Folly".  There is no statue of William Seward on the site of the park, however there is a statue of his adopted daughter, Olive Risley Seward located at a private residence at the corner of 6th Street and North Carolina Avenue, SE.  The statue was sculpted in 1971 by John Cavanaugh.

Passyunk Square, Philadelphia: Passyunk Square is a neighborhood in South Philadelphia bounded by Broad Street to the west, 6th Street to the east, Tasker Street to the south and Washington Avenue to the north.  Passyunk Square is bordered by the Bella Vista, Hawthorne, Central South Philadelphia, Wharton and Point Breeze neighborhoods.  The neighborhood got its Lenape name from the 1800s Passyunk Township, Pennsylvania which named Passyunk Square Park, located between 12th, 13th, Reed and Wharton Streets.  The park was eventually renamed Columbus Square Park, and subsequently the neighborhood became known as Columbus Square.  Geoff DiMasi revived the Passyunk Square name when forming the Passyunk Square Civic Association in 2003.

Question: Connaught Square is just north of a park that is divided by what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "square_name": {
      "type": "string",
      "description": "The name of the square mentioned in the question."
    },
    "nearby_park": {
      "type": "string",
      "description": "The name of the park located near the square."
    },
    "park_location_relative_to_square": {
      "type": "string",
      "description": "The directional relationship of the park to the square (e.g., north, south, east, west)."
    },
    "park_dividing_features": {
      "type": "array",
      "description": "A list of features that divide the nearby park.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "square_name",
    "nearby_park",
    "park_location_relative_to_square",
    "park_dividing_features"
  ],
  "additionalProperties": false
}
