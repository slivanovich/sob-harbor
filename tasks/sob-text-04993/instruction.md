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
The River Wild: The River Wild is a 1994 American adventure crime-thriller film directed by Curtis Hanson and starring Meryl Streep, Kevin Bacon, David Strathairn, John C. Reilly, Benjamin Bratt, and Joseph Mazzello as Roarke.  The film is about a family on a whitewater rafting trip who encounter two violent criminals in the wilderness.

Georgina González Rodríguez: Georgina graduated with a BA in filmmaking from Centro Universitario de Estudios Cinematográficos (CUEC-UNAM) and MFA in Producing from University of Southern California’s Peter Stark program with Fulbright Program, HBO, Consejo Nacional de Ciencia y Tecnología, and FONCA scholarships.

Second Thoughts (1983 film): Second Thoughts is a 1983 American drama film directed by Lawrence Turman and starring Lucie Arnaz, Craig Wasson, Ken Howard and Anne Schedeen.

Polly Cohen Johnsen: Polly Cohen Johnsen is an American film executive and producer.  She went to college at the University of California at San Diego, where she majored in Chinese, and is also a graduate of the Peter Stark Producing Program at the University of Southern California.

Lawrence Turman: Lawrence Turman (born November 28, 1926 in Los Angeles) is a film producer who currently serves as the director of The Peter Stark Producing Program at the University of Southern California.  He was nominated for an Academy Award for "The Graduate" (1967).  He has also produced such films such as "Pretty Poison" (1968), "The Great White Hope" (1970), "The Thing" (1982), "Mass Appeal" (1984), "Short Circuit" (1986), "The River Wild" (1994), and "American History X" (1998).

The Cure (1995 film): The Cure is a 1995 American drama film starring Brad Renfro and Joseph Mazzello.  The film follows two boys searching for the cure of AIDS, from which one of them is suffering.  It was directed by Peter Horton and written by Robert Kuhn.

Chris Wyatt (producer): Christopher Aaron Wyatt, sometimes credited as Chris "Doc" Wyatt, (born October 5, 1975 in Atlanta, Georgia) is an American film producer, writer, and second unit director.  He produced the 2004 film "Napoleon Dynamite", the 2006 film "Think Tank", the 2007 film "Beneath", the 2007 film "Coyote", and the 2009 film "Broken Hill" featuring Oscar-winner Timothy Hutton.  He is a graduate of the Peter Stark Producing Program at the University of Southern California.

2006 NFL Draft: The 2006 National Football League Draft, the 71st in league history, took place in New York City, New York, at Radio City Music Hall on April 29 and April 30, 2006.  For the 27th consecutive year, the draft was telecast on ESPN and ESPN2, with additional coverage offered by ESPNU and, for the first time, by the NFL Network.  Having signed a contract with the Houston Texans on the evening before the draft, Mario Williams, a defensive end from North Carolina State, became the draft’s first pick.  The selection surprised many commentators, who predicted that the Texans would draft Southern California running back Reggie Bush or Texas quarterback Vince Young.  Ohio State produced the most first round selections (five), while Southern California produced the most overall selections (eleven).  Twenty-seven compensatory and supplemental compensatory selections were distributed amongst seventeen teams; Tampa Bay, Baltimore, and Tennessee each held three compensatory picks.  The league also held a supplemental draft after the regular draft and before the regular season.  The 255 players chosen in the draft were composed of:

USC School of Cinematic Arts: The USC School of Cinematic Arts (commonly referred to as SCA)—formerly the USC School of Cinema-Television, otherwise known as CNTV—is a private media school within the University of Southern California in Los Angeles, in the U.S. state of California.  The school offers multiple undergraduate and graduate programs covering film production, screenwriting, cinema and media studies, animation and digital arts, media arts + practice, and interactive media & games.  Additional programs include the Peter Stark Producing Program and the Business of Entertainment (offered in conjunction with the USC Marshall School of Business MBA Program).

The Lost World: Jurassic Park: The Lost World: Jurassic Park is a 1997 American science-fiction adventure film and the second installment in the "Jurassic Park" film series.  A sequel to 1993's "Jurassic Park", the film was directed by Steven Spielberg and written by David Koepp, loosely based on Michael Crichton's 1995 novel "The Lost World".  The film was produced by Gerald R. Molen and Colin Wilson.  Actor Jeff Goldblum returns as the chaos-theorist and eccentric mathematician Ian Malcolm, leading a cast that includes Julianne Moore, Pete Postlethwaite, Vince Vaughn, Vanessa Lee Chester and Arliss Howard.  Goldblum is the only actor from the previous film to return with a major role.  Cameos feature return appearances by Richard Attenborough as John Hammond and a brief appearance by Joseph Mazzello and Ariana Richards as Hammond's grandchildren Tim and Lex.

Question: Lawrence Turman, currently the director of the peter Stark Program at the University of Southern California produced an American adventure crime-thriller film starring Joseph Mazzello as who? 

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
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        }
      },
      "required": [
        "title",
        "year",
        "genre",
        "director"
      ],
      "additionalProperties": false
    },
    "producer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the producer."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "actor_character_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "character_name": {
          "type": "string",
          "description": "The name of the character played by the actor."
        }
      },
      "required": [
        "actor_name",
        "character_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_details",
    "producer_details",
    "actor_character_details"
  ],
  "additionalProperties": false
}
