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
Seohyun: Seo Ju-hyun (born June 28, 1991), known professionally as Seohyun, is a South Korean singer and actress.  She debuted as a member of girl group Girls' Generation (and later its subgroup TTS) in August 2007, who went on to be one of the best-selling artists in South Korea and one of South Korea's most popular girl groups worldwide.  Apart from her group's activities, she has established herself as an actress, notably through her participation in the original and Korean versions of stage musicals including "Moon Embracing the Sun", "Gone with the Wind" and "Mamma Mia".  She also starred in the drama "".  She debuted as a solo artist with her debut mini album, "Don't Say No", on January 17, 2017, making her the third Girls' Generation member to debut as a solo artist.

2013 Korean Series: The Best-of-7 2013 Korean Series began on Tuesday, October 24, at the Daegu Baseball Stadium in Daegu, South Korea.  It featured the Samsung Lions, who had claimed homefield advantage by finishing in first place at the end of the regular season, and the Doosan Bears, who finished second during the regular season and defeated the LG Twins in a best-of-5 playoff series (3 games to 2) to advance to the Finals.  The Samsung Lions won the series in seven games to collect their fifth Korean Series championship.

Our Gap-soon: Our Gap-soon () is a 2016–2017 South Korean television series starring Kim So-eun and Song Jae-rim.  This is the first time that a virtual couple from MBC's "We Got Married" co-stars as main cast in a serial drama on a national Korean television network.  It aired on SBS every Saturdays to Sundays at 20:45 (KST) from August 27 to October 30, 2016, and then 2 episodes every Saturdays from November 5, 2016 to April 8, 2017.  This change generated a rating increase that led to an 11-episode extension, making the series end with 61 episodes.

2012 Korean Series: The Best-of-7 2012 Korean Series began on Tuesday, October 24, at the Daegu Baseball Stadium in Daegu, South Korea.  It featured the Samsung Lions, who had claimed homefield advantage by finishing in first place at the end of the regular season, and the SK Wyverns, who finished second during the regular season and defeated the Lotte Giants in a best-of-5 playoff series (3 games to 2) to advance to the Finals.  The Samsung Lions won the series in six games to collect their fifth Korean Series championship.

Bad Thief, Good Thief: Bad Thief, Good Thief (Hangul: 도둑놈, 도둑님 ; RR: "Dodungnom, Dodungnim " ) is a 2017 South Korean television series starring Ji Hyun-woo, Seohyun, Kim Ji-hoon, Lim Ju-eun and others.  It replaced "Father, I'll Take Care For You" and airs on MBC on Saturdays and Sundays at 22:00 (KST) starting May 13, 2017 for 50 episodes.

Takes a Real Man: Takes a Real Man () is a Chinese variety show that airs on Hunan Television.  The show is based on the South Korean series "Real Men" by MBC.  The show is a large national defence education special program in the People's Republic of China.  Season 1 began airing on May 1, 2015, Friday nights at 10:00 PM with 12 episodes total.  Season 2 began airing on October 21, 2016 on Friday nights with 14 episodes total.  Season 3 will start filming on June 18, 2017.

Living Together in Empty Room: Living Together in Empty Room () is a 2017 South Korean television program starring many cast members.  After premiered as the pilots on January 27 and 28, it officially replaced "Duet Song Festival" and began to air on MBC on Fridays at 21:50 (KST) starting April 14, 2017.

Man in the Kitchen: Man in the Kitchen () is a 2017 South Korean television series starring Choi Soo-young, On Joo-wan, Seo Hyo-rim, and Park Jin-woo.  The series aired on MBC every Saturday and Sunday from 8:45 p.m. to 10:00 p.m. (KST).

Radiant Office: Radiant Office (Hangul: 자체발광 오피스 ; RR: "Jachebalgwang Opiseu "; lit.  "Self-Dazzling Office" ) is a 2017 South Korean television series starring Go Ah-sung and Ha Seok-jin.  The series is written by a rookie screenwriter who won the 2016 MBC TV Drama Screenplay Competition in Miniseries category.  It aired on MBC from March 15 to May 4, 2017 on Wednesdays and Thursdays at 22:00 (KST) for 16 episodes.

True Justice (South Korean TV series): True Justice (Korean: 정의본색 ), also known as Define True Colors, is a South Korean variety show that aired on MBC from December 18, 2014 to January 8, 2015.  The show was also broadcast through MBC Plus Media’s four channels: MBC Every1, MBC Music, MBC Dramanet, and MBC Queen.

Question: Seo Ju-hyun stars in a 2017 South Korean series that replaced what show on MBC?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The professional name of the actress."
    },
    "series_starring_actress": {
      "type": "string",
      "description": "The title of the South Korean series the actress starred in."
    },
    "series_year": {
      "type": "integer",
      "description": "The year the series starring the actress aired."
    },
    "replaced_show_name": {
      "type": "string",
      "description": "The title of the show that was replaced by the series starring the actress."
    },
    "network_of_replaced_show": {
      "type": "string",
      "description": "The television network on which the show was replaced."
    }
  },
  "required": [
    "actress_name",
    "series_starring_actress",
    "series_year",
    "replaced_show_name",
    "network_of_replaced_show"
  ],
  "additionalProperties": false
}
