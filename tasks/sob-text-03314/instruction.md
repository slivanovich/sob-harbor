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
When a Man Falls in the Forest: When A Man Falls in the Forest is a 2007 American drama film directed by Ryan Eslinger and starring Dylan Baker, Timothy Hutton, Sharon Stone, and Pruitt Taylor Vince.  It premiered in competition at the 2007 Berlin Film Festival where it was nominated for the Golden Bear and later screened at the SXSW Film Festival.

Sunshine State (film): Sunshine State is a 2002 American comedy–drama film written and directed by John Sayles.  The picture stars an ensemble cast that features Angela Bassett, Edie Falco, Jane Alexander, Alan King, Timothy Hutton, Mary Steenburgen, Bill Cobbs, and others.  The movie was filmed on Amelia Island, Florida, which includes settings in historic Fernandina Beach.  Amelia Island is located 30 or so miles north of Jacksonville.

The Falcon and the Snowman: The Falcon and the Snowman is a 1985 American spy drama film directed by John Schlesinger.  The screenplay by Steven Zaillian is based on the 1979 book "The Falcon and the Snowman: A True Story of Friendship and Espionage" by Robert Lindsey, and tells the true story of two young American men, Christopher Boyce (Timothy Hutton) and Andrew Daulton Lee (Sean Penn), who sold US security secrets to the Soviet Union.  The film features the song "This Is Not America," written and performed by David Bowie and the Pat Metheny Group.

Q&amp;A (film): Q & A is a 1990 American crime film written and directed by Sidney Lumet, based on a novel by New York State Supreme Court judge Edwin Torres.  It stars Nick Nolte, Timothy Hutton and Armand Assante.

The Long Home: The Long Home is an upcoming indie drama film directed by and starring James Franco, based on the novel of the same name by William Gay.  It also stars Josh Hutcherson, Tim Blake Nelson, Courtney Love, Timothy Hutton, Giancarlo Esposito, Ashton Kutcher, Josh Hartnett, Zoe Levin, Analeigh Tipton, Scott Haze, and Robin Lord Taylor.  The film follows a young contractor who is hired to build a "honky-tonk" in Tennessee by the man who killed his father.

Taps (film): Taps is a 1981 American drama film starring George C. Scott and Timothy Hutton, with Ronny Cox, Tom Cruise, Sean Penn and Evan Handler in supporting roles.  Hutton was nominated for a Golden Globe award in 1982.  The film was directed by Harold Becker from a screenplay by Robert Mark Kamen, James Lineberger, and Darryl Ponicsan, based on Devery Freeman's 1979 novel "Father Sky".  The original music score was composed by Maurice Jarre.

Jim Hutton: Dana James Hutton (May 31, 1934 – June 2, 1979) was an American actor in film and television best remembered for his role as Ellery Queen in the 1970s TV series of the same name and his screen partnership with Paula Prentiss in five films, starting with "Where the Boys Are".  He is the father of actor Timothy Hutton.

Timothy Hutton: Timothy Tarquin Hutton (born August 16, 1960) is an American actor and director.  He is the youngest male actor to win the Academy Award for Best Supporting Actor, which he won at the age of 20 for his performance as Conrad Jarrett in "Ordinary People" (1980).  Hutton has since appeared regularly in feature films and on television, with featured roles in the drama "Taps" (1981), the spy film "The Falcon and the Snowman" (1985), and the horror film "The Dark Half" (1993), among others.

Christopher John Boyce: Christopher John Boyce (born February 16, 1953) is a former American defense industry employee who was convicted for selling US spy satellite secrets to the Soviet Union in the 1970s.

Made in Heaven (1987 film): Made in Heaven is a 1987 fantasy-comedy film directed by Alan Rudolph, script from Bruce A. Evans and Raynold Gideon, and produced by Lorimar Productions.  The film stars Timothy Hutton and Kelly McGillis and has cameos by Tom Petty, Ric Ocasek, Ellen Barkin and Neil Young.  An additional character known only as "Emmett" in the film was played by Debra Winger (Hutton's then wife), who acted as a chain-smoking male angel.

Question: With which state did this American man, portrayed by Timothy Hutton in the film "The Falcon and the Snowman," have dealings with, for which he was later convicted?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the American man portrayed in the film."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who portrayed the American man."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film in which the man was portrayed."
    },
    "entity_dealt_with": {
      "type": "string",
      "description": "The state or entity with which the person had dealings."
    },
    "reason_for_conviction": {
      "type": "string",
      "description": "The reason for which the person was convicted related to these dealings."
    }
  },
  "required": [
    "person_name",
    "actor_name",
    "film_title",
    "entity_dealt_with",
    "reason_for_conviction"
  ],
  "additionalProperties": false
}
