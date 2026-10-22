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
Natasha Henstridge: Natasha Tonya Henstridge (born August 15, 1974) is a Canadian actress and former fashion model.  In 1995, she came to prominence with her debut movie role as the genetically engineered human-alien hybrid Sil in the science-fiction thriller "Species", then the human-alien hybrid Eve in "Species II" and "Species III".  Other notable on-screen roles include "The Whole Nine Yards", "The Whole Ten Yards", "It Had to Be You", "Ghosts of Mars", "She Spies", the television series "Eli Stone", and the Canadian miniseries "Would Be Kings", for which she won the Gemini Award for best actress.  Her most recent role is as Dawn Chamberlain on the television series "The Secret Circle".

Sunshine (1973 film): Sunshine is a 1973 made-for-television docudrama, directed by Joseph Sargent and produced by George Eckstein, about a young wife and mother who dies of cancer at age 20.  The movie starred Cristina Raines in the lead role of Kate Hayden (Raines' first big movie role), Cliff DeYoung as Kate's husband Sam Hayden, and twins Lindsay and Sidney Greenbush as Jill, Kate and Sam's daughter, as a toddler.  The movie originally aired on CBS as an episode of the "CBS Friday Night Movie" on November 9, 1973.  When first aired, "Sunshine" was the most watched made-for-TV movie in history.  The film used John Denver's song "Sunshine on My Shoulders" as a theme.

Caitlin Stasey: Caitlin Jean Stasey (born 1 May 1990) is an Australian actress.  She is known for her role as Rachel Kinski in "Neighbours".  Previously she played Francesca Thomas in "The Sleepover Club", although her breakthrough movie role came in "Tomorrow, When the War Began", a 2010 movie adaption of the teen novel of the same name in which she played lead protagonist Ellie Linton.  She also played Lady Kenna in the American series "Reign" from 2013 to 2015 and had a recurring role in the ABC2 series "Please Like Me" from 2013 to 2016.  In 2017 Stasey starred as Ada on the Fox television drama "APB", which was cancelled after one season in May 2017.

Kariya (film): Kariya is a 2003 Kannada film directed by Prem, starring Darshan Thoogudeep and Abinayasri.  The sequel of this film titled Kariya 2 is set to release in 2017 starring Santosh Balaraj and Mayuri Kyatari

Night After Night (film): Night After Night is a 1932 American Pre-Code drama film starring George Raft, Constance Cummings, and Mae West in her first movie role.  Others in the cast include Wynne Gibson, Alison Skipworth, Roscoe Karns, Louis Calhern, and Bradley Page.  Directed by Archie Mayo, it was adapted for the screen by Vincent Lawrence and Kathryn Scola, based on the Cosmopolitan magazine story "Single Night" by Louis Bromfield, with West allowed to contribute to her lines of dialogue.

Mercy chinwo: Mercy Chinwo is a Nigerian singer and actress, who came into limelight for winning the Etisalat and Pepsi sponsored, Nigerian Idol, Season 2 in 2012.  She started her musical career by lending her vocals to musical projects by popular Nigerian gospel music artists such as Sammie Okposo, JoePraize, Buchi, Chris Morgan, and Preye.  A year after winning the Nigerian Idols, she nicked her first movie role in Yvonne Nelson's award winning movie,House of Gold starring alongside Yvonne Nelson, Majid Michel, Omawumi, Ice Prince, Francis Odega and Eddie Watson, where she was also nominated at the 2013 Ghana Movie Awards for best music, original song.

The Test of Honor: The Test of Honor (1919) is an American silent film drama produced by Famous Players-Lasky, released by Paramount, directed by John S. Robertson, and starring John Barrymore.  Considered the actor's first drama movie role after years of doing film comedies and farces.  It is based on author E. Phillips Oppenheim 1906 novel "The Malefactor".

Baywatch (film): Baywatch is a 2017 American action comedy film directed by Seth Gordon and based on the television series of the same name.  Written by Mark Swift and Damian Shannon, the film stars Dwayne Johnson, Zac Efron, Priyanka Chopra, Alexandra Daddario, Kelly Rohrbach and Jon Bass.  The plot follows lifeguard Mitch Buchannon and his team, who in an effort to save their beach have to take down a druglord.

Aquaman (film): Aquaman is an upcoming American superhero film based on the DC Comics character of the same name, distributed by Warner Bros.  Pictures.  It is intended to be the sixth installment in the DC Extended Universe (DCEU).  The film is being directed by James Wan, with a screenplay by Will Beall, from a story by Wan and Geoff Johns, and stars Jason Momoa, Amber Heard, Patrick Wilson, Willem Dafoe, Yahya Abdul-Mateen II, Temuera Morrison, Dolph Lundgren, and Nicole Kidman.

Yahya Abdul-Mateen II: Yahya Abdul-Mateen II is an American actor, best known for his role Cadillac in the television series "The Get Down".  He also starred in "Baywatch" (2017), and will appear in "The Greatest Showman" and DC's "Aquaman".

Question: Yahya Abdul-Mateen II's 2017 starring movie role was directed by this individual?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "movie_role_year": {
      "type": "integer",
      "description": "The year of the actor's starring movie role."
    },
    "movie_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the movie."
        },
        "director": {
          "type": "string",
          "description": "The director of the movie."
        }
      },
      "required": [
        "title",
        "director"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "movie_role_year",
    "movie_details"
  ],
  "additionalProperties": false
}
