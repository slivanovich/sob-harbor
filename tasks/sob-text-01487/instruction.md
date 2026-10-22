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
Tron: Deadly Discs: Tron: Deadly Discs is a video game for Mattel's Intellivision console, and was published by Mattel in 1982.  The initial game design was done by Don Daglow, with further design and programming by Steven Sents.  It is the first of three Intellivision games based on the Disney motion picture "Tron".  Adaptations of this game have been developed and released for the Atari 2600, under the M Network banner, and the Mattel Aquarius.

Tron: Tron is a 1982 American science fiction action-adventure film written and directed by Steven Lisberger, based on a story by Lisberger and Bonnie MacBird and produced by Walt Disney Productions.  The film stars Jeff Bridges as a computer programmer who is transported inside the software world of a mainframe computer where he interacts with programs in his attempt to escape.  Bruce Boxleitner, David Warner, Cindy Morgan, and Barnard Hughes star in supporting roles.

Deewana (1992 film): Deewana (English: 'Crazy' ) is a 1992 Indian romantic drama film directed by Raj Kanwar, and produced by Guddu Dhanoa and Lalit Kapoor and featuring Shah Rukh Khan, Divya Bharti and Rishi Kapoor in the lead.  This was Shah Rukh's debut release, and he appears only in the second half of the film.  He replaced Armaan Kohli, who walked out of the project due to creative differences after the first schedule.  The film released on June 25, 1992. " Dil Aashna Hai" was supposed to be the debut movie of Shahrukh Khan however "Deewana" was released first.

Toys in the Attic (2009 film): Toys in the Attic (Czech: Na půdě aneb Kdo má dneska narozeniny?  ; festival title: In the Attic: Who Has a Birthday Today?)  is a 2009 Czech-French-Japanese-Slovak primarily stop-motion animated fantasy comedy thriller family film directed by Jiří Barta and written by Edgar Dutka and Barta which depicts a community of toys and other objects in an attic who come to life when no human is around.  It is an international co-production of Czech, Japanese and Slovak companies.  The film was released first in the Czech Republic on 5 March 2009 and has been shown subtitled at film festivals internationally.  An American dub – adapted, produced and directed by Vivian Schilling and performed by actors including Forest Whitaker, Joan Cusack, Cary Elwes and Schilling herself – has been recorded, which the film was first shown with on 3 March 2012 at the New York International Children's Film Festival and was released nationally on 24 August 2012 by Hannover House.

Discs of Tron: Discs of Tron, is the second arcade game based on the Disney film "Tron" (1982).  While the first "Tron" arcade game had several mini-games (Gridbugs, Light Cycles, entering the MCP cone and Digital tanks), "Discs of Tron" is inspired by the jai alai–style sequence in the film in which Kevin Flynn is forced to play against Crom, leading to Crom being "derezzed" by Sark.  Tron is also introduced later, as Flynn witnesses him competing against (and defeating) four of the MCP's "warrior elite".

Game (2016 film): Game in Kannada, Oru Melliya Kodu (English: A thin line) in Tamil, is a 2016 Indian bilingual language crime thriller film directed by A. M. R. Ramesh.  This movie is an unofficial remake of the 2012 Spanish thriller El Cuerpo (Spanish title) also known as "The Body", and features Arjun Sarja, Shaam and Manisha Koirala in the lead roles.  With music composed by Ilayaraaja, the film was simultaneously shot in Kannada and Tamil; the former released first on February 26, 2016 while the later released on July 1, 2016.  The film was dubbed and released in Telugu as "Notuku Potu" in 2017.

Tron RUN/r: Tron RUN/r is a 2016 endless runner video game developed by Sanzaru Games and published by Disney Interactive Studios as part of the "Tron" franchise.  It was first released on February 16, 2016 for the PlayStation 4, Xbox One, and Windows.  It was first announced at the Games Award 2015, where it was described as an "action arcade" game.

The Misadventures of Tron Bonne: The Misadventures of Tron Bonne, known in Japan as Tron ni Kobun (トロンにコブン , lit.  "Tron and Henchmen") , is an action-adventure game that was developed and published by Capcom for the PlayStation.  Released in Japan in 1999 and in North America and Europe in 2000, the game is part of the "Mega Man Legends" ("Rockman DASH") series.  It is also a prequel and spin-off of the first Legends game.

Snegithiye: Snegithiye (English:Oh Friend! " (female)" ) is a 2000 Tamil mystery thriller film directed by Priyadarshan.  The story is loosely based on the 1999 Marathi film "Bindhaast" written by Chandrakant Kulkarni.  The film notably features only female characters in the lead roles, played by Jyothika, Sharbani Mukherjee, Tabu and Ishita Arun.  Music was composed by Vidyasagar.  The film, released in 2000, proved to be an average grosser at the box office but bagged positive reviews from critics.  Today, it is considered a cult classic that was underrated at the time of its release.  Originally planned to be made as a bilingual, in Tamil and in Malayalam, the film released first in Tamil only, while the Malayalam dubbed version, "Raakilipattu", as well as the dubbed Hindi version, "Friendship", released seven years later.

Maleficent (film): Maleficent is a 2014 American dark fantasy film directed by Robert Stromberg from a screenplay by Linda Woolverton, and starring Angelina Jolie as the titular character with Sharlto Copley, Elle Fanning, Sam Riley, Imelda Staunton, Juno Temple, and Lesley Manville in supporting roles.  Loosely based on Charles Perrault's original fairy tale and inspired by Walt Disney's 1959 animated film "Sleeping Beauty", the film portrays the story from the perspective of the eponymous antagonist, depicting her conflicted relationship with the princess and king of a corrupt kingdom.

Question: Which film was released first,Tron or Maleficent

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          }
        },
        "required": [
          "film_title",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "first_released_film_title": {
      "type": "string"
    },
    "release_year_difference": {
      "type": "integer",
      "description": "The difference in years between the release of the two films."
    }
  },
  "required": [
    "film_comparison",
    "first_released_film_title",
    "release_year_difference"
  ],
  "additionalProperties": false
}
