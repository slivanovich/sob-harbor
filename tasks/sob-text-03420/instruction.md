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
TV 101: TV 101 is an American drama series that aired on CBS from 1988 until 1989.  The series stars Sam Robards, Brynn Thayer, Leon Russom and Andrew Cassese.  Other notable cast members include Stacey Dash, Teri Polo, Alex Désert and Matt LeBlanc.  The music for this show was created and produced by Todd Rundgren.

Nidhi Yasha: Nidhi Yasha (born 26 April 1983) is an Indian costume designer.  Nidhi designs costumes for "Zee TV"<nowiki>'</nowiki>s "Buddha and Star Plus TV" series Mahabharat (2013 TV series)(2013) with Bhanu Athaiya as her consulting faculty for the show.  Yasha said they studied over 450 books related to period textiles, costume and jewellery to arrive at the look for the show.

Saurav Gurjar: Saurav Gurjar is an Indian professional wrestler, Sportsperson and actor.  He is best known for his role as Bheem in the mythological TV show "Mahabharat".  Recently he has appeared in tv Show Sankatmochan Mahabali Hanuman As a Ravana& Vali (Ramayana) aired on Sony tv.  after Ramayan, after Mahabharat (2013 TV series) he acted/Anchor in Indonesia tv channel one of the popular tv show The New Eat Bulaga!  Indonesia

The Fosters (season 1): The first season of "The Fosters" premiered on June 3, 2013 and ended on March 24, 2014.  The season consisted of 21 episodes and stars Teri Polo and Sherri Saum as Stef Foster and Lena Adams, an interracial lesbian couple, who foster a girl (Maia Mitchell) and her younger brother (Hayden Byerly) while also trying to juggle raising Latino twin teenagers, (Cierra Ramirez and Jake T. Austin), and Stef's biological son (David Lambert).

Tapas Relia: Tapas Relia (Gujarati: તપસ રેલિયા ; born August 11, 1978) is an Indian music composer and producer, known for his famous advertising campaigns for brands like Close-Up (toothpaste), Domino's Pizza, Amaron Batteries, IPL and Mahabharat (2013 TV series).  In Mumbai since 1996, he has also scored music for Bollywood films, including India’s first major commercial animation film ‘Hanuman (2005 film)’ and the recently released film ‘Lakshmi (2014 film)’, a film on child trafficking by acclaimed director Nagesh Kukunoor.  Based in Mumbai, he works and operates from his own recording studio.

List of The Fosters episodes: "The Fosters" is an American drama series on Freeform (then known as ABC Family) that premiered on June 3, 2013.  The series follows the lives of Lena Adams (Sherri Saum) and Stef Foster (Teri Polo), the Fosters, who are an interracial, lesbian couple living in the Mission Bay area of San Diego, raising Stef's biological son, Brandon (David Lambert), along with adopted twins, Jesus (Jake T. Austin/Noah Centineo) and Mariana (Cierra Ramirez).  Lena is a charter school vice principal and Stef is a police officer.  Lena decides to take in "troubled" teenager Callie (Maia Mitchell) and then later her younger brother Jude (Hayden Byerly), who have endured a series of abusive foster homes.

Ali Hassan (actor): Ali Hassan is an Indian actor best known for playing Aryan in the Star Plus show, Kahaani Ghar Ghar Kii.  Apart from this, he has done many roles in various Indian television shows like Raja Ki Aayegi Baraat (TV series), Naaginn, Star One Horror Nights, Veer Shivaji, Mahabharat (2013 TV series), CID, SuperCops vs Supervillains, Savdhaan India, Singhasan Battisi, Sapne Suhane Ladakpan Ke.  As of May 2015 his most recent role was in Aahat.

Adam Willits: Adam Charles Willits (born 18 February 1972) is an Australian actor, best known for being an original cast member of the television soap opera "Home and Away" as foster child Steven Matheson from 1988 to 1991.  In 1995, Willits returned to the show as a regular and a love interest for the character of Selina, portrayed by Tempany Deckert and remained until late 1996 as well as returning for guest stints in 1997, 1998, 2000, 2002, 2003 and most recently in 2008.  He appeared in the film "Mad Max Beyond Thunderdome" and TV series including Hampton Court and All Saints.

Maia Mitchell: Maia Mitchell (born 18 August 1993) is an Australian actress and singer.  She is known for her roles as Brittany Flune in the children's television series "Mortified" for the Nine Network, and as Natasha Ham in the Seven Network's teen drama "Trapped".  For American audiences, she currently co-stars in the Freeform drama "The Fosters" as Callie Jacob.  She also co-starred with Ross Lynch in the Disney Channel original films "Teen Beach Movie" and "Teen Beach 2" as McKenzie.

Jeremy Schoenberg: Jeremy Schoenberg (born May 8, 1972), born in Los Angeles County, California, United States.  Jeremy started out as a child star on both film and television.  He played on "Days of Our Lives" from 1980 to 1982 as Johnny, Marlena's foster child.  Jeremy was nominated for this role in the category of Best Young Actor - Daytime TV Series in the 2nd Annual Young Artist Awards.  He also voiced Linus van Pelt on "Is This Goodbye, Charlie Brown? "

Question: What Australian actress born in 1993 played the tv foster child of Teri Polo in a 2013 tv series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the Australian actress."
    },
    "actress_nationality": {
      "type": "string",
      "description": "The nationality of the actress."
    },
    "actress_birth_year": {
      "type": "integer",
      "description": "The birth year of the actress."
    },
    "tv_series_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the TV series."
        },
        "premiere_year": {
          "type": "integer",
          "description": "The year the TV series premiered."
        },
        "actress_character_name": {
          "type": "string",
          "description": "The name of the character played by the actress."
        },
        "foster_parent_actress_name": {
          "type": "string",
          "description": "The name of the actress who played the foster parent."
        },
        "foster_parent_character_name": {
          "type": "string",
          "description": "The name of the character played by the foster parent actress."
        },
        "relationship_type": {
          "type": "string",
          "description": "The type of relationship between the actress's character and the foster parent's character (e.g., 'foster child')."
        }
      },
      "required": [
        "title",
        "premiere_year",
        "actress_character_name",
        "foster_parent_actress_name",
        "foster_parent_character_name",
        "relationship_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "actress_nationality",
    "actress_birth_year",
    "tv_series_details"
  ],
  "additionalProperties": false
}
