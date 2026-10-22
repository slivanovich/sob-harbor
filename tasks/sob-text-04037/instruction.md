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
Heroes and Villains (Once Upon a Time): "Heroes and Villains" is the Twelfth episode and mid-season finale of the fourth season of the American fantasy drama series "Once Upon a Time", which aired on December 14, 2014.  This episode marked the return of the villainess Maleficent, as well as the introductions of Cruella de Vil and Ursula the Sea Witch.

Susanne Blakeslee: Susanne Ann Blakeslee (also known as Susan Blakeslee, Suzanne Blakeslee and Suzanne Blakesley; born January 27, 1956) is an American voice actress and musical theatre actress.  Among her notable roles are the voices of Timmy Turner's fairy godmother Wanda and his mother Mrs. Turner on Nickelodeon's "The Fairly OddParents"; and as the voice of Maleficent in the "Kingdom Hearts" video game series and "Disney media".  She also does voices of Lady Tremaine, Queen Grimhilde, Cruella de Vil, and Madame Leota in Disney direct-to-video sequels, theme parks and merchandise.  In 2012, Blakeslee won an Ovation Award for Lead Actress in a Musical for "Forbidden Broadway Greatest Hits, Volume 2".

Disney's Animated Storybook: 101 Dalmatians: Disney's Animated Storybook: 101 Dalmatians is the sixth entry in the "Disney's Animated Storybook" point-and-click adventure interactive storybook PC game series, based on theatrical and home video releases.  This game was based on the Disney franchise of "One Hundred and One Dalmatians", which began with the 1961 film of the same name.  Like that movie, the plot of the game sees villain and fashionista Cruella de Vil steal a series of dalmatian puppies from married couple Roger and Anita and their pets Pongo and Perdita, who then attempt to rescue them back.  The game was developed by Media Station and published by Disney Interactive.  It was released on March 18, 1997.  The game is the only "Animated Storybook" title based on a Walt Disney Animation Studios film that was made before the Disney Renaissance (ignoring the two "Winnie the Pooh"-based titles).

Cruella de Vil: Cruella de Vil (spelled de Vil in the novel, spelled De Vil by Disney) is a character who appeared in Dodie Smith's 1956 novel "The Hundred and One Dalmatians", Disney's animated film adaptations "101 Dalmatians" and "", and Disney's live-action film adaptations "101 Dalmatians" and "102 Dalmatians" as the main antagonist.

Betty Lou Gerson: Betty Lou Gerson (April 20, 1914 – January 12, 1999) was an American actress, predominantly active in radio, but also in film and television, and as a voice actress.  She is best known as the voice of the villainous, selfish socialite Cruella de Vil from Walt Disney's animated film, "One Hundred and One Dalmatians" (1961) for which she was named a Disney Legend in 1996.

Victoria Smurfit: Victoria Smurfit (born 31 March 1974) is an Irish actress.  She is known for her role as Cruella De Vil in "Once Upon a Time".

102 Dalmatians: 102 Dalmatians is a 2000 American live action and CG-animated film adventure drama film directed by Kevin Lima in his live-action directorial debut and produced by Edward S. Feldman and Walt Disney Pictures.  It is the sequel to the 1996 film "101 Dalmatians", a live-action remake of the 1961 Disney animated film of the same name and stars Glenn Close reprising her role as Cruella de Vil as she attempts to steal puppies for her "grandest" fur coat yet.  Close and Tim McInnerny were the only two actors from the first film to return for the sequel, however.  The film was nominated for an Academy Award for Best Costume Design, but lost to "Gladiator."

Trial &amp; Retribution: Trial & Retribution is a feature-length ITV police procedural television drama series that first aired on ITV1 on 19 October 1997.  Written and devised by Lynda La Plante as a follow-on from her successful television series "Prime Suspect", each episode was typically broadcast over two nights.  David Hayman stars as the main protagonist of the series, DCS Michael "Mike" Walker.  Throughout the series, he has two main sidekicks: DI Pat North (Kate Buffery) and DCI Róisín Connor (Victoria Smurfit).

One Hundred and One Dalmatians: One Hundred and One Dalmatians, often abbreviated as 101 Dalmatians, is a 1961 American animated adventure film produced by Walt Disney and based on the 1956 novel "The Hundred and One Dalmatians" by Dodie Smith.  The 17th Disney animated feature film, the film tells the story of a litter of dalmatian puppies who are kidnapped by the villainous Cruella de Vil (Betty Lou Gerson), who wants to use their fur to make into coats.  Their parents, Pongo and Perdita, (Rod Taylor and Cate Bauer respectively) set out to save their children from Cruella, all the while rescuing 84 additional puppies that were bought in pet shops, bringing the total of dalmatians to 101.

Rotten to the Core (song): "Rotten to the Core" is a song from Disney Channel's 2015 television film "Descendants", whose music and lyrics were composed by Joacim Persson, Shelly Peiken and Johann Alkenas.  The song was performed in its original show-tune version in the film by the main cast – Dove Cameron, Cameron Boyce, Booboo Stewart and Sofia Carson– in their vocal roles as Mal (daughter of Maleficent), Carlos (son of Cruella de Vil), Jay (son of Jafar) and Evie (daughter of The Evil Queen).  The song peaked at number 38 in the Billboard Hot 100.  A second version, performed by actress and singer Sofia Carson, was released as a single on December 18, 2015.

Question: What is the name of the actor who portrays the main protagonist in the 1997 police procedural television drama, broadcast on ITV1, that also featured the Irish actress who played Cruella De Vil in "Once Upon a Time"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_drama": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the police procedural television drama."
        },
        "first_aired_year": {
          "type": "integer",
          "description": "The year the television drama first aired."
        },
        "broadcast_network": {
          "type": "string",
          "description": "The network on which the television drama was broadcast."
        }
      },
      "required": [
        "title",
        "first_aired_year",
        "broadcast_network"
      ],
      "additionalProperties": false
    },
    "protagonist_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who portrays the main protagonist."
        },
        "character_name": {
          "type": "string",
          "description": "The name of the character played by the protagonist actor."
        }
      },
      "required": [
        "name",
        "character_name"
      ],
      "additionalProperties": false
    },
    "linking_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress who appeared in both the TV drama and 'Once Upon a Time'."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        },
        "role_in_tv_drama": {
          "type": "string",
          "description": "The character role of the actress in the TV drama."
        },
        "role_in_once_upon_a_time": {
          "type": "string",
          "description": "The character role of the actress in 'Once Upon a Time'."
        }
      },
      "required": [
        "name",
        "nationality",
        "role_in_tv_drama",
        "role_in_once_upon_a_time"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tv_drama",
    "protagonist_actor",
    "linking_actress"
  ],
  "additionalProperties": false
}
