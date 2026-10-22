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
Devil's Partner: Devil's Partner is a 1958 American film starring Ed Nelson, directed by Charles R. Rondeau and produced by Hugh Hooker, an actor and stuntman who had previously made the 1958 film "The Littlest Hobo".  However the film was not released until 1961 when it was acquired by Roger and Gene Corman's Filmgroup as a double feature with "Creature from the Haunted Sea" The film was co-written by actor Stanley Clements and Laura Jean Mathews.

Morgan Freeman on screen and stage: American actor and director Morgan Freeman has had a prolific career on film, television and on the stage.  His film debut was as an uncredited character in the Sidney Lumet–directed drama "The Pawnbroker" in 1964.  Freeman also made his stage debut in the same year by appearing in the musical "Hello, Dolly! " He followed this with further stage appearances in "The Niggerlovers" (1967), "The Dozens" (1969), "Exhibition" (1969), and the musical "Purlie" (1970–71).  He played various characters on the children's television series "The Electric Company" (1971–77).  Freeman subsequently appeared in the films "Teachers" in 1984, and "Marie" in 1985 before making his breakthrough with 1987's "Street Smart".  His role earned him a nomination for the Academy Award for Best Supporting Actor.  Two years later he appeared in war film "Glory" (1989), and starred as Hoke Coleburn in the comedy-drama "Driving Miss Daisy" (1989).  Freeman won the Golden Globe Award for Best Actor – Motion Picture Musical or Comedy for his performance in the latter and also earned a nomination for the Academy Award for Best Actor.

Hello London: Hello London is a 1958 documentary film starring Sonja Henie and Michael Wilding.  This was also Oliver Reed's film debut.

Asad Shan: Asad Shan is a British Actor, Fashion Model, TV presenter.  He is an ex Investment Banker having worked for the likes of ABN AMRO, HSBC and Thompson Financials.  He was crowned Mr. Asia UK 2004.  His first feature film 7 Welcome to London saw him make his big screen debut as well as his directorial debut.  It received massive critical and commercial acclaim after its UK release and has gone on to become the most successful British made Hindi language film in the UK.  Shan's other notable appearances include being a veejay for B4U Music and he is currently on Zee TV's Zing as a host for weekend film show"Brits Bollywood" and daily rude tube show "Grinds My Teeth".  Shan has also starred in New York Film Academy and Lee Strasberg Theatre Institute productions of the well-renowned East is East and The Glass Menagerie.  He has recently endorsed campaigns for major brands like Sky Digital, HSBC and most recently - One For The Boys, a charity chaired by Samuel L. Jackson.

Eva Christian: Eva Christian (born Evelyne Gutmann; 27 May 1937) is a German actress who has appeared in numerous films since her 1958 film debut.  Born in Berlin, she grew up in Romania, and made her stage debut at the .  In 1962, she went to Germany, where she appeared at the , under Erwin Piscator.

I Want Your Love (Atomic Kitten song): "I Want Your Love" is a song by Atomic Kitten, released as the third single from their debut album "Right Now".  The single peaked at number 10 on the UK Singles Chart, and also reached number 48 in Ireland.  The song heavily samples the theme to the 1958 film "The Big Country".  Almost exactly a decade earlier, the same sample had been used on the song "The Only Rhyme That Bites" by MC Tunes vs 808 State, which also peaked at number 10 on the UK Singles Chart.  Initial copies of "I Want Your Love" contained a sample of the KLF's 1991 hit single "Justified and Ancient"; later copies had the sample removed.  The video & radio versions contained vocals from Kerry Katona; these vocals were replaced on the album version by Jenny Frost.  The song was produced, arranged, recorded and mixed by Damien Mendis at Metropolis Studios, London.  "I Want Your Love" is also featured on the "Greatest Hits" album.

Oliver Reed: Robert Oliver Reed (13 February 1938 – 2 May 1999) was an English actor known for his upper-middle class, macho image, hellraiser lifestyle, and "tough guy" roles.  Notable films include "The Trap" (1966), "Oliver! " (1968), "Women in Love" (1969), "Hannibal Brooks" (1969), "The Devils" (1971), "The Three Musketeers" (1973), "Tommy" (1975), "Lion of the Desert" (1981), "Castaway" (1986), "The Adventures of Baron Munchausen" (1988) and "Funny Bones" (1995).  For "Gladiator" (2000), his final film, Reed was posthumously nominated for the BAFTA Award for Best Actor in a Supporting Role.

The Gun Runners: The Gun Runners is a 1958 film noir crime film directed by Don Siegel, is the third adaptation of Ernest Hemingway's novel "To Have and Have Not", starring Audie Murphy and Patricia Owens.  Everett Sloane essays the part of the alcoholic sidekick originally played by Walter Brennan in the film's first adaptation, although Sloane's interpretation is less overtly comic.  Eddie Albert delivers a bravura performance as a charismatic villain; other cast members include Jack Elam and Richard Jaeckel.  Gita Hall, "Miss Stockholm of 1953", made her film debut as Albert's girlfriend Eva.

The Road a Year Long: The Road a Year Long (Italian: "La strada lunga un anno" , ) is a 1958 film directed by Giuseppe De Santis.  A Yugoslavian-Italian co-production, it was Yugoslavia's first ever submission for the Academy Award for Best Foreign Language Film and was nominated for the award at the 31st Academy Awards in April 1959.  It won the Golden Globe Award for Best Foreign Language Film.  For his performance Massimo Girotti was awarded best actor at the San Francisco International Film Festival.

Vertigo (film score): The music score for Alfred Hitchcock's 1958 film "Vertigo" was composed by Bernard Herrmann between 3 January and 19 February 1958.  The recordings were made in London and Vienna, with orchestra conducted by Muir Mathieson.  A musicians' strike had prevented the score from being recorded in Los Angeles with Herrmann conducting.

Question: The 1958 film Hello London saw the film debut of an actor that died in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "debut_actor": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor who made their film debut."
        },
        "death_year": {
          "type": "integer",
          "description": "The year the actor died."
        }
      },
      "required": [
        "actor_name",
        "death_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "debut_actor"
  ],
  "additionalProperties": false
}
