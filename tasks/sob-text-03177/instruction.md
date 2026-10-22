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
Wiggins in Storyland: Wiggins in Storyland is an educational computer game designed for MS-DOS and Microsoft Windows.  It was released by Virgin Sound and Design in 1994.  The game centers around a green bookworm named Wiggins and features voice acting by Doug Preis, Joseph Siravo, Eden Rigal, Richmond Hoxie, Polly Adams, and Daniel Rysnyder.

Charlie Strapp and Froggy Ball Flying High: Charlie Strapp and Froggy Ball Flying High (Swedish: "Kalle Stropp och Grodan Boll på svindlande äventyr" ) is a 1991 Swedish animated feature film directed by Jan Gissberg after an original script by Thomas Funck, using Funck's already well-established characters.  It follows a shorter film made by the same team in 1987, "Kalle Stropp och Grodan Boll räddar Hönan".  This is the first time since before 1954 where a Kalle Stropp production features voice acting by others than only Funck himself, only with the exception of children that had participated in other productions as well.

Girly Edition: "Girly Edition" is the twenty-first episode in the ninth season of the American animated television series "The Simpsons".  It originally aired on the Fox network in the United States on April 19, 1998.  In the episode, Lisa and Bart Simpson must co-anchor a new news program, though when Bart is seen as a more successful news anchor, Lisa becomes jealous and seeks revenge.  Meanwhile, in the subplot, Homer Simpson gets a monkey helper because of his laziness.  "Girly Edition" was the first episode written by Larry Doyle and was directed by Mark Kirkland.  Much of the subplot was inspired by the film "Monkey Shines".  Critics gave the episode positive reviews and it was well received by Lisa's voice actress Yeardley Smith.

Lisa Simpson: Lisa Marie Simpson is a fictional character in the animated television series "The Simpsons".  She is the middle child and most intelligent of the Simpson family.  Voiced by Yeardley Smith, Lisa first appeared on television in "The Tracey Ullman Show" short "Good Night" on April 19, 1987.  Cartoonist Matt Groening created and designed her while waiting to meet James L. Brooks.  Groening had been invited to pitch a series of shorts based on his comic "Life in Hell", but instead decided to create a new set of characters.  He named the elder Simpson daughter after his younger sister Lisa Groening.  After appearing on "The Tracey Ullman Show" for three years, the Simpson family were moved to their own series on Fox, which debuted on December 17, 1989.

Kalle Stropp, Grodan Boll och deras vänner: Kalle Stropp, Grodan Boll och deras vänner is a 1956 Swedish live-action/stop-motion feature film directed by after an original script by Thomas Funck, using Funck's already well-established characters.  It follows a shorter animated film made by the same team in 1987, "Kalle Stropp och Grodan Boll räddar Hönan".  This is the first time since before 1987 where a Kalle Stropp production features voice acting by others than only Funck himself, only with the exception of children that had participated in other productions as well.

List of The Simpsons cast members: "The Simpsons" is an American animated sitcom that includes six main voice actors, and numerous regular cast and recurring guest stars.  The principal cast consists of Dan Castellaneta, Julie Kavner, Nancy Cartwright, Yeardley Smith, Hank Azaria and Harry Shearer.  Tress MacNeille, Pamela Hayden, Maggie Roswell, Russi Taylor, Marcia Wallace, Marcia Mitzman Gaven and Karl Wiedergott have appeared as supporting cast members.  Repeat guest cast members include Albert Brooks, Phil Hartman, Jon Lovitz, Joe Mantegna and Kelsey Grammer.  With one exception, episode credits list only the voice actors, and not the characters they voice.

Chaos Rings II: Chaos Rings II (ケイオスリングス , Keiosu Ringusu II ) is a role-playing video game developed by Media.Vision and published by Square Enix.  The game released on 14 March 2012, one day ahead of schedule.  Effective May 31, 2016, Square Enix ended distribution of this game, and it is no longer available for download except on the Amazon App Store.  It is the sequel to "Chaos Rings", and the third game in "Chaos Rings" series that consists of the prequel "Chaos Rings Omega" game and the original.  A teaser trailer for the game has been released by Square Enix.  Like the previous games in the series, the game features voice acting (but only in Japanese).

Yeardley Smith: Martha Maria Yeardley Smith ( ; born July 3, 1964) is a French-American actress, voice actress, writer, author, comedian, and painter.  She is best known for her long-running role as Lisa Simpson on the animated television series "The Simpsons".

The Simpsons Movie: The Simpsons Movie is a 2007 American animated comedy film based on the Fox television series "The Simpsons".  The film was directed by David Silverman, and stars the regular television cast of Dan Castellaneta, Julie Kavner, Nancy Cartwright, Yeardley Smith, Hank Azaria, Harry Shearer, Tress MacNeille, Pamela Hayden, Marcia Wallace, Maggie Roswell and Russi Taylor, along with Tom Hanks, Green Day and Albert Brooks.  The film follows Homer Simpson, whose irresponsibility gets the better of him when he pollutes the lake in Springfield after the town has cleaned it up following receipt of a warning from the Environmental Protection Agency.  As the townspeople exile him and eventually his family abandons him, Homer works to redeem his folly by stopping Russ Cargill, the head of the EPA, when he intends to destroy Springfield.

The Simpsons: The Simpsons is an American animated sitcom, aimed at adolescents and adults, created by Matt Groening for the Fox Broadcasting Company.  The series is a satirical depiction of working-class life, epitomized by the Simpson family, which consists of Homer, Marge, Bart, Lisa, and Maggie.  The show is set in the fictional town of Springfield and parodies American culture and society, television, and the human condition.

Question: Which show is set in the fictional town of Springfield and features voice acting by Yeardley Smith?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the television show."
    },
    "setting_location": {
      "type": "string",
      "description": "The fictional town where the show is set."
    },
    "voice_actor_name": {
      "type": "string",
      "description": "The name of the voice actor featured in the show."
    },
    "is_animated_series": {
      "type": "boolean",
      "description": "Indicates if the show is an animated series."
    },
    "main_characters": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the main characters in the show."
    }
  },
  "required": [
    "show_name",
    "setting_location",
    "voice_actor_name",
    "is_animated_series",
    "main_characters"
  ],
  "additionalProperties": false
}
