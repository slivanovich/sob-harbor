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
Revue: A revue (from French 'magazine' or 'overview') is a type of multi-act popular theatrical entertainment that combines music, dance, and sketches.  The revue has its roots in 19th century popular entertainment and melodrama but grew into a substantial cultural presence of its own during its golden years from 1916 to 1932.  Though most famous for their visual spectacle, revues frequently satirized contemporary figures, news or literature.  Similar to the related subforms of operetta and musical theatre, the revue art form brings together music, dance and sketches to create a compelling show.  In contrast to these, however, revue does not have an overarching storyline.  Rather, a general theme serves as the motto for a loosely-related series of acts that alternate between solo performances and dance ensembles.

Laura Ingalls Wilder: Laura Ingalls Wilder ( ; February 7, 1867 – February 10, 1957) was an American writer known for the "Little House on the Prairie" series of children's books released from 1932 to 1943 which were based on her childhood in a settler and pioneer family.

Kate Klise: Catherine "Kate" Klise (born April 13 in 1963) is an American writer known for children's fiction.  Many of her books are illustrated by her sister, M. Sarah Klise.  Their popular "Regarding" series is presented in a scrapbook format, with letters, journal entries, and related ephemera telling the story.  She is also known for her picture books as well as the bestselling 43 Old Cemetery Road series.  Klise's first adult novel, "In the Bag", was released in 2012.  She is a contributor to "The Huffington Post".

Stephen R. Lawhead: Stephen R. Lawhead, born (1950--) 2 1950 (age 67 ) , is a UK–based American writer known for his works of fantasy, science fiction, and historical fiction, particularly Celtic historical fiction.  He has written over 28 novels and numerous children's and non-fiction books.

Jennifer Jones: Jennifer Jones (born Phylis Lee Isley; March 2, 1919 – December 17, 2009), also known as Jennifer Jones Simon, was an American actress during Hollywood's golden years.  Jones, who won the Academy Award for Best Actress for her performance in "The Song of Bernadette" (1943), was also Academy Award-nominated for her performances in four other films.  She was married three times, most notably to film producer David O. Selznick.

Debra Evans: Debra Evans (born 1953) is an American writer known for her books on issues related to contemporary Christian spirituality, reproductive health, women's wellness, and family relationships.  She has written over 22 non-fiction books.

Judy Blume: Judy Blume (born Judith Sussman; February 12, 1938) is an American writer known for children's and young adult (YA) fiction.  Some of her best known works are "Are You There God?  It's Me, Margaret" (1970), "Tales of a Fourth Grade Nothing" (1972), "Deenie" (1973), and "Blubber" (1974).  "The New Yorker" has called her books "talismans that, for a significant segment of the American female population, marked the passage from childhood to adolescence."

Victor Milan: Victor Woodward Milán (born 1954 in Tulsa, Oklahoma) is an American writer known for libertarian science fiction and an interest in cybernetics.  In 1986 he won the Prometheus Award for "Cybernetic Samurai".  He has also written several shared universe works for the Forgotten Realms, "Star Trek", and Wild Cards Universes.  He has also written books under the pseudonyms Richard Austin (Jove Books "The Guardians" series), Robert Baron (Jove Books "Stormrider" series), and S. L. Hunter ("Steele" series with Simon Hawke, who used the pen name J. D. Masters).  He also wrote at least 9 novels under the "house name" of James Axler for the Harlequin Press/Gold Eagle Books "Deathlands" and "Outlanders" series.  He has published almost 100 novels and numerous short stories.

These Happy Golden Years: These Happy Golden Years is an autobiographical children's novel written by Laura Ingalls Wilder and published in 1943, the eighth of nine books in her "Little House" series – although it originally ended it.  It is based on her later adolescence near De Smet, South Dakota, featuring her short time as a teacher, beginning at age 15, and her courtship with Almanzo Wilder.  It spans the time period from 1882 to 1885, when they marry.

List of Little House on the Prairie books: The original Little House books were a series of eight autobiographical children's novels written by Laura Ingalls Wilder and published by Harper & Brothers from 1932 to 1943.  The eighth book, "These Happy Golden Years", featured Laura Ingalls at ages 15 to 18 and was originally published with one page at the end containing the note, "The end of the Little House books."  The ninth and last novel written by Ingalls Wilder, "The First Four Years" was published posthumously and unfinished in 1971.  Although her intentions are unknown, it is commonly considered part of the Little House series and is included in the 9-volume paperback box set "Little House, Big Adventure" (Harper Trophy, May 1994).

Question: These happy Golden Years was written by what American writer known for her series of children's books that were released from 1932 to 1943?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the American writer."
    },
    "author_nationality": {
      "type": "string",
      "description": "The nationality of the writer."
    },
    "known_for_series": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the children's book series the author is known for."
        },
        "publication_years": {
          "type": "object",
          "properties": {
            "start_year": {
              "type": "integer",
              "description": "The start year of the series' release."
            },
            "end_year": {
              "type": "integer",
              "description": "The end year of the series' release."
            }
          },
          "required": [
            "start_year",
            "end_year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "series_name",
        "publication_years"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "author_name",
    "author_nationality",
    "known_for_series"
  ],
  "additionalProperties": false
}
