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
Brad's Status: Brad's Status is a 2017 American comedy-drama film written and directed by Mike White.  The film stars Ben Stiller, Michael Sheen, Jenna Fischer, Luke Wilson, and Austin Abrams.  It was selected to be screened in the Platform section at the 2017 Toronto International Film Festival, where it premiered on September 9, 2017.  The film was released on September 15, 2017, by Amazon Studios.

I Love You, Daddy: I Love You, Daddy is a 2017 American comedy-drama film written and directed by Louis C.K. and starring C.K., Chloë Grace Moretz, Pamela Adlon, John Malkovich, Rose Byrne, Charlie Day, and Helen Hunt.  It is C.K.'s first film as director since "Pootie Tang", released sixteen years prior.

Yasue Sato: Yasue Sato (佐藤 康恵 , Satō Yasue , born December 7, 1978 in the Saitama Prefecture, Honshū, Japan) is a Japanese actress and model, and formally trained in ballet.  She made her acting debut in the movie Bounce Ko Gals (1997), for which she was given a Best New Talent award at the Yokohama Film Festival.  She has since appeared in other feature films including I Love Peace (2003), Mimibukuro Ghost Stories (2004) and Welcome, Patient (2005).  She has also made numerous stage performances, including Mirandolina (1998) and Wee Thomas (2003).  in 2001, made a guest appearance in the movie Hyakujuu Sentai Gaoranger: Fire Mountain Roars.  She played as Nagi Saijyo in Ultraman Nexus.  Her most recent role was a guest appearance in GARO where she played as the Makai Priestess Jabi for 3 episodes.  She returned to show in .  She is also a music artist under the Japan Sony label.  She was also the voice actress for Demento, or the voice actor for the video game, Haunting Ground.  She worked under her stage name "さとう やすえ" (the same reading) from 2006 to 2012.

Amy Berg (writer): Amy Berg grew up in Castro Valley, California, USA.  She is an American TV writer and showrunner, known best for her work on "Counterpart", "Da Vinci's Demons", "Person of Interest", "Eureka", "Leverage", and "The 4400".  Her other television credits include "Boomtown" and "Threshold".  She was also a featured performer at w00tstock 3.0 during San Diego Comic Con in 2011.  In September 2011, she made a guest appearance as herself in an episode of "Eureka" guest star Felicia Day's web series "The Guild".  Similarly, in May 2013 she made a guest appearance as herself in an episode of "Eureka" and "Leverage" guest star Wil Wheaton's web series "TableTop".

Britt Robertson: Brittany Leanna Robertson (born April 18, 1990) is an American actress.  She began acting as a child at the Greenville Little Theater in South Carolina and she made her screen debut as the younger version of the title character in an episode of "Sheena" in 2000.  She made a guest appearance on "Power Rangers Time Force" the following year and received a Young Artist Award nomination for Best Performance in a TV Movie, Miniseries, or Special - Leading Young Actress for her role in "The Ghost Club" (2003).  Robertson went on to have roles in "" (2004), "Keeping Up with the Steins" (2006), "Dan in Real Life" (2007), "The Tenth Circle" (2008), "Mother and Child" (2009), "Avalon High" (2010), "Scream 4" (2011) and "The First Time" (2011).

Oz Pearlman: Oz Pearlman is an international mentalist, speaker, magician, and athlete best known for his 3rd Place finish on "America's Got Talent", Season 10 (2015).  He was a guest on "Late Night with Jimmy Fallon" on April 15, 2010.  He also made guest appearances on "NBC Today Show" on August 23, 2015, and three times in 2016.  On January 26, 2017 he appeared on NBC Today Show again and appeared to predict the American Super Bowl result.  Oz aired on "The Meredith Vieira Show" on December 1, 2015 and February 8, 2016.  He was a guest on CNBC "Squawk Box" on December 23, 2015.  Pearlman appeared on The Dr. Oz Show on December 20, 2016.  He appeared on ABC World News Tonight on July 24, 2009.  Oz made a guest appearance on CBS’s "Early Show" on May 30, 2009.  He appeared as a guest at "Wall Street Journal"' s studio on April 7, 2016.  Pearlman was featured on a commercial for "Mohegan Sun" in China.  Pearlman was a guest on the national radio show "Elvis Duran and the Morning Show".  He won the Long Island Marathon in 2015 when he completed the 26-mile marathon in 2 hours, 25 minutes, and 25 seconds.

Izzy Gets the F*ck Across Town: Izzy Gets the F*ck Across Town is a 2017 American comedy-drama film written and directed by Christian Papierniak.  The film stars Mackenzie Davis as a woman at rock bottom who must find her way across Los Angeles in order to crash her ex-boyfriend's engagement party.  The film had its world premiere at the Los Angeles Film Festival on June 17, 2017.

Bodied: Bodied is a 2017 American comedy-drama film directed by Joseph Kahn, and written by Alex Larsen.  The film was produced by Eminem.  The movie first premiered at the 2017 Toronto International Film Festival.  The film stars Calum Worthy as Adam, a graduate student who becomes a competitive battle rapper after becoming immersed in the scene while working on his graduate thesis on the subject.

A Thousand Junkies: A Thousand Junkies is a 2017 American comedy-drama film directed by and starring Tommy Swerdlow.  It is Swerdlow's directorial debut.

A Dog's Purpose (film): A Dog's Purpose is a 2017 American comedy-drama film directed by Lasse Hallström and written by W. Bruce Cameron, Cathryn Michon, Audrey Wells, Maya Forbes and Wally Wolodarsky, based on the 2010 novel of the same name by Cameron.  The film stars Britt Robertson, KJ Apa, Juliet Rylance, John Ortiz, Kirby Howell-Baptiste, Peggy Lipton, Dennis Quaid and Josh Gad.

Question:  A Dog's Purpose is a 2017 American comedy-drama film starring an American actress who made a guest appearance on what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the American actress starring in the film."
        },
        "guest_appearance_show": {
          "type": "string",
          "description": "The name of the show where the actress made a guest appearance."
        }
      },
      "required": [
        "name",
        "guest_appearance_show"
      ],
      "additionalProperties": false
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    }
  },
  "required": [
    "film_title",
    "actress_details",
    "film_year"
  ],
  "additionalProperties": false
}
