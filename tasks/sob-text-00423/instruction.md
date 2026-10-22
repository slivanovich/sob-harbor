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
5 Men and a Limo: 5 Men and a Limo is a 1997 American short film produced by Aspect Ratio Films as an introduction sketch for the 26th Annual "Hollywood Reporter" Key Art Awards.  In the film voiceover actor Don LaFontaine picks up four other voiceover actors in his limo to travel to the awards.  The actors talk about themselves and the awards, making humorous references to common phrases and techniques they use when voicing movie trailers.  Besides LaFontaine, the other actors appearing in the film are John Leader, Nick Tate, Mark Elliot, and Al Chalk.  Hal Douglas provides his voice for a telephone call, but does not appear.

Kamara's Tree: Kamara's Tree is a 2013 Nigerian comedy drama film, directed by Desmond Elliot, and starring Desmond Elliot, Lydia Forson, Ivie Okujaye, Tessy Abubakar, Bobby Obodo, Ginnefine Kanu, Morris K Sesay and Dabota Lawson.  The film which is set and was shot in Freetown, Sierra Leone, tells the story of a family who gather in Freetown to attend the wedding of their sister, after long years of separation; each of the family members has to deal with the diverse behaviours of the others as a result.

Andre (film): Andre is a 1994 comedy drama film starring Tina Majorino about a child's encounter with a seal.  It is an adaptation of the book "A Seal Called Andre", which in turn was based on a true story.  It was shot in Vancouver and Mississippi.

Love Is a Many-Splendored Thing (film): Love Is a Many-Splendored Thing is a 1955 Deluxe color American drama-romance film in CinemaScope.  Set in 1949–50 in Hong Kong, it tells the story of a married, but separated, American reporter Mark Elliot (played by William Holden), who falls in love with a Eurasian doctor Han Suyin originally from China (played by Jennifer Jones), only to encounter prejudice from her family and from Hong Kong society.

A Trip to Jamaica: A Trip to Jamaica is a Nigerian comedy drama film directed by Robert Peters, starring Ayo Makun, Funke Akindele, Nse Ikpe Etim and Dan Davies.  The film received mainly mixed to negative reviews from critics, however, it was a huge box office success, breaking the earlier record set by "30 Days in Atlanta".  The movie had its worldwide premiere on September 25, 2016 in Lagos State.  The event also featured a celebrity football game involving ex-internationals, like Kanu Nwankwo, Jay Jay Okocha, Peter Rufai, Joseph Yobo and Stephen Appiah.  The film tells a story about the adventures of a newly engaged couple in their relatives residence outside Nigeria, and how the secrets of their host led to the eventual breakup of their union amidst the culture shock of the new country and living with upper-class citizens.

Mark Elliot (voice-over artist): Mark Elliot (born September 24, 1939) is an American voice-over artist best known as the primary voice for Walt Disney Entertainment from 1983 to 2008.  He also provided voice overs for trailers of non-Disney films, logos, feature presentation bumpers and commercials.  He's well known for his voice overs in theatrical and home video trailers for films produced by The Walt Disney Studios from the 1980s to the 2000s.  He was also the voice of CBS and FOX throughout the 1980s and 1990s, and various theatrical trailers for such non-Disney animated movies as "All Dogs Go to Heaven", "The Seventh Brother", "Rover Dangerfield", "Rock-A-Doodle", "", "The Magic Voyage", "The Thief and the Cobbler", "Once Upon a Forest", "The Princess And The Goblin", "Andre", "Asterix Conquers America", "The Swan Princess", "The Pagemaster", "The Pebble and the Penguin", "Balto", "All Dogs Go to Heaven 2", "Tiny Heroes" ("Vacak 2 - az erdő hőse"), "Zeus and Roxanne", "The Fearless Four", "The Prince of Egypt", "The Adventures of Brer Rabbit", "", "House Arrest", and "".  In addition to his behind-the-scenes work, Elliott starred with four other notable voice artists in the 1997 short film "5 Men and a Limo".  One of his most well-known voice-overs for Disney is the catchphrase "And now, our feature presentation," which he says at the start of most animated Disney films on video on a "Feature Presentation" bumper.

The Missing Postman: The Missing Postman is a two-part comedy drama originally broadcast on BBC1 on the consecutive evenings of 29 and 30 March 1997.  Adapted from the Mark Wallington novel, it received the award for Best BBC Comedy Drama at the British Comedy Awards in 1997.

Jang Min-hyeok: Jang Min-Hyeok (Korean: 장민혁 ; born December 28, 1978) is a South Korean voice actor.  In 2006, he started his career by joining Korean Broadcasting System's voice acting division.  Two years later, the voice actor won a KBS Radio Drama Award for Best New Voice Actor.  After being a freelancer, Min-Hyeok became popular with his cover of Shia LaBeouf on the Korean dub of "Transformers", and has recently been known for his role as Sherlock Holmes on the Korean dub of a British television series "Sherlock".

The Better 'Ole (1926 film): The Better 'Ole is a 1926 American silent World War I comedy drama film.  Released by Warner Bros.  Pictures, Inc., this film is the second full-length film to utilize the Vitaphone sound-on-disc process, two months after the first Vitaphone feature "Don Juan"; with no audible dialogue, the film does have a synchronized musical score and sound effects.  This film was also the second onscreen adaptation of the 1917 musical play "The Better 'Ole" by Bruce Bairnsfather and Arthur Elliot.  Charlie Chaplin's eldest brother Sydney Chaplin played the main lead as Old Bill in perhaps his best-known film today.  This film is also believed by many to have the first spoken word of dialog, ""coffee"", although there are those who disagree.  At one point during the film, Harold Goodwin's character whispers a word to Sydney Chaplin which is also faintly heard.

Tom McGrath (animator): Thomas "Tom" McGrath (born August 7, 1964) is an American film director, animator, and voice actor known for co-directing (with Eric Darnell) the 2005 comedy "Madagascar" and its sequels, "" in 2008 and "" in 2012, also providing the voice of Skipper in all films, short films and "The Penguins of Madagascar" television series.  He has portrayed Skipper in every "Madagascar" installment, being the only voice actor to do so.  He has also worked as a voice actor on other DreamWorks animated features like "Flushed Away" in 2006 and "Shrek the Third" in 2007.  He also stepped in on "Flushed Away" to help make improvements prior to its release.  He has also directed other DreamWorks Feature Films such as Megamind and The Boss Baby.

Question: Mark Elliot was a voice actor in what comedy drama film about involving an encounter with a seal?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "plot_summary_keywords": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key elements or themes from the film's plot."
    },
    "voice_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the voice actor."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role the actor had (e.g., 'voice-over artist')."
        }
      },
      "required": [
        "name",
        "role_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genres",
    "plot_summary_keywords",
    "voice_actor"
  ],
  "additionalProperties": false
}
