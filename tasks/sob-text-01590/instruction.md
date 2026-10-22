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
Butterfly Collectors: Butterfly Collectors is a two part ITV miniseries.  It was broadcast between 19 April and 20 April 1999.  A two-part psychological thriller about a disillusioned policeman who develops an unlikely friendship with two teenagers arrested for murder.  "Butterfly Collectors" was written by Paul Abbott, who has also written for many other television serials including "Shameless", "Clocking Off" and "Children's Ward".  The drama stars British actor Pete Postlethwaite, who is supported by actress and comedian Crissy Rock.

Noah's Ark (1928 film): Noah's Ark is a 1928 American epic romantic melodramatic disaster film directed by Michael Curtiz and starring Dolores Costello and George O'Brien.  The story is by Darryl F. Zanuck.  The film was released by the Warner Bros. studio.  It is representative of the transition from silent movies to "talkies", although it is essentially a hybrid film known as a part-talkie, which used the new Vitaphone sound-on-disc system.  Most scenes are silent with a synchronized music score and sound effects, in particular the biblical ones, while some scenes have dialogue.

2012 (film): 2012 is a 2009 American epic disaster film directed by Roland Emmerich, and stars John Cusack, Chiwetel Ejiofor, Amanda Peet, Oliver Platt, Thandie Newton, Danny Glover and Woody Harrelson.  The film was produced by Centropolis Entertainment and distributed by Columbia Pictures.

Chiwetel Ejiofor: Chiwetel Umeadi Ejiofor, CBE ( ; born 10 July 1977) is a British actor.  After enrolling at the National Youth Theatre in 1995, and gaining a scholarship to the London Academy of Music and Dramatic Art, at age 19 and three months into his course, Ejiofor was cast by Steven Spielberg to play a supporting role in the film "Amistad" (1997) as James Covey.

Fire! (1977 film): Fire!  is a 1977 American made-for-television action-drama disaster film produced by Irwin Allen starring Ernest Borgnine, Vera Miles, Patty Duke Astin, Alex Cord, Donna Mills, Lloyd Nolan, Neville Brand, Ty Hardin and Erik Estrada.  It was directed by Earl Bellamy, who directed another made-for-TV disaster film one year before titled "Flood! ".

Tidal Wave (film): Tidal Wave () is a 2009 South Korean disaster film.  Billed as South Korea's first disaster film, "Tidal Wave" is directed by Yoon Je-kyoon and stars Sol Kyung-gu, Ha Ji-won, Park Joong-hoon and Uhm Jung-hwa.

Sylvia (1985 film): Sylvia (1985) is a biographical film about New Zealand educator Sylvia Ashton-Warner, inspired by two of her books.  The film was directed and co-written by New Zealander Michael Firth, and stars British actor Eleanor David as Ashton-Warner, alongside Tom Wilkinson, Nigel Terry and Mary Regan.

The Crossing (2014 film): The Crossing (Chinese: 太平轮) is a 2014 Chinese-Hong Kong epic historical romance-war drama (part 1) and disaster film (part 2) directed by John Woo and written by Hui-Ling Wang.  The film stars Zhang Ziyi, Takeshi Kaneshiro, Song Hye-kyo, Huang Xiaoming, Tong Dawei and Masami Nagasawa.  The film is based on the sinking of the steamer "Taiping" in 1949.  The incident led to the deaths of over 1,500 passengers and crew.  The film's first part was released in China on December 2, 2014.  Part two was released on July 30, 2015.

Into the Storm (2014 film): Into the Storm is a 2014 American found footage disaster film directed by Steven Quale, written by John Swetnam, starring Richard Armitage and Sarah Wayne Callies.  The film was released by Warner Bros.  Pictures on August 8, 2014.  It is a meteorological disaster film about a rash of tornadoes striking Silverton, Oklahoma.

The Javone Prince Show: The Javone Prince Show is a 2015 variety/comedy sketch show, produced by BBC.  The show stars British actor Javone Prince, best known for his role as Jerwayne in "PhoneShop".  In 2016, Prince was nominated for the British Academy Television Award for Best Male Comedy Performance for his work on the show.

Question: Who directed "2012," an American epic disaster film which stars British actor Chiwetel Umeadi Ejiofo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "key_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of key actors starring in the film."
    },
    "british_actor_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the British actor mentioned in the question."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_genre",
    "director_name",
    "key_actors",
    "british_actor_info"
  ],
  "additionalProperties": false
}
