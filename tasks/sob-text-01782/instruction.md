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
Half of My Heart: "Half of My Heart" is a song by American rock singer John Mayer featuring American country pop singer Taylor Swift.  It is the third single from Mayer's 2009 album, "Battle Studies".  Mayer was nominated for a Grammy Award for Best Male Pop Vocal Performance in 2011 for the song.

Seo Jung-won: Seo Jung-Won (born December 17, 1970 in Gwangju, South Korea) is a football player and coach from South Korea.  Nicknamed "nalssen dori" (speedy Gonzales-equivalent in Korean) in his native Korea, he was even offered a contract from Barcelona in his early twenties which he turned down.  As of 2006, he played forward and midfielder for Ried, a club in the Austrian Bundesliga.  Seo moved to Ried from Austria Salzburg in June 2005.

Seo Min-woo: Seo Min-woo (Hangul: 서민우; born February 8, 1985) is a South Korean idol singer and actor.  He is a member of South Korean boy group 100% under the label of TOP Media, as the leader and vocalist.

Seohyun: Seo Ju-hyun (born June 28, 1991), known professionally as Seohyun, is a South Korean singer and actress.  She debuted as a member of girl group Girls' Generation (and later its subgroup TTS) in August 2007, who went on to be one of the best-selling artists in South Korea and one of South Korea's most popular girl groups worldwide.  Apart from her group's activities, she has established herself as an actress, notably through her participation in the original and Korean versions of stage musicals including "Moon Embracing the Sun", "Gone with the Wind" and "Mamma Mia".  She also starred in the drama "".  She debuted as a solo artist with her debut mini album, "Don't Say No", on January 17, 2017, making her the third Girls' Generation member to debut as a solo artist.

John Mayer: John Clayton Mayer ( ; born October 16, 1977) is an American singer-songwriter, guitarist, and producer.  He was born in Bridgeport, Connecticut, and raised in nearby Fairfield.  He attended Berklee College of Music in Boston, but disenrolled and moved to Atlanta in 1997 with Clay Cook.  Together, they formed a short-lived two-man band called Lo-Fi Masters.  After their split, Mayer continued to play local clubs—refining his skills and gaining a following.  After his appearance at the 2001 South by Southwest Festival, he was signed to Aware Records, and then Columbia Records, which released his first EP, "Inside Wants Out".  His following two full-length albums—"Room for Squares" (2001) and "Heavier Things" (2003)—did well commercially, achieving multi-platinum status.  In 2003, he won the Grammy Award for Best Male Pop Vocal Performance for the single "Your Body Is a Wonderland".

Born and Raised World Tour: The Born and Raised World Tour was a concert tour by American singer John Mayer in support of his fifth and sixth studio albums, "Born and Raised" and "Paradise Valley".  On March 22, 2013, the tour was first announced and tickets went on sale March 29 and 30, 2013.  The tour began on July 6, 2013 in Milwaukee and ended in June 2014.  This was Mayer's first tour in three years and after undergoing his vocal surgery.

K-pop: K-pop (abbreviation of Korean pop; Hangul: 케이팝 ) is a music genre originating in South Korea that is characterized by a wide variety of audiovisual elements.  Although it includes all genres of "popular music" within South Korea, the term is often used in a narrower sense to describe a modern form of South Korean pop music drawing inspiration on a range of styles and genres incorporated from the rest of the world such as Western pop music, rock, experimental, jazz, gospel, Latin, hip hop, R&B, reggae, electronic dance, folk, country and classical on top of its uniquely traditional Korean music roots.  The more modern form of the genre emerged with one of the earliest K-pop groups, Seo Taiji and Boys, forming in 1992.  Their experimentation with different styles and genres of music and integration of foreign musical elements helped reshape and modernize South Korea's contemporary music scene.

The Search for Everything: Wave One: The Search for Everything: Wave One (also shortened as Wave One) is an extended play (EP) by American singer John Mayer.  Released on January 20, 2017, the EP contains the first four tracks from Mayer's seventh studio album, "The Search for Everything".  It includes the lead single "Love on the Weekend" and three new tracks.

Seo Taiji: Jung Hyun-Chul (hangul: 정현철; born February 21, 1972), better known as Seo Taiji or Seo Tae-Ji (서태지), is a South Korean singer, musician, songwriter and record producer.  After dropping out of high school to pursue a music career, he has risen to become one of the most prominent and influential cultural icons in South Korea, with many referring to him as "the President of Culture".

Seo Jae-weong: Jae Weong Seo (Hangul: 서재응; Hanja: 徐在應; ] ; born May 24, 1977 in Gwangju, South Korea), usually referred to as simply Jae Seo and pronounced "Jay So", is a retired Korean professional baseball player.  Originally signed by the New York Mets of Major League Baseball, Seo went on to play in the KBO League for the Kia Tigers.

Question: Which singer is from South Korea, Seo Min-woo or John Mayer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_from_south_korea": {
      "type": "string",
      "description": "The name of the singer who is from South Korea."
    },
    "singer_nationality": {
      "type": "string",
      "description": "The nationality of the identified singer."
    },
    "other_singer_name": {
      "type": "string",
      "description": "The name of the other singer mentioned in the question."
    },
    "other_singer_nationality": {
      "type": "string",
      "description": "The nationality of the other singer."
    },
    "is_south_korean": {
      "type": "boolean",
      "description": "True if the identified singer is South Korean, false otherwise."
    }
  },
  "required": [
    "singer_from_south_korea",
    "singer_nationality",
    "other_singer_name",
    "other_singer_nationality",
    "is_south_korean"
  ],
  "additionalProperties": false
}
