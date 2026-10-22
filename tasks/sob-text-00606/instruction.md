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
Warren Furman: Warren Adam Furman (born 3 July 1972) is a British actor and television presenter who is best known for his role of Ace on the British TV show "Gladiators" from 1996 to 2000.  He currently resides in East Yorkshire having previously appeared on the BBC TV show "DIY SOS" in Lowri Turner's team as a temporary replacement.

Ramesh Pisharody: Ramesh Pisharody is an Indian stand-up comedian, mimicry artist, television host and film actor mostly known for his works in Malayalam television and films.  He appeared in the TV shows "Cinemala" and gained huge popularity after his TV show "Bluff Masters" aside his creative partner and friend Dharmajan Bolgatty.  He debuted as an actor through the film "Positive" (2008).  Though he first acted in the film "Positive", first released movie was "Nasrani".  He has acted in several Malayalam films, mostly in supporting roles like "To Noora with Love" (2014), which include comedy as well as negative roles.  He had a lead role in the film "Kappal Muthalaali" (2009).  His other notable films are "Celluloid"," Left Right Left", and "Immanuel".  He is currently hosting the TV show "Badai Bunglow"

I Know My Kid's a Star: I Know My Kid's a Star is an American competitive reality television TV show for aspiring child actors and their parents.  The show aired from March to May 2008 on VH1.  The show's host and primary judge is Danny Bonaduce, who is best known as having been a child actor himself on the 1970s TV show "The Partridge Family".  Casting agent Marki Costello stars as co-host and secondary judge.  The show features ten parent/child pairings, with each pair working together as a team to further the child's career.

Nardole: Nardole is a fictional character created by Steven Moffat and portrayed by Matt Lucas in the long-running British science fiction television series "Doctor Who".  He is a companion of the Twelfth Doctor, the current incarnation of the alien time traveller known as The Doctor, portrayed by Peter Capaldi.  He initially appeared in the 2015 Christmas special "The Husbands of River Song" as a companion of River Song, before returning in the following episode "The Return of Doctor Mysterio", having become the Doctor's companion in the meantime.

Russell Howard: Russell Joseph Howard (born 23 March 1980) is an English comedian, television and radio presenter and actor, best known for his TV show "Russell Howard's Good News" and his appearances on the topical panel TV show "Mock the Week".  He won "Best Compère" at the 2006 Chortle Awards and was nominated for an if.comedy award for his 2006 Edinburgh Festival Fringe show.  Howard cited comedians Lee Evans, Richard Pryor, Frank Skinner as influences.

Saurav Gurjar: Saurav Gurjar is an Indian professional wrestler, Sportsperson and actor.  He is best known for his role as Bheem in the mythological TV show "Mahabharat".  Recently he has appeared in tv Show Sankatmochan Mahabali Hanuman As a Ravana& Vali (Ramayana) aired on Sony tv.  after Ramayan, after Mahabharat (2013 TV series) he acted/Anchor in Indonesia tv channel one of the popular tv show The New Eat Bulaga!  Indonesia

Ali Asgar (actor): Ali Asgar is an Indian actor and stand-up comedian.He has appeared in many Indian TV serials and movies and was helped by macline castelino to grow in the industry.  He is currently doing a role of pushpa Nani in "The Kapil Sharma Show."  Asgar appeared as Kamal Agarwal in Star Plus TV show "Kahaani Ghar Ghar Ki".  He also appeared in SAB TV's show F.I.R. as Inspector Raj Aryan.  He is commonly known for his role in Colors TV show "Comedy Nights with Kapil" as Dadi.

Team Batista no Eikō: Team Batista no Eikō (チーム·バチスタの栄光 , The Glorious Team Batista ) is a Japanese mystery film and television show adapted from the best-selling novel of the same name by Takeru Kaidō.  The story revolves around a hospital with a team of doctors known for their success with a type of heart surgery.  After a series of failed operations that result in the patient's death, an internal investigation is initiated, led by a doctor named Taguchi and a brash government official.  In the original novel the main character Taguchi, was a male doctor in his forties.  However, for the film adaptation TBS suggested replacing the character with a young female resulting in Yuko Takeuchi being cast as in the role.  For the TV show, Taguchi is a man, with Atsushi Itō playing the role.

Matt Lucas: Matthew Richard Lucas (born 5 March 1974) is an English comedian, screenwriter, actor and singer, best known for his work with David Walliams in the television show "Little Britain", as well as for his portrayals of the scorekeeping baby Georgie Dawes in the comedy panel game "Shooting Stars" and both Tweedle Dum and Tweedle Dee in "Alice in Wonderland" and its sequel, "Alice Through the Looking Glass".

Sivannarayana Naripeddi: Sivannarayana Naripeddi (Telugu: శివన్నారాయణ నారిపెద్ది ) is a Telugu actor.  He started his film career with Grahanam.  He won the Best comedian Nandi Award 2007 for ammamma.com TV show.  He is best known to the Telugu audience as "Appaji" from Amrutham popular TV show.  He acted in more than 100 films.

Question: For what TV show, is the actor who plays the role of Nardole in Doctor Who, best known ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character in the TV show."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who portrays the character."
    },
    "character_tv_show": {
      "type": "string",
      "description": "The TV show where the character appears."
    },
    "actor_best_known_tv_show": {
      "type": "string",
      "description": "The TV show for which the actor is best known."
    }
  },
  "required": [
    "character_name",
    "actor_name",
    "character_tv_show",
    "actor_best_known_tv_show"
  ],
  "additionalProperties": false
}
