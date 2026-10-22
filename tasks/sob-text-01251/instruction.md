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
Buckaroo Bugs: Buckaroo Bugs is a Warner Bros. "Looney Tunes" theatrical cartoon short released in August 1944, directed by Robert Clampett.  It was the last "Looney Tunes" cartoon to be produced by Leon Schlesinger.  It was also the first "Looney Tunes" cartoon to star Bugs Bunny.

Little Orphan Annie: Little Orphan Annie is a daily American comic strip created by Harold Gray and syndicated by the Tribune Media Services.  The strip took its name from the 1885 poem "Little Orphant Annie" by James Whitcomb Riley, and made its debut on August 5, 1924, in the New York "Daily News".

Looney Tunes: Rabbits Run: Looney Tunes: Rabbits Run is a 2015 American animated direct-to-video film based on "The Looney Tunes Show", produced by Warner Bros.  Animation.  It is the first new "Looney Tunes" direct-to-video film in nine years since "Bah, Humduck!  A Looney Tunes Christmas".  The film was directed by Jeff Siergey, a supervising animator on "Space Jam" and lead animator on "".  He was also a director on "The Looney Tunes Show".  It was released on August 4, 2015 by Warner Home Video, but it was released early on July 7, 2015 on Vudu and Walmart.

Punch Trunk: Punch Trunk is a 1953 Looney Tunes cartoon written by Mike Maltese and directed by Chuck Jones.  It is a one-shot cartoon (that is, not featuring a regular character from the Looney Tunes series) about a miniature elephant who inadvertently terrorizes a city.

List of unreleased Warner Bros. animated shorts: Following is the list of the "Looney Tunes" and "Tom and Jerry" animated short subjects proposed by either Warner Bros.  Cartoon studio in the 1930s-1960s or Warner Bros.  Animation in the 2000s.  In 1945, Bob Clampett planned to direct a Looney Tunes cartoon that would fictionalize the life of Franklin D. Roosevelt as a dog but when Roosevelt died the project was abandoned.  In the 1950s, Friz Freleng pondered the idea of a one-shot cartoon that would combine Marilyn Monroe's life with the fairytale of Snow White but this project was also shelved when it was deemed too similar to Monroe's own personal life.  Not all abandoned Looney Tunes shorts were one-shots as Looney Tunes comprises several sub-series such as Bugs Bunny, Pepé Le Pew and the Road Runner, to name few.  It is no surprise that not all planned sub-series didn't get off the ground, and many of them ended up either not being produced at all or being reworked into one-shots.  Some of these sub-series were Keystone Kops, Rapid Rabbit and Quick Brown Fox, Corn Plastered, The Eager Beaver, Canyon Kiddies, etc.  None of these went so far as to have individual titles mapped out.

Carrotblanca: Carrotblanca is a 1995 8-minute Looney Tunes cartoon.  It was originally shown in theaters alongside "The Amazing Panda Adventure" (in the US) and "The Pebble and the Penguin" (internationally).  It was subsequently released on video packaged with older "Looney Tunes" cartoons and was included in the special edition DVD, and later HD DVD and Blu-ray, releases of "Casablanca", the film to which it is both a parody and an homage.  At the time of release, WB did not own the rights to "Casablanca" (such rights were with Turner Entertainment - they still technically hold the film today, but WB became responsible for distribution a year after the short's release as a result of their parent company's purchase of Turner in 1996).

The Hole Idea: The Hole Idea is a 1955 Looney Tunes cartoon directed by Robert McKimson.  It was the last cartoon about black-and-white sequences.  He was also the sole animator on the short, as this was during the time he was re-assembling his unit after the brief 1953 shutdown of Warner Bros.  Animation.  It was a "one shot" short; that is not starring a regular Looney Tunes character.

Little Orphan Airedale: Little Orphan Airedale is a Warner Bros. "Looney Tunes" cartoon directed by Charles M. Jones and released on October 4, 1947.  It was later reissued as a Blue Ribbon Merrie Melodies short.  Its major significance is its status as the debut of Jones's character Charlie Dog.  The title is a play on "Little Orphan Annie".

Quacker Tracker: Quacker Tracker is a 1967 Looney Tunes cartoon, starring Daffy Duck and Speedy Gonzales.  It was the first of three "buffer cartoons" produced by Format Films in between Warner Bros. ending its contract with previous Looney Tunes producers DePatie-Freleng Enterprises and re-establishing its own cartoon studio.

Speedy Ghost to Town: "Speedy Ghost to Town" is a Merrie Melodies 1967 animated short starring Daffy Duck and Speedy Gonzales.  It is the first cartoon released under the newly reopened Warner Bros.  Animation department, as from 1963 to 1967, all Looney Tunes cartoons were developed at DePatie-Freleng Enterprises and Format Films instead.  It is also the first Looney Tunes cartoon to be directed by Alex Lovy.

Question: Who directed the Looney Tunes cartoon with the title based on the Harold Grey comic strip?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cartoon_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the Looney Tunes cartoon."
        },
        "director": {
          "type": "string",
          "description": "The director of the cartoon."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the cartoon."
        },
        "significance": {
          "type": "string",
          "description": "A notable significance or debut associated with the cartoon."
        }
      },
      "required": [
        "title",
        "director",
        "release_date",
        "significance"
      ],
      "additionalProperties": false
    },
    "title_inspiration": {
      "type": "object",
      "properties": {
        "source_work_title": {
          "type": "string",
          "description": "The title of the work that inspired the cartoon's title."
        },
        "source_work_type": {
          "type": "string",
          "description": "The type of the source work (e.g., comic strip, poem)."
        },
        "source_work_creator": {
          "type": "string",
          "description": "The creator of the source work."
        }
      },
      "required": [
        "source_work_title",
        "source_work_type",
        "source_work_creator"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the director of the identified cartoon."
    }
  },
  "required": [
    "cartoon_details",
    "title_inspiration",
    "final_answer"
  ],
  "additionalProperties": false
}
