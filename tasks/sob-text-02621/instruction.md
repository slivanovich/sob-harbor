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
Linda Aronson: Linda Aronson (born 20 March 1950) is a British-born Australian screenwriter.  She wrote the film "Kostas".  She also wrote "The 21st Century Screenplay."

Ken Shadie: Kenneth George "Ken" Shadie {'1': ", '2': ", '3': ", '4': "} (born 8 December 1935) is an Australian screenwriter, who co-wrote the Academy Award-nominated screenplay for the film "Crocodile Dundee" with Paul Hogan and John Cornell.

Mark Hoffman: Detective Lieutenant Mark Hoffman is a fictional character from the "Saw" franchise.  He is portrayed by Australian actor Costas Mandylor.  While the character was first shown as a police officer in "Saw III", later films in the series have expanded his role and revealed him to be an apprentice, and subsequently the successor of the Jigsaw Killer.  Like his mentor and partner, he designs death traps that, for survivors, give them reason to appreciate their lives.  On the other hand, he has no emotion towards his victims, and in general, brandishes a very monotone personality.

Saw III: Saw III is a 2006 American horror film directed by Darren Lynn Bousman from a screenplay by Leigh Whannell and story by James Wan and Whannell.  It is the third installment in the "Saw" franchise and stars Tobin Bell, Shawnee Smith, Angus Macfadyen, Bahar Soomekh, and Dina Meyer.  "Saw III" marks the first appearances of Costas Mandylor and Betsy Russell, albeit minor roles; they would later become major characters in the series.

Jimmy Jack: Jimmy Jack, also credited as Jimmy the Exploder, is an Australian screenwriter, film director, actor and producer best known for achieving success following his work on the 2008 film "The Black Balloon".

Leigh Whannell: Leigh Whannell (born 17 January 1977) is an Australian screenwriter, producer, director and actor.  He is best known for writing films directed by his friend James Wan, including "Saw" (2004), "Dead Silence" (2007), "Insidious" (2011) and "" (2013).  Whannell made his directorial debut on "", which was released in 2015.

Stuart Beattie: Stuart Beattie (born 1972) is an Australian screenwriter and film director.  His screenplay for "Collateral" (2004) earned him nominations for the BAFTA Award for Best Original Screenplay, Satellite Award for Best Original Screenplay and Saturn Award for Best Writing.

Jigsaw (Saw franchise): John Kramer—known as The Jigsaw Killer or simply Jigsaw—is a fictional character and appearing in the "Saw" franchise as the main antagonist.  Jigsaw made his debut in the first film of the series, "Saw", and he later appeared in "Saw II", "Saw III", "Saw IV", "Saw V", "Saw VI", "Saw 3D" and, eventually, "Jigsaw".  He is portrayed by American actor Tobin Bell.

David Tapp: Detective David Tapp is a fictional character from the "Saw" franchise, introduced in "Saw" and featured through archive footage in "Saw III" and "Saw V".  He also appears in the 2009 "Saw: The Video Game" as the lead character.  He was portrayed by actor Danny Glover in the films and voiced by Earl Alexander in the game.

Gregg Hoffman: Gregg Hoffman (June 11, 1963 – December 4, 2005), born in Phoenix, Arizona, was a film producer responsible for developing "Saw" and "Saw II".  He studied communications, law and economics at American University in Washington, D.C.  Hoffman was working on "Saw III" and other films for Twisted Pictures when he died in a hospital in Hollywood, California of natural causes.  He was 42 years old at his death.  The movie "Dead Silence" (2007) was dedicated to him.  He was also thanked in the movie "Gross misconduct", mentioned as dedicatee for "Saw III", and posthumously credited with producing the "Saw" films from 2007 through 2017.

Question: When was the Australian screenwriter, producer, director and actor born who screenplay the Saw III?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the individual."
    },
    "person_nationality": {
      "type": "string",
      "description": "The nationality of the individual."
    },
    "person_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professional roles held by the individual."
    },
    "film_screenplay_credit": {
      "type": "string",
      "description": "The title of the film for which the individual wrote the screenplay."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the individual."
    }
  },
  "required": [
    "person_name",
    "person_nationality",
    "person_roles",
    "film_screenplay_credit",
    "birth_date"
  ],
  "additionalProperties": false
}
