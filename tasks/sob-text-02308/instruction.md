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
List of The Simpsons video games: "The Simpsons" is an American animated television sitcom created by Matt Groening for the Fox Broadcasting Company.  The series is a satirical parody of a middle class American lifestyle epitomized by its eponymous family, which consists of Homer, Marge, Bart, Lisa and Maggie.  It is set in the fictional town of Springfield, and lampoons American culture, society and television, and many aspects of the human condition.  The family was conceived by Groening shortly before a pitch for a series of animated shorts with producer James L. Brooks.  Groening created a dysfunctional family and named the characters after members of his own family, substituting Bart for his own name.  The shorts became a part of "The Tracey Ullman Show" on April 19, 1987 and after a three-season run, the sketch was developed into a half-hour prime time show and became a hit series for Fox.  The growing popularity of the series motivated video game developers to create video games based on the series.  Two pinball machines have also been produced; one self-titled, that was only made available for a limited time after the first season finale (1990) and "The Simpsons Pinball Party" (2003).  Additionally, several handheld device games have been released, such as "Bartman: Avenger of Evil" (1990) and "Bart Simpson's Cupcake Crisis" (1991).

Simpson family: The Simpson family are cartoon characters featured in the animated television series "The Simpsons".  The Simpsons are a nuclear family consisting of married couple Homer and Marge and their three children Bart, Lisa and Maggie.  They live at 742 Evergreen Terrace in the fictional town of Springfield, United States and they were created by cartoonist Matt Groening who conceived the characters after his own family members, substituting "Bart" for his own name.  The family debuted April 19, 1987 in "The Tracey Ullman Show" short "Good Night" and were later spun off into their own series which debuted on December 17, 1989.

Maggie Simpson: Margaret Evelyn "Maggie" Simpson is a fictional character in the animated television series "The Simpsons".  She first appeared on television in the "Tracey Ullman Show" short "Good Night" on April 19, 1987.  Maggie was created and designed by cartoonist Matt Groening while he was waiting in the lobby of James L. Brooks' office.  She received her first name from Groening's youngest sister.  After appearing on "The Tracey Ullman Show" for three years, the Simpson family was given their own series on the Fox Broadcasting Company which debuted December 17, 1989.

Marge Simpson: Marjorie Jacqueline "Marge" Simpson (née Bouvier) is a fictional character in the American animated sitcom "The Simpsons" and part of the eponymous family.  She is voiced by Julie Kavner and first appeared on television in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.  Marge was created and designed by cartoonist Matt Groening while he was waiting in the lobby of James L. Brooks' office.  Groening had been called to pitch a series of shorts based on "Life in Hell" but instead decided to create a new set of characters.  He named the character after his mother Margaret Groening.  After appearing on "The Tracey Ullman Show" for three seasons, the Simpson family received their own series on Fox, which debuted December 17, 1989.

Lisa Simpson: Lisa Marie Simpson is a fictional character in the animated television series "The Simpsons".  She is the middle child and most intelligent of the Simpson family.  Voiced by Yeardley Smith, Lisa first appeared on television in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.  Cartoonist Matt Groening created and designed her while waiting to meet James L. Brooks.  Groening had been invited to pitch a series of shorts based on his comic "Life in Hell", but instead decided to create a new set of characters.  He named the elder Simpson daughter after his younger sister Lisa Groening.  After appearing on "The Tracey Ullman Show" for three years, the Simpson family were moved to their own series on Fox, which debuted on December 17, 1989.

Homer Simpson: Homer Jay Simpson is a fictional character and the main protagonist of the American animated television series "The Simpsons" as the patriarch of the eponymous family.  He is voiced by Dan Castellaneta and first appeared on television, along with the rest of his family, in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.  Homer was created and designed by cartoonist Matt Groening while he was waiting in the lobby of James L. Brooks' office.  Groening had been called to pitch a series of shorts based on his comic strip "Life in Hell" but instead decided to create a new set of characters.  He named the character after his father, Homer Groening.  After appearing for three seasons on "The Tracey Ullman Show", the Simpson family got their own series on Fox that debuted December 17, 1989.

The Simpsons (franchise): The Simpsons is an American animated comedy franchise whose eponymous family consists of Homer, Marge, Bart, Lisa, and Maggie.  The Simpsons were created by cartoonist Matt Groening for a series of animated shorts that debuted on "The Tracey Ullman Show" on Fox on April 19, 1987.  After a three-season run, the sketch was developed into "The Simpsons", a half-hour prime time show that was an early hit for Fox, becoming the first Fox series to land in the Top 30 ratings in a season (1989–1990).  The popularity of "The Simpsons" has made it a billion-dollar merchandising and media franchise.  Alongside the television series, the characters of the show have been featured in a variety of media, including books, comic books, a magazine, musical releases and video games.

The Simpsons: An Uncensored, Unauthorized History: The Simpsons: An Uncensored, Unauthorized History is a non-fiction book about the American animated television series "The Simpsons".  It was written by John Ortved, and first published in October 2009 by Faber and Faber.  In the United Kingdom, the book is called Simpsons Confidential: The uncensored, totally unauthorised history of the world's greatest TV show by the people that made it.  The book is an oral history of the show, and concentrates particularly on the writers and producers of the show.  The book includes entire chapters devoted to key figures such as creator Matt Groening and James L. Brooks and Sam Simon, who helped develop the series.  According to National Public Radio reviewer Linda Holmes, "Ortved's thesis, essentially, is that lots of people are responsible for the success of "The Simpsons", and their creator, Matt Groening, has too often been viewed as the sole source to the detriment of others who also deserve to be praised."

Bart Simpson: Bartholomew JoJo "Bart" Simpson is a fictional character in the American animated television series "The Simpsons" and part of the Simpson family.  He is voiced by Nancy Cartwright and first appeared on television in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.  Cartoonist Matt Groening created and designed Bart while waiting in the lobby of James L. Brooks' office.  Groening had been called to pitch a series of shorts based on his comic strip, "Life in Hell", but instead decided to create a new set of characters.  While the rest of the characters were named after Groening's family members, Bart's name is an anagram of the word "brat".  After appearing on "The Tracey Ullman Show" for three years, the Simpson family received its own series on Fox, which debuted December 17, 1989.

The Way We Was: "The Way We Was" is the twelfth episode of "The Simpsons"<nowiki>'</nowiki> second season.  It originally aired on the Fox network in the United States on January 31, 1991.  In the episode, Marge tells the story of how she and Homer first met and fell in love.  Flashing back to 1974, we see how Homer falls in love with Marge in high school and tries to get close to her by enlisting her as his French tutor.  After several hours of verb conjugation, Marge falls for Homer too, only to become enraged when he admits that he is not a French student.  Marge rejects Homer's invitation to the prom and goes with Artie Ziff.  Artie turns out to be a terrible date and Marge realizes that it is Homer she really wants.

Question: Which character from the twelfth episode of "The Simpsons" second season was created and designed by cartoonist Matt Groening?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character from the specified episode."
    },
    "creator": {
      "type": "string",
      "description": "The person who created and designed the character."
    },
    "episode_details": {
      "type": "object",
      "properties": {
        "episode_title": {
          "type": "string",
          "description": "The title of the episode."
        },
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "episode_number_in_season": {
          "type": "integer",
          "description": "The episode number within its season."
        }
      },
      "required": [
        "episode_title",
        "season_number",
        "episode_number_in_season"
      ],
      "additionalProperties": false
    },
    "creation_context": {
      "type": "string",
      "description": "Contextual details about the character's creation."
    }
  },
  "required": [
    "character_name",
    "creator",
    "episode_details",
    "creation_context"
  ],
  "additionalProperties": false
}
