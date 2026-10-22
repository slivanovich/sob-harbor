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
That's My Boy (U.S. TV series): That's My Boy is a largely forgotten 1954-1955 CBS situation comedy television series based on the 1951 Dean Martin and Jerry Lewis film of the same name.

The Jerry Lewis Show: The Jerry Lewis Show was the name of several separate but similar American variety, talk and comedy programs starring comedian Jerry Lewis that aired non-consecutively between September 21, 1963 – 1984.  The original version of the series aired on ABC from September 21, 1963–December 21, 1963.  A second series also called The Jerry Lewis Show aired on NBC from September 12, 1967–May 27, 1969.  A final version also called The Jerry Lewis Show aired in first-run syndication for one week in June 1984.

Boeing Boeing (1965 film): Boeing (707) Boeing (707) (alternately titled Boeing Boeing) is a 1965 American bedroom farce comedy film, based on the 1960 French play "Boeing-Boeing", and starring Jerry Lewis and Tony Curtis.  It was released on December 22, 1965, and was the last film Paramount Pictures made with Lewis, who had made films exclusively with the studio since "My Friend Irma" (1949).

Jerry Lewis: Jerry Lewis (born either Jerome Levitch or Joseph Levitch, depending on the source; March 16, 1926 – August 20, 2017) was an American comedian, actor, singer, producer, director, screenwriter, and humanitarian.

How to Smuggle a Hernia Across the Border: How to Smuggle the Hernia Across the Border is a short 1949 comedy film directed by Jerry Lewis and starring Jerry Lewis, Janet Leigh, and Tony Curtis.  The film was not released commercially.  The film is based on a funny story by Dean Martin's wartime personal problems with hernia.

The Geisha Boy: The Geisha Boy is a 1958 American comedy film starring Jerry Lewis, distributed by Paramount Pictures.  Filmed from June 16 to August 7, 1958, it had its first screening in New York City on December 19, 1958.  This film marked the film debut of Suzanne Pleshette.

Max Rose: Max Rose is a 2016 American drama film starring Jerry Lewis and written and directed by Daniel Noah.  The film also stars Kevin Pollak, Kerry Bishe, Dean Stockwell and Claire Bloom.  It is Lewis' first starring film role since 1995's "Funny Bones", as well as his final starring role.  Oscar winners Michel Legrand with Alan and Marilyn Bergman created an original song for the feature.  The film was produced by Lightstream Entertainment's Garrett Kelleher and Blackbird’s Lawrence Inglee, along with Rush River’s Bill Walton.

The Errand Boy: The Errand Boy is a 1961 American comedy film directed, co-written and starring Jerry Lewis.

Will the Real Jerry Lewis Please Sit Down: Will the Real Jerry Lewis Please Sit Down is a 1970 animated showcase for various caricatured Jerry Lewis characters, all based on characters from the Lewis film, "The Family Jewels" and styled in a fashion similar to "Archie's TV Funnies" and the "Groovie Goolies".  The title is a variant of the deciding question on the game show "To Tell the Truth": "Will the real __________ please stand up?" .  Like most 1970s-era Saturday morning cartoon series, "Will the Real Jerry Lewis Please Sit Down" contained an adult laugh track.

The Day the Clown Cried: The Day the Clown Cried is an unreleased 1972 American drama film directed by and starring Jerry Lewis.  It is based on a script of the same name by Joan O'Brien, who had co-written the original script with Charles Denton ten years previously.  The film was met with controversy regarding its premise and content, which features a circus clown who is imprisoned in a Nazi concentration camp.  Lewis repeatedly insisted that "The Day the Clown Cried" would never be released because it is an embarrassingly "bad work" of which he was ashamed.  Despite claims the film will never be screened, Lewis reportedly donated a copy of the film to the Library of Congress in 2015, under the stipulation that it wouldn't be screened before June 2024.

Question: What was the television series That's my boy based on starring Jerry Lewis? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "based_on_type": {
      "type": "string",
      "description": "The type of media the series was based on (e.g., film, play)."
    },
    "based_on_title": {
      "type": "string",
      "description": "The title of the work the series was based on."
    },
    "based_on_year": {
      "type": "integer",
      "description": "The release year of the work the series was based on."
    },
    "starring_actors_in_original": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of actors who starred in the original work."
    },
    "jerry_lewis_starred_in_original": {
      "type": "boolean",
      "description": "Indicates if Jerry Lewis starred in the original work."
    }
  },
  "required": [
    "tv_series_name",
    "based_on_type",
    "based_on_title",
    "based_on_year",
    "starring_actors_in_original",
    "jerry_lewis_starred_in_original"
  ],
  "additionalProperties": false
}
