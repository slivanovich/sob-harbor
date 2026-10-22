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
Natalie Zea: Natalie Zea (born March 17, 1975) is an American actress, known for her performances on television.  Zea began her acting career in theatre.  Her first major role was on the NBC daytime soap opera "Passions" (2000–2002), where she played the role of Gwen Hotchkiss.  Her breakout role was on the ABC primetime soap opera "Dirty Sexy Money" as socialite Karen Darling, where she starred from 2007 to 2009.  Zea also has made many guest appearances on television, starred in the number of independent and made-for-television movies, and had the recurring roles in "The Shield", "Hung" and "Californication".

Jennifer Lopez filmography: American entertainer Jennifer Lopez has appeared in many motion pictures and television programs.  She is one of the highest paid actresses in Hollywood and is the highest paid actress of Latin descent, making up to US$15 million per film role.  She is also the richest actress in Hollywood, with an estimated net worth of $320 million (as of 2014).  Lopez made her acting debut at age 16 with a small role in the 1986 film "My Little Girl".  From there, she received her first high-profile job in 1991 as a Fly Girl dancer on the television comedy program "In Living Color".  Following her departure from the show in 1993, Lopez made several guest appearances in the television series "South Central", appeared in the made-for-television movie "Lost in the Wild" (1993) and starred as Melinda Lopez in the television series "Second Chances" (1993) and its spin-off "Hotel Malibu" (1994).  "Second Chances" and "Hotel Malibu" ran for only a brief period, receiving negative reviews.  Lopez's first major film role came in the 1995 motion picture "Money Train", alongside Wesley Snipes and Woody Harrelson.  The film faced negative reviews and is considered to be a box office bomb.  Her next two film roles in "Jack" (1996) and "Blood and Wine" (1997) were received similarly; however, critics were divided by the latter.  Lopez received her first leading role in the Selena biopic of the same name in 1997.  The film was a commercial and critical success and is often cited by critics as her breakout role.  Later that year, Lopez starred as Terri Flores in the film "Anaconda", which garnered negative reviews by critics despite being a box office success.  In 1998, Lopez starred alongside George Clooney in the crime film "Out of Sight" (1998).  The film met with positive reviews and was a box office success.  In the same year, she also lent her voice to the animated film "Antz".

Ang Yaman ni Lola: Ang Yaman ni Lola "(lit.  Grandma's Treasure)" is a weekday comedy-reality show that aired over GMA Network and produced by GMA News and Public Affairs.  It is the counterpart of ABS-CBN's noontime variety show "Pilipinas Win Na Win".  The show features Nanette Inventor as Lola Barbie, a rich and generous old widow who shares her wealth by hiring workers every week.  The workers are real people from different professions chosen via audition.  Every week, new challenges will be given by Lola Barbie and the most efficient worker of the week will receive P100,000.  The show premiered on August 23, 2010 and officially ended on January 21, 2011.

Riz Ahmed: Rizwan Ahmed (Urdu: ‎ ; born 1 December 1982), also known as Riz MC, is a British-Pakistani actor, rapper and activist.  As an actor, he won an Emmy Award, out of two Emmy nominations, and was also nominated for a Golden Globe, Screen Actors Guild Award, and three British Independent Film Awards.  He was initially known for his work in independent films such as "The Road to Guantanamo" (2006), "Shifty" (2008), "Four Lions" (2010), "Trishna" (2011), and "Ill Manors" (2012), before his breakout role in "Nightcrawler" (2014).  In 2016, he starred in "Una", "Jason Bourne", and as Bodhi Rook in the first "Star Wars" "Anthology" film, "Rogue One".  That year, he also starred in the HBO miniseries "The Night Of" as Nasir Khan; the show and his performance were critically lauded.  At the 2017 Emmy Awards, he received two nominations, for his performance in "The Night Of" and his guest spot in "Girls"; he won the award for Outstanding Lead Actor in a Limited Series or Movie for "The Night Of", becoming the first Asian and first Muslim to win in the category, the first South Asian male to win an acting Emmy, and the first Muslim and first South Asian to win a lead acting Emmy.

Grandma (film): Grandma is a 2015 American comedy-drama film written, produced, and directed by Paul Weitz.  It stars Lily Tomlin as Elle, a lesbian poet and widow whose teenage granddaughter (played by Julia Garner) visits her to ask for money for an abortion.  Over the space of a day, they visit numerous people from Elle's past to call in favors in an effort to raise the money.

Masiela Lusha: Masiela Lusha ( ; born October 23, 1985) is an American actress, author, producer and humanitarian.  Lusha gained worldwide recognition for playing her first major role as Carmen Consuelo Lopez on the globally syndicated ABC sitcom "George Lopez", a role which earned her two consecutive Young Artist Awards for Leading Young Actress in a Comedy or Drama.  After transitioning into film, she had her breakout role in Sony Picture's "".  Lusha also starred alongside David Hasselhoff and Ian Ziering in SyFy's television movie "".

Megan Fox: Megan Denise Fox (born May 16, 1986) is an American actress and model.  She began her acting career in 2001, with several minor television and film roles, and played a regular role on the "Hope & Faith" television sitcom.  In 2004, she made her film debut with a role in the teen comedy "Confessions of a Teenage Drama Queen".  In 2007, she co-starred as Mikaela Banes, the love interest of Shia LaBeouf's character, in the blockbuster action film "Transformers", which became her breakout role.  Fox reprised her role in the 2009 sequel, "".  Later in 2009, she starred as the eponymous lead in the black comedy horror film "Jennifer's Body".

Breakthrough role: A breakthrough role, also known as breakout role, is a term in the film industry to describe the performance of an actor or actress in a film or television show which contributed significantly to the development of their career and beginning of critical recognition.  Such a moment in an actor's career may often occur some time after they begin acting as their roles become more substantial.  Often a breakthrough role is a significant increase in importance in the actor's part in the film moving up from a minor character or extra to one of the leading cast, or a "high impact" role in a film which has mainstream success and results in the widespread recognition or popularity of the actor.  Martin Shingler defines a breakthrough performance as one which "attracts the attention of film critics, or receives rave reviews and is subsequently nominated for a major film award."

Lily Tomlin: Mary Jean "Lily" Tomlin (born September 1, 1939) is an American actress, comedian, writer, singer, and producer.  Tomlin began her career as a stand-up comedian, and performing Off-Broadway during the 1960s.  Her breakout role was performing as a cast member on the variety show "Rowan & Martin's Laugh-In" from 1969 until 1973.  She currently stars on the Netflix series "Grace and Frankie" as Frankie Bergstein.  Her performance as Frankie garnered her three consecutive nominations for the Primetime Emmy Award for Outstanding Lead Actress in a Comedy Series in 2015, 2016, and 2017.

The Flip Wilson Show: The Flip Wilson Show was an hour-long variety show that aired in the U.S. on NBC from September 17, 1970 to June 27, 1974.  The show starred American comedian Flip Wilson; the program was one of the first American television programs starring a black person in the title role to become highly successful with a white audience.  Specifically, it was the first successful network variety series starring an African American.  During its first two seasons, its Nielsen ratings made it the nation's second most watched show.

Question: Grandma was a film that starred the actree and comedian who had a breakout role on what variety show?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "starring_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress who starred in the film."
        },
        "breakout_role_details": {
          "type": "object",
          "properties": {
            "role_description": {
              "type": "string",
              "description": "Description of the breakout role."
            },
            "show_title": {
              "type": "string",
              "description": "The title of the show where the breakout role occurred."
            },
            "show_type": {
              "type": "string",
              "description": "The type of show (e.g., variety show, sitcom)."
            }
          },
          "required": [
            "role_description",
            "show_title",
            "show_type"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "breakout_role_details"
      ],
      "additionalProperties": false
    },
    "answer_variety_show_title": {
      "type": "string",
      "description": "The title of the variety show where the actress had her breakout role."
    }
  },
  "required": [
    "film_title",
    "starring_actress",
    "answer_variety_show_title"
  ],
  "additionalProperties": false
}
