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
Antoine Fuqua: Antoine Fuqua (born January 19, 1966) is an American film director and producer.  Initially active as a music video director, he has worked primarily in the action and thriller film subgenres, and is best known for his 2001 Academy Award-winning film "Training Day".

The Equalizer (film): The Equalizer is a 2014 American neo-noir vigilante action thriller film directed by Antoine Fuqua and written by Richard Wenk, nominally based on the television series of the same name.  It stars Denzel Washington, Marton Csokas, Chloë Grace Moretz, David Harbour, Bill Pullman and Melissa Leo.

Moon (film): Moon is a 2009 British science fiction drama film co-written and directed by Duncan Jones.  The film follows Sam Bell (Sam Rockwell), a man who experiences a personal crisis as he nears the end of a three-year solitary stint mining helium-3 on the far side of the Moon.  It was the feature debut of director Duncan Jones.  Kevin Spacey voices Sam's robot companion, GERTY.  "Moon" premiered at the 2009 Sundance Film Festival and was released in selected cinemas in New York and Los Angeles on 12 June 2009.  The release was expanded to additional theatres in the United States and Toronto on both 3 and 10 July and to the United Kingdom on 17 July.

Training Day: Training Day is a 2001 American neo-noir crime thriller film directed by Antoine Fuqua, and written by David Ayer.  Denzel Washington and Ethan Hawke star as two LAPD narcotics officers over a 24-hour period in the gang-ridden neighborhoods of the LAPD Rampart Division and South Central Los Angeles.

Brooklyn's Finest: Brooklyn's Finest is a 2009 American crime film directed by Antoine Fuqua and written by Michael C. Martin.  The film stars Richard Gere, Don Cheadle, Ethan Hawke and Wesley Snipes.  The film was released on January 16, 2009.  The film takes place within the notoriously rough Brownsville section of Brooklyn and especially within the Van Dyke housing projects in the NYPD's (fictional) 65th precinct.  The action revolves around three policemen whose relationships to their jobs are drastically different.

Dawn Lambertsen Kelly: Dawn Lambertsen Kelly, aka Dawn Kelly, is an American television writer and writer's assistant.  She wrote an episode of the second series of Lost, and was also a writer's assistant on the show.  The "Lost" writing staff were nominated for the Writers Guild of America (WGA) Award for Best Dramatic Series at the February 2007 ceremony for their work on the second and third seasons.  She has also been a writer's assistant for Antoine Fuqua, and has collaborated with him on four of his films.

Duncan Jones: Duncan Zowie Jones ( ; born 30 May 1971) is an English film director, film producer, and screenwriter.  He is best known for directing the science fiction film "Moon" (2009), winning the BAFTA Award for Outstanding Debut by a British Writer, Director or Producer, "Source Code" (2011) and "Warcraft" (2016).  He is the son of late English singer David Bowie and American model Angie Bowie.

London Has Fallen: London Has Fallen is a 2016 American action thriller film directed by Babak Najafi and written by Creighton Rothenberger, Katrin Benedikt, Chad St. John and Christian Gudegast.  It is a sequel to Antoine Fuqua's 2013 film "Olympus Has Fallen" and stars Gerard Butler, Aaron Eckhart and Morgan Freeman, with Alon Moni Aboutboul, Angela Bassett, Robert Forster, Jackie Earle Haley, Melissa Leo, Radha Mitchell, Sean O'Bryan, Waleed Zuaiter and Charlotte Riley in supporting roles.  It is the second installment in the "Has Fallen" film series.

The Replacement Killers: The Replacement Killers is a 1998 American action film directed by Antoine Fuqua in his feature film directorial debut, and starring Chow Yun-fat, Mira Sorvino, Michael Rooker and Kenneth Tsang.  The film was released in the United States on February 6, 1998.  The storyline was conceived from a screenplay written by Ken Sanzel.  Veteran action director John Woo co-produced and choreographed the action sequences.  The film is set in modern-day Los Angeles and follows an emotionally disillusioned assassin who is forced to settle a violent vendetta for a ruthless crime boss.  The film marks the American acting debut for Chow, as his previous film credits included Hong Kong action cinema only.

After Dark (comics): After Dark is a three-issue, dark science fiction limited series published by Radical Comics in a 56-page graphic novella format.  The series concept and characters were created by film director/writer Antoine Fuqua (director of Training Day) and actor Wesley Snipes (star of the Blade series).  The series is written by Peter Milligan (best known for Marvel Comics's X-Statix series) and illustrated by Jeff Nentrup.

Question: Antoine Fuqua and Duncan Jones both have what job?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "shared_job_titles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Job titles that both Antoine Fuqua and Duncan Jones share."
    },
    "individuals_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "all_job_titles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All job titles associated with the individual as per the context."
          }
        },
        "required": [
          "name",
          "all_job_titles"
        ],
        "additionalProperties": false
      },
      "description": "Details for each individual mentioned, including all their job titles."
    },
    "number_of_shared_job_titles": {
      "type": "integer",
      "description": "The count of job titles shared by both individuals."
    }
  },
  "required": [
    "shared_job_titles",
    "individuals_details",
    "number_of_shared_job_titles"
  ],
  "additionalProperties": false
}
