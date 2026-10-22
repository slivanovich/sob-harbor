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
Kim Min-soo (judoka): Kim Min-soo (born January 22, 1975) is a South Korean former judoka, professional mixed martial artist and K-1 kickboxer.  He is best known for becoming a K-1 World Grand Prix 2006 Finalist and also winning the 1996 Summer Olympics in Atlanta earning a Silver Medal in Judo.  He is also known for his fights with current WWE professional wrestler and former UFC Heavyweight Champion and veteran Brock Lesnar, former WWE wrestler and K-1 fighter Sean O'Haire and former NFL football player turned K-1 kickboxer and New Japan Pro Wrestling contender Bob Sapp.  Min-soo holds a notable kickboxing win over former UFC fighter Scott Junk.  He announced his retirement from contact sports in 2011 with brief stints as color commentator for Japanese and Korean mixed martial arts and professional wrestling events.  Kim is also the Judo head coach for Korean Top Team.

Curt Hennig: Curtis Michael Hennig (March 28, 1958 – February 10, 2003) was an American professional wrestler, manager, and color commentator who performed under his real name for the American Wrestling Association (AWA), the World Wrestling Federation (now WWE), World Championship Wrestling (WCW), and Total Nonstop Action Wrestling (TNA).  In the WWF, he found his greatest success as Mr. Perfect, a nickname introduced in his second run with the company which gradually became his official ring name.  Hennig used the same ring name in his third and final run.  However, his real name was widely acknowledged.  He is the son of wrestler Larry "The Axe" Hennig, and father of current WWE wrestler Curtis Axel.

Universal Soldier: The Return: Universal Soldier: The Return is a 1999 American science fiction action film directed by Mic Rodgers in his directorial debut, and written by William Malone and John Fasano.  The film stars Jean-Claude Van Damme, Michael Jai White, Bill Goldberg, Heidi Schanz, Kiana Tom and Xander Berkeley.  The film was released in the United States on August 20, 1999.  This was Jean-Claude Van Damme's last widely released film until 2012's "The Expendables 2".

The Honky Tonk Man: Roy Wayne Farris (born January 25, 1953), better known by the ring name The Honky Tonk Man, is an American professional wrestler.  Currently working on the independent circuit, he previously wrestled for World Championship Wrestling (WCW) and World Wrestling Federation (WWF, now WWE).  He is best known for his first run with WWF, where he held the WWF Intercontinental Championship for a record 64 weeks, and lost it to The Ultimate Warrior at the inaugural SummerSlam.  He is the cousin of fellow professional wrestler and color commentator Jerry Lawler.

Universal Soldier: Day of Reckoning: Universal Soldier: Day of Reckoning (formerly known as Universal Soldier: A New Dimension) is a 2012 American science fiction action film co-written, co-edited and directed by John Hyams.  The film stars Jean-Claude Van Damme, Dolph Lundgren, Scott Adkins and Andrei "The Pit Bull" Arlovski.  It is the fourth and final theatrical installment in the "Universal Soldier series".

Corey Graves: Matthew Polinsky (born February 24, 1984) is an American color commentator, columnist, and former professional wrestler.  He is currently signed to WWE as a color commentator for "Raw" and "SmackDown Live" under the ring name Corey Graves.  He is a former NXT Tag Team Champion with Adrian Neville.  Polinsky is also known for his work on the independent circuit under the ring name Sterling James Keenan.

William Regal: Darren Kenneth Matthews (born 10 May 1968) is an English retired professional wrestler, color commentator and trainer.  He is currently signed to WWE on the NXT brand under the ring name William Regal, acting as the brand's general manager.  He is also known for his time in World Championship Wrestling (WCW) under the ring name Steven Regal.  Having started his career on a rare surviving carnival booth in Britain, he moved on to wrestle for national-level promotions on the British wrestling circuit and on British television.  He then progressed to touring around the world, in countries such as Germany and South Africa, before being called up to WCW in 1993.

Universal Soldier (1992 film): Universal Soldier is a 1992 American military science fiction action film directed by Roland Emmerich, produced by Mario Kassar and Allen Shapiro, and written by Richard Rothstein and Dean Devlin.  The film tells the story of Luc Deveraux, a former US Army soldier who was killed in Vietnam War in 1969, and returned to life following a secret military project called the "Universal Soldier" program.  However, he finds out about his past even although his memory was erased, and escapes alongside a young TV journalist.  Along the way, they have to deal with the return of his archenemy, Sgt. Andrew Scott, who had lost his sanity in the Vietnam War, and became a psychotic megalomaniac, intent on killing him and leading the Universal Soldiers.  "Universal Soldier" was released by TriStar Pictures on July 10, 1992.  The film grossed $36 million worldwide against its budget of $23 million.  It spawned a series of films, including several rather poorly received direct-to-TV films: "", which has since been removed from the series canon, followed by "" and "".

Bill Goldberg: William Scott Goldberg (born December 27, 1966) is an American professional wrestler, actor, former professional football player and former mixed martial arts color commentator known for his time in WWE and WCW under the ring name Goldberg.

Universal Soldier: Regeneration: Universal Soldier: Regeneration (also known in some countries as Universal Soldier: A New Beginning) is a 2009 American sci-fi action film directed and edited by John Hyams (the son of director Peter Hyams, who previously worked with Jean-Claude Van Damme on three films, 1994's "Timecop", 1995's "Sudden Death" and 2013's "Enemies Closer"; in this film Peter is the director of photography).  The film stars Jean-Claude Van Damme and Dolph Lundgren, who both reprise their roles from the first film.  It is the third theatrical installment in the "Universal Soldier series".  The film is a direct sequel to the original "Universal Soldier" from 1992, unrelated to the two "Universal Soldier" television sequels that were produced in 1998 and completely ignores the events from the 1999 theatrical sequel "".

Question: Universal Soldier: The Return is a 1999 American science fiction action film directed by Mic Rodgers in his directorial debut, stars include which American professional wrestler, actor, former professional football player and former mixed martial arts color commentator known for his time in WWE and WCW under the ring name Goldberg?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "actor_identified": {
      "type": "string",
      "description": "The name of the actor identified by the description."
    },
    "actor_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professional roles or careers of the identified actor."
    },
    "wrestling_promotions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of wrestling promotions the actor was known for."
    },
    "ring_name": {
      "type": "string",
      "description": "The primary ring name used by the actor in wrestling."
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "actor_identified",
    "actor_roles",
    "wrestling_promotions",
    "ring_name"
  ],
  "additionalProperties": false
}
