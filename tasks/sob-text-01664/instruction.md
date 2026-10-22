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
Swiss Family Robinson (1974 TV series): Swiss Family Robinson is a 1974–1975 Canadian television drama series, based on Johann David Wyss' novel "The Swiss Family Robinson".

The Adventures of Swiss Family Robinson: The Adventures of Swiss Family Robinson is a 1998 family adventure series that originally aired on the PAX network (now Ion Television).  Based on the 1812 novel "The Swiss Family Robinson", it follows the adventures of nine survivors of a shipwreck as they attempt to adapt to life on a deserted island.  It lasted for one season.

The Swiss Family Robinson (1975 TV series): The Swiss Family Robinson is an American action and adventure series that was broadcast during the 1975–76 TV season.  The two-hour pilot for the series was first shown on April 15, 1975.  Based upon the novel "The Swiss Family Robinson", the pilot and its 20 subsequent episodes of the series were produced by Irwin Allen, who had earlier produced a futuristic adaptation of the same novel in the TV series "Lost in Space".

Swiss Family Robinson (1940 film): Swiss Family Robinson is a 1940 American film released by RKO Radio Pictures and directed by Edward Ludwig.  It is based on the novel "The Swiss Family Robinson" by Johann David Wyss and is the first feature-length film version of the story.

The New Swiss Family Robinson: The New Swiss Family Robinson is a 1998 adventure film directed by Stewart Raffill.  The film is based on "The Swiss Family Robinson" and stars Jane Seymour, David Carradine, James Keach, John Mallory Asher, Blake Bashoff, and Jamie Renée Smith.

Tonka (film): Tonka is a 1958 Walt Disney Western adventure film about the US cavalry horse that survived the Battle of the Little Big Horn.  Also released under the title A Horse Named Comanche, it stars Sal Mineo as a Sioux who fought there.  It was filmed in Bend, Oregon, and distributed by Buena Vista Distribution.

The Mysterious Island: The Mysterious Island (French: "L'Île mystérieuse" ) is a novel by Jules Verne, published in 1874.  The original edition, published by Hetzel, contains a number of illustrations by Jules Férat.  The novel is a crossover sequel to Verne's famous "Twenty Thousand Leagues Under the Sea" and "In Search of the Castaways", though its themes are vastly different from those books.  An early draft of the novel, initially rejected by Verne's publisher and wholly reconceived before publication, was titled "Shipwrecked Family: Marooned With Uncle Robinson," seen as indicating the influence on the novel of "Robinson Crusoe" and "The Swiss Family Robinson".  Verne developed a similar theme in his later novel, "Godfrey Morgan" (French: "L'École des Robinsons", 1882).

Swiss Family Robinson (1960 film): Swiss Family Robinson is a 1960 American Adventure film starring John Mills, Dorothy McGuire, James MacArthur, Janet Munro, Tommy Kirk and Kevin Corcoran in a tale of a shipwrecked family building an island home, loosely based on the 1812 novel "Der Schweizerische Robinson" (literally, "The Swiss Robinson") by Johann David Wyss.  The film was directed by Ken Annakin and shot in Tobago and Pinewood Studios outside London.  It was the second feature film version of the story (the first film version was released by RKO in 1940) and was a commercial success.

Johann David Wyss: Johann David Wyss ] (May 28, 1743 in Bern – January 11, 1818 in Bern) was a Swiss author, best remembered for his book "The Swiss Family Robinson" ("Der schweizerische Robinson") (1812).  It is said that he was inspired by Daniel Defoe's "Robinson Crusoe", but wanted to write a story from which his own children would learn, as the father in the story taught important lessons to his children. " The Swiss Family Robinson" was first published in 1812 and translated into English two years later.  It has since become one of the most popular books of all time.  The book was edited by his son, Johann Rudolf Wyss, a scholar who wrote the Swiss national anthem.  Another son, Johann Emmanuel Wyss, illustrated the book.  Unlike his son, Johann David Wyss lived up to the age of 74, dying in 1818.

The Swiss Family Robinson: The Swiss Family Robinson (German: "Der Schweizerische Robinson") is a novel by Johann David Wyss, first published in 1812, about a Swiss family shipwrecked in the East Indies en route to Port Jackson, Australia.

Question: What is the American adventure film of a shipwrecked family building an island home, Swiss Family Robinson or Tonka?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_film_title": {
      "type": "string",
      "description": "The title of the film that matches the description."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the identified film."
    },
    "is_american": {
      "type": "boolean",
      "description": "True if the film is American."
    },
    "is_adventure_genre": {
      "type": "boolean",
      "description": "True if the film is an adventure genre."
    },
    "involves_shipwrecked_family": {
      "type": "boolean",
      "description": "True if the film's plot involves a shipwrecked family."
    },
    "involves_building_island_home": {
      "type": "boolean",
      "description": "True if the film's plot involves building an island home."
    },
    "meets_all_criteria": {
      "type": "boolean",
      "description": "True if the identified film meets all criteria specified in the question."
    }
  },
  "required": [
    "identified_film_title",
    "release_year",
    "is_american",
    "is_adventure_genre",
    "involves_shipwrecked_family",
    "involves_building_island_home",
    "meets_all_criteria"
  ],
  "additionalProperties": false
}
