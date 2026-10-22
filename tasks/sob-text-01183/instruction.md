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
Modern Family: Modern Family (stylized as modern family) is an American television mockumentary family sitcom that premiered on ABC on September 23, 2009, which follows the lives of Jay Pritchett and his family, all of whom live in suburban Los Angeles.  Pritchett's family includes his second wife, her son and his stepson, as well as his two adult children and their spouses and children.  Christopher Lloyd and Steven Levitan conceived the series while sharing stories of their own "modern families".  "Modern Family" employs an ensemble cast.  The series is presented in mockumentary style, with the fictional characters frequently talking directly into the camera.  The series premiered on September 23, 2009, and the ninth season premiered on September 27, 2017.  The series was renewed for a tenth season on May 10, 2017.

Busy Philipps: Elizabeth Jean "Busy" Philipps (born June 25, 1979) is an American actress, known for her supporting roles on the television series "Freaks and Geeks" and "Dawson's Creek".  She has also performed significant roles in films like "The Smokers" (2000), as Karen Carter, the drama film "Home Room" (2002) as Alicia Browning, she appeared in "White Chicks" (2004), played a supporting role in "Made of Honor" (2008) and appeared in "He's Just Not That Into You" (2009).  She played Laurie Keller in the TV series "Cougar Town" for which she won the Critics' Choice Television Award for Best Supporting Actress in a Comedy Series in 2011.

Pilot (Modern Family): The pilot episode of the television series "Modern Family", written by Steven Levitan and Christopher Lloyd and directed by Jason Winer, premiered on ABC in the United States on September 23, 2009.  The pilot introduces viewers to three sets of people who make up a single family.  The episode is shot in a mockumentary style, with a cameraman following the characters around their everyday lives and interviewing them at various intervals.  It cuts between the experiences of the three separate units before they all come together at the end of the episode.

Charlie Babcock: Charlie Babcock (born 1979) is an American actor born in Grosse Pointe, Michigan as Charles William Babcock.  Babcock has guest starred on several present-day television programs which include a recurring role on the ABC series "Desperate Housewives" as Stu who was Lynette Scavo's assistant at Parcher & Murphy until he sued his boss (Joely Fisher) for a sexual harassment suit.  Other guest star appearances include "8 Simple Rules" and "Cold Case".  He is also known for parts in "Special" (2006), "RewinD" (2005) and "Spoonaur" (2004)

Conan the Adventurer (1997 TV series): Conan The Adventurer is a weekly one hour American television live action-adventure series.  It was produced by Max A. Keller and Micheline Keller from 1997 to 1998 and loosely based on the fantasy hero Conan the Barbarian.  The TV show premiered on September 22, 1997.  It comprised 22 episodes and was filmed mainly in Puerto Vallarta, Jalisco, Mexico.  The series has reached many countries of the world, more than 150.  Keller Entertainment Group, the same production company responsible for the series "" and "Acapulco H.E.A.T.", continues to market and distribute the series worldwide and the series has longevity among international broadcasters and DVD aggregators.  The role of Conan was played by Ralf Moeller (AKA Rolf Muller), two time Mr. Universe, a native of Germany, and friend to Arnold Schwarzenegger.  The rest of the ensemble cast included Danny Woodburn (Otli), Robert McRay (Zzeben), T.J. Storm (Bayu), Aly Dunne (Karella), and briefly, Andrew Craig (Vulkar).  The script for the 2 hour pilot was written by Steve Hayes, the head of Project Development for the series.  The show was not promoted to be "authentic Conan", but rather a mixture of Arnold Schwarzenegger's and John Milius' interpretation of Conan.  Indeed, the storyline deviated from the essence of the Conan character, as well as that of the Conan earlier depicted in the various Conan comic book series by Marvel Comics, because the adaptation was too peaceful and childish.

Marcus Welby, M.D.: Marcus Welby, M.D. was an American medical drama television program that aired Tuesdays at 10:00–11:00 p.m. (EST) on ABC from September 23, 1969 to July 29, 1976.  It starred Robert Young as the title character, a family practitioner with a kind bedside manner, who was on a first name basis with many of his patients (and who also made house-calls), James Brolin, as Steve Kiley, M.D, a younger doctor who played Welby's partner, and Elena Verdugo, who played Welby and Kiley's dedicated and loving nurse and office manager, Consuelo Lopez.  "Marcus Welby, M.D.", was produced by David Victor and David J. O'Connell.  The pilot, "A Matter of Humanities", had aired as an "ABC Movie of the Week" on March 26, 1969.

A Gifted Man: A Gifted Man is an American television series, which premiered on CBS on September 23, 2011.  The series is about a talented but self-absorbed surgeon (Patrick Wilson) who starts questioning his purpose in life when he is visited by the spirit of his deceased ex-wife (Jennifer Ehle).  The pilot episode was directed by Jonathan Demme, who also served as an executive producer on the show along with writer Susannah Grant.  The first thirteen episodes were aired in the Friday 8:00 p.m. timeslot (September 23, 2011 – February 10, 2012), while the final three episodes of the 16 episode season order were aired in the Friday 9:00 p.m. timeslot (February 17, 2012 – March 2, 2012).

Cougar Town: Cougar Town is an American television sitcom that ran for 102 episodes over six seasons, from September 23, 2009 until March 31, 2015.  The first three seasons aired on ABC, with the series moving to TBS for the final three seasons.  The pilot episode was broadcast after "Modern Family".  ABC officially gave the series a full season pickup on October 8, 2009.

Steve Arbuckle: Stephen "Steve" George Arbuckle is a Canadian born actor born in the village of Donkin (Arbuckle Lane), Cape Breton Island, Nova Scotia.  He started his career as a theatre actor at Cape Breton University, then made his first move into film in 2003 with the lead role in the short film "Todd and the Book of Pure Evil", which also starred Julian Richings and John Bregar.  He appeared as Oliver Peele in 2010 in the pilot episode of the CBS show "Blue Bloods".  Arbuckle is now living in Toronto, Ontario.

Pilot (Cougar Town): "Pilot" is the pilot episode of the American television sitcom "Cougar Town", which premiered on ABC on September 23, 2009.  The episode was directed by series creator Bill Lawrence, and written by Lawrence and Kevin Biegel.  The pilot introduces seven main cast members: Jules Cobb (Courteney Cox) as a 40-year-old mother who’s newly single; Ellie Torres (Christa Miller), Jules' next door neighbor and best friend; Laurie Keller (Busy Philipps), Jules' younger employee; Bobby Cobb (Brian Van Holt), Jules' unemployed ex-husband; Travis Cobb (Dan Byrd), Jules' 17-year-old son; Andy Torres (Ian Gomez), Ellie's husband; and Grayson Ellis (Josh Hopkins), Jules' newly divorced neighbor.

Question: When was the actor born who starred in Pilot as Laurie Keller which premiered on ABC on September 23, 2009?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "role": {
      "type": "string"
    },
    "episode": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "series_title": {
          "type": "string"
        },
        "premiere_date": {
          "type": "string",
          "format": "date"
        },
        "network": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "series_title",
        "premiere_date",
        "network"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor",
    "role",
    "episode"
  ],
  "additionalProperties": false
}
