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
Shrek 2: Shrek 2 is a 2004 American computer-animated fantasy film produced by DreamWorks Animation and directed by Andrew Adamson, Kelly Asbury and Conrad Vernon.  It is the sequel to 2001's "Shrek", with Mike Myers, Eddie Murphy and Cameron Diaz reprising their respective voice roles of Shrek, Donkey, and Fiona from the first film, joined by Antonio Banderas, Julie Andrews, John Cleese, Rupert Everett, and Jennifer Saunders.  Sometime after the first film, Shrek, Donkey and Fiona go to visit Fiona's parents (voiced by Andrews and Cleese), while Shrek and Donkey discover that a greedy Fairy God Mother (voiced by Saunders) is plotting to destroy Shrek and Fiona's marriage so Fiona can marry her son, Prince Charming (voiced by Everett).  Shrek and Donkey team up with a swashing cat named Puss in Boots (voiced by Banderas) to stop her.

Austin Powers in Goldmember: Austin Powers in Goldmember is a 2002 American spy action comedy film.  It is the third and final installment of the "Austin Powers" trilogy starring Mike Myers in the title role.  The film was directed by Jay Roach, and co-written by Mike Myers and Michael McCullers.  Myers also plays the roles of Dr. Evil, Goldmember, and Fat Bastard.  The movie co-stars Beyoncé in her theatrical film debut, as well as Robert Wagner, Seth Green, Michael York, Verne Troyer, Michael Caine, Mindy Sterling and Fred Savage.  There are a number of cameo appearances including Steven Spielberg, Kevin Spacey, Britney Spears, Quincy Jones, Tom Cruise, Danny DeVito, Katie Couric, Gwyneth Paltrow, John Travolta, Nathan Lane, and The Osbournes.

Shrek Forever After: Shrek Forever After (often promoted as Shrek: The Final Chapter) is a 2010 American 3D computer-animated fantasy comedy-drama film and the fourth installment in the "Shrek" series, produced by DreamWorks Animation.  Mike Myers, Eddie Murphy, Cameron Diaz, Antonio Banderas, Julie Andrews, John Cleese reprise their previous roles, with Walt Dohrn joining them in the role of Rumpelstiltskin.  Taking place after 2007's "Shrek the Third", Shrek is now a family man and beloved among the local villagers.  Yearning for the days when he was feared, he makes a deal with Rumpelstiltskin and accidentally wipes out his entire existence.  To restore his existence, Shrek has to regain Fiona's love and kiss her before the sun rises, or he will disappear forever.

X-Men: The Last Stand (soundtrack): X-Men: The Last Stand – Original Motion Picture Soundtrack was composed by John Powell and released on May 23, 2006 by Varèse Sarabande. ""  was the third film in the series, and Powell was the third composer used.  He came on the heels of John Ottman and Michael Kamen, both of which were criticized for their work on the scores.

Tinker Bell and the Legend of the NeverBeast: Tinker Bell and the Legend of the NeverBeast is a 2014 American computer-animated fantasy film directed by Steve Loter.  It is the sixth and most recent installment in the DisneyToon Studios "Tinker Bell" film series, based on the character Tinker Bell from J. M. Barrie's "Peter and Wendy".

John Powell (film composer): John Powell (born 18 September 1963) is an English composer, best known for his scores to motion pictures.  He has been based in Los Angeles since 1997 and has composed the scores to over fifty feature films.  He is particularly known for his scores for animated films, including "Antz", "Chicken Run", "Shrek" (all three co-composed with Harry Gregson-Williams), "Robots", "Happy Feet" (and its sequel), three "Ice Age" sequels, "Rio", "How to Train Your Dragon", for which he was nominated for an Academy Award, and its 2014 sequel.

Horton Hears a Who! (film): Horton Hears a Who!  (also known as Dr. Seuss’ Horton Hears a Who!)  is a 2008 American computer-animated fantasy adventure comedy film based on the book of the same name by Dr. Seuss.  Produced by Blue Sky Studios, the film was directed by Jimmy Hayward and Steve Martino and written by Cinco Paul and Ken Daurio, with music by John Powell.  It features the voices of Jim Carrey and Steve Carell.

Shrek: Shrek is a 2001 American computer-animated fantasy film loosely based on William Steig's 1990 fairy tale picture book of the same name and directed by Andrew Adamson and Vicky Jenson in their directorial debut.  It stars the voices of Mike Myers, Eddie Murphy, Cameron Diaz, and John Lithgow, and somewhat serves as a parody of other films adapted from numerous fairy tales, mainly animated Disney films.

Shrek the Third: Shrek the Third is a 2007 American computer-animated fantasy comedy film and the third installment in the "Shrek" franchise, produced by DreamWorks Animation.  It is the sequel to 2004's "Shrek 2", and is the first in the series to be distributed by Paramount Pictures , which acquired DreamWorks Pictures, the former parent of DreamWorks Animation, in 2006.  Chris Miller and Raman Hui directed and co-directed the film, respectively, with the former also co-writing the screenplay with Jeffrey Price, Peter S. Seaman, and Aron Warner.  In addition to Mike Myers, Eddie Murphy, Cameron Diaz, Antonio Banderas, Rupert Everett, Julie Andrews, and John Cleese, who reprise their roles from "Shrek 2", the film also features Justin Timberlake in the role of Arthur Pendragon and Eric Idle as Merlin.  Harry Gregson-Williams composed the original music for the film.  The story takes place eight months after the marriage of Shrek and Fiona in the first film.  Reluctantly reigning over the kingdom of Far, Far Away, Shrek sets out to find the next heir to the throne—Fiona's cousin Artie, while Prince Charming is plotting to overthrow Shrek and become king.

Ice Age: The Meltdown: Ice Age: The Meltdown is a 2006 American computer-animated comedy adventure film produced by Blue Sky Studios and released by 20th Century Fox.  As the first sequel to the 2002 film "Ice Age", it focuses on The Herd escaping an upcoming flood, during which Manny finds love.  It was directed by Carlos Saldanha, co-director of the first film, with the music composed by John Powell.  The original voice cast — Ray Romano, John Leguizamo, Denis Leary and Chris Wedge — is joined by Queen Latifah, Seann William Scott and Josh Peck.

Question: What is the title of the 2001 American computer-animated fantasy film that stars the voice of Mike Myers and in which John Powell composed the scores for?

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
    "composer_details": {
      "type": "object",
      "properties": {
        "composer_name": {
          "type": "string",
          "description": "The name of the primary composer."
        },
        "composition_type": {
          "type": "string",
          "description": "Describes the composer's role (e.g., 'composed', 'co-composed')."
        },
        "co_composers": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of other composers, if the score was co-composed."
        }
      },
      "required": [
        "composer_name",
        "composition_type"
      ],
      "additionalProperties": false
    },
    "main_voice_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the main voice actors in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "composer_details",
    "main_voice_actors"
  ],
  "additionalProperties": false
}
