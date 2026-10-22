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
Robin Hood (DC Comics): Robin Hood is a fictional character, a comic book Outlaw published by DC Comics.  Robin Hood debuted in "New Adventure Comics" vol.  1 #23 (January 1938), and was created by Sven Elven.  The character is based on the legendary archer Robin Hood whose earliest recorded literary appearance was in William Langland's 14th century narrative poem, Piers Plowman.  The character of Robin Hood was made popular by Howard Pyle's 19th century novel "The Merry Adventures of Robin Hood".

Robin Hood Daffy: Robin Hood Daffy is a 1958 Warner Bros.  Pictures, Inc theatrical cartoon comedy short, starring Daffy Duck (in the role of Robin Hood) and Porky Pig, as part of the Merrie Melodies series, directed by Chuck Jones and written by Michael Maltese.  It was the last of Jones' parody cartoons with the duo, and the last appearance of Porky in a theatrical cartoon directed by Jones during the Golden Age of Animation.  It was also the second parody of Robin Hood directed by Chuck Jones, after the 1949 Bugs Bunny short "Rabbit Hood".  An edited version of "Robin Hood Daffy" was included in the theatrical film "The Bugs Bunny/Road Runner Movie" (1979).

Robin Hood (Disney character): Robin Hood is a fictional character who is the protagonist in Walt Disney Productions series’ 21st animated feature film Robin Hood (1973).  Robin Hood is voiced by Shakespearean and Tony Award winning actor Brian Bedford.  The film is based on the legends of Robin Hood and Reynard the fox, a 12th century Alsatian fairy tale character, but uses anthropomorphic animals rather than people.  The story follows the adventures of Robin Hood, Little John and the inhabitants of Nottingham as they fight against the excessive taxation of Prince John, and Robin Hood wins the hand of Maid Marian.

Robin of Sherwood: Robin of Sherwood (retitled Robin Hood in the United States) is a British television series, based on the legend of Robin Hood.  Created by Richard Carpenter, it was produced by HTV in association with Goldcrest, and ran from 1984 to 1986 on the ITV network.  In America it was retitled "Robin Hood" and shown on the premium cable TV channel Showtime and, later, on PBS.  The show starred Michael Praed and Jason Connery as two different incarnations of the title character.  Unlike previous adaptations of the Robin Hood legend, "Robin of Sherwood" combined a gritty, authentic production design with elements of real-life history, 20th century fiction, and pagan myth.  The series is also notable for its musical score by Clannad, which won a BAFTA award.

Robyn Hod and the Shryff off Notyngham: Robyn Hod and the Shryff off Notyngham is the manuscript fragment of a late medieval play about Robin Hood, the earliest known Robin Hood playscript and the only surviving medieval script of a Robin Hood play.  The manuscript dates from c1475, that is it is approximately as old as the earliest copies of the ballads.  In addition to being incomplete the script has no scene or stage directions, and does not identify speakers, so it offers uncertainties of interpretation.  However it has been interpreted as telling essentially the same story as Robin Hood and Guy of Gisborne .  If correct this would confirm the medieval origin of the Gisbourne story.  The play is also important for containing the earliest reference to Friar Tuck,"ffrere Tuke", as a member of Robin Hood's band.

Guy of Gisbourne: Sir Guy of Gisbourne (also spelled Gisburne, Gisborne, Gysborne, or Gisborn) is a character from the Robin Hood legends of English folklore.  He first appears in "Robin Hood and Guy of Gisborne" (Child Ballad 118), where he is a hired killer who attempts to kill Robin Hood but is killed by him.  In later depictions, he has become a romantic rival to Robin Hood for Maid Marian's love.

Harry Lloyd: Harry Charles Salusbury Lloyd (born 17 November 1983) is an English actor.  He is known for his roles as Will Scarlet in the 2006 BBC drama "Robin Hood", Jeremy Baines in the 2007 "Doctor Who" episodes "Human Nature" and "The Family of Blood", and Viserys Targaryen in the HBO series "Game of Thrones".  He has also appeared on stage, and in films including "The Theory of Everything" and "Anthropoid".

The Adventures of Robin Hood (TV series): The Adventures of Robin Hood is a British television series comprising 143 half-hour, black and white episodes broadcast weekly between 1955 and 1959 on ITV.  It stars Richard Greene as the outlaw Robin Hood and Alan Wheatley as his nemesis, the Sheriff of Nottingham.  The show followed the legendary character Robin Hood and his band of merry men in Sherwood Forest and the surrounding vicinity.  While some episodes dramatised the traditional Robin Hood tales, most episodes were original dramas created by the show's writers and producers.

Closer to the Moon: Closer to the Moon (Romanian: Mai aproape de lună ) is a 2013 Romanian-American comedy-drama film written and directed by Nae Caranfil, and starring Vera Farmiga, Mark Strong, Harry Lloyd, Joe Armstrong, Tim Plester, Christian McKay, and Anton Lesser.  Based on the true story of the Ioanid Gang, it is one of the most expensive productions in Romanian cinema.

List of Robin Hood (2006 TV series) characters: Robin Hood is a British television drama series, produced by Tiger Aspect Productions for BBC One, which debuted in October 2006.  The programme uses the majority of the familiar characters from the traditional Robin Hood legends, notably featuring no appearances by Friar Tuck and Prince John in the first 2 series (although the latter was frequently mentioned as an off-screen character), though introducing them in the third series, portrayed by David Harewood and Toby Stephens respectively.  Some have been given new back-stories or characteristics not evident in previous versions of the legend.  A peculiar innovation of this version of Robin Hood is its anachronistic distortion of the ethnic make-up of 12th century England.  It adds several characters of African and Asian origin, fully integrated into English society.  While most of these characters are minor, two are members of the Merry Men.

Question: Which character from the BBC drama "Robin Hood" did this famous English actor who also starred in "Closer to the Moon", play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the English actor."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "tv_series_title": {
      "type": "string",
      "description": "The title of the BBC drama series."
    },
    "tv_series_year": {
      "type": "integer",
      "description": "The debut year of the TV series."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actor in the specified TV series."
    },
    "actor_other_notable_tv_series": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other notable TV series the actor is known for."
    },
    "actor_film_appearances": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Films the actor has appeared in."
    }
  },
  "required": [
    "actor_name",
    "actor_nationality",
    "tv_series_title",
    "tv_series_year",
    "character_played",
    "actor_other_notable_tv_series",
    "actor_film_appearances"
  ],
  "additionalProperties": false
}
