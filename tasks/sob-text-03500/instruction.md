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
The Art of Seduction (film): Art of Seduction () is a 2005 South Korean romantic comedy film starring Son Ye-jin, Song Il-gook and directed by Oh Ki-hwan.  It was released on 21 December 2005.

Jeong Jae-heon: Jeong Jae-heon (Korean: 정재헌 ; born April 18, 1975) is a South Korean voice actor and actor.  He joined Munhwa Broadcasting Corporation's voice acting division in 2002.  After being a freelancer, Jae-heon made a brief appearance on a 2005 South Korean film "Quiz King", playing his role as a television news reporter.  The voice actor became popular with his dub of Kiyomaro Takamine on "Zatch Bell! ", which has been one of his signature works.  He gained popularity also by replacing Adam Rodriguez on "", and Archie Kao on "".  In late 2011, Jae-heon once was on stage, portraying Lee Mong-ryong in a South Korean charity play "Hyang-dan, Fly".  He has recently been known for his voicing Shota Kazehaya on the Korean dub of a Japanese television animation series "From Me to You", which made many fans of Jae-heon call him 정재하야 (Jeong-jae-ha-ya, a compound word formed from "Jeong Jae"-heon and Kaze"haya").

Lee Gae-byok: Lee Gae-byok (born September 4, 1971) is a South Korean film director and screenwriter.  Lee debuted with the romantic-comedy "The Beast and the Beauty" (2005).  After a 10-year break, he returned with the 2016 action-comedy film "Luck Key", a box office hit with more than 6.9 million admissions.

Luck Key: Luck Key () is a 2016 South Korean film directed by Lee Gae-byok.  It is a remake of the 2012 Japanese comedy film "Key of Life".

Lee Seok-hoon: Lee Seok-hoon (born January 6, 1972) is a South Korean film director and screenwriter.  Lee began his directorial debut with the high school comedy "See You After School" (2006), followed by romantic comedy "Two Faces of My Girlfriend" (2007) - both films starring Bong Tae-gyu as the leading role.  His romantic comedy "Dancing Queen" (2012) was a commercial success with over four million admissions and the period adventure film "The Pirates" (2014), starring Son Ye-jin and Kim Nam-gil, was also a hit with more than 8.6 million admissions at the end of its run.

My Girl (2005 TV series): My Girl () is a 2005 South Korean television series starring Lee Da-hae, Lee Dong-wook, Lee Joon-gi and Park Si-yeon.  It aired on SBS from December 14, 2005 to February 2, 2006 on Wednesdays and Thursdays at 21:55 for 16 episodes.  The romantic comedy series was a hit during its run—it placed number one in its timeslot and reached a peak viewership rating of 24.9%.  It also catapulted actors Lee Da-hae, Lee Dong-wook and Lee Joon-gi into Korean Wave stardom.

The Beast and the Beauty: The Beast and the Beauty () is a 2005 South Korean romantic comedy film.

Lee Ho-jae: Lee Ho-jae (born January 3, 1973) is a South Korean film director and screenwriter.  Lee debuted with the crime thriller "The Scam" (2009).  The first Korean film to ride the stock market, Lee spent two years researching and interviewing financial traders to achieve authenticity.  He also found himself dabbling in the stock market during that time, and ended up losing about 94 percent of the little amount he had invested.  Lee hopes movie-goers feeling the pinch of the global financial crisis will come out of the theaters feeling hopeful that everyman can come out on top.  It won Best New Director at the 46th Grand Bell Awards in 2009 and 46th Baeksang Arts Awards in 2010.

Lee Hwan-kyung: Lee Hwan-kyung (born 1970) is a South Korean film director and screenwriter.  Lee debuted with "He Was Cool" (2004).  His next two features, "Lump Sugar" (2006) revolves around Si-eun who dreams of becoming a jockey and "Champ" (2011), which is based on a true story, depicts the relationship between a recently injured racehorse and the jockey who is gradually losing his eyesight.  His fourth feature "Miracle in Cell No. 7" (2013) became the biggest hit of the year with more than 12.32 million viewers.

My Boyfriend Is Type B: My Boyfriend is Type B () is a 2005 South Korean romantic comedy film.  The basic premise of the film comes from the blood type personality theory, which claims that a person's blood type can determine their personality traits.  The heroine is type A (conservative and introverted) while her love interest is type B (passionate and irresponsible).

Question: Lee Gae-byok, is a South Korean film director and screenwriter, Lee debuted with which 2005 South Korean romantic comedy film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "nationality",
        "roles"
      ],
      "additionalProperties": false
    },
    "debut_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "genre": {
          "type": "string"
        },
        "is_romantic_comedy": {
          "type": "boolean"
        }
      },
      "required": [
        "title",
        "year",
        "genre",
        "is_romantic_comedy"
      ],
      "additionalProperties": false
    },
    "question_answered": {
      "type": "boolean"
    }
  },
  "required": [
    "director",
    "debut_film",
    "question_answered"
  ],
  "additionalProperties": false
}
