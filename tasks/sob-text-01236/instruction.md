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
Jade Warrior (band): Jade Warrior are a British group that were formed in 1970, originally evolving out of a band named July.  The founding members were Tony Duhig (guitar) (born Anthony Christopher Duhig, 18 September 1941, Acton, west London; died 11 November 1990, Somerset, England), Jon Field (flute, percussion, keyboards) (born John Frederick Field, 5 July 1940, Harrow, Middlesex) and Glyn Havard (vocals, bass) (born 15 February 1947, Nantyglo, South Wales).

Nelson, Lancashire: Nelson is a town and civil parish in the Borough of Pendle in Lancashire, England, with a population of 29,135 in 2011.  It is 4 miles (6.4 km) north of Burnley on the Leeds and Liverpool Canal.

Tony Hicks: Anthony Christopher "Tony" Hicks (born 16 December 1945 in Nelson, Lancashire, England) is a guitarist and singer who has been a member of the British pop group The Hollies since 1963, and as such was inducted into the Rock and Roll Hall of Fame in 2010.

Stephen Lloyd: Stephen Anthony Christopher Lloyd (born 15 June 1957) is a British Liberal Democrat politician and current MP for the constituency of Eastbourne in the House of Commons.

Christian and Nick Candy: Nicholas Anthony Christopher Candy (born 23 January 1973) and Christian Peter Candy (born 31 July 1974) are British luxury property developers.  The brothers are partly of Greek Cypriot descent, and were estimated to share a joint net worth of £1.5 billion in the "Estates Gazette" rich list 2010, placing them at position 52 in the list of the richest property developers in the United Kingdom.

Tony Kubek: Anthony Christopher Kubek (born October 12, 1935) is an American former professional baseball player and television broadcaster.  During his nine-year playing career with the New York Yankees, Kubek played in six World Series in the late 1950s and early 1960s, starting in 37 World Series games.  For NBC television, he later broadcast twelve World Series between 1968 and 1982, and fourteen League Championship Series between 1969 and 1989.  Kubek received the Ford C. Frick Award in 2009.

Tony Gallagher (businessman): Anthony Christopher Gallagher (born November 1951) is a British billionaire property developer, the founder and former chairman of Gallagher Estates and Gallagher Developments.

Tony Clark: Anthony Christopher Clark (born June 15, 1972), is a former Major League Baseball first baseman and current executive director of the Major League Baseball Players Association.

Anthony Adur: Anthony Christopher Bahadur or Anthony Adur (born February 25, 1988 in Toronto, Ontario) is a Canadian soccer player who played in the Canadian Soccer League, USL Premier Development League, S. League, Thai Premier League, National Premier Soccer League, and the North American Soccer League.

The Twilite Tone: Anthony Christopher Khan (born July 13, 1971), professionally known as as The Twilite Tone, is an American record producer recording artist, composer, DJ and radio host.  Among others, he has worked with Gorillaz, Kanye West, Common, Kendrick Lamar, Pusha T, Big Sean, Judith Hill, and John Legend.

Question: What is the population of the town where Anthony  Christopher "Tony" Hicks was born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "birth_town": {
      "type": "string",
      "description": "The town where the person was born."
    },
    "town_population": {
      "type": "integer",
      "description": "The population of the birth town."
    },
    "population_year": {
      "type": "integer",
      "description": "The year the population count was recorded."
    }
  },
  "required": [
    "person_name",
    "birth_town",
    "town_population",
    "population_year"
  ],
  "additionalProperties": false
}
