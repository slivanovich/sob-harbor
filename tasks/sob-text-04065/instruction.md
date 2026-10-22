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
Terminator Salvation: Terminator Salvation is a 2009 American post-apocalyptic science fiction war film directed by McG, starring Christian Bale and Sam Worthington.  It is the fourth installment of the "Terminator" film series.  In a departure from the previous installments, which were set between 1984 and 2004 and used time travel as a key plot element, "Salvation" is a post-apocalyptic film set in the year 2018, fourteen years after the events of "".  It focuses on the war between Skynet's machine network and humanity; the remnants of the world's military have organized as the Resistance, fighting against Skynet's killing machines.  Bale portrays John Connor, Resistance fighter and central character to the franchise, while Worthington portrays cyborg Marcus Wright.  Anton Yelchin plays as a young Kyle Reese, a character first introduced in "The Terminator", and the film depicts the origin of the T-800 (Model 101) Terminator, played by Roland Kickinger, who replaces Arnold Schwarzenegger as the title character, though CGI was used to recreate Schwarzenegger's facial likeness from the original film, with his consent.

After Earth: After Earth is a 2013 American post-apocalyptic science fiction action film directed by M. Night Shyamalan, who co-wrote it with Gary Whitta, based on an original story idea by Will Smith.  It is the second film after "The Pursuit of Happyness" that stars real-life father and son Will and Jaden Smith; Will Smith also produced via his company Overbrook Entertainment, and the distribution was by Columbia Pictures.  The film takes place in the 31st Century, when the Earth has long been abandoned and humans have been in conflict with a mysterious alien race.  It tells the story of a high-ranking general in the peacekeeping organization Ranger Corps, and his son, who, after an incident during a spaceflight, find themselves fighting for survival on a hostile planet (which is Earth itself).

Oblivion (2013 film): Oblivion is a 2013 American post-apocalyptic science fiction film based on Joseph Kosinski's unpublished Radical Publishing graphic novel of the same name.  The film was co-produced and directed by Kosinski.  It stars Tom Cruise, Morgan Freeman, Andrea Riseborough, and Olga Kurylenko.  The film was released in the U.S. on April 19, 2013.  According to Kosinski, "Oblivion" pays homage to science fiction films of the 1970s.

Steel Dawn: Steel Dawn is a 1987 American post-apocalyptic science fiction action film that mixes the genres of science fiction and western.  It stars Patrick Swayze and his wife, Lisa Niemi.

Zach McGowan: Zachary Brendan "Zach" McGowan (born May 5, 1981) is an American film and television actor and voice-over artist.  He is known for his roles in television series "Shameless" as Jody, "Black Sails" as Charles Vane, and "The 100" as Roan.  Other highlights include parts in the films "Terminator Salvation", "The Hunt for Eagle One", and the sequel "The Hunt for Eagle One: Crash Point".  He guest-starred in the television series "Numb3rs", "", and "Cold Case", with voice-over work for the "Scream Awards", "Animal Planet" and the video games "", "", and "Iron Man".

On the Beach (1959 film): On the Beach is a 1959 American post-apocalyptic science fiction drama film from United Artists, produced and directed by Stanley Kramer, that stars Gregory Peck, Ava Gardner, Fred Astaire and Anthony Perkins.  This black-and-white film is based on Nevil Shute's 1957 novel of the same name depicting the aftermath of a nuclear war.  Unlike the novel, no blame is placed on whoever started the war; it is hinted in the film that the threat of annihilation may have arisen from an accident or misjudgment.

Silent Running: Silent Running is a 1972 environmentally-themed American post-apocalyptic science fiction film starring Bruce Dern, featuring Cliff Potts, Ron Rifkin and Jesse Vint.  It was directed by Douglas Trumbull, who had previously worked as a special effects supervisor on science fiction films, including "" and "The Andromeda Strain".

Plughead Rewired: Circuitry Man II: Plughead Rewired: Circuitry Man II is a 1994 American post-apocalyptic science fiction film written and directed by Steven Lovy and Robert Lovy, and starring Jim Metzler, Vernon Wells, Deborah Shelton, Dennis Christopher, Nicholas Worth and Traci Lords.  It is the sequel to the 1990 cult classic movie "Circuitry Man".

Revolution (TV series): Revolution is an American post-apocalyptic science fiction television series that ran from September 17, 2012 until May 21, 2014; it was cancelled by NBC in May 2014.  The show takes place in the post-apocalyptic near-future of the year 2027, 15 years after the start of a worldwide, permanent electrical-power blackout in 2012.  Created by Eric Kripke and produced by J. J. Abrams' Bad Robot Productions for the NBC network, it originally aired on Mondays at 10:00 pm (ET) doing well enough that NBC ordered a second season shortly after the first season finale.

The Hunt for Eagle One: The Hunt for Eagle One is a 2006 direct-to-video war film.  The story takes place during Operation Enduring Freedom in the Philippines.  A group of U.S. Marines are sent to rescue a captured U.S. Marine Captain and a Filipino Major while tracking down a group of Al-Qaeda terrorists intent on launching biological weapons.  The film was produced by the legendary B-movie producer Roger Corman.  "The Hunt for Eagle One" stars Mark Dacascos, Theresa Randle, Rutger Hauer, Joe Suba and Zach McGowan.

Question: Zach McGowan played in what 2009 American post-apocalyptic science fiction war film? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film Zach McGowan played in that matches the specified criteria."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres that describe the film."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor whose filmography is being queried."
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "film_genres",
    "actor_name"
  ],
  "additionalProperties": false
}
