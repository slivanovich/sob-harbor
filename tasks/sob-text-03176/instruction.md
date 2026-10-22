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
Van Oekel's Discohoek: Van Oekel's Discohoek was a Dutch television show, aired on VPRO in 1974-1975.  The show, written by Wim T. Schippers and produced by Ellen Jens, starred Dolf Brouwers as the comedic character Sjef van Oekel, and parodied music television programs of the era.  Artists lip-synched their songs, but were frequently interrupted and insulted by van Oekel.  The show had a real coup when Captain Beefheart made an appearance.  The show also starred one of the first TV appearances of Donna Summer, who later claimed that her breakthrough began with her performance of her song "Hostage", in which she gracefully went along with the scripted absurdity and chaos.  The show inspired a similarly absurd show on the German WDR.

Superman/Batman: Public Enemies: Superman/Batman: Public Enemies is a 2009 original direct-to-video animated superhero film adaptation of "Public Enemies"—the opening story arc of DC Comics' "Superman/Batman"—which focuses on Superman and Batman teaming up to prevent a meteorite from striking Earth and take down Lex Luthor, who has been elected President of the United States.  The film is the sixth in the line of the DC Universe Animated Original Movies line released by Warner Premiere and Warner Bros.  Animation.  Voice actors from the DCAU reprised their roles, although it is not a DCAU production and is said not to be connected with that universe beyond sharing of voice actors.  The film is directed by Sam Liu.

List of Family Guy cast members: "Family Guy" is an American animated sitcom that features five main voice actors, and numerous regular cast and recurring guest stars.  The principal voice cast consists of show creator Seth MacFarlane, Alex Borstein, Mila Kunis (who replaced Lacey Chabert after the first season), Seth Green, and Mike Henry.  Recurring voice actors include Patrick Warburton, Adam West, John G. Brennan, Nicole Sullivan and Jennifer Tilly, and repeat guest stars include Phyllis Diller, Charles Durning, Rush Limbaugh, and Phil LaMarr.

What's with Andy?: What's with Andy?  is a Canadian children's animated series that started airing on June 30, 2001 and ended on March 4, 2007.  It was originally an interactive Flash movie with completely different voice actors and a promotion for Fox Kids.  Shortly after, a TV series was developed with new voice actors and it aired on Teletoon.  The series was produced by CinéGroupe, with Season 2 being co-produced with SIP Animation.  Super RTL was involved in the production of Seasons 2 and 3.  It was based on a series of books by Andy Griffiths.

List of The Simpsons cast members: "The Simpsons" is an American animated sitcom that includes six main voice actors, and numerous regular cast and recurring guest stars.  The principal cast consists of Dan Castellaneta, Julie Kavner, Nancy Cartwright, Yeardley Smith, Hank Azaria and Harry Shearer.  Tress MacNeille, Pamela Hayden, Maggie Roswell, Russi Taylor, Marcia Wallace, Marcia Mitzman Gaven and Karl Wiedergott have appeared as supporting cast members.  Repeat guest cast members include Albert Brooks, Phil Hartman, Jon Lovitz, Joe Mantegna and Kelsey Grammer.  With one exception, episode credits list only the voice actors, and not the characters they voice.

The Little Mermaid (TV series): Disney's The Little Mermaid is an American animated television series produced by Walt Disney Television Animation based on the 1989 Disney film of the same name.  It features the adventures of Ariel as a mermaid prior to the events of the film.  This series is the first Disney television series to be spun off from a major animated film.  Some of the voice actors of the film reprise their roles in the series, among them Jodi Benson as Ariel, Samuel E. Wright as Sebastian, Kenneth Mars as King Triton and Pat Carroll as Ursula.  Other voice actors include Edan Gross and Bradley Pierce as Flounder, and Jeff Bennett as Prince Eric.

List of The Little Mermaid episodes: Disney's "The Little Mermaid" is a 1992–1994 American 2D hand-drawn animated television series produced by Walt Disney Television Animation, based on the 1989 Disney film of the same name and following the adventures of Ariel as a mermaid prior to the events of the film.  Some of the voice actors of the film reprise their roles in the series, among them Jodi Benson as Ariel, Samuel E. Wright as Sebastian, Kenneth Mars as King Triton and Pat Carroll as Ursula.  Other voice actors include Edan Gross and Bradley Pierce as Flounder, and Jeff Bennett as Prince Eric.

Fable III: Fable III is an action role-playing open world video game, developed by Lionhead Studios and published by Microsoft Game Studios for the Xbox 360 and Microsoft Windows.  The third game in the "Fable" series, the story focuses on the player character's struggle to overthrow the King of Albion, the player character's brother, by forming alliances and building support for a revolution.  After a successful revolt, the player becomes the monarch and is tasked with attempting to defend Albion from a great evil.  The game includes voice acting by Ben Kingsley (Sabine), Stephen Fry (Reaver), Simon Pegg (Ben Finn), Naomie Harris (Page), Michael Fassbender (Logan), Zoë Wanamaker (Theresa), Bernard Hill (Sir Walter Beck), Nicholas Hoult (Elliot), John Cleese (Jasper), Kellie Bright (Hero of Brightwall female), and Louis Tamone (Hero of Brightwall male).

List of What's with Andy? episodes: "What's with Andy? " is a Canadian animated series that aired from 2001 to 2007.  It was originally an interactive Flash movie with completely different voice actors and a promotion for Fox Kids.  Shortly after, a TV series was developed with new voice actors and it aired on Teletoon.  The series was produced by CinéGroupe.  It was based on a series of books written by Andy Griffiths and illustrated by Terry Denton, which was entitled "Just...".

Naomie Harris: Naomie Melanie Harris, {'1': ", '2': ", '3': ", '4': "} (born 6 September 1976) is an English actress.  She started her career as a child actress, appearing on the children television series "Simon and the Witch" in 1987.  She played voodoo witch Tia Dalma in the second and third "Pirates of the Caribbean" films, Selena in "28 Days Later", and Winnie Mandela in "".  She played Eve Moneypenny in the James Bond films "Skyfall" and "Spectre".  In 2016, she starred in the critically acclaimed film "Moonlight"; a performance which earned her several nominations for Best Supporting Actress awards, including the Golden Globe, BAFTA, and the Academy Award.

Question: In which 2016 film starred one of the voice actors from Fable III?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film released in 2016."
    },
    "voice_actor_from_fable_iii": {
      "type": "string",
      "description": "The name of the actor who was a voice actor in Fable III and starred in the film."
    },
    "fable_iii_character_voiced": {
      "type": "string",
      "description": "The character voiced by the actor in Fable III."
    }
  },
  "required": [
    "film_title",
    "voice_actor_from_fable_iii",
    "fable_iii_character_voiced"
  ],
  "additionalProperties": false
}
