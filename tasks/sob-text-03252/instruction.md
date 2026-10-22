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
Equilibrium (film): Equilibrium is a 2002 American dystopian science fiction action film written and directed by Kurt Wimmer and starring Christian Bale, Emily Watson, and Taye Diggs.

The Maze Runner (film): The Maze Runner is a 2014 American dystopian science fiction action thriller film directed by Wes Ball, in his directorial debut, based on James Dashner's 2009 novel of the same name.  The film is the first installment in "The Maze Runner" film series and was produced by Ellen Goldsmith-Vein, Wyck Godfrey, Marty Bowen, and Lee Stollman with a screenplay by Noah Oppenheim, Grant Pierce Myers, and T.S. Nowlin.  The film stars Dylan O'Brien, Kaya Scodelario, Aml Ameen, Thomas Brodie-Sangster, Ki Hong Lee, Will Poulter, and Patricia Clarkson.  The story follows sixteen-year-old Thomas, portrayed by O'Brien, who awakens in a rusty elevator with no memory of who he is, only to learn he's been delivered to the middle of an intricate maze, along with a large number of other boys, who have been trying to find their way out of the ever-changing labyrinth — all while establishing a functioning society in what they call the Glade.

2004 in film: The year 2004 in film involved some significant events.  Major releases of sequels took place.  It included blockbuster films like "Shrek 2", "Harry Potter and the Prisoner of Azkaban", "The Bourne Supremacy", "Van Helsing", "The Passion of the Christ", "", "Thunderbirds", "Meet the Fockers", "Harold and Kumar", "The Day After Tomorrow", "Anchorman", "Saw", "", "Spider-Man 2", "Alien vs. Predator", "The Incredibles", "Kill Bill Vol.  2", "Fahrenheit 9/11", "I, Robot", "Ocean's Twelve" and "".

I, Robot (film): I, Robot (stylized as i,robot ) is a 2004 American neo-noir dystopian science fiction action film directed by Alex Proyas.  The screenplay by Jeff Vintar and Akiva Goldsman is from a screen story by Vintar, suggested by Isaac Asimov's short-story collection of the same name.  The film stars Will Smith, Bridget Moynahan, Bruce Greenwood, James Cromwell, Chi McBride, Alan Tudyk and Shia LaBeouf.

Harrison Ford: Harrison Ford (born July 13, 1942) is an American actor and film producer.  He gained worldwide fame for his starring roles as Han Solo in the "Star Wars" film series and as the title character of the "Indiana Jones" film series.  Ford is also known for his roles as Rick Deckard in the neo-noir dystopian science fiction film "Blade Runner" (1982); John Book in the thriller "Witness" (1985), for which he was nominated for the Academy Award for Best Actor; and Jack Ryan in the action films "Patriot Games" (1992) and "Clear and Present Danger" (1994).

Ridley Scott: Sir Ridley Scott (born 30 November 1937) is an English film director and producer.  Following his commercial breakthrough with the science-fiction horror film "Alien" (1979), his best known works include the neo-noir dystopian science fiction film "Blade Runner" (1982), historical drama and Best Picture Oscar winner "Gladiator" (2000), and science fiction film "The Martian" (2015).

Alien Nation (film): Alien Nation is a 1988 American buddy cop neo-noir science fiction action film directed by Graham Baker.  The ensemble cast features James Caan, Mandy Patinkin and Terence Stamp.  The film depicts the assimilation of the "Newcomers", an alien race settling in Los Angeles, much to the initial dismay of the local population.  The plot integrates the neo-noir and buddy cop film genres with a science fiction theme, centering on a union between a veteran police investigator (Caan) and an extraterrestrial (Patinkin); the first Newcomer detective.  The duo probe a criminal underworld attempting to solve a homicide.

Dark City (1998 film): Dark City is a 1998 American-Australian neo-noir science fiction film directed by Alex Proyas.  The screenplay was written by Proyas, Lem Dobbs and David S. Goyer.  The film stars Rufus Sewell, Kiefer Sutherland, Jennifer Connelly, and William Hurt.  Sewell plays John Murdoch, an amnesiac man who finds himself suspected of murder.  Murdoch attempts to discover his true identity and clear his name while on the run from the police and a mysterious group known only as the "Strangers".

James Cameron filmography: James Cameron is a Canadian director, screenwriter, and producer who has had an extensive career in film and television.  Cameron's debut was the 1978 science fiction short "Xenogenesis", which he directed, wrote and produced.  In the early part of his career, he did various technical jobs such as special visual effects producer, set dresser assistant, matte artist, and photographer.  His feature directorial debut was the 1981 release "".  The next film he directed was the science fiction action thriller "The Terminator" (1984).  It starred Arnold Schwarzenegger as the titular cyborg assassin, and was Cameron's breakthrough feature.  In 1986, he directed and wrote the science fiction action sequel "Aliens" starring Sigourney Weaver.  He followed this by directing another science fiction film "The Abyss" (1989).  In 1991, Cameron directed the sequel to "The Terminator", "" (with Schwarzenegger reprising his role), and also executive produced the action crime film "Point Break".  Three years later he directed a third Schwarzenegger-starring action film "True Lies" (1994).

Divergent (film): Divergent is a 2014 American dystopian science fiction action film directed by Neil Burger, based on the novel of the same name by Veronica Roth.  The film is the first installment in "The Divergent Series" and was produced by Lucy Fisher, Pouya Shabazian, and Douglas Wick, with a screenplay by Evan Daugherty and Vanessa Taylor.  It stars Shailene Woodley, Theo James, Ashley Judd, Jai Courtney, Ray Stevenson, Zoë Kravitz, Miles Teller, Tony Goldwyn, Ansel Elgort, Maggie Q and Kate Winslet.  The story takes place in a dystopian and post-apocalyptic Chicago where people are divided into distinct factions based on human virtues.  Beatrice Prior is warned that she is Divergent and thus will never fit into any one of the factions.  She soon learns that a sinister plot is brewing in the seemingly perfect society.

Question: What other film, beside the American neo-noir dystopian science fiction action film directed by Alex Proyas was considered a blockbuster in 2004?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the blockbuster film from 2004, excluding the specified film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "is_blockbuster": {
      "type": "boolean",
      "description": "Indicates if the film was considered a blockbuster."
    },
    "excluded_film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film that was explicitly excluded from the answer."
        },
        "director": {
          "type": "string",
          "description": "The director of the excluded film."
        }
      },
      "required": [
        "title",
        "director"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "is_blockbuster",
    "excluded_film_details"
  ],
  "additionalProperties": false
}
