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
The Prophet (book): The Prophet is a book of 26 prose poetry fables written in English by the Lebanese-American artist, philosopher and writer Kahlil Gibran.  It was originally published in 1923 by Alfred A. Knopf.  It is Gibran's best known work.  "The Prophet" has been translated into over 40 different languages and has never been out of print.

Gibran Museum: The Gibran Museum, formerly the Monastery of Mar Sarkis, is a biographical museum in Bsharri, Lebanon, 120 km from Beirut.  It is dedicated to the Lebanese writer, philosopher, and artist Kahlil Gibran.

The Prophet (2014 film): The Prophet (full title Kahlil Gibran's The Prophet) is a 2014 animated film adapted from Kahlil Gibran's book "The Prophet".  The film was produced by Salma Hayek, who also performed voice work.  The production consisted of different directors for each of the film's collective essays, with animation director Roger Allers supervising and credited as screenwriter.  Segment directors include Paul and Gaëtan Brizzi, Joan C. Gratz, Mohammed Saeed Harib, Tomm Moore, Nina Paley, Bill Plympton, Joann Sfar and Michal Socha.  The film had an in-progress preview at the 2014 Cannes Film Festival and its world premiere at the 2014 Toronto International Film Festival.

The Seven Arts: The Seven Arts, an early example of the Little Magazine, was edited by James Oppenheim, Waldo Frank, and Van Wyck Brooks; it appeared monthly from November 1916 through October 1917.  Jointly envisaged by Oppenheim and Frank, "The Seven Arts" was an attempt to anticipate and influence the United States' emerging “renascent period;” in the first issue the editors explain: “In short, "The Seven Arts" is not a magazine for artists, but an expression of artists for the community.”  Of the many contributors to the magazine, Sherwood Anderson, J. D. Beresford, Randolph Bourne, Theodore Dreiser, Robert Frost, Kahlil Gibran, D. H. Lawrence, Amy Lowell, Paul Rosenfeld, and Louis Untermeyer were among the most prolific.

Kahlil Gibran: Khalil Gibran ( ; sometimes spelled Kahlil; full Arabic name Gibran Khalil Gibran (Arabic: جبران خليل جبران‎ ‎ / ALA-LC: "Jubrān Khalīl Jubrān" or "Jibrān Khalīl Jibrān") (January 6, 1883 – April 10, 1931) was a Lebanese writer, poet, and visual artist.

Sinclair Lewis: Harry Sinclair Lewis (February 7, 1885 – January 10, 1951), better known as Sinclair Lewis, was an American novelist, short-story writer, and playwright.  In 1930, he became the first writer from the United States to receive the Nobel Prize in Literature, which was awarded "for his vigorous and graphic art of description and his ability to create, with wit and humor, new types of characters."  His works are known for their insightful and critical views of American capitalism and materialism between the wars.  He is also respected for his strong characterizations of modern working women.  H. L. Mencken wrote of him, "[If] there was ever a novelist among us with an authentic call to the trade ... it is this red-haired tornado from the Minnesota wilds."  He has been honored by the U.S. Postal Service with a postage stamp in the Great Americans series.

Sinclair Lewis Boyhood Home: The Sinclair Lewis Boyhood Home is a historic house museum and National Historic Landmark located at 812 Sinclair Lewis Avenue, formerly South 3rd Street, in Sauk Centre, Minnesota, United States.  The house was the childhood home of Nobel prize-winning author Sinclair Lewis, who was born February 7, 1885, in a house directly across the street.  His most famous book, "Main Street" was inspired by his home town of Sauk Centre as he perceived it from this home.  The house is open for tours between Memorial Day and Labor Day, or by appointment.

National Lampoon This Side of Parodies: National Lampoon This Side of Parodies is an American humor book that was published by Warner Paperback Books in 1974.  It was a spin-off of "National Lampoon" magazine.  The book consisted of parodies of the work of famous writers, including Richard Brautigan, Boccaccio, Raymond Chandler, Henri Charrière, John Cleland, ee cummings, T. S. Eliot, Kahlil Gibran, Gerard Manley Hopkins, and Shakespeare.

The Earth Gods: The Earth Gods is a literary work written by poet and philosopher Kahlil Gibran.  It was originally published in 1931, also the year of the author's death.  The story's structured as a dialogue between three unnamed earth gods, only referred to as First God, Second God, and Third God.  As is typical of Gibran's works, it's a classic that focuses on spiritual concepts.

Kahlil Gibran (sculptor): Kahlil Gibran (`ka-lil jə-ˈbrän) (November 29, 1922 – April 13, 2008), sometimes known as "Kahlil George Gibran" (note the artist’s preferred Americanized spelling of his first name), was a Lebanese American painter and sculptor from Boston, Massachusetts.  A student of the painter Karl Zerbe at the School of the Museum of Fine Arts, Boston, Gibran first received acclaim as a magic realist painter in the late 1940s when he exhibited with other emerging artists later known as the "Boston Expressionists". .  Called a "master of materials", as both artist and restorer, Gibran turned to sculpture in the mid-fifties.  In 1972, in an effort to separate his identity from his famous relative and namesake, the author of "The Prophet", Gibran Kahlil Gibran, who was cousin both to his father Nicholas Gibran and his mother Rose Gibran, the sculptor co-authored with his wife Jean a biography of the poet entitled "Kahlil Gibran His Life And World".  Gibran is known for multiple skills, including painting; wood, wax, and stone carving; welding; and instrument making.

Question: Were both Sinclair Lewis and Kahlil Gibran from America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "author_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first author."
        },
        "is_from_america": {
          "type": "boolean",
          "description": "True if the author is identified as being from America."
        },
        "nationality_details": {
          "type": "string",
          "description": "Specific details about the author's nationality from the context."
        }
      },
      "required": [
        "name",
        "is_from_america",
        "nationality_details"
      ],
      "additionalProperties": false
    },
    "author_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second author."
        },
        "is_from_america": {
          "type": "boolean",
          "description": "True if the author is identified as being from America."
        },
        "nationality_details": {
          "type": "string",
          "description": "Specific details about the author's nationality from the context."
        }
      },
      "required": [
        "name",
        "is_from_america",
        "nationality_details"
      ],
      "additionalProperties": false
    },
    "both_from_america": {
      "type": "boolean",
      "description": "True if both authors are identified as being from America, otherwise false."
    }
  },
  "required": [
    "question_asked",
    "author_1",
    "author_2",
    "both_from_america"
  ],
  "additionalProperties": false
}
