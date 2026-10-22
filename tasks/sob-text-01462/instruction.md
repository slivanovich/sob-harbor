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
The Nightmare Before Christmas: The Nightmare Before Christmas (also known as Tim Burton's The Nightmare Before Christmas) is a 1993 American stop-motion animated musical dark fantasy film directed by Henry Selick, and produced and conceived by Tim Burton.  It tells the story of Jack Skellington, a resident from "Halloween Town" who stumbles through a portal to "Christmas Town" and decides to celebrate the holiday, with some dastardly and comical consequences.  Danny Elfman wrote the songs and score, and provided the singing voice of Jack.  The principal voice cast also includes Chris Sarandon, Catherine O'Hara, William Hickey, Ken Page, Paul Reubens and Glenn Shadix.

Tramway (film): Tramway (Polish: "Tramwaj" ) is a 1966 short silent film by Polish director Krzysztof Kieślowski, produced while he was a student at the Łódź Film School.  The film is included as an extra feature on the American and Artificial Eye Region 2 DVD releases of Kieslowski's "A Short Film About Love".

Rings (2005 film): Rings is a 2005 American horror short film.  It was initially released as an extra disc with a re-release of "The Ring" on DVD.  The events in "Rings" lead up to the sequel "The Ring Two", on whose DVD "Rings" is also included as a bonus feature.

One by One (film): One by One is a traditionally animated short film directed by Pixote Hunt and released by Walt Disney Pictures on August 31, 2004, as an extra feature on the DVD release of "" Special Edition.  The short was intended to be one of the segments for the proposed but never completed "Fantasia 2006".

Vincent (1982 film): Vincent is a 1982 stop motion short horror film written, designed and directed by Tim Burton, and produced by Rick Heinrichs.  It is the second Disney horror film, the first being "The Watcher in the Woods".  At approximately six minutes in length, there is currently no individual release of the film except for a few bootleg releases.  It can be found on the 2008 Special Edition and Collector's Edition DVDs of "The Nightmare Before Christmas" as a bonus feature and on the Cinema16 DVD "".

Oh Lucy! (2014 film): Oh Lucy!  is a short film directed by Atsuko Hirayanagi.  The short film made its world premiere at the 2014 Cannes Film Festival receiving 2nd place in the Cinéfondation.  Oh Lucy!  has since become Academy Qualified by winning the Best International Short Film Award at the 2015 Flickerfest as well as the Short Film Jury Award: International Fiction at the 2015 Sundance Film Festival.  The short film is the basis of an upcoming eponymous film adaption, also directed by Hirayanagi.

Lorenzo (film): Lorenzo is a 2004 American animated short film produced by Walt Disney Feature Animation about a cat, Lorenzo, who is "dismayed to discover that his tail has developed a personality of its own."  The short was directed by Mike Gabriel and produced by Baker Bloodworth.  It premiered at the Florida Film Festival on March 6, 2004, and later appeared as a feature before the film "Raising Helen"; however, it did not appear on the DVD release of the film.  It is based on an original idea by Joe Grant, who started working on the film in 1949, but it was eventually shelved.  It was later found along with "Destino".  The short intended to be one of the segments for the proposed but never completed "Fantasia 2006".  It was included on the "Walt Disney Animation Studios Short Films Collection" Blu-ray/DVD set released on August 18, 2015.

Eva Burrows: General Eva Evelyn Burrows, AC, OF (15 September 192920 March 2015) was an Australian Salvation Army Officer and was, from 1986 to 1993, the 13th General of the Salvation Army.  She served as an Officer of the Salvation Army from 1951 to her retirement in 1993.  In 1993 Henry Gariepy released her biography, "General of God's Army the Authorized Biography of General Eva Burrows".

Noah's Arc: The Short Film: Noah's Arc: The Short Film is a 2004 short film written, directed and produced by Patrik-Ian Polk.  The film became the foundation of the LOGO television series "Noah's Arc".  The cast features Darryl Stephens, Rodney Chester, Christian Vincent, Doug Spearman, Jensen Atwood, Jonathan Julian and Carlos Tinoco.  All cast members of the short film eventually starred in the television series except for Tinoco.

George &amp; A.J.: George & A.J. is a short film created by Pixar which uses characters from the film "Up" to tell what Nurses George and A.J. did after Carl Fredricksen left with his house tied to balloons in the feature film.  Instead of being released on DVD like "Partly Cloudy", "Dug's Special Mission", or any other Pixar short film, "George & A.J." was initially released on iTunes as an extra feature that came with a purchase of the film.  It was later released to fans of Disney/Pixar on their Facebook page and later to the official Disney/Pixar YouTube page.  It was later released on "Pixar Short Films Collection Volume 2".  All of the animation is done in a limited "storyboard" style, with some objects moving by keyframes, while other things like characters and their mouths barely move at all; however, the characters' expressions and the story are still conveyed.

Question: Vincent is a short film that can be found as an extra on which 1993 Henry Selick-directed DVD?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "feature_film_title": {
      "type": "string",
      "description": "The title of the main feature film on the DVD."
    },
    "feature_film_release_year": {
      "type": "integer",
      "description": "The release year of the main feature film."
    },
    "feature_film_director": {
      "type": "string",
      "description": "The director of the main feature film."
    },
    "short_film_title": {
      "type": "string",
      "description": "The title of the short film found as an extra feature."
    },
    "is_bonus_feature": {
      "type": "boolean",
      "description": "Indicates if the short film is included as a bonus feature on the DVD."
    }
  },
  "required": [
    "feature_film_title",
    "feature_film_release_year",
    "feature_film_director",
    "short_film_title",
    "is_bonus_feature"
  ],
  "additionalProperties": false
}
