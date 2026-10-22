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
Albert Reed Jr.: Albert Reed Jr. (January 28, 1910May 31, 1986) was an American actor and law enforcement officer.  He was mostly known for his recurring role as Alderman Fred C. Davis on "Good Times".  He also had a recurring role on the children's adventure series "The Secret of Isis" as Dr. Joshua Barnes and made guest appearances on "The Jeffersons" and "Sanford & Son".  On "Sanford & Son", he appeared in the role of Grady Wilson, a cousin of Fred's, a part he played for just one episode; another role which involved a character named Grady Wilson, a longtime friend of Fred, would later go to actor Whitman Mayo.  He portrayed "Lieutenant Ned Ordway" in the original "Airport" movie (1970), a case of art imitating life, as Reed was also an airport law enforcement official.

Etric Pruitt: Etric Pruitt (born August 16, 1981) is a former American football defensive back for the Mobile Bay Tarpons.  Pruitt played for the Seattle Seahawks in 2005 as a special teams player and 3rd string safety.  Having never played safety throughout the season as well as the playoffs, he played an important role in Super Bowl XL as Seattle's second string safety Marquand Manuel (filling in for 1st string Ken Hamlin who was out most of the season) was injured in the 2nd quarter.  In 2010, Pruitt signed to play with the Southern Indoor Football League team, the Mobile Bay Tarpons.

Bruce Locke: Bruce Asato Locke is an American actor born and raised in Oregon.  Though he wasn't originally a martial artist, Locke frequently portrayed action characters who are, which led to his own career in martial arts.  He is trained in kempo, wing chun, shaolin kung fu and Choy Li Fut.

Donovan Greer: Donovan Orlando Greer (born September 11, 1974 in Houston, Texas) is a former American football cornerback in the National Football League for the Atlanta Falcons, New Orleans Saints, Buffalo Bills, Washington Redskins, and the Detroit Lions.  He played college football at Texas A&M University.  In 2002, he appeared as himself in the TV film "Second String".

Bill Dana: William Szathmary (October 5, 1924 June 15, 2017), known professionally by his stage name Bill Dana, was an American comedian, actor, and screenwriter.  He often appeared on television shows such as "The Ed Sullivan Show", frequently in the guise of a heavily accented Bolivian character named José Jiménez.  Dana often portrayed the Jiménez character as an astronaut.

Shankudeb Panda: Shankudeb Panda (born 31 July 1980) was the State General Secretary of All India Trinamool Congress, a political party in India.  He was removed from all the posts he held in the party on 14 December 2015, on charges of corruption.  Before joining Trinamool Congress, he worked as a Journalist of a second string Bengali new channel NE Bangla.  In 2008, he conducted an unauthorized sting operation voluntarily on Mohammed Ilyas, the then CPI MLA from Nandigram, and claimed to have caught him on camera, taking money in lieu of his constituency's developmental work.

Second String: Second String is a direct-to-TV film from 2002 about the Buffalo Bills football team who find its first string (led by real-life Bills quarterback Doug Flutie, who had left the team by the time the film was released) out for a month after a food poisoning incident, leading the team's head coach, "Chuck Dichter" (portrayed by Jon Voight), to hire an insurance salesman named Dan Heller (played by Gil Bellows) as the team's backup quarterback.  Teri Polo also appeared as Heller's wife; Flutie, Mike Ditka, Chris Berman, Van Miller, Bills cornerback Donovan Greer and Ken "Pinto Ron" Johnson appear as themselves.  The film originally aired on TNT.

Jon Voight: Jonathan Vincent Voight ( ; born December 29, 1938) is an American actor.  He is the winner of one Academy Award, having been nominated for four.  He has also won four Golden Globe Awards and was nominated for eleven.  He is the father of actress Angelina Jolie and actor James Haven.

The Shaggy Dog (2006 film): The Shaggy Dog is a 2006 American family comedy film directed by Brian Robbins and written by Geoff Rodkey, Jack Amiel, Michael Begler, Cormac Wibberley and Marianne Wibberley.  It is the second remake of the 1959 film of the same name, which was first remade as a television film in 1994.  Both the 1959 and 1994 features, as well as the 1976 theatrical sequel and the 1987 television sequel, had a character named Wilby Daniels transforming into an Old English Sheepdog, whereas this remake presents a character named Dave Douglas transforming into a Bearded Collie.  It stars Tim Allen, Robert Downey, Jr., Kristin Davis, Danny Glover, Spencer Breslin, Jane Curtin, Zena Grey and Philip Baker Hall.

Chartchai Ngamsan: Chartchai Ngamsan (Thai: ชาติชาย งามสรรพ์ , born 1973) is a Thai actor.  His most notable role is as Sua Dum ("Black Tiger") in "Tears of the Black Tiger", a 2000 Thai western film.  Before that, he had a supporting role in "Dang Bireley's and Young Gangsters", also playing a character named Dum, who was a sidekick to Puu Bottlebomb, portrayed by Supakorn Kitsuwon.  In "Tears of the Black Tiger", Chartchai took the lead role and Supakorn portrayed an unwilling sidekick.  He got a Bachelor from Bangkok University

Question:  Second String had a character named Chuck Dichter portrayed by which American actor born on December 29,1938? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character portrayed."
    },
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the actor in YYYY-MM-DD format."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        }
      },
      "required": [
        "actor_name",
        "birth_date",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "character_name",
    "actor_details"
  ],
  "additionalProperties": false
}
