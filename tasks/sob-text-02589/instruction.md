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
Chim Chim Cher-ee: "Chim Chim Cher-ee" is a song from "Mary Poppins", the 1964 musical motion picture.  It was originally sung by Dick Van Dyke and Julie Andrews, and also is featured in the Cameron Mackintosh/Disney "Mary Poppins" musical.  The song can be heard in the "Mary Poppins" scene of The Great Movie Ride at Disney's Hollywood Studios and during the "Mary Poppins" segment of "" at Disneyland.

Mary Poppins (soundtrack): Mary Poppins (Original Soundtrack) is the soundtrack album to the 1964 film "Mary Poppins".

Vincent Cirelli: Vincent Cirelli is a special effects supervisor.  Known for his works at Luma Pictures as a visual effects supervisor in acclaimed films such as "" (2007), "No Country for Old Men" (2007), "The Midnight Meat Train" (2008), "" (2008), "Harry Potter and the Half-Blood Prince" (2009), "The Book of Eli" (2010), "" (2011), "" (2012), "Prometheus" (2012), "The Avengers" (2012), "Saving Mr. Banks" (2013), "Guardians of the Galaxy" (2014), "" (2015), "In the Heart of the Sea" (2015), "Deadpool" (2015) and "Doctor Strange" (2016), for which he received an Academy Award for Best Visual Effects nomination at the 89th Academy Awards.

Mary Poppins Opens the Door: Mary Poppins Opens the Door is a British children's fantasy novel by the Australian-British writer P.L. Travers, the third book and last novel in the "Mary Poppins" series that features the magical English nanny Mary Poppins.  It was published in 1943 by Harcourt, Brace & World, Inc and illustrated by Mary Shepard and Agnes Sims.

Mary Poppins (song): "Mary Poppins" is a song from the 2015 stage musical "Love Birds" with music and lyrics by Robert J. Sherman.  It is sung by "The Original Quack Pack", a penguin barbershop quartet who resemble the penguins from the 1964 Walt Disney motion picture, "Mary Poppins".  In dialogue leading up to the song, the penguins explain that while they did know the same nanny, (Mary Poppins) they are not the same penguins as in the movie.  The song expresses their longing for the magical nanny of literary fame.

Mary Poppins Returns: Mary Poppins Returns (also known as Mary Poppins 2) is an upcoming American musical fantasy film directed by Rob Marshall and written by David Magee.  It is the sequel to the 1964 film "Mary Poppins".  The film stars Emily Blunt, Lin-Manuel Miranda, Ben Whishaw, Emily Mortimer, Pixie Davies, Joel Dawson, Nathanael Saleh, Julie Walters, Colin Firth, Dick Van Dyke and Meryl Streep.  Set 25 years after the 1964 film, it will feature Mary Poppins, the former nanny of Jane and Michael Banks, re-visiting them after a family tragedy.  The film is scheduled for release on December 25, 2018, giving it one of the longest gaps between film sequels in history.

Mary Poppins (film): Mary Poppins is a 1964 American musical-fantasy film directed by Robert Stevenson and produced by Walt Disney, with songs written and composed by the Sherman Brothers.  The screenplay is by Bill Walsh and Don DaGradi, loosely based on P. L. Travers' book series "Mary Poppins".  The film, which combines live-action and animation, stars Julie Andrews in the role of Mary Poppins who visits a dysfunctional family in London and employs her unique brand of lifestyle to improve the family's dynamic.  Dick Van Dyke, David Tomlinson, and Glynis Johns are featured in supporting roles.  The film was shot entirely at the Walt Disney Studios in Burbank, California using painted London background scenes.

I Love to Laugh: "I Love to Laugh", also called "We Love to Laugh", is a song from Walt Disney's film "Mary Poppins".  It was composed by Richard M. Sherman and Robert B. Sherman.  The song is sung in the film by "Uncle Albert" (Ed Wynn), and "Bert" (Dick Van Dyke) as they levitate uncontrollably toward the ceiling, eventually joined by Mary Poppins (Julie Andrews) herself.  The premise of the scene, that laughter and happiness cause Uncle Albert (and like-minded visitors) to float into the air, can be seen as a metaphor for the way laughter can "lighten" a mood.  (Compare Peter Pan's flight power, which is also powered by happy thoughts.)  Conversely, thinking of something sad literally brings Albert and his visitors "down to earth" again.  The song states a case strongly in favor of laughter, even if Mary Poppins appears to disapprove of Uncle Albert's behavior, especially since it not only complicates the task of getting Albert down, but the infectious mood sends Bert and the Banks children into the air as well.

Step in Time: "Step In Time" is a song and dance number from Walt Disney's 1964 film "Mary Poppins", and it is composed by Richard M. Sherman and Robert B. Sherman.  The choreography for this song was provided by Marc Breaux and Dee Dee Wood.  It is sung by Bert, the chimney sweep (Dick Van Dyke) and the other chimney sweeps on the rooftops of London.  In the first part of the song, the lines he says in the verses are "Kick your knees up", "'Round the chimney", "Flap like a birdie", "Up on the railing", "Over the rooftops" and "Link your elbows" followed by an interlude.  The interlude continues with Bert, Mary Poppins, Michael, Jane and all the chimney sweepers dancing around the rooftops and as Admiral Boom looks at them with the telescope, he thinks that they're Hottentots, so he orders Mr. Binnacle to make them scram with colorful fireworks.  In the second part, as all the chimney sweepers get in the house of George Banks, Mrs. Brill walks into the living room looking at them and screams, "They're at it again!"  and she runs away trying to strike one of the chimney sweepers with a frying pan.  As Jane, Michael, Mary Poppins and Bert get in the same place, Ellen runs around the dining room with an "OW!"  and the chimney sweepers flip her.  The other phrases in the rest of the musical number are "Votes for women," "It's the master," and "What's all this?"

Saving Mr. Banks: Saving Mr. Banks is a 2013 period drama film directed by John Lee Hancock from a screenplay written by Kelly Marcel and Sue Smith.  Centered on the development of the 1964 film "Mary Poppins", the film stars Emma Thompson as author P. L. Travers and Tom Hanks as filmmaker Walt Disney, with supporting performances by Paul Giamatti, Jason Schwartzman, Bradley Whitford, and Colin Farrell.  Deriving its title from the father in Travers' story, "Saving Mr. Banks" depicts the author's fortnight-long meetings during 1961 in Los Angeles, during which Disney attempts to obtain the screen rights to her novels.

Question: Vincent Cirelli worked on what film centered on the development of the 1964 film "Mary Poppins"?

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
    "person_involved": {
      "type": "string",
      "description": "The name of the person involved in the film."
    },
    "person_role": {
      "type": "string",
      "description": "The role of the person in the film."
    },
    "film_focus": {
      "type": "string",
      "description": "What the film is centered on or about."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "person_involved",
    "person_role",
    "film_focus"
  ],
  "additionalProperties": false
}
