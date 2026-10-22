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
Thor: The Dark World: Thor: The Dark World is a 2013 American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the sequel to 2011's "Thor" and the eighth film in the Marvel Cinematic Universe.  The film was directed by Alan Taylor, with a screenplay by Christopher Yost and Christopher Markus & Stephen McFeely.  It stars Chris Hemsworth, Natalie Portman, Tom Hiddleston, Anthony Hopkins, Stellan Skarsgård, Idris Elba, Christopher Eccleston, Adewale Akinnuoye-Agbaje, Kat Dennings, Ray Stevenson, Zachary Levi, Tadanobu Asano, Jaimie Alexander, and Rene Russo.  In "Thor: The Dark World", Thor teams up with Loki to save the Nine Realms from the Dark Elves led by the vengeful Malekith, who intends to plunge the universe into darkness.

Captain America: The Winter Soldier: Captain America: The Winter Soldier is a 2014 American superhero film based on the Marvel Comics character Captain America, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the sequel to 2011's "" and the ninth film in the Marvel Cinematic Universe (MCU).  The film was directed by Anthony and Joe Russo, with a screenplay by Christopher Markus & Stephen McFeely, who had also written "The First Avenger".  It stars Chris Evans as Captain America, leading an ensemble cast that includes Scarlett Johansson, Sebastian Stan, Anthony Mackie, Cobie Smulders, Frank Grillo, Emily VanCamp, Hayley Atwell, Robert Redford, and Samuel L. Jackson.  In "Captain America: The Winter Soldier", Captain America, Black Widow, and Falcon join forces to uncover a conspiracy within S.H.I.E.L.D. while facing a mysterious assassin known as the Winter Soldier.

Guardians of the Galaxy (film): Guardians of the Galaxy (retroactively referred to as Guardians of the Galaxy Vol.  1) is a 2014 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the tenth film in the Marvel Cinematic Universe.  The film was directed by James Gunn, who wrote the screenplay with Nicole Perlman, and features an ensemble cast including Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel, Bradley Cooper, Lee Pace, Michael Rooker, Karen Gillan, Djimon Hounsou, John C. Reilly, Glenn Close, and Benicio del Toro.  In "Guardians of the Galaxy", Peter Quill forms an uneasy alliance with a group of extraterrestrial misfits who are fleeing after stealing a powerful artifact.

Doctor Strange (2016 film): Doctor Strange is a 2016 American superhero film based on the Marvel Comics character of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the fourteenth film of the Marvel Cinematic Universe (MCU).  The film was directed by Scott Derrickson, who wrote it with Jon Spaihts and C. Robert Cargill, and stars Benedict Cumberbatch as Stephen Strange, along with Chiwetel Ejiofor, Rachel McAdams, Benedict Wong, Michael Stuhlbarg, Benjamin Bratt, Scott Adkins, Mads Mikkelsen, and Tilda Swinton.  In "Doctor Strange", surgeon Strange learns the mystic arts after a career-ending car accident.

Michael Stuhlbarg: Michael Stuhlbarg ( ; born July 5, 1968) is an American actor.  He played troubled university professor Larry Gopnik in the 2009 dark comedy film "A Serious Man", organized-crime boss Arnold Rothstein in the HBO television series "Boardwalk Empire" (2010–2013), René Tabard in "Hugo" (2011), Griffin in "Men in Black 3" (2012), Dr. Flicker in "Blue Jasmine" (2013), Edward G. Robinson in "Trumbo" (2015), computer scientist and inventor Andy Hertzfeld in the biopic "Steve Jobs" (2015), and Nicodemus West in superhero film "Doctor Strange" (2016).

The Avengers (2012 film): Marvel's The Avengers (classified under the name Marvel Avengers Assemble in the United Kingdom and Ireland), or simply The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the sixth film in the Marvel Cinematic Universe.  The film was written and directed by Joss Whedon and features an ensemble cast that includes Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Tom Hiddleston, Clark Gregg, Cobie Smulders, Stellan Skarsgård, and Samuel L. Jackson.  In the film, Nick Fury, director of the peacekeeping organization S.H.I.E.L.D., recruits Iron Man, Captain America, the Hulk, and Thor to form a team that must stop Thor's brother Loki from subjugating Earth.

Iron Man 3: Iron Man 3 (stylized onscreen as Iron Man Three) is a 2013 American superhero film based on the Marvel Comics character Iron Man, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the sequel to 2008's "Iron Man" and 2010's "Iron Man 2", and the seventh film in the Marvel Cinematic Universe.  Shane Black directed a screenplay he co-wrote with Drew Pearce, which uses concepts from the "Extremis" story arc by Warren Ellis.  The film stars Robert Downey Jr., Gwyneth Paltrow, Don Cheadle, Guy Pearce, Rebecca Hall, Stephanie Szostak, James Badge Dale, Jon Favreau, and Ben Kingsley.  In "Iron Man 3", Tony Stark deals with posttraumatic stress disorder caused by the events of "The Avengers", while investigating the reemergence of the Ten Rings, led by the mysterious Mandarin and comes into a conflict with an old enemy: Aldrich Killian.

Black Panther (film): Black Panther is an upcoming American superhero film based on the Marvel Comics character of the same name.  Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is intended to be the eighteenth film installment of the Marvel Cinematic Universe.  The film is directed by Ryan Coogler from a screenplay by him and Joe Robert Cole, and stars Chadwick Boseman as T'Challa / Black Panther alongside Michael B. Jordan, Lupita Nyong'o, Danai Gurira, Martin Freeman, Daniel Kaluuya, Angela Bassett, Forest Whitaker, and Andy Serkis.  In "Black Panther", T'Challa returns home as king of Wakanda but finds his sovereignty challenged by a long-time adversary in a conflict that has global consequences.

Captain America: Civil War: Captain America: Civil War is a 2016 American superhero film based on the Marvel Comics character Captain America, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the sequel to 2011's "" and 2014's "", and the thirteenth film of the Marvel Cinematic Universe (MCU).  The film is directed by Anthony and Joe Russo, with a screenplay by Christopher Markus & Stephen McFeely, and features an ensemble cast, including Chris Evans, Robert Downey Jr., Scarlett Johansson, Sebastian Stan, Anthony Mackie, Don Cheadle, Jeremy Renner, Chadwick Boseman, Paul Bettany, Elizabeth Olsen, Paul Rudd, Emily VanCamp, Tom Holland, Frank Grillo, William Hurt, and Daniel Brühl.  In "Captain America: Civil War", disagreement over international oversight of the Avengers fractures them into opposing factions—one led by Steve Rogers and the other by Tony Stark.

Thor: Ragnarok: Thor: Ragnarok is an upcoming American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is intended to be the sequel to 2011's "Thor" and 2013's "" and the seventeenth film installment of the Marvel Cinematic Universe (MCU).  The film is directed by Taika Waititi with a screenplay by Eric Pearson and the writing team of Craig Kyle and Christopher Yost, and stars Chris Hemsworth, Tom Hiddleston, Cate Blanchett, Idris Elba, Jeff Goldblum, Tessa Thompson, Karl Urban, Mark Ruffalo, and Anthony Hopkins.  In "Thor: Ragnarok", Thor must defeat the Hulk in a gladiatorial duel in time to save Asgard from Hela and the coming Ragnarök.

Question: Michael Stuhlbarg ( born July 5, 1968) is an American actor, he played Nicodemus West in Doctor Strange, a 2016 American superhero film based on the Marvel Comics character of the same name, produced by which organization, and distributed by Walt Disney Studios Motion Pictures?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_type": {
      "type": "string",
      "description": "The genre or type of the film."
    },
    "producer": {
      "type": "string",
      "description": "The studio or organization that produced the film."
    },
    "distributor": {
      "type": "string",
      "description": "The studio or organization that distributed the film."
    },
    "actor_information": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "character_played": {
          "type": "string",
          "description": "The name of the character played by the actor in the film."
        }
      },
      "required": [
        "actor_name",
        "character_played"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_type",
    "producer",
    "distributor",
    "actor_information"
  ],
  "additionalProperties": false
}
