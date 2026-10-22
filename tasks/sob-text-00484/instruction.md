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
Start Wearing Purple: "Start Wearing Purple" is a song by gypsy punk band Gogol Bordello, written by frontman Eugene Hütz.  The song was packaged as a double single along with "Sally", and released as the band's second single in February 2006.  It appears on their third album "".  This version is a re-recording of the initial one which was featured in the band's first album, 1999's "Voi-La Intruder".  It also appears in the soundtrack for the 2005 film "Everything Is Illuminated", in which Hütz stars as Alex.

Balthazar Getty: Paul Balthazar Getty ( ; born January 22, 1975) is an American actor, member of the band Ringside, the producer-half of rap duo The Wow, and a member of the Getty family.  He is known for having played the roles of Ralph in "Lord of the Flies", Thomas Grace on the American action drama "Alias" and Tommy Walker on the American drama "Brothers & Sisters", the latter two of which have aired on ABC.

Precollection: Precollection is a 2003 album by Lilys released by Manifesto Records.  The album was recorded over two years by the band's only constant member Kurt Heasley with a new line-up of the band, which included producer Mike Musmanno on keyboards.  The album was reissued in 2004 on the Rainbow Quartz International label under the title "The Lilys", with different sleeve art and three bonus tracks.  Lyrical themes include "the acquisition of illegal substances" in the Hunting Park area of Philadelphia on "Will My Lord Be Gardening", which Heasley stated is "about loving someone after they get fucked up, I mean fucked...and that's fucked up," and his relationship with his children ("The Perception Room").  "Will My Lord Be Gardening" was included on the soundtrack of the 2005 film "Waiting...".

Trevor Goodchild: Trevor Goodchild is a fictional character featured in the 1990s animated television series, "Æon Flux", the 2005 "Æon Flux" live-action film, and the 2005 "Æon Flux" video game.  He is played by voice actor John Rafter Lee in the half-hour series (the "Liquid Television" series of shorts had no dialogue).  In the 2005 film, he is portrayed by Marton Csokas.  In the 2005 video game, he is voiced by Troy Baker.

Amu (film): Amu is a 2005 film directed by Shonali Bose, on the 1984 anti-Sikh riots.  The film is based on Bose's own novel by the same name.  It stars Konkona Sen Sharma, Brinda Karat, and Ankur Khanna.  The film premiered at the Berlin Film Festival and the Toronto International Film Festival in 2005.

Insomniac (Enrique Iglesias album): Insomniac is the eighth studio album, and fourth English-language album, released by Spanish singer Enrique Iglesias.  The album was produced by John Shanks, Kristian Lundin, Sean Garrett, Anders Bagge, Jesper Andersen, Mark Taylor, Stargate, and Maratone.  It also contains his first collaboration with a rapper, Lil Wayne, as well as a cover of indie band Ringside's "Tired of Being Sorry".  This album is said to be different from his prior albums, incorporating a more contemporary pop style.  As well as the aforementioned hip hop collaboration, the album also includes elements of R&B and Latin pop.  It was released worldwide on 11 June 2007 and in the USA on 12 June 2007.

Melissa Elias: Melissa Elias (born March 12, 1978) is a Canadian actress.  She stars in the television series "Falcon Beach" on the Global Television Network and ABC Family.  She is in a Lions Gate theatrical picture released in 2005 called Tamara (2005 film).  Elias also stars in the dystopian Gen RX distributed by Tricoast Worldwide, winning 2014 California Film Competition at California Film Awards.

Guess Who (film): Guess Who is a 2005 American comedy film about race relations directed by Kevin Rodney Sullivan.  It is a loose remake of the 1967 film "Guess Who's Coming to Dinner", in the form of a romantic comedy.  While the 1967 film covered interracial romance of a black man with a white woman, the 2005 film covered the topic of a white man with a black woman.  The film stars Bernie Mac, Ashton Kutcher, and Zoe Saldana.

Slingshot (film): Slingshot is a 2005 American independent crime film directed by Jay Alaimo and written by Alaimo & Matt Fiorello and Matthew Quinn Martin.  Story by Martin.  It stars David Arquette, Thora Birch, Balthazar Getty and Julianna Margulies.

Jack Griffo: Jack Davis Griffo (born December 11, 1996) is an American actor and singer.  He stars as Max Thunderman on the Nickelodeon series "The Thundermans".  Griffo also had starring roles in the Nickelodeon original movies "Jinxed" and "Splitting Adam".  In 2013, he released his debut solo single, "Slingshot".

Question: Who is the the actor who stars in the 2005 film Slingshot that also is a member of the band Ringside?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the actor."
        },
        "is_member_of_band": {
          "type": "boolean",
          "description": "Indicates if the actor is a member of a band."
        },
        "band_memberships": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "band_name": {
                "type": "string",
                "description": "The name of the band the actor is a member of."
              }
            },
            "required": [
              "band_name"
            ],
            "additionalProperties": false
          },
          "description": "List of bands the actor is a member of."
        }
      },
      "required": [
        "name",
        "is_member_of_band",
        "band_memberships"
      ],
      "additionalProperties": false
    },
    "film": {
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
        "stars_actor": {
          "type": "boolean",
          "description": "Indicates if the identified actor stars in this film."
        }
      },
      "required": [
        "title",
        "release_year",
        "stars_actor"
      ],
      "additionalProperties": false
    },
    "final_answer_actor_name": {
      "type": "string",
      "description": "The name of the actor who meets all criteria."
    }
  },
  "required": [
    "actor",
    "film",
    "final_answer_actor_name"
  ],
  "additionalProperties": false
}
