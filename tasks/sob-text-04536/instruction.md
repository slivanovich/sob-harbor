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
Chris Hemsworth: Chris Hemsworth (born 11 August 1983) is an Australian actor.  He is known for playing Kim Hyde in the Australian TV series "Home and Away" (2004-07) and Thor in the Marvel Cinematic Universe since 2011.  Hemsworth has also appeared in the science fiction action film "Star Trek" (2009), the thriller adventure "A Perfect Getaway" (2009), the horror comedy "The Cabin in the Woods" (2012), the dark-fantasy action film "Snow White and the Huntsman" (2012), the war film "Red Dawn" (2012), and the biographical sports drama film "Rush" (2013).

Frank Gatliff: Frank Gatliff (1927–1990), was an Australian actor in Britain, in several films but mostly on TV, in such shows as "Gideon's Way", "The Baron", "Danger Man", "The Avengers", "Department S", "Strange Report", "The Persuaders! ", "Doctor Who" (in the serial "The Monster of Peladon"), "Rising Damp", "The Good Life", "The Onedin Line", "Blake's 7", "Minder" and "C.A.B.".

Paul Karo: Paul Karo is an Australian actor of Moroccan Sephardi Jewish descent, best known for his role as Lee Whiteman in the 1970s television soap opera "The Box".  In 1976 he won the Best Australian Actor category at the Logie Awards.

Avengers A.I.: Avengers A.I. was an ongoing comic book series published by Marvel Comics that was released in July 2013, as part of the company's Marvel NOW!  initiative.  The series takes place after the events of Age of Ultron, where the world has been colonized by A.I.s "who may or may not have positive feelings about the way humanity has been treating them for the past 100 years."  The series ended in April, 2014.

Don Crosby: George Wallace Donald "Don" Crosby, OAM (29 October 1924 – 3 December 1985), was an Australian actor of radio, stage, television and film, radio producer, stage manager, airman and trade unionist, the fifth child of actor Joseph Alexander (Marshall) Crosby and Theresa Crosby (formerly King).  He was named after his father's friend, the actor and comedian George Stevenson Wallace.  At the age of one, he was taken on stage by his father in a production of the operetta "His Royal Highness".  At age 12, he started producing radio sketches at the Australian Broadcasting Corporation (ABC, then known as the Australian Broadcasting Commission).

John Frawley (actor): John Frawley (died 3 March 1999, Melbourne, Australia) was an Australian actor with a number of film, television and stage credits to his name.  After a television career in the United Kingdom during the 1960s, which included episodes of "The Prisoner" and "The Avengers", Frawley appeared mainly in Australian films during the 1970s.  He returned to television in the 1980s and 1990s, including appearances in "Prisoner" and "Brides of Christ".

Steve Dodd: Steve Dodd (1 June 1928 – 10 November 2014) was an Indigenous Australian actor, notable for playing indigenous characters across seven decades of Australian film.  After beginning his working life as a stockman and rodeo rider, Dodd was given his first film roles by prominent Australian actor Chips Rafferty.  His career was interrupted by six years in the Australian Army during the Korean War, and limited by typecasting.

Avengers: Age of Ultron (soundtrack): Marvel's Avengers: Age of Ultron Original Soundtrack is the film score for the Marvel Studios film, "" by Brian Tyler and Danny Elfman.  Hollywood Records released the album digitally on April 28, 2015, and in physical formats on May 19, 2015.

Vuyo Dabula: Vuyo Dabula (born 11 September 1976) is a South African actor most famous for acting as Kumkani Phakade brother-in law of Tau Mogale (Rapulana Seiphemo) in the soap "Generations.  Vuyo also appeared in Avengers: Age of Ultron (2015) and is set to play a lead role in the upcoming movie Five Fingers.

Avengers: Age of Ultron: Avengers: Age of Ultron is a 2015 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.  It is the sequel to 2012's "The Avengers" and the eleventh film in the Marvel Cinematic Universe (MCU).  The film was written and directed by Joss Whedon and features an ensemble cast that includes Robert Downey Jr., Chris Hemsworth, Mark Ruffalo, Chris Evans, Scarlett Johansson, Jeremy Renner, Don Cheadle, Aaron Taylor-Johnson, Elizabeth Olsen, Paul Bettany, Cobie Smulders, Anthony Mackie, Hayley Atwell, Idris Elba, Stellan Skarsgård, James Spader, and Samuel L. Jackson.  In "Avengers: Age of Ultron", the Avengers fight Ultron, an artificial intelligence obsessed with causing human extinction.

Question: What year did Australian actor ChrisHemswoth appeared on the Avengers: Age of Ultron?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        },
        "is_superhero_film": {
          "type": "boolean",
          "description": "Indicates if the film is a superhero film."
        },
        "is_mcu_film": {
          "type": "boolean",
          "description": "Indicates if the film is part of the Marvel Cinematic Universe."
        }
      },
      "required": [
        "title",
        "release_year",
        "is_superhero_film",
        "is_mcu_film"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "actor_nationality",
    "film_details"
  ],
  "additionalProperties": false
}
