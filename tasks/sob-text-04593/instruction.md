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
Kevin Spencer (TV series): Kevin Spencer is an animated television series developed by Greg Lawrence, aired in Canada on The Comedy Network and aimed at adult audiences.  It takes its name from the main character.  The half-hour show takes place in Ottawa, Ontario.

A Star Is Burns: "A Star Is Burns" is the eighteenth episode of "The Simpsons"<nowiki>'</nowiki> sixth season.  It first aired on the Fox network in the United States on March 5, 1995.  In the episode, Springfield decides to hold a film festival, and famed critic Jay Sherman is invited to be a judge.

Marvin the Tap-Dancing Horse: Marvin the Tap-Dancing Horse is a Canadian/Korean animated television show produced by Nelvana that first aired on Teletoon on March 5, 2000.  It tells the stories of a young horse named Marvin who is part of a carnival.  Among the executive producers are Michael Paraskevas and Betty Paraskevas, creators of Maggie and the Ferocious Beast.  who also created the book that the show is based on.  The show first aired on the Treehouse block before moving to just before Tiny Pop.  In the United States, the series also aired on PBS Kids as part of the PBS Kids Bookworm Bunch from 2000 to 2002.  In 2007, reruns of the show began airing on Qubo Channel in the US.

Eric Forman: Eric Albert Forman (born March 5, 1960) is a fictional character in Fox Network's "That '70s Show", portrayed by Topher Grace.  Eric is based on the adolescence of show creator Mark Brazill.  Most of the show takes place at the Formans' home, particularly in the basement, where he and his five friends hang out.

List of Wolfblood episodes: "Wolfblood" is a teen supernatural-drama television series, broadcast on the CBBC channel in the United Kingdom, and also shown worldwide.  A webisode titled "The Scape Goat" takes place between the first and second series.  A series of seven webisodes known as "Jana Bites" takes place between the second and third series.  An online animated motion comic known as "New Moon Rising", which comes in three parts, takes place between the third and fourth series.  An online animated motion comic known as "Hunter's Moon", which comes in three parts, takes place between the fourth and fifth series.  Ten mini-episodes known as "Wolfblood Secrets", which also takes place between the fourth and fifth series, has aired.  An extra webisode called "Lore" aired 19 October 2016.  An online animated motion comic known as "Wolfblood Alpha", which is in three parts, takes place after the fourth series.  s of 1 2017, episodes of "Wolfblood " have aired, concluding the first half of the  series.

Dead Set: Dead Set is a British television horror series created by Charlie Brooker.  The show takes place primarily on the set of a fictional series of the real television show "Big Brother".  The five episodes, aired over five consecutive nights, chronicle a zombie outbreak that strands the housemates and production staff inside the "Big Brother" House, which quickly becomes a shelter from the undead.

Springfield (The Simpsons): Springfield is the fictional town in which the American animated sitcom "The Simpsons" is set.  A mid-sized town in an undetermined state of the United States, Springfield acts as a complete universe in which characters can explore the issues faced by modern society.  The geography of the town and its surroundings is flexible, changing to address whatever an episode's plot calls for.

Martha Speaks (TV series): Martha Speaks is an American-Canadian children's educational animated television series based on the 1992 children's book of the same name by Susan Meddaugh, about a talking dog named Martha (voiced by Tabitha St. Germain), who is owned by ten-year-old Helen Lorraine (known in the books as Helen Finney).  When Helen feeds Martha some alphabet soup, the soup travels to her brain instead of her stomach, resulting in her ability to speak.  The show focuses on synonyms and vocabulary, with each episode featuring an underlying theme illustrated with keywords.  The show takes place in the fictional town of Wagstaff City, a parody of Flagstaff, Arizona.

Top Model: Top Model or Next Top Model is a fashion-themed reality television show format produced in many countries throughout the world and seen in over 120 countries producing over 200 seasons (referred to as "cycles").  The show takes the form of a modeling competition whose winners typically receive a contract with a major modeling agency and a cover shoot and fashion photo spread in a fashion magazine.  The format was created by Tyra Banks for the original series, "America's Next Top Model" which was first aired in 2003, produced by Ken Mok's 10 by 10 Entertainment.

The Kids in the Hall: Death Comes to Town: The Kids in the Hall: Death Comes to Town (or simply "Death Comes to Town") is an eight-episode Canadian mini-series that aired on CBC Television on Tuesdays between January 12 and March 16, 2010.  The show takes place in a fictional Ontario town called Shuckton where their mayor has been murdered.  As the Shuckton residents cope with the loss, a new lawyer moves in to prosecute a suspect – though another resident, unsatisfied with the evidence, tries to find the real killer.  At the same time, a character who is a personification of death waits at a motel room for the latest Shuckton residents to die.

Question: Which television show takes place in the fictional town of Springfielld and first aired on Fox network in the United States on March 5, 1995?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the television show."
    },
    "network": {
      "type": "string",
      "description": "The network on which the show first aired."
    },
    "first_air_date": {
      "type": "string",
      "format": "date",
      "description": "The date when the show first aired."
    },
    "setting": {
      "type": "object",
      "properties": {
        "town_name": {
          "type": "string",
          "description": "The name of the town where the show takes place."
        },
        "is_fictional": {
          "type": "boolean",
          "description": "Indicates if the town is fictional."
        },
        "country": {
          "type": "string",
          "description": "The country where the show's setting is located."
        }
      },
      "required": [
        "town_name",
        "is_fictional",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "show_name",
    "network",
    "first_air_date",
    "setting"
  ],
  "additionalProperties": false
}
