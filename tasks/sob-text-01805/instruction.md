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
Catherine O'Hara: Catherine Anne O'Hara {'1': ", '2': ", '3': ", '4': "} (born March 4, 1954) is a Canadian-American actress, writer, and comedian.  She is known for her comedy work on "Second City Television" (1976–84) and in films such as "After Hours" (1985), "Beetlejuice" (1988), "Home Alone" (1990), "" (1992), and "The Nightmare Before Christmas" (1993).  Her other film appearances include the mockumentary films written and directed by Christopher Guest: "Waiting for Guffman" (1996), "Best in Show" (2000), "A Mighty Wind" (2003), and "For Your Consideration" (2006).

Stu Osborn Show: The Stu Osborn Show is a 2007 web viral video advertisement for Microsoft.  It is made to look like a mockumentary of a fictional television interview show of the same name.  The video is directed by Christopher Guest who is well known for being the creative force behind other mockumentaries like "Waiting for Guffman" and "Best In Show".  It stars Michael Hitchcock as Stu Osborn, the awkward and somewhat disoriented "host" and Fred Willard as a failed businessman-turned-author who is Osborn's "guest."  Much of the dialogue is improvised by the actors.  Both Hitchcock and Willard are frequent performers in Guest's films.

Eugene Levy: Eugene Levy, CM (born December 17, 1946) is a Canadian actor, comedian, producer, director, musician and writer.  He is the only actor to have appeared in all eight of the "American Pie" films, in his role as Noah Levenstein.  He often plays nerdy, unconventional figures, with his humour often deriving from his excessive explanations of matters and the way in which he deals with sticky situations.  Levy is a regular collaborator of actor-director Christopher Guest, appearing in and co-writing four of his films, commencing with "Waiting for Guffman" (1997).

Best in Show (film): Best in Show is a 2000 American mockumentary comedy film co-written (along with Eugene Levy) and directed by Christopher Guest.  The film follows five entrants in a prestigious dog show, and focuses on the slightly surreal interactions among the various owners and handlers, as they travel to the show and then compete during the show.  There are also short depictions of the characters six months after the show is over.  Among the comedic aspects of the film are similarities between the personalities and characteristics of the owners and those of their dogs.  Much of the dialogue was improvised.  Many of the comic actors were also involved in Guest's other films, including "This Is Spinal Tap", "Waiting for Guffman", "A Mighty Wind", "For Your Consideration", and "Mascots".

Christopher Guest: Christopher Haden-Guest, 5th Baron Haden-Guest (born February 5, 1948), simply known as Christopher Guest, is an English-American screenwriter, composer, musician, director, actor, and comedian who holds dual British and American citizenship.  Guest is most widely known in Hollywood for having written, directed and starred in his series of comedy films shot in mock-documentary (mockumentary) style.  Many scenes and character backgrounds in Guest's films are written and directed, although actors have no rehearsal time and the ensemble improvise scenes while filming them.  The series of films began with "This Is Spinal Tap" (directed by Rob Reiner), and continued with "Waiting for Guffman", "Best In Show", "A Mighty Wind", "For Your Consideration", and "Mascots".

Waiting for Guffman: Waiting for Guffman is a 1997 American mockumentary comedy film co-written and directed by Christopher Guest.  The film's cast includes Catherine O'Hara, Eugene Levy, Fred Willard, and Parker Posey.

Fred Willard: Frederick Charles "Fred" Willard (born September 18, 1939) is an American actor, comedian, voice actor and writer, best known for his improvisational comedy.  He is known for his roles in the Rob Reiner mockumentary film "This Is Spinal Tap", the Christopher Guest mockumentary films "Waiting for Guffman", "Best in Show", "A Mighty Wind", "For Your Consideration", and "Mascots", and the "" films.  He is an alumnus of The Second City.  He received three Emmy nominations for his recurring role on the TV series "Everybody Loves Raymond" as Robert Barone's father-in-law, Hank MacDougall.  In 2010 he received an Emmy nomination for Outstanding Guest Actor in a Comedy Series for his role on the ABC TV series "Modern Family" as Phil Dunphy's father, Frank Dunphy.

Waiting at the Church: "Waiting at the Church" is a popular British music hall song written by Fred Leigh (words) and Henry Pether (music) for Vesta Victoria.  It is sung by a bride-to-be who has given her fiancé, Obadiah Binks, all her money to buy a ring or a house only to be left "waiting at the church", and finds out the truth when Obadiah sends her a note telling her he is already married.  It has featured in a number of films since the earliest days of cinema.  The silent film "Waiting at the Church" featured a performance by Victoria as she acted out the lyrics.  Several other silent films were made to accompany recordings of the song.  Sound films which use the song include "Here Come the Huggetts", "Millions Like Us" and "I Thank You".  Richard Thompson included it on his album "1000 Years of Popular Music".  It has also been covered many times, including by Julie Andrews and Miss Piggy.

Waiting for Duffman: "Waiting for Duffman" is the seventeenth episode of the twenty-sixth season of the American animated sitcom "The Simpsons", and the 569th overall episode of the series.  It originally aired on the Fox network in the United States on March 15, 2015.  R. Lee Ermey reprises his role of Colonel Leslie Hapablap from "Sideshow Bob's Last Gleaming".  The title is a play on "Waiting for Guffman".

Parker Posey: Parker Christian Posey (born November 8, 1968) is an American actress and musician.  Following her role in Richard Linklater's 1993 cult hit "Dazed and Confused", she became known during the 1990s after a series of roles in independent films such as "Party Girl" (1995) and "The House of Yes" (1997) that gained her the nickname "Queen of the Indies".  She later played improvisational roles in Christopher Guest mockumentaries, including "Waiting for Guffman" (1996), "Best in Show" (2000), "A Mighty Wind" (2003), "For Your Consideration" (2006) and "Mascots" (2016).  Her other film appearances include "You've Got Mail" (1998), "Scream 3" (2000), "Superman Returns" (2006), and the Woody Allen films "Irrational Man" (2015) and "Café Society" (2016).  On television, Posey has guest-starred in series such as "Will & Grace", "Boston Legal", "The Good Wife", "Louie", "Parks and Recreation", and "Search Party".

Question: What Canadian actor acted with Catherine O'hara in "Waiting for Guffman"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film where the actors co-starred."
    },
    "canadian_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Canadian actor."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "co_star_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the co-star actor mentioned in the question."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the co-star actor."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "canadian_actor",
    "co_star_actor"
  ],
  "additionalProperties": false
}
