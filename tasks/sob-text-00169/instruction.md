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
Three Miles North of Molkom: Three Miles North of Molkom is a 2008 documentary film directed by Corinna Villari-McFarlane and Robert Cannan.  It was nominated in the Best British Documentary category for the British Independent Film Awards 2008.

Zeitgeist Films: Zeitgeist Films is an American independent film distributor based in New York City founded in 1988 by co-Presidents Nancy Gerstman and Emily Russo.  Films distributed by Zeitgeist are strongly auteur-driven by directors such as Christopher Nolan, Guy Maddin, Atom Egoyan, Todd Haynes, Nuri Bilge Ceylan, Olivier Assayas, Abbas Kiarostami, Deepa Mehta, Jan Švankmajer and the Brothers Quay.  The expansive Zeitgeist film library includes "Trouble the Water", "The Corporation", "Jellyfish", "Examined Life", "Into Great Silence", Ten and Irma Vep.  In June 2008, the MoMA honored two decades of Zeitgeist successes with a month-long, twenty film retrospective entitled "Zeitgeist: The Films of Our Time", exhibiting the distributor's twenty most critically acclaimed, intellectually stimulating titles.

Where in the World Is Osama bin Laden?: Where in the World Is Osama Bin Laden?  is a 2008 documentary film, conceived by Adam Dell and co-written, produced, directed by and starring Morgan Spurlock, an American independent filmmaker.

John and James Woolf: Sir John Woolf (15 March 1913, London – 28 June 1999, London) and his brother James Woolf (2 March 1920, London – 30 May 1966) were British film producers.  John and James founded the production companies Romulus Films and Remus Films, which were active during the 1950s and 1960s, and the distribution company Independent Film Distributors (known as IFD), which was active 1950–59 and handled the UK distribution of films such as "The African Queen" and "Gift Horse", as well as several films made by their two production companies (such as "Room at the Top").

Britney: For the Record: Britney: For the Record is a 2008 documentary television film about American singer and actress Britney Spears, following her return to the recording industry after her much-publicized personal struggles.  The film was shot in Beverly Hills and New York City during the third quarter of 2008; main shooting began on September 5, 2008, two days before Spears's appearance at the MTV Video Music Awards.  It was directed by Phil Griffin.  MTV, one of the two official distributors of the documentary, posted on their website the first promotional trailer on October 9, 2008.

List of General Film Distributors films: This is a list of films released by the British distribution company General Film Distributors.  GFD was part of the Rank Organisation, and handled films produced by the various companies controlled by or linked to Rank including Gainsborough Pictures, Two Cities Films and Ealing Studios.  The list also includes films released by Rank's other distribution outlet Eagle-Lion Films.  Foreign films which were handled in Britain by GFD, such as imports from the Hollywood studio Universal Pictures, are not included.  In 1955 GFD was abolished and replaced by Rank Film Distributors.

Benelux Film Distributors: Benelux Film Distributors (BFD) is a joint venture of various independent film distributors and markets a wide range of films in Cinemas in the Netherlands, Belgium and Luxembourg.

Citizen Koch: Citizen Koch is a 2013 documentary film directed by Tia Lessin and Carl Deal, concerning the political influence of American plutocrats following "Citizens United v. FEC" and of the eponymous Koch brothers, in particular.  The film also focuses on the election of Wisconsin governor Scott Walker and his relationship with the Koch Brothers.

Trouble the Water: Trouble the Water is a 2008 documentary film produced and directed by Tia Lessin and Carl Deal, producers of "Fahrenheit 9/11".  "Trouble the Water" is a redemptive tale of a couple surviving failed levees, bungling bureaucrats, and their own troubled past and a portrait of a community abandoned long before Hurricane Katrina hit, featuring music by Massive Attack, Mary Mary, Citizen Cope, John Lee Hooker, The Roots, Dr. John and Blackkoldmadina.  "Trouble the Water" is distributed by Zeitgeist Films and premiered in theaters in New York City and Los Angeles on August 22, 2008, followed by a national release in more than 200 theaters.  It had its television premiere on HBO and has been rebroadcast on National Geographic Channel and Turner Classic Movies.  "Trouble the Water" is available on DVD.

Monica Hampton: Monica Hampton is an award-winning New York-based narrative and documentary filmmaker.  Her documentary film credits include Michael Moore's "Fahrenheit 9/11", "Heavy Metal in Baghdad", the 2008 documentary on Iraqi heavy metal band Acrassicauda and the 2008 documentary "Slacker Uprising", a film about Michael Moore's 2004 tour across the United States.  In 2000 she produced Kevin Smith's View Askew Productions' "Vulgar", a narrative film directed by Bryan Johnson.  She began her film career as an assistant director and production manager on low budget indie films in New York including "Palookaville", "Wishful Thinking" (Drew Barrymore, Jon Stewart) and "Chasing Amy" (Ben Affleck, Jason Lee).  She appears in front of the camera uncredited in "Chasing Amy", "Dogma" and "Vulgar".  She is currently producing Barnaby Clay's upcoming documentary about legendary rock photographer Mick Rock and a documentary on Egypt's Bassem Youssef.

Question: What 2008 documentary film produced and directed by Tia Lessin and Carl Deal, is included in an American independent film distributors library who's films are strongly auteur-driven?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the documentary film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the documentary film."
    },
    "film_type": {
      "type": "string",
      "description": "The type of film, e.g., 'documentary'."
    },
    "production_team": {
      "type": "object",
      "properties": {
        "directors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of directors for the film."
        },
        "producers": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of producers for the film."
        }
      },
      "required": [
        "directors",
        "producers"
      ],
      "additionalProperties": false
    },
    "distributor_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film distributor."
        },
        "type": {
          "type": "string",
          "description": "The type of distributor, e.g., 'American independent film distributor'."
        },
        "base_location": {
          "type": "string",
          "description": "The base location of the distributor."
        },
        "film_style_characteristic": {
          "type": "string",
          "description": "A characteristic describing the films distributed by this company."
        }
      },
      "required": [
        "name",
        "type",
        "base_location",
        "film_style_characteristic"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_type",
    "production_team",
    "distributor_info"
  ],
  "additionalProperties": false
}
