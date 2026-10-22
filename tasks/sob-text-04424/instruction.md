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
Lucy Sullivan Is Getting Married: Lucy Sullivan Is Getting Married is an international best selling 1996 novel by Irish author, Marian Keyes.  It chronicles the life of Lucy Sullivan, a 26-year-old perpetually broke, unlucky-in-love office worker from London, who has a penchant for bad boys, a needy, alcoholic and flawed father, a dead-end job and exasperating flat-mates, dippy Charlotte and bossy Karen.  The book is written in the first person and is described by Keyes as a "sideways" sequel to her first novel "Watermelon".  The novel was adapted into a television series in 1999.  It aired on the ITV network, but struggled with numerous scheduling changes.  The series has aired internationally and has been released on DVD.

Spanish Fry: "Spanish Fry" is the 17th episode in the fourth production season of the American animated television series "Futurama".  It originally aired on the Fox network in the United States on July 13, 2003.  Set in a retro-futuristic 31st century, the series follows the adventures of the employees of Planet Express, an interplanetary delivery company.  In this episode, Fry's nose has mysteriously disappeared so he seeks to get it back.  David X. Cohen admitted that this episode is one of the most "filthy" in the series' history.

Gadget Man: Gadget Man (previously Stephen Fry: Gadget Man) is a British television series, which began airing on 19 November 2012 on Channel 4 and is presented by Richard Ayoade, who took over from the previous host, Stephen Fry, from the second series.  Each episode presents a variety of innovative products related to the episode's theme.  The series is filmed in and around The Lime House, a 1930s art deco converted water tower in Norton, Kent.

Lucy Fry: Lucy Elizabeth Fry (born 13 March 1992) is an Australian actress.  She is known for portraying Zoey in "Lightning Point", Lyla in "", and Vasilisa Dragomir in the film "Vampire Academy".  Fry was also cast in Hulu's eight part miniseries "11.22.63" as Marina Oswald, wife of Lee Harvey Oswald, and played the lead in the 2016 Australian horror television series "Wolf Creek".

Wolf Creek (TV series): Wolf Creek is a 2016 Australian horror web television series which screens on Stan.  It is a spin-off of the movies "Wolf Creek" and "Wolf Creek 2" and follows Eve, a 19-year-old American tourist, who is targeted by crazed serial killer Mick Taylor, survives his attack and embarks on a mission of revenge.  The first series of "Wolf Creek" consists of six episodes, and was released on 12 May 2016.  John Jarratt, who portrayed Mick Taylor in the films, reprises his role for the series.  The show was renewed for a second six-episode series in February 2017, and filming began in July.

Fry and Laurie: Fry and Laurie are an English comedy double act, mostly active in the 1980s and 1990s.  The duo consisted of Stephen Fry and Hugh Laurie, who met in 1980 through mutual friend Emma Thompson whilst all three attended the University of Cambridge.  They initially gained prominence in a television sketch comedy, "A Bit of Fry & Laurie" (1987, 1989–1995), and have collaborated on numerous other projects including, most notably, the television series "Jeeves and Wooster" (1990–1993) in which they portrayed P. G. Wodehouse's literary characters Jeeves (Fry) and Wooster (Laurie).

Stephen Fry bibliography and filmography: Stephen Fry is an English actor, comedian, author and television presenter.  With Hugh Laurie, as the comedy double act Fry and Laurie, he co-wrote and co-starred in "A Bit of Fry and Laurie", and the duo also played the title roles in "Jeeves and Wooster".  Fry played the lead in the film "Wilde", was Melchett in the "Blackadder" television series and is the host of celebrity comedy trivia show, "QI".  He has contributed columns and articles for newspapers and magazines, and has written four novels and three autobiographies, "Moab Is My Washpot", "", and "More Fool Me: A Memoir".

Gaols Act 1823: The idea of prison reform was promoted in the early 19th century by Elizabeth Fry and her brother Joseph John Gurney.  In particular, Fry was appalled at the conditions in the women's section of Newgate Prison.  This act was introduced and supported by Home Secretary Robert Peel.  It introduced regular visits to prisoners by chaplains.  It provided for the payment of gaolers, who had previously been paid out of fees that the prisoners themselves were required to pay.  It prohibited the use of irons and manacles.  It also required the installation of female wardens to guard female prisoners.  The act was largely ineffective, because there were no inspectors to make sure that it was being followed.

Charlotte Anley: Charlotte Anley (1796–1893) was a 19th-century English didactic novelist, social and religious writer, composer and lyricist.  She was a Quaker, and spent the years 1836–38 in Australia, researching for a report on women's prisons commissioned by Elizabeth Fry.

John Connor: John Connor is a fictional character of the "Terminator" franchise.  Created by writer and director James Cameron, the character is first referred to in the 1984 film "The Terminator" and first appears in its 1991 sequel "" initially portrayed by Michael Edwards (briefly as the older Connor) and then by teenage actor Edward Furlong throughout the remainder of the film; in addition, Linda Hamilton's real-life son Dalton Abbot played John as a toddler in a dream sequence.  The character is subsequently portrayed by 23-year-old Nick Stahl in the 2003 film "" and by 19-year-old Thomas Dekker in the 2008 television series "".  English actor Christian Bale portrays 33-year-old Connor in the film series's fourth installment, "Terminator Salvation", and Australian actor Jason Clarke portrays a 44-year-old Connor, who becomes the T-3000 and serves as the antagonist of the film series's fifth installment, "Terminator Genisys".

Question: Lucy Elizabeth Fry played the lead in a television series that follows Eve who is a 19-year-old what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "television_series": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "year_released": {
          "type": "integer"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "year_released",
        "genre"
      ],
      "additionalProperties": false
    },
    "character": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "age": {
          "type": "integer"
        },
        "description": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "age",
        "description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress",
    "television_series",
    "character"
  ],
  "additionalProperties": false
}
