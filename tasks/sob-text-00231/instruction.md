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
Smetana (disambiguation): Smetana often refers to the Czech composer Bedřich Smetana.

Libuše (opera):    is a '"festival opera" in three acts, with music by Bedřich Smetana.  The libretto was originally written in German by Josef Wenzig, and was then translated into Czech by Ervin Špindler.  In Czech historical myth, Libuše, the title character, prophesied the founding of Prague.  The opera was composed in 1871–72 for the coronation of Franz Josef as Czech king.  This did not happen and Smetana saved "Libuše" for the opening of the National Theatre in Prague, which took place nine years later on 11 June 1881.  After the destruction of the National Theatre in a fire, the same opera opened the reconstructed theatre in 1883.  The first US performance was reported to have occurred March 1986, in a concert version at Carnegie Hall with Eve Queler and the Opera Orchestra of New York.

Oscar Peterson Plays George Gershwin: Oscar Peterson Plays George Gershwin is a 1952 album by pianist Oscar Peterson of popular songs written by George Gershwin and Ira Gershwin.  Several tracks were included on the 1959 album "Oscar Peterson Plays the George Gershwin Songbook".

Antonín Dvořák: Antonín Leopold Dvořák ( ; ] ; 8 September 1841 – 1 May 1904) was a Czech composer.  After Bedřich Smetana, he was the second Czech composer to achieve worldwide recognition.  Following Smetana's nationalist example, Dvořák frequently employed aspects, specifically rhythms, of the folk music of Moravia and his native Bohemia.  Dvořák's own style has been described as "the fullest recreation of a national idiom with that of the symphonic tradition, absorbing folk influences and finding effective ways of using them."

List of compositions by Bedřich Smetana: Below is a List of compositions by Bedřich Smetana sorted by genre, catalogue numbers, original and English titles.  JB numbers are from "Tematický katalog skladeb Bedřicha Smetany" (Thematic Catalogue of Works by Bedřich Smetana) by Jiří Berkovec (Prague, 1999).  B. numbers are from the catalogue by František Bartoš.  T. numbers are from the 1893 catalogue by Karel Teige.

George Gershwin: George Jacob Gershwin ( ; September 26, 1898 July 11, 1937) was an American composer and pianist.  Gershwin's compositions spanned both popular and classical genres, and his most popular melodies are widely known.  Among his best-known works are the orchestral compositions "Rhapsody in Blue" (1924) and "An American in Paris" (1928) as well as the opera "Porgy and Bess" (1935).

Eleanora Ehrenbergů: Eleanora Ehrenbergů (sometimes spelled Eleanora Ehrenbergová or Eleanora Ehrenberg) (1 November 1832 – 30 August 1912) was a Czech operatic soprano.  In 1854 she made her professional opera debut at the Estates Theatre in the title role of Donizetti's "Lucia di Lammermoor".  In 1866 she created the role of Mařenka in the world première of Bedřich Smetana's "The Bartered Bride", and in 1868 she portrayed Jitka in the premiere of Smetana's "Dalibor".  She retired from the stage sometime in the 1880s.

Bedřich Smetana Museum: The Bedřich Smetana Museum (Muzeum Bedřicha Smetany) in Prague is a museum which is dedicated to the life and works of famous Czech composer Bedřich Smetana (1824–1884).  It is situated in the centre of Prague in a small block of buildings right next to Charles Bridge on the right bank of the river Vltava in the Old Town (Novotného lávka 1, 110 00 Praha 1).

Viola (opera): Viola is an unfinished romantic opera by Bedřich Smetana.  The libretto was written by Eliška Krásnohorská, and is based on Shakespeare's play "Twelfth Night".  The composer did some work on it in 1874 and then came back to it in 1883, when he only managed to orchestrate a few scenes; the opera was left incomplete upon Smetana's death in 1884.

Bedřich Smetana: Bedřich Smetana (] ; 2 March 1824 – 12 May 1884) was a Czech composer who pioneered the development of a musical style which became closely identified with his country's aspirations to independent statehood.  He is thus widely regarded in his homeland as the father of Czech music.  Internationally he is best known for his opera "The Bartered Bride" and for the symphonic cycle "Má vlast" ("My Homeland"), which portrays the history, legends and landscape of the composer's native land.

Question: Whose musical style was most influenced by politics, Bedřich Smetana or George Gershwin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_influenced_by_politics": {
      "type": "string",
      "description": "The name of the composer whose musical style was most influenced by politics."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why this composer's style was politically influenced, based on the provided context."
    },
    "influenced_composer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "political_influence_description": {
          "type": "string",
          "description": "How their style was linked to political or national aspirations."
        }
      },
      "required": [
        "name",
        "nationality",
        "political_influence_description"
      ],
      "additionalProperties": false
    },
    "other_composer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "political_influence_not_mentioned": {
          "type": "boolean",
          "description": "Indicates if political influence on their style was not mentioned in the context."
        }
      },
      "required": [
        "name",
        "nationality",
        "political_influence_not_mentioned"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "composer_influenced_by_politics",
    "reasoning",
    "influenced_composer_details",
    "other_composer_details"
  ],
  "additionalProperties": false
}
