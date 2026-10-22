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
David Michôd: David Michôd ( ; born 30 November 1972) is an Australian film director, screenwriter, producer and actor.  He is best known for directing the critically acclaimed 2010 film "Animal Kingdom" and the 2014 film "The Rover".  He also co-wrote "Hesher".

Paddington (film): Paddington is a 2014 comedy film directed by Paul King, written by King and Hamish McColl and produced by David Heyman.  Based on "Paddington Bear" by Michael Bond, the film stars Ben Whishaw as the voice of the title character, along with Hugh Bonneville, Sally Hawkins, Julie Walters, Jim Broadbent, Peter Capaldi and Nicole Kidman in live-action roles.  The film was co-produced by the French company StudioCanal and the British company Heyday Films.  It was released in the United Kingdom on 28 November 2014 and grossed $265.3 million worldwide on a €38.5 million budget.  Among several honours, King was nominated for the BAFTA Award for Best Adapted Screenplay and both he and Heyman were nominated for the BAFTA Award for Best British Film.  A sequel, "Paddington 2", is scheduled to be released in 2017.

Mark Romanek: Mark Romanek (born September 18, 1959) is an American filmmaker whose directing work includes feature films, television, music videos and commercials.  Romanek wrote and directed the 2002 film "One Hour Photo" and directed the 2010 film "Never Let Me Go".  His most notable music videos include "Hurt" (Johnny Cash), "Closer" (Nine Inch Nails), "Can't Stop" (Red Hot Chili Peppers), "Bedtime Story" (Madonna), and "Scream" (Michael & Janet Jackson).  Romanek's music videos have won 20 MTV Video Music Awards, including Best Direction for Jay-Z's "99 Problems", and he has won three Grammy Awards for Best Short Form Music Video - more than any other director.

Black Swan (film): Black Swan is a 2010 American psychological horror film directed by Darren Aronofsky.  The screenplay by Mark Heyman, Andres Heinz and John McLaughlin is from a story by Heinz.  It stars Natalie Portman, Vincent Cassel, Mila Kunis, Barbara Hershey and Winona Ryder.  The plot revolves around a production of Tchaikovsky's "Swan Lake" ballet by a prestigious New York City company.  The production requires a ballerina to play the innocent and fragile White Swan, for which the committed dancer Nina (Portman) is a perfect fit, as well as the dark and sensual Black Swan, which are qualities better embodied by the new arrival Lily (Kunis).  Nina is overwhelmed by a feeling of immense pressure when she finds herself competing for the part, causing her to lose her tenuous grip on reality and descend into a living nightmare.

Peepers (film): Peepers is a 2010 film directed by Seth W. Owen and co-written with Daniel Perlmutter and Mark Slutsky.

Mark Heyman: Mark Heyman (born 1979) is an American screenwriter and film producer who is best known for co-writing "Black Swan" (2010) and "The Skeleton Twins" (2014).

Kick-Ass 2 (film): Kick-Ass 2 is a 2013 superhero comedy film based on the comic book of the same name and "Hit-Girl", both by Mark Millar and John Romita, Jr., and is the sequel to the 2010 film "Kick-Ass".  The film was written and directed by Jeff Wadlow and co-produced by Matthew Vaughn, who directed the first film.  Aaron Taylor-Johnson, Christopher Mintz-Plasse and Chloë Grace Moretz reprise their roles from the first film as Dave Lizewski, Chris D'Amico, and Mindy Macready, respectively.  Other returning actors include Clark Duke, Yancy Butler, Garrett M. Brown, Lyndsy Fonseca and Sophie Wu.

Jennifer Ventimilia: Jennifer Ventimilia (born Jeffrey Ventimilia and also known as J.R. Ventimilia) is an American television writer.  Ventimilia co-wrote "The Simpsons" episode "Simpson Tide" (with Joshua Sternin) and the teleplay of the episode "'Round Springfield", based on a story idea by Al Jean and Mike Reiss.  Other credits include "Murphy Brown", "That '70s Show", and "The Critic".  In 2002, Ventimilia and Sternin created a show for Fox called "The Grubbs", starring Randy Quaid.  Due to negative critical reaction, the show was canceled before it went on air.  Ventimilia co-wrote the screenplay for the 2004 film "Surviving Christmas" and the 2010 film "Tooth Fairy" and she also served as an executive producer and writer for "Kitchen Confidential", "Robot and Monster", and the 2012 Nickelodeon reboot of "Teenage Mutant Ninja Turtles".

Young Detective Dee: Rise of the Sea Dragon: Young Detective Dee: Rise of the Sea Dragon (狄仁傑之神都龍王) is a 2013 Chinese action-adventure fantasy mystery film directed, produced, and co-written by Tsui Hark.  It is a prequel to Hark's 2010 film "Detective Dee and the Mystery of the Phantom Flame", which starred Andy Lau.  Taiwanese-Canadian actor Mark Chao takes over from him as a young Detective Dee, while Feng Shaofeng, Lin Gengxin, Kim Bum (in his Chinese debut), and Angelababy co-star alongside a returning Carina Lau from "Mystery of the Phantom Flame", rounding up the ensemble cast.

Littlerock (film): Littlerock is a 2010 film directed by Mike Ott.  It debuted at the 2010 San Francisco International Film Festival, and played at over 40 film festivals including AFI Fest, Viennale, Cairo International Film Festival, Warsaw International Film Festival, Reykjavik International Film Festival, Thessaloniki International Film Festival, and Hong Kong International Film Festival before its U.S. theatrical release on August 12, 2011.

Question: Mark Heyman co-wrote the 2010 film directed by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "string",
      "description": "The name of the person whose work is being queried."
    },
    "person_role": {
      "type": "string",
      "description": "The role of the person in the film."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "director"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_of_interest",
    "person_role",
    "film_details"
  ],
  "additionalProperties": false
}
