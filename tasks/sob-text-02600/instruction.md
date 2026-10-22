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
Michael's Birthday: "Michael's Birthday" is the nineteenth episode of the second season of the American comedy television series "The Office", and the show's twenty-fifth episode overall.  Written by Gene Stupnitsky and Lee Eisenberg, and directed by Ken Whittingham, the episode first aired in the United States on March 30, 2006 on NBC.  The episode guest stars Nancy Walls as Carol Stills.

Lust Control: Lust Control is a Christian thrash punk band, originally formed in 1988.  They are known for their explicit lyrical content, which is devoted to matters of sexual purity and sin, including abstinence, masturbation, pornography, sex ed, and related topics.  For their unwavering views on sexual purity, "CCM" magazine has called Lust Control as "the Josh McDowell of the Christian rock world."  Musically they have been likened to The Ramones or The Dead Milkmen.  The band formed as a joke and was not meant for long term exposure, which has led some to refer to it as a Christian version of Spinal Tap.  Lust Control received the title of "The Worst Christian Band of the Decade" for the 1990s from "HM".

Office Olympics: "Office Olympics" is the third episode of the second season of the television series "The Office", and the show's ninth episode overall.  It was written by Michael Schur and directed by Paul Feig.  It originally aired on October 5, 2005 on NBC.  The episode guest starred Nancy Carell, the real-life wife of series star Steve Carell, as Carol Stills.

Sex Ed: The Series: Sex Ed the Series is an American comedy web series created and written by Ernie Vecchione and produced and directed by Tamela D'Amico.  It was originally conceived as a television pilot in 2009 and was later made into a five-part web series on the official Sex Ed website.

Sex Ed (disambiguation): Sex Ed is the process of educating people about sex.

Sex Ed (film): Sex Ed is a 2014 American comedy film directed by Isaac Feder and written by Bill Kennedy.  The film stars Haley Joel Osment, Lorenza Izzo, Laura Harring, Abby Elliott, Glen Powell, Retta, and Matt Walsh.  "Sex Ed" premiered at the Portland Film Festival on August 29, 2014, and was released in theaters on November 7, 2014, by MarVista Entertainment.

Stephanie Mitelman: Stephanie Mitelman Bercovitch (February 25, 1976-) is a Sex Education and Family Life Education professor, public speaker, entrepreneur, sex educator, and author specializing in special education, particularly for youth with autism spectrum disorders.  She is the owner and creator of Senseez Pillows, a company making vibrating pillows for people with sensory needs, and Sex Ed Mart, a sex education publishing and distribution company specializing in sex education for youth with special needs.  Stephanie also runs a private sex education practice for youth on the autism spectrum, their parents, and couples who are neurologically diverse.

Nancy Carell: Nancy Ellen Carell (née Walls; born July 19, 1966) is an American actress, comedian, and writer best known for her work on "Saturday Night Live", "The Daily Show", and "The Office".  She is the wife of actor-comedian Steve Carell.  The couple are creators of the TBS comedy series "Angie Tribeca".

Casino Night: "Casino Night" is the second season finale of the American comedy television series "The Office", and the twenty-eighth episode overall.  Written by Steve Carell, who also acts in the show as Michael Scott, and directed by Ken Kwapis, the episode originally aired in the United States on May 11, 2006 on NBC.  The episode guest stars Nancy Carell as Carol Stills and Melora Hardin as Jan Levinson.

Sex Ed (The Office): "Sex Ed" is the fourth episode of the seventh season of the American comedy television series "The Office", and the show's 130th episode overall.  Written and directed by Paul Lieberstein, the episode aired on NBC in the United States on October 14, 2010.  The episode features the return of several recurring characters, most notably Melora Hardin as Jan Levinson, Linda Purl as Helene Beesly, and Nancy Carell as Carol Stills.  Actresses Amy Pietz and Amy Ryan—who portray Donna and Holly Flax—only make vocal cameos.

Question: Who is the husband of the actress that plays Carol Stills in the "Sex Ed" episode of "The Office"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_details": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the television series."
        },
        "episode_title": {
          "type": "string",
          "description": "The title of the specific episode."
        }
      },
      "required": [
        "series_name",
        "episode_title"
      ],
      "additionalProperties": false
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character in the episode."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "actress_name": {
          "type": "string",
          "description": "The name of the actress playing the character."
        },
        "husband_name": {
          "type": "string",
          "description": "The name of the actress's husband."
        }
      },
      "required": [
        "actress_name",
        "husband_name"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the husband of the actress."
    }
  },
  "required": [
    "episode_details",
    "character_played",
    "actress_details",
    "final_answer"
  ],
  "additionalProperties": false
}
