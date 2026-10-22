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
The Joe Schmo Show: The Joe Schmo Show is a reality television hoax show created by Paul Wernick and Rhett Reese.  The series is broadcast in the U.S. on the cable network Spike.  The show's premise is that a target person or persons are led to believe that they are contestants on a reality television show; in reality, all of the other participants in the purported show – including the host – are actors, and their actions and the outcome of the purported show are all scripted in an attempt to elicit comedic reactions from the targets.  The show's first season, The Joe Schmo Show, aired in 2003, and its second season, Joe Schmo 2, aired in 2004.  The first season's hoax was conducted as a typical reality competition show while the second hoax was a "Bachelor"-like dating series.

Matt Kennedy Gould: Matt Kennedy Gould (born October 4, 1975) is an American former television personality.  He rose to prominence in 2003, when he was the protagonist of "The Joe Schmo Show", a fake reality show in which, unbeknownst to him, all the participants but Gould were actors portraying broad reality show participant archetypes.

Free Radio (TV series): Free Radio is a television show, created by Lance Krall and Rory Rosegarten.  The show originated on VH1, but has also played on Comedy Central, and Super Channel (Canada).  It stars Lance Krall, prominent for his role on "The Joe Schmo Show", and Anna Vocino, who also starred with Krall on "The Lance Krall Show".  The show focuses on a dysfunctional radio station, KBOM.  Krall plays a moronic intern turned moronic DJ when KBOM's regular shock jock, Rip Rebel, defects to satellite radio.  Lance eventually gets his own show entitled "Moron in the Morning".  Real celebrities guest star as themselves with Lance, who often either does not realize who they are or mixes them up with other celebrities on the air.  Most of the dialogue is improvised.

Ralph Garman: Ralph Garman (born November 17, 1964) is an American actor, comedian, and radio host best known as the host of "The Joe Schmo Show", for his voice work on the Fox animated series "Family Guy", and as the entertainment reporter and impressionist for the "Kevin and Bean" morning show on Los Angeles radio station KROQ-FM.

List of The Joe Schmo Show episodes: "The Joe Schmo Show" is an American reality television hoax show created by Paul Wernick and Rhett Reese.  The series premiered in the United States on Spike on September 2, 2003.  The show's third season premiered on January 8, 2013.

Lance Krall: Lance Krall (born December 9, 1970 in Monterey, California) is an American comedian and actor, television writer, director, and producer of Vietnamese descent.  He became well known after his portrayal as "Kip" in the role in faux-reality show "The Joe Schmo Show".  He went on to create and star in "The Lance Krall Show" and "Free Radio."

The Lance Krall Show: The Lance Krall Show is a 30-minute comedy television show featuring sketches and on-the-street interaction starring Lance Krall, who gained recognition through his character Kip on "The Joe Schmo Show".  The Lance Krall Show aired on Spike TV Mondays at 11:05 pm, with encores Thursdays at 11:05 pm.  The cast included Annie Humphrey, Phil Cater, Sarah Baker, Anna Vocino, Loren Tarquinio, Rob Poynter, and Michael Sweeney all performed together with Krall at The Whole World Theatre in Atlanta, Georgia.

Robert Belushi: Robert James Belushi (born October 23, 1980) is an American actor.  In films, he is best known for his work on "Sorority Row", "One Small Hitch", and "Valentine's Day".  On television, he is best known as Allen ("The Buddy") on the of Spike TV's "The Joe Schmo Show" and Linus the Bartender on the ninth and final season of CBS's "How I Met Your Mother".

Brian Goes Back to College: "Brian Goes Back to College" is the 15th episode of the fourth season of the American animated television series "Family Guy".  It originally aired on the Fox network in the United States on November 13, 2005.  Guest stars on the show were Ralph Garman, Mark Hentemann and Phil LaMarr.  The episode was described by show creator Seth MacFarlane to be "a real treat for "The A-Team" fans".  The episode contained several connections with "The New Yorker"; in response, they wrote a friendly article about the episode.  The plot consists of Peter, Joe, Cleveland and Quagmire winning a costume contest dressed as characters from "The A-Team", and deciding to improve their community by continuing to act like the characters of the show.  Brian is hired by "The New Yorker", but is later dismissed as he did not complete college, so he returns to finish his education.  It was rated TV-14-D in the United States and was rated 12 in the United Kingdom.

Stone Stanley Entertainment: Stone Stanley Entertainment is an American film and television production company, founded in 1990 by David G. Stanley and Scott A. Stone as Stone Stanley Productions.  Since then, Stone Stanley has produced several television programs, most notably "Shop 'til You Drop", "Loveline", "Legends of the Hidden Temple", "The Man Show", "The Mole", "Popstars", and "The Joe Schmo Show", plus six of the most successful Jane Fonda exercise videos, and the first Dimension Films theatrical motion picture release, "".

Question: Who is best known as the host of "The Joe Schmo Show" and was a guest star for Seth MacFarlane's television show?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person identified."
    },
    "role_in_joe_schmo_show": {
      "type": "string",
      "description": "The role the person is best known for in 'The Joe Schmo Show'."
    },
    "guest_star_appearance": {
      "type": "object",
      "properties": {
        "show_name": {
          "type": "string",
          "description": "The name of the television show where the person was a guest star."
        },
        "show_creator": {
          "type": "string",
          "description": "The creator of the television show where the person was a guest star."
        },
        "episode_name": {
          "type": "string",
          "description": "The specific episode name where the person guest-starred."
        },
        "episode_air_date": {
          "type": "string",
          "description": "The original air date of the episode."
        }
      },
      "required": [
        "show_name",
        "show_creator",
        "episode_name",
        "episode_air_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "role_in_joe_schmo_show",
    "guest_star_appearance"
  ],
  "additionalProperties": false
}
