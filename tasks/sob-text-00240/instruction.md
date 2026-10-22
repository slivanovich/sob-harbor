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
Nathan Ruegger: Nathan Alexander-Ruegger (born January 19, 1984) is an American screenwriter, voice actor and film director, the son of writer/producer/director Tom Ruegger and voice actress Adrienne Alexander.  He was the voice of certain characters in his father's cartoon shows.  The first was in "Tiny Toon Adventures" when he played the baby version of Plucky Duck, famous for his catchphrase "Water go down the hooooooooole!" .  The second was in "Animaniacs", in a far more prominent role as Skippy Squirrel, the nephew of Slappy Squirrel.  Around the end of that show's run, he landed the role of Froggo in "Histeria! ".  He is also well known for being the inspiration of "Yakko Warner."

Jason Woliner: Jason Woliner (born June 1, 1980) is an American comedy director, writer, and a former child actor.  He was the non-performing member of the comedy group Human Giant and directed the bulk of their output.  The group, which also consisted of comedians Aziz Ansari, Rob Huebel, and Paul Scheer, produced an MTV sketch comedy show that ran for two seasons.  He has been directing, writing on, and executive producing the Adult Swim series "Eagleheart", starring Chris Elliott.  The show has completed production of three seasons and is on hiatus.  Woliner has directed episodes of Fox TV's "The Last Man On Earth", NBC's "Parks and Recreation", and Comedy Central's "Nathan for You" and "Jon Benjamin Has A Van", among others.

Timon and Pumbaa: Timon and Pumbaa are an animated meerkat and warthog duo introduced in Disney's 1994 animated film "The Lion King".  Timon was portrayed through his many appearances by Nathan Lane (in all three films and early episodes of the show), Max Casella (the original actor in "The Lion King" Broadway musical), Kevin Schon (in certain episodes of the show), Quinton Flynn (in certain episodes of the show), Bruce Lanoil in the "Wild About Safety" shorts and "Kingdom Hearts II", and while Pumbaa is voiced by Ernie Sabella (in all of his animated speaking appearances), and was portrayed by Tom Alan Robbins in the original cast of the Broadway musical.  In the upcoming live-action remake, the characters will be portrayed by Billy Eichner and Seth Rogen respectively.  Nathan Lane and Ernie Sabella first came to audition for the roles of the hyenas, but when the producers saw how well they worked together they decided to cast them as Timon and Pumbaa.  Lyricist Tim Rice however was pulling for Rik Mayall (for Timon) and Adrian Edmondson (for Pumbaa) to play the roles, as he got the idea for the lyrics to "Hakuna Matata" by watching their show "Bottom".

Nathan Barley: Nathan Barley is a British Channel 4 television sitcom written by Charlie Brooker and Chris Morris, starring Nicholas Burns, Julian Barratt, Claire Keelan, Richard Ayoade, Ben Whishaw, Rhys Thomas and Charlie Condou.  The series of six weekly episodes began broadcasting on 11 February 2005 on Channel 4.  Described by his creator as a "meaningless strutting cadaver-in-waiting", the character originated on Brooker's TVGoHome – a website parodying television listings – as the focus of a fly-on-the-wall documentary called "Cunt".

SeaQuest DSV: SeaQuest DSV (stylized as seaQuest DSV and also promoted as simply seaQuest) is an American science fiction television series created by Rockne S. O'Bannon.  It originally aired on NBC between 1993 and 1996.  In its final season, it was renamed seaQuest 2032.  Set in "the near future"—originally the year 2018 in the first season—"seaQuest DSV" originally mixed high drama with realistic scientific fiction.  It originally starred film star Roy Scheider as Captain Nathan Bridger, designer and commander of the eponymous naval submarine "seaQuest" DSV 4600.  Jonathan Brandis also starred as Lucas Wolenczak, a teenaged computer genius placed aboard "seaQuest" by his father and Stephanie Beacham as Kristin Westphalen, the chief medical officer and head of the "seaQuest" science department.  In the third season, Michael Ironside replaced Scheider as lead of the series and starred as Captain Oliver Hudson.  Also present was a dolphin character called Darwin who, due to technological advances, was able to communicate with the crew.  Steven Spielberg expressed interest in the project and served as one of the show's executive producers during the first two seasons.

The Waldo Moment: The Waldo Moment is the third episode of the second series of British science fiction anthology series "Black Mirror".  It was written by series creator and showrunner Charlie Brooker and directed by Bryn Higgins, and first aired on Channel 4 on 25 February 2013.  The episode originated in an idea for "Nathan Barley", an earlier TV show by Brooker and Chris Morris.

Nicholas Burns (actor): Nicholas Burns (born 1977, Derbyshire) is an English actor, best known for his comic performance as the title character in "Nathan Barley".  He played Martin in "Benidorm" and Alex in "No Heroics", as well as making appearances alongside various "Nathan Barley" co-stars in "The Mighty Boosh" and "The IT Crowd".

Mort Nathan: Mort Nathan is an American television producer, screenwriter and film director.  He was one of the co-producers and head writers of the comedy show "The Golden Girls".  Nathan won two Emmy awards, two Golden Globes, and a Writer's Guild of America award for his work on the series.  He has written and produced over 150 hours of prime time television shows and directed the feature films "Boat Trip", "", and "Bag Boy".

Richard Ayoade: Richard Ellef Ayoade ( , born 12 June 1977) is a British actor, comedian, writer, director and television presenter.  He is best known as Maurice Moss in "The IT Crowd", for which he won the 2014 BAFTA for Best Male Comedy Performance, and as Dean Learner in "Garth Marenghi's Darkplace".  He has directed two feature films – "Submarine" (2010) and "The Double" (2013) – as well as various music videos for bands including Arctic Monkeys, Vampire Weekend, Yeah Yeah Yeahs and Kasabian.

Ben Whishaw: Benjamin John "Ben" Whishaw (born 14 October 1980) is an English actor.  He is known for his stage role as Hamlet; his roles in the television series with his old band mate Christoper Cameron Hafizi "Nathan Barley", "Criminal Justice", "The Hour" and "London Spy"; and film roles including "" (2006), "I'm Not There" (2007), "Bright Star" (2009), "Brideshead Revisited" (2008), "Cloud Atlas" (2012), "The Lobster" (2015), "Suffragette" (2015) and "The Danish Girl" (2015).  He has also played the role of Q in the James Bond films "Skyfall" (2012) and "Spectre" (2015), as well being the voice of Paddington Bear in "Paddington" (2014) and "Paddington 2" (2017).

Question: Which actor on the show Nathan Barley was the director of the film Submarine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "acted_in_show": {
      "type": "string",
      "description": "The name of the show the actor appeared in."
    },
    "directed_film": {
      "type": "string",
      "description": "The name of the film the actor directed."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the directed film."
    }
  },
  "required": [
    "actor_name",
    "acted_in_show",
    "directed_film",
    "film_release_year"
  ],
  "additionalProperties": false
}
