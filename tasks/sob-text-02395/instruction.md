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
Harley Jessup: Harley Jessup (born 1954) is an American production designer and visual effects art director who has been nominated for two visual effects Academy Awards, and won once.  Currently working at Pixar Animation Studios, Jessup has served as production designer for "Monsters, Inc." (with Bob Pauley), "Ratatouille", "Cars 2", "Presto", "The Good Dinosaur" and an upcoming Pixar feature.  Before coming to Pixar, Jessup was production designer on Walt Disney Pictures' "James and the Giant Peach".

Spawn (film): Spawn is a 1997 American supernatural superhero horror film based on the comic book character of the same name.  Directed and co-written by Mark A.Z. Dippé, the film stars Michael Jai White in the title role, and is the first film to feature an African American actor portraying a major comic book superhero.  "Spawn" depicts the origin story of the title character, beginning with the murder of soldier/assassin Al Simmons.  He is resurrected as Spawn, the reluctant, demonic leader of Hell's army.  He ultimately refuses to lead the army in the war against Heaven and turns away from evil.  The film co-stars John Leguizamo (as The Violator, Al's demonic guide and enemy of the film's antagonist) and Nicol Williamson (as Al's mentor, Cogliostro).  Martin Sheen, Theresa Randle, D. B. Sweeney, Melinda Clarke, and Frank Welker (as the voice of Malebolgia) also star in the film.

Dan Ouellette: Dan Ouellette is an American artist, illustrator, director, author and production designer.  He began drawing as a child inspired by Escher, Dalí and Moebius.  His drawings usually begin with very rough sketches and are intended to capture a moment of tension or eroticism.  His art pushes his audience into areas where people feel less than comfortable, stating that the "US which is so puritanical, our bodies are usually a great source of anxiety and fear".  As a production designer, he has designed over fifteen independent feature films in the past decade as well as numerous commercials and music videos.  He is best known as the director for the music videos "Blue" and "Looking Glass" by The Birthday Massacre, receiving over 4 million combined views on YouTube, and has directed music videos for the industrial band Android Lust.  He has done production design for many films over the years including "Chasing Sleep" starring Jeff Daniels.  Dan's artwork is strongly themed around surrealism and mostly done in pencil.  As an artist he has exhibited widely.  He has been published in numerous anthology art books including "Bio-Mannerism" which also features work by H.R. Giger and Beksinski, and he has been featured in magazines internationally.  David Bowie commented while looking at Dan's art that he has noticed a strong influence of science fiction on contemporary art.  Giger saw a different aspect, saying simply "Very bony."  He grew to adore the cinema of Fellini and later to marvel at Lynch's "Eraserhead".  Rather than pursue a formal education in the fine arts he chose to study the craft of film making and after college he became a production designer working on feature films in New York City starting with his work as a production designer for Hal Hartley in 1990 with Trust and then, in 1992, with Simple Men.

Eden Is West: Eden Is West (French: "Eden à l'ouest" ) is a 2009 film by Greek-French director Costa-Gavras about an illegal immigrant called Elias who tries to get to Paris.  The original title in Greek is “Paradissos sti Dysi” (“Paradise in West”) and since it is a Greek-French production, the also original French title is “Eden à l'ouest'.  The nationality of the central hero is not disclosed because Gavras wants to make a point about the odysseys of the illegal immigrants of any nationality, since he himself was an immigrant 50 years ago in France, before he became a well known director.  His hero seems to tolerate the sea, the cold of snowy mountains and the hunger, the rapists and robbers he meets, the cops that are after him all the time, the racists who push him aside, the fellow immigrants who steal his clothes and in the best case the women who see him as a lover they could also take advantage of.  His only comfort is his dream of Paris and, in the complexity of human condition, the good within the evil and vice versa.

Underworld (film series): Underworld is a series of action horror films directed by Len Wiseman, Patrick Tatopoulos, Måns Mårlind, Björn Stein and Anna Foerster.  The first film, "Underworld", was released in 2003.  It tells the story of Selene (Kate Beckinsale), a vampire who works as a Death Dealer, killing the lycans who allegedly slaughtered her family.  The second film, "", was released in 2006.  In this film, Selene takes Michael Corvin, a lycan/vampire hybrid, to a vampire safehouse and plans to return to Viktor's estate to awaken another elder Markus, whom they discover is the first Vampire and a powerful enemy.  The third film, "", is the prequel to the series, chronicling the origins of the vampire-lycan war (it was released on January 23, 2009).  The fourth film, "", is the sequel to "Underworld: Evolution" and was released on January 20, 2012.  In this film, humans have discovered the existence of the vampire and lycan clans, and are trying to eradicate both species.  A fifth film titled "" was released internationally on November 24, 2016, and in the United States on January 6, 2017.

Patrick Tatopoulos: Patrick Tatopoulos is a Greek-French production designer, who lives and works in the United States.  His designs have appeared in numerous motion pictures, including "Pitch Black", "Underworld", "I, Robot", "The Chronicles of Riddick", "Independence Day", "Bram Stoker's Dracula", "Stargate", "Spawn", "Godzilla", "Stuart Little", "300", "I Am Legend", "Man of Steel", "", "Justice League", "10,000 BC", and "Live Free or Die Hard".

Ryo Sugimoto: Ryo Sugimoto Born in 1976.  Sugimoto worked on number of films as an art assistant under Production Designer Mitsuo Harada and Yohei Taneda.  Sugimoto joined NOUVELLE VAGUE Co.,Ltd .  in 2005, has worked on films such as "AEGIS"and "Tokyo Tower" as a set designer and was the art director on "BABEL"(Dir: Alejandro González Iñárritu) which won the Art Excellence in Production Design Award(2006) from the Art Directors Guild.  Sugimoto was the first Production Designer for Junji Sakamoto "Chameleon"(2007), and is the Production designer for "Map of the sounds of Tokyo" directed by Isabel Coixet.  Sugimoto also provides designs for commercials, music videos and interiors,

Underworld: Rise of the Lycans: Underworld: Rise of the Lycans is a 2009 American action horror film directed by Patrick Tatopoulos.  It is the third installment in the "Underworld" franchise and a prequel to the 2003 film "Underworld".  The film focuses primarily on the origins of the characters and the events that lead up to the Vampire–Lycan war.

Art department: Art department in movie terms means the section of a production's crew concerned with visual artistry.  Working under the supervision of the production designer and/or art director, the art department is responsible for arranging the overall "look" of the film (i.e. modern/high-tech, rustic, Victorian, etc.) as desired by the film director.  Individual positions within this department include: production designer, art director, assistant art director, storyboard artist, concept artist, draftsman, art department coordinator, set decorator, set dresser, makeup artist, painter, property master, leadman, swing gang, production buyer, Film sculptor, and property assistant.

Face Off (TV series): Face Off is an American reality television game show on the Syfy cable network in which a group of prosthetic makeup artists compete against each other to create prostheses such as those found in science fiction and horror films. Each episode features one or more challenges, with the work reviewed by a panel of judges and eliminating one or more artists each week until a final winner is chosen.  Actress McKenzie Westmore, known for her role as Sheridan Crane on the former NBC/DirecTV soap opera "Passions" and a member of the Westmore family of makeup artists, serves as the show's host.  For each assignment, the contestants' work is individually evaluated by a panel of professional special effects makeup artists who serve as judges.  These judges have included Academy Award-winning makeup artist Ve Neill, and television and film makeup artist Glenn Hetrick, creature designer and director Patrick Tatopoulos (Season 1 - 3), and Neville Page (Season 3 - present).  Industry figures and artists including Brian Grazer, Kevin Smith, Paul W. S. Anderson, Greg Nicotero, Rick Baker, Doug Jones, Len Wiseman and Gale Anne Hurd have served as guest judges.

Question: Who is the director of the 1997 American horror film which features the designs of Greek-French production designer Patrick Tatopoulos?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    },
    "film_director": {
      "type": "string",
      "description": "The director of the film."
    },
    "production_designer": {
      "type": "string",
      "description": "The production designer whose designs are featured in the film."
    }
  },
  "required": [
    "film_details",
    "film_director",
    "production_designer"
  ],
  "additionalProperties": false
}
