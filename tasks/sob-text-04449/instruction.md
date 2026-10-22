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
Sholem Asch: Sholem Asch (Yiddish: שלום אַש‎ , Polish: "Szalom Asz" ; 1 November 1880 – 10 July 1957), also written Shalom Ash, was a Polish-Jewish novelist, dramatist, and essayist in the Yiddish language who settled in the United States.

The Bloody Chamber: The Bloody Chamber (or The Bloody Chamber and Other Stories) is a collection of short fiction by Angela Carter.  It was first published in the United Kingdom in 1979 by Gollancz and won the Cheltenham Festival Literary Prize.  All of the stories share a common theme of being closely based upon fairytales or folk tales.  However, Angela Carter has stated:

Isaac Meir Weissenberg: I. M. (Isaac Meir) Weissenberg (1881, Żelechów - August 13, 1938, Warsaw) was a Yiddish-language writer in Warsaw, Poland.  A disciple of I.L. Peretz, he began writing in 1904 and gained recognition for his 1906 masterpiece "A Shtetl" (A Town).  This novella, still regarded as his major achievement, was a literary response to a story by Sholem Asch called "The Shtetl".  Unlike Asch's sentimental view of Eastern European Jewish unity in the waning years of the Russian Empire, Weissenberg used a naturalistic form to explore the deep divides between Jews, usually along class lines.  In the process, he "stressed the impact of the new revolutionary doctrines upon the townlets, rousing them from their lethargy and shattering their foundations" (Liptzin, p. 257).  (See Shtetl for more on the history of these towns).  "Almost alone among Yiddish writers, Weissenberg was a worker and the son of workers," critic Ruth Wisse notes (p. 27), a fact which shaped both his subject matter and his use of language.  He wrote several novels and plays, but remained a consistently strong writer of novellas and short stories.

Shadow Dance (novel): Shadow Dance was Angela Carter's first novel, published in England by Heinemann in 1966.  It was published under the name Honeybuzzard in the United States.  Upon publication it was acclaimed by Anthony Burgess, who wrote that he "read this book with admiration, horror and other relevant emotions... Angela Carter has remarkable descriptive gifts, a powerful imagination, and... a capacity for looking at the mess of contemporary life without flinching."

Anagrams of Desire: Anagrams of Desire is an academic textbook about Angela Carter's media writings.  Written by Charlotte Crofts and published by Manchester University Press in 2003, the full title is "Anagrams of Desire: Angela Carter's Writing for Radio, Film and Television".

Indecent (play): Indecent is a play by Paula Vogel.  It recounts the controversy surrounding the play "God of Vengeance" by Sholem Asch, which was produced on Broadway in 1923, for which the cast of the original production were arrested on the grounds of obscenity.

The Company of Wolves: The Company of Wolves is a 1984 British Gothic fantasy-horror film directed by Neil Jordan and starring Sarah Patterson, Angela Lansbury, Stephen Rea and David Warner.  It was written by Angela Carter and Jordan.

Rikuda Potash: Rikuda Potash (1906–May 15, 1965) was a Polish-born Israeli Yiddish language poet and short story writer.  Sholem Asch called her "the Poetess of Jerusalem".

Angela Carter: Angela Olive Carter-Pearce (née Stalker; 7 May 1940 – 16 February 1992), known professionally as Angela Carter, was an English novelist, short story writer and journalist, known for her feminist, magical realism, and picaresque works.  In 2008, "The Times" ranked Carter tenth in their list of "The 50 greatest British writers since 1945".  In 2012, "Nights at the Circus" was selected as the best ever winner of the James Tait Black Memorial Prize.

The Man Who Loved Children: The Man Who Loved Children is a 1940 novel by Australian writer Christina Stead.  It was not until a reissue edition in 1965, with an introduction by poet Randall Jarrell, that it found widespread critical acclaim and popularity.  "Time" magazine included the novel in its "TIME 100 Best English-language Novels from 1923 to 2005".  The novel has been championed by novelists Robert Stone, Jonathan Franzen and Angela Carter.  Carter believed Stead's other novels "Cotters England"; "A Little Tea, A Little Chat"; and "For Love Alone" to be as good, if not better than "The Man Who Loved Children".

Question: Were Sholem Asch and Angela Carter both novelists?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_novelists": {
      "type": "boolean",
      "description": "True if both individuals were novelists, false otherwise."
    },
    "sholem_asch_professions": {
      "type": "array",
      "description": "A list of professions attributed to Sholem Asch.",
      "items": {
        "type": "string"
      }
    },
    "angela_carter_professions": {
      "type": "array",
      "description": "A list of professions attributed to Angela Carter.",
      "items": {
        "type": "string"
      }
    },
    "common_professions": {
      "type": "array",
      "description": "A list of professions shared by both individuals.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "are_both_novelists",
    "sholem_asch_professions",
    "angela_carter_professions",
    "common_professions"
  ],
  "additionalProperties": false
}
