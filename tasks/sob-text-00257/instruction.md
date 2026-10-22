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
Prix Sainte-Beuve: The Prix Sainte-Beuve, established in 1946, is a French literary prize awarded each year to a writer in the categories "novels" (or "poetry") and "essays" (or "critics"); it is named after the writer Charles-Augustin Sainte-Beuve.  The founding jury included Raymond Aron, Maurice Blanchot, , Maurice Nadeau, Jean Paulhan and Raymond Queneau.

Rajae Benchemsi: Rajae Benchemsi (born 1957 in Meknes) is a Moroccan writer.  Benchemsi studied literature in Paris and wrote her thesis on Maurice Blanchot.  She has published collections of poetry in Morocco and in France "Fracture du désir", a collection of articles published by Actes Sud in 1998.  In 2006, she wrote 'Houda et Taqi'.  Rajae Benchemsi is also the host of a Moroccan television program on books.

Tom Robbins: Thomas Eugene "Tom" Robbins (born July 22, 1932) is an American novelist.  His best-selling novels are "seriocomedies" (also known as "comedy-drama"), often wildly poetic stories with a strong social and philosophical undercurrent, an irreverent bent, and scenes extrapolated from carefully researched bizarre facts.  His novel "Even Cowgirls Get the Blues" was made into a movie in 1993 by Gus Van Sant and stars Uma Thurman, Lorraine Bracco, and Keanu Reeves.

Limit-experience: A limit-experience (French: "expérience limite" ) is a type of action or experience which approaches the edge of living in terms of its intensity and its seeming impossibility.  This approach has led to the seeking of limit experiences as a sort of dark mysticism.  A limit experience breaks the subject from itself.  The idea is associated with writers Georges Bataille, Maurice Blanchot, and Michel Foucault.

Maurice Blanchot: Maurice Blanchot (] ; 22 September 1907 – 20 February 2003) was a French writer, philosopher, and literary theorist.  His work had a strong influence on post-structuralist philosophers such as Gilles Deleuze, Michel Foucault, and Jacques Derrida.

Charlotte Mandell: Charlotte Mandell (born 1968) is an American literary translator.  She has translated many works of poetry, fiction and philosophy from French to English, including work by Honoré de Balzac, Gustave Flaubert, Jules Verne, Guy de Maupassant, Marcel Proust, Maurice Blanchot, Antoine de Baecque, Abdelwahab Meddeb, Bernard-Henri Lévy, Jean-Luc Nancy Matias Énard and Jonathan Littell.

L'Arrêt de mort: Death Sentence (French: "L'Arrêt de mort" ) is a philosophical novel by Maurice Blanchot.  First published in 1948, it is his second complete work of fiction.

Kevin Hart (poet): Kevin John Hart (born 5 July 1954) is an Anglo-Australian theologian, philosopher and poet.  He is currently Edwin B. Kyle Professor of Christian Studies and Chair of the Religious Studies Department at the University of Virginia.  As a theologian and philosopher, Hart's work epitomizes the "theological turn" in phenomenology, with a focus on figures like Maurice Blanchot, Emmanuel Levinas, Jean-Luc Marion and Jacques Derrida.  He has received multiple awards for his poetry, including the Christopher Brennan Award and the Grace Leven Prize for Poetry twice.

Christopher Fynsk: Christopher Ingebreth Fynsk (born August 30, 1952) is an American philosopher.  He is Professor and Dean of the Division of Philosophy, Art, and Critical Thought at the European Graduate School in Saas-Fee, Switzerland and Professor Emeritus at the University of Aberdeen.  He is well known for his work relating the political and literary aspects of continental philosophy.  Fynsk's work is closely involved with that of Martin Heidegger, Maurice Blanchot, Emmanuel Levinas, Walter Benjamin and several contemporary artists, including Francis Bacon and Salvatore Puglia.

Robert D. Lamberton: Robert Drummond Lamberton is a classics scholar, poet, and translator of ancient and contemporary literature, most notably Maurice Blanchot's "Thomas the Obscure".  He is currently a professor in the Classics Department at Washington University in St. Louis.  Professor Lamberton was born in Providence, Rhode Island and graduated in 1964 from Harvard College "magna cum laude" with a degree in Romance languages and literatures.  He has a master's (1970) and a doctoral degree in comparative literature from Yale University (1979), and has taught at Columbia, Princeton, and Cornell universities.  He has written eight books.

Question: Which philosophical writer, Tom Robbins or Maurice Blanchot, was born first?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_focus": {
      "type": "string",
      "description": "The main subject of the comparison."
    },
    "writers_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the writer."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the writer."
          },
          "is_philosophical_writer": {
            "type": "boolean",
            "description": "Indicates if the writer is considered a philosophical writer based on the context or question framing."
          }
        },
        "required": [
          "name",
          "birth_year",
          "is_philosophical_writer"
        ],
        "additionalProperties": false
      },
      "description": "A list of writers being compared, with their relevant attributes."
    },
    "writer_born_first": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the writer who was born first."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the writer who was born first."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "earliest_birth_year": {
      "type": "integer",
      "description": "The earliest birth year among the compared writers."
    }
  },
  "required": [
    "question_focus",
    "writers_compared",
    "writer_born_first",
    "earliest_birth_year"
  ],
  "additionalProperties": false
}
