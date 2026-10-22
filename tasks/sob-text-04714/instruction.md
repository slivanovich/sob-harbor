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
James Burke (actor): James Burke (September 24, 1886 – May 23, 1968) was an American film and television actor born in New York City.  He made his stage debut in New York around 1912 and went to Hollywood in 1933.  He made over 200 film appearances during his career, which ranged from 1932 to 1964; he was more often than not cast as a cop, usually a none-too-bright one, most notably as Sgt. Velie in Columbia's Ellery Queen mysteries in the early 1940s.  He appeared in "The Maltese Falcon", "At the Circus", "Lone Star", and many others.  One of his best roles was as Charles Ruggles' rowdy rancher pal in "Ruggles of Red Gap".

Has Fallen: Has Fallen is a series of action thriller films based on the characters written by Creighton Rothenberger and Katrin Benedikt.  It features Gerard Butler as Secret Service agent Mike Banning and Aaron Eckhart as Benjamin Asher, the President of the United States.  The series also features Morgan Freeman as the Speaker of the House Allan Trumbull.  The series consists of "Olympus Has Fallen" (2013) and "London Has Fallen" (2016), with the third film titled "Angel Has Fallen", in development.  The series has grossed over $376 million worldwide.

A Good Day to Die Hard: A Good Day to Die Hard is a 2013 American action thriller film and the fifth installment in the "Die Hard" film series.  The film was directed by John Moore and written by Skip Woods, and stars Bruce Willis as John McClane.  The main plot finds McClane travelling to Russia to get his estranged son, Jack, an undercover CIA agent, out of prison.  He is soon caught in the crossfire of a global terrorist plot.  Alongside Willis, the film also stars Jai Courtney, Cole Hauser, Yuliya Snigir and Sebastian Koch as the film's villain.

F/X2: F/X2 (also known as F/X2: The Deadly Art of Illusion) is a 1991 American action thriller film directed by Richard Franklin and starring Bryan Brown and Brian Dennehy.  It is a sequel to the 1986 film "F/X".  This was Franklin's final American film before he returned to his native Australia.

Brush with Danger: Brush with Danger is an American action thriller film produced and directed by Livi Zheng.  The film stars Ken Zheng, Livi Zheng, Norman Newkirk, Nikita Breznikov, Michael Blend, and Stephanie Hilbert.  The film was written, produced, and directed by a brother-sister duo from Indonesia; Livi Zheng and Ken Zheng, who after pursuing martial arts and filmmaking separately, came together to create this martial arts action thriller.  The film also includes collaborations with David L Boushey (stunt coordinator) and Garry Schyman (composer).  The film was released in theaters in the United States on September 19, 2014.

Olympus Has Fallen: Olympus Has Fallen is a 2013 American action thriller film.  Directed by Antoine Fuqua and written by Creighton Rothenberger & Katrin Benedikt, it stars Gerard Butler, Aaron Eckhart, and Morgan Freeman, with Angela Bassett, Robert Forster, Cole Hauser, Ashley Judd, Melissa Leo, Dylan McDermott, Radha Mitchell, and Rick Yune in supporting roles.  The film depicts a North Korean-led guerrilla assault on the White House, and focuses on disgraced Secret Service agent Mike Banning's (Butler) efforts to rescue the President (Eckhart).

London Has Fallen: London Has Fallen is a 2016 American action thriller film directed by Babak Najafi and written by Creighton Rothenberger, Katrin Benedikt, Chad St. John and Christian Gudegast.  It is a sequel to Antoine Fuqua's 2013 film "Olympus Has Fallen" and stars Gerard Butler, Aaron Eckhart and Morgan Freeman, with Alon Moni Aboutboul, Angela Bassett, Robert Forster, Jackie Earle Haley, Melissa Leo, Radha Mitchell, Sean O'Bryan, Waleed Zuaiter and Charlotte Riley in supporting roles.  It is the second installment in the "Has Fallen" film series.

Sean O'Bryan: Sean Michael O'Bryan (born September 10, 1963) is an American film and television actor from Louisville, Kentucky, where he attended and graduated from St. Xavier High School.

The Keeping Room: The Keeping Room is a 2014 American action thriller film directed by Daniel Barber and written by Julia Hart.  The film stars Brit Marling, Hailee Steinfeld, Muna Otaru, Sam Worthington, Amy Nuttall, and Ned Dennehy.  It was screened in the Special Presentations section of the 2014 Toronto International Film Festival.  The film was in a limited release in the United States on September 25, 2015, by Drafthouse Films.  The film was made available on Netflix US on May 4, 2016.

In the Line of Fire: In the Line of Fire is a 1993 American action thriller film, directed by Wolfgang Petersen and starring Clint Eastwood, John Malkovich and Rene Russo.  Written by Jeff Maguire, the film is about a disillusioned and obsessed former CIA agent who attempts to assassinate the President of the United States and the Secret Service agent who tracks him.  Eastwood's character is the sole active-duty Secret Service agent remaining from the detail guarding John F. Kennedy in Dallas, Texas, at the time of his assassination in 1963.  The film also stars Dylan McDermott, Gary Cole, John Mahoney, and Fred Thompson.

Question: American action thriller film London Has Fallen stars this American film and television actor born in 1963 from which state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the American film and television actor."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the actor."
    },
    "birth_state": {
      "type": "string",
      "description": "The birth state of the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the actor starred in."
    }
  },
  "required": [
    "actor_name",
    "birth_year",
    "birth_state",
    "film_title"
  ],
  "additionalProperties": false
}
