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
Charlie and the Chocolate Factory (film): Charlie and the Chocolate Factory is a 2005 musical fantasy film directed by Tim Burton and written by John August, based on the 1964 British novel of the same name by Roald Dahl.  The film stars Johnny Depp as Willy Wonka and Freddie Highmore as Charlie Bucket.  The storyline follows Charlie, who wins a contest and is along with four other contest winners, subsequently led by Wonka on a tour of his chocolate factory, the most magnificent in the world.

Ed Wood (film): Ed Wood is a 1994 American biographical period comedy-drama film directed and produced by Tim Burton, and starring Johnny Depp as cult filmmaker Ed Wood.  The film concerns the period in Wood's life when he made his best-known films as well as his relationship with actor Bela Lugosi, played by Martin Landau.  Sarah Jessica Parker, Patricia Arquette, Jeffrey Jones, Lisa Marie, and Bill Murray are among the supporting cast.

Dark Shadows (film): Dark Shadows is a 2012 American horror comedy film based on the gothic television soap opera of the same name, that was broadcast between 1966 and 1971.  The film was directed by Tim Burton and stars Johnny Depp, Michelle Pfeiffer, Helena Bonham Carter, Eva Green, Jackie Earle Haley, Jonny Lee Miller, Chloë Grace Moretz, and Bella Heathcote in a dual role.  The film had a limited release on May 10, 2012, and was officially released the following day in the United States.

Edward Scissorhands: Edward Scissorhands is a 1990 American romantic dark fantasy film directed by Tim Burton, produced by Denise Di Novi and Tim Burton, and written by Caroline Thompson from a story by Tim Burton and Caroline Thompson, starring Johnny Depp as an artificial man named Edward, an unfinished creation who has scissor blades instead of hands.  The young man is taken in by a suburban family and falls in love with their teenage daughter Kim (Winona Ryder).  Additional roles were played by Dianne Wiest, Anthony Michael Hall, Kathy Baker, Vincent Price and Alan Arkin.

Tim Burton: Timothy Walter Burton ( ; born August 25, 1958) is an American film director, producer, artist, writer, and animator.  He is known for his dark, gothic, eccentric, and quirky fantasy films such as "Beetlejuice" (1988), "Edward Scissorhands" (1990), the animated musical "The Nightmare Before Christmas" (1993), the biographical film "Ed Wood" (1994), the horror fantasy "Sleepy Hollow" (1999), and later efforts such as "Corpse Bride" (2005), "" (2007), "Dark Shadows" (2012), and "Frankenweenie" (2012).  He is also known for blockbusters such as the adventure comedy "Pee-wee's Big Adventure" (1985), the superhero films "Batman" (1989) and its first sequel "Batman Returns" (1992), the sci-fi film "Planet of the Apes" (2001), the fantasy drama "Big Fish" (2003), the musical adventure film "Charlie and the Chocolate Factory" (2005), and the fantasy film "Alice in Wonderland" (2010), which garnered a worldwide gross of over $1 billion.

Alice Through the Looking Glass (2016 film): Alice Through the Looking Glass is a 2016 American fantasy adventure film directed by James Bobin, written by Linda Woolverton and produced by Tim Burton, Joe Roth, Suzanne Todd, and Jennifer Todd.  It is based on the characters created by Lewis Carroll and is the sequel to the 2010 film "Alice in Wonderland".  The film stars Johnny Depp, Anne Hathaway, Mia Wasikowska, Matt Lucas, Rhys Ifans, Helena Bonham Carter, and Sacha Baron Cohen and features the voices of Stephen Fry, Michael Sheen, Timothy Spall, and Alan Rickman, in his final film role.

Winona Ryder: Winona Ryder (born Winona Laura Horowitz; October 29, 1971) is an American actress.  One of the most successful and iconic actresses of the 1990s, she made her film debut in the film "Lucas" (1986).  As Lydia Deetz, a goth teenager in Tim Burton's "Beetlejuice" (1988), she won critical acclaim and widespread recognition.  After appearances in film and on television, Ryder continued her acting career with the cult film "Heathers" (1988), a controversial satire of teenage suicide and high school life that has since become a landmark teen film.  She later appeared in the coming of age drama "Mermaids" (1990), earning a Golden Globe Award nomination, and in the same year appeared alongside Johnny Depp in Burton's dark fairy-tale "Edward Scissorhands" (1990), and shortly thereafter with Keanu Reeves in Francis Ford Coppola's gothic romance "Bram Stoker's Dracula" (1992).

Sleepy Hollow (film): Sleepy Hollow is a 1999 American Gothic supernatural horror film directed by Tim Burton.  It is a film adaptation loosely inspired by the 1820 short story "The Legend of Sleepy Hollow" by Washington Irving and stars Johnny Depp and Christina Ricci, with Miranda Richardson, Michael Gambon, Casper Van Dien, and Jeffrey Jones in supporting roles.  The plot follows police constable Ichabod Crane (Depp) sent from New York City to investigate a series of murders in the village of Sleepy Hollow by a mysterious Headless Horseman.

Alice in Wonderland (2010 film): Alice in Wonderland is a 2010 American fantasy adventure film directed by Tim Burton from a screenplay written by Linda Woolverton.  The film stars Johnny Depp, Anne Hathaway, Helena Bonham Carter, Crispin Glover, Matt Lucas, and Mia Wasikowska and features the voices of Alan Rickman, Stephen Fry, Michael Sheen, and Timothy Spall.  Based on Lewis Carroll's fantasy novels, "Alice's Adventures in Wonderland" and "Through the Looking-Glass".  This film tells the story of a nineteen-year-old Alice Kingsley (stated in the film to be a daughter of Charles Kingsley), who is told that she can restore the White Queen to her throne, with the help of the Mad Hatter.  She is the only one who can slay the Jabberwock, a dragon-like creature that is controlled by the Red Queen and terrorizes Underland's inhabitants.

Corpse Bride: Corpse Bride is a 2005 British-American stop-motion-animated musical fantasy film directed by Mike Johnson and Tim Burton with a screenplay by John August, Caroline Thompson and Pamela Pettler based on characters created by Burton and Carlos Grangel.  The plot is set in a fictional Victorian era village in Europe.  Johnny Depp leads the cast as the voice of Victor, while Helena Bonham Carter voices Emily, the titular bride.  "Corpse Bride" is the third stop-motion feature film produced by Burton and the first directed by him (the previous two films, "The Nightmare Before Christmas" and "James and the Giant Peach", were directed by Henry Selick).  This is also the first stop-motion feature from Burton that was distributed by Warner Bros.  Pictures.  It was dedicated to executive producer Joe Ranft, who died during production.

Question: Timothy Walter Burton, is an American film director, producer, artist, writer, and animator, he is known for his dark, gothic, eccentric, and quirky fantasy films such as which 1994 American biographical period comedy-drama film directed and produced by Tim Burton, and starring Johnny Depp as a cult filmmaker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
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
    },
    "producer": {
      "type": "string",
      "description": "The producer of the film."
    },
    "lead_actor": {
      "type": "string",
      "description": "The lead actor in the film."
    },
    "actor_role": {
      "type": "string",
      "description": "The character played by the lead actor."
    },
    "genre": {
      "type": "string",
      "description": "The genre description of the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "producer",
    "lead_actor",
    "actor_role",
    "genre"
  ],
  "additionalProperties": false
}
