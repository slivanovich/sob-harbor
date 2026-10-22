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
Raw Nerve (company): Raw Nerve is a film production company.  Members of Raw Nerve include Eli Roth, Scott Spiegel, and Boaz Yakin.

Now You See Me (film): Now You See Me is a 2013 American heist thriller film directed by Louis Leterrier and written by Ed Solomon, Boaz Yakin and Edward Ricourt.  The film features an ensemble cast of Jesse Eisenberg, Mark Ruffalo, Woody Harrelson, Mélanie Laurent, Isla Fisher, Dave Franco, Michael Caine, and Morgan Freeman.  The plot follows an FBI agent and an Interpol detective who track a team of illusionists who pull off bank heists during their performances and reward their audiences with the money.  This is the first installment of the series.

Hostel (2005 film): Hostel is a 2005 American horror film written and directed by Eli Roth.  It stars Jay Hernandez and was produced by Mike Fleiss, Eli Roth, and Chris Briggs; Boaz Yakin, Scott Spiegel, and Quentin Tarantino are executive producers.  It is the first installment of the "Hostel" trilogy, followed by "" (2007) and "" (2011).  The film tells the story of two college students traveling across Europe, who find themselves preyed upon by a mysterious group that tortures and kills kidnapped victims.

Prince of Persia: The Sands of Time (film): Prince of Persia: The Sands of Time is a 2010 American action fantasy film directed by Mike Newell.  The film was written by Jordan Mechner, Boaz Yakin, Doug Miro, and Carlo Bernard, produced by Jerry Bruckheimer, and released by Walt Disney Pictures on May 28, 2010.  The film stars Jake Gyllenhaal as Prince Dastan, Gemma Arterton as Princess Tamina, Ben Kingsley as Nizam, and Alfred Molina as Sheik Amar.  The film has the same title as the video game "", and is primarily based on it.  Elements from "" and "", the two other titles from the "Sands of Time" trilogy of the "Prince of Persia" video game franchise, are also incorporated.  The film was premiered in London on May 5, 2010 and was officially released on May 28, 2010 in the United States.  It received mixed reviews from critics, and grossed over $336 million against a production budget of $150–200 million.

Uptown Girls: Uptown Girls is a 2003 comedy-drama film directed by Boaz Yakin, who was working from a screenplay which Julia Dahl, Mo Ogrodnik and Lisa Davidowitz had adapted from the story by Allison Jacobs.  It stars Brittany Murphy as a 22-year-old living a charmed life as the daughter of a famous rock and roll musician.  Dakota Fanning, Heather Locklear, Marley Shelton, Donald Faison and Jesse Spencer also feature in the film.

Boaz Yakin: Boaz Yakin (born June 20, 1966) is an American screenwriter and film director based in New York City.  He has written such screenplays as "Fresh" and "A Price Above Rubies", and he directed the feature film "Remember the Titans", among others.

Safe (2012 film): Safe is a 2012 American action crime thriller film written and directed by Boaz Yakin and starring Jason Statham, Chris Sarandon, Robert John Burke and James Hong.  Statham plays an ex-cop and former cage fighter who winds up protecting a gifted child who is being chased by the Russian mafia, Chinese Triads, and corrupt New York City police.

Max (2015 film): Max is a 2015 American adventure drama film directed by Boaz Yakin, and co-written with Sheldon Lettich.  The film stars Josh Wiggins, Mia Xitlali, Dejon LaQuake, Thomas Haden Church, Robbie Amell, Lauren Graham, Luke Kleintank, and Jay Hernandez.  The film was released by Warner Bros. on June 26, 2015.

The Rookie (1990 film): The Rookie is a 1990 American buddy cop film directed by Clint Eastwood and produced by Howard G. Kazanjian, Steven Siebert and David Valdes.  It was written from a screenplay conceived by Boaz Yakin and Scott Spiegel.  The film stars Charlie Sheen, Clint Eastwood, Raúl Juliá, Sônia Braga, Lara Flynn Boyle, and Tom Skerritt.  Eastwood plays a veteran police officer teamed up with a younger detective played by Sheen ("the rookie"), whose intent is to take down a German crime lord in downtown Los Angeles following months of investigation into an exotic car theft ring.

Jack Hill: Jack Hill (born January 28, 1933) is an American film director in the exploitation film genre.  Several of Hill's later films have been characterized as feminist works.

Question: Who is older, Jack Hill or Boaz Yakin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "older_person_name": {
      "type": "string",
      "description": "The name of the person who is older."
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in years between the two people's birth years."
    }
  },
  "required": [
    "person_1",
    "person_2",
    "older_person_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
