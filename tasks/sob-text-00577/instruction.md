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
Eric Cartman: Eric Theodore Cartman, often referred to as just Cartman, is a main character in the animated television series "South Park", created by Matt Stone and Trey Parker, and voiced by Trey Parker.  Cartman, generally referred to by his surname, is one of four central characters in "South Park", along with his friends Stan Marsh, Kyle Broflovski, and Kenny McCormick.  Cartman first appeared, originally named Kenny, in prototypical form in a 1992 animated short "Jesus vs. Frosty", and a 1995 animated short "Jesus vs. Santa", and first appeared on television in the pilot episode of "South Park", "Cartman Gets an Anal Probe", on August 13, 1997.

Cartman's Incredible Gift: "Cartman's Incredible Gift" is episode 124 of the Comedy Central series "South Park".  It originally aired December 8, 2004 as part of the series' eighth season.  In the episode, local police become convinced that Eric Cartman has psychic abilities, which Cartman exploits for personal gain, much to the ire of Kyle Broflovski, other psychic detectives, and the true serial killer behind a series of murders that Cartman falsely attributes to others.

Dances with Smurfs: "Dances with Smurfs" is the thirteenth episode of the thirteenth season of the American animated television series "South Park".  The 194th overall episode of the series, it originally aired on Comedy Central in the United States on November 11, 2009.  In the episode, Eric Cartman becomes the reader of the elementary school announcements, and starts making politically charged accusations against student body president Wendy Testaburger The episode was written and directed by series co-creator Trey Parker, and was rated TV-MA L in the United States and M (as) in Australia.

Cat Orgy: "Cat Orgy" is the seventh episode of the third season of the American animated sitcom "South Park", and the 38th episode of the series overall.  It originally aired on Comedy Central on July 14, 1999.  It is the first episode of a three-part story arc, often known as "The Meteor Shower Trilogy", which tells three different stories all taking place on the same night.  The other two episodes are "Two Guys Naked in a Hot Tub" and "Jewbilee".  As such, it features only one of the four main characters, Eric Cartman.

Cartman Sucks: "Cartman Sucks" is episode 1102 (#155) of Comedy Central's "South Park" and the second episode of the show's 11th season.  It originally aired on March 14, 2007.  The main plot deals with Eric Cartman's efforts to recover an incriminating photograph that may call his sexual orientation into question, whereas the subplot, which focuses on Butters Stotch, explores childhood gay conversion therapy.

Cartman Gets an Anal Probe: "Cartman Gets an Anal Probe" is the first episode of the American animated television series "South Park".  It first aired on Comedy Central in the United States on August 13, 1997.  The episode introduces child protagonists Eric Cartman, Kyle Broflovski, Stan Marsh and Kenny McCormick, who attempt to rescue Kyle's younger brother Ike from being abducted by aliens.

Cartman's Mom Is a Dirty Slut: "Cartman's Mom Is a Dirty Slut" is the first season finale of the American animated television series "South Park".  It originally aired on Comedy Central in the United States on February 25, 1998.  The episode is the highest viewed episode in the entire "South Park" series, with 6.4 million views.  It is part one of a two-episode story arc, which concluded with "Cartman's Mom Is Still a Dirty Slut".  The episode follows Eric Cartman, one of the show's child protagonists, becoming curious about the identity of his father.  He discovers that his father is most likely a man his mother had sexual intercourse with during an annual party called "The Drunken Barn Dance".  Meanwhile, his friends Stan, Kyle and Kenny participate on "America's Stupidest Home Videos", after filming Cartman playing in his yard with plush toys.

The Death of Eric Cartman: "The Death of Eric Cartman" is the sixth episode in the ninth season of the American animated television series "South Park".  The 131st episode overall, it originally aired on Comedy Central in the United States on April 13, 2005.  In the episode, the other boys begin ignoring Cartman, leading to him concluding that he must be a ghost.

Eek, a Penis!: "Eek, a Penis!"  is the fifth episode in the twelfth season of the American animated series "South Park".  The 172nd episode of the series overall, it originally aired on Comedy Central in the United States on April 9, 2008.  In the episode, Mrs. Garrison seeks to become a man again through the help of a new medical procedure, and Cartman helps teach struggling inner-city school children how to succeed by cheating.  This episode is a parody of the 1988 film "Stand and Deliver", with Eric Cartman playing a role similar to that of Edward James Olmos's character.

201 (South Park): "201" is the sixth episode of the fourteenth season of "South Park", and the 201st overall episode of the series.  It originally aired on Comedy Central in the United States on April 21, 2010.  The episode continued multiple storylines from the previous episode, "200", in which a group of angry celebrities demand South Park produce the Muslim prophet Muhammad.  In "201", a superhero-like group of religious figures team up to save South Park from the celebrities and their monster Mecha-Streisand, while Eric Cartman learns the true identity of his father.

Question: The pilot episode that starred a character named Eric Cartman, aired in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character featured in the pilot episode."
    },
    "episode_title": {
      "type": "string",
      "description": "The title of the pilot episode."
    },
    "air_year": {
      "type": "integer",
      "description": "The year the pilot episode originally aired."
    }
  },
  "required": [
    "character_name",
    "episode_title",
    "air_year"
  ],
  "additionalProperties": false
}
