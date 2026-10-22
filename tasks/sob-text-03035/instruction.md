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
Bright Young Things (film): Bright Young Things is a 2003 British drama film written and directed by Stephen Fry.  The screenplay, based on the 1930 novel "Vile Bodies" by Evelyn Waugh, provides satirical social commentary about the Bright Young People: young and carefree London aristocrats and bohemians, as well as society in general, in the late 1920s through to the early 1940s.  It was John Mills' final film before his death in 2005.

Elizabeth Taylor: Dame Elizabeth Rosemond Taylor, DBE (February 27, 1932 – March 23, 2011) was a British-American actress, businesswoman, and humanitarian.  She began her career as a child actress in the early 1940s, and was one of the most popular stars of classical Hollywood cinema in the 1950s.  She continued her career successfully into the 1960s, and remained a well known public figure for the rest of her life.  In 1999, the American Film Institute named her the seventh-greatest female screen legend.

Jenny Agutter: Jennifer Ann Agutter {'1': ", '2': ", '3': 'OBE', '4': "} (born 20 December 1952) is a British actress.  She began her career as a child actress in 1964's "East of Sudan" and went on to appear in "Star! " and two adaptations of "The Railway Children"—the BBC's 1968 television adaptation and the 1970 film version.  She also starred in the critically acclaimed 1971 film "Walkabout", before moving to Hollywood in 1974.  Her Hollywood film roles included parts in "Logan's Run" (1976), "An American Werewolf in London" (1981) and "Child's Play 2" (1990).  Agutter won the Emmy Award for Outstanding Supporting Actress in a Drama for the 1971 TV film "The Snow Goose", and the BAFTA Award for Best Actress in a Supporting Role for playing Jill Mason in the 1977 film "Equus".

Jane Withers: Jane Withers (born April 12, 1926) is an American actress, model, and singer.  Beginning a prolific career as a child actress at the age of three, Withers is a Young Artist Award–Former Child Star "Lifetime Achievement" Award honoree, best known for being one of the most popular child film stars of the 1930s and early 1940s, as well as for her portrayal of "Josephine the Plumber" in a series of TV commercials for Comet cleanser in the 1960s and early 1970s and probably best known for playing the obnoxious Joy Smythe in the movie she paired with Shirley Temple, "Bright Eyes".  Also a singer, she debuted the Jule Styne-Sammy Cahn torch song "Guess I'll Hang My Tears Out to Dry" in 1944 in "Glad To See You", a musical intended for Broadway which closed out of town in Philadelphia.

Boom! (film): Boom!  is a 1968 British drama film starring Elizabeth Taylor, Richard Burton and Noël Coward, directed by Joseph Losey, and adapted from the play "The Milk Train Doesn't Stop Here Anymore" by Tennessee Williams.

Margaret O'Brien: Margaret O'Brien (born Angela Maxine O'Brien; January 15, 1937) is an American film, radio, television, and stage actress.  Beginning a prolific career as a child actress in feature films for Metro-Goldwyn-Mayer at the age of four, O'Brien became one of the most popular child stars in cinema history and was honored with a Juvenile Academy Award as the outstanding child actress of 1944.  In her later career, she appeared on television, on stage, and in supporting film roles.

Katy Kurtzman: Katy Kurtzman (born September 16, 1965, Washington, D.C.) is an American actress.  She began her career as a child actress.  In 1977, Michael Landon cast Katy as stuttering Anna who was abused by Nellie on "Little House on the Prairie".  Katy also starred in the "Little House on the Prairie" fourth season episode "I Remember, I Remember" with Matthew Laborteaux, playing young Caroline and young Charles, respectively.  This episode aired on January 23, 1978 and is Production # 4016.

Sowcar Janaki: Sankaramanchi Janaki (born 12 December 1931), popularly known as Sowcar Janaki, is a south-Indian actress who has acted in over 387 Tamil, Telugu, Kannada, Hindi and Malayalam films.  She also performed on stage in over 300 shows and was a radio artist during her earlier years.  Her career as film actress began after her marriage only.  She became a popular actress with hits across languages between 1949 and 1975 as the lead heroine such as "Sowcar" (Telugu), Valayapathy, Rojulu Marayi in Telugu, then in Tamil like Naan Kanda Sorgam, Kaviya Thalavi, Bhagya Lakshmi, Pallum Pazhamum, Paar Magale Paar, Thayikku Thalaimagan, Kumudham, Panam Paadithavan, "Puthiya Paravai" , Bama Vijayam, Oli Villaku, Ethir Neechal,Maanavan, Uyardha Manidhan, Nimarundhu Nil, Thunaivan, Needhi and "Iru Kodugal" (Tamil), with Kannada films like Devakaanika, Saaku Magalu, Sadarame, Thayige Thakka Maga and then with Malayalam debut Schoolmaster (1964) and with a film in Hindi - Teen Bahuraniyan.  She worked with famous directors such as Dada Mirasee and K Balachandar.  She moved to supporting roles after 1975 and her performances in Cinema Paithiyam, Thee, Thillu Mullu, Vetri Vizha, Kaanche were widely appreciated.  She served as jury member for the National Indian Films awards committee and as chair person for state Telugu Films awards committee.

Yoo Yeon-mi: Yoo Yeon-mi (born July 7, 1999) is a South Korean actress.  She began her career as a child actress, notably in Jeon Soo-il's indie film "With a Girl of Black Soil" (2007), for which she received the Best Actress award at the Marrakech International Film Festival.  Yoo also starred in the television dramas "Golden Apple" (2005), "Great Expectations" (2006), and "Missing You" (2012).

Tanvi Hegde: Tanvi Hegde is an Indian film and television actress.  Her family is from Karnataka.  She started her career as a child actress in Hindi films and television series.  She started her career at the age of 3 by winning the Rasna Baby contest and did a campaign for the same.  She is widely known for her lead role of Frooti in the highly successful children's television serial "Son Pari", that aired on Star Plus.  She also appeared in some episodes of another successful children's show "Shaka Laka Boom Boom", also on Star Plus.  Hedge has been a part of more than 150 commercials.

Question: What actress began her career as a child actress in the early 1940s and also starred in the British drama film Boom!?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who meets the specified criteria."
    },
    "career_start_details": {
      "type": "object",
      "properties": {
        "started_as_child_actress": {
          "type": "boolean",
          "description": "Indicates if the actress began her career as a child actress."
        },
        "child_career_start_period": {
          "type": "string",
          "description": "The specific period when the actress started her career as a child actress."
        }
      },
      "required": [
        "started_as_child_actress",
        "child_career_start_period"
      ],
      "additionalProperties": false
    },
    "film_appearance": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film the actress starred in."
        },
        "film_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "film_genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "other_starring_actors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other prominent actors who starred in the film."
        }
      },
      "required": [
        "film_title",
        "film_year",
        "film_genre",
        "other_starring_actors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "career_start_details",
    "film_appearance"
  ],
  "additionalProperties": false
}
