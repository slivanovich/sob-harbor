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
Adult Swim Singles Program 2011: Adult Swim Singles Program 2011 is a series of free download single releases in which the Cartoon Network franchise Adult Swim released a song from a different artist every Tuesday from June 6, 2011 to August 2, 2011.  The series followed the success of the first series, "Adult Swim Singles Program 2010".  Both series were presented by Kia Motors.  Each single originally had to be downloaded separately.

Rick and Morty (season 3): The third season of the animated television series "Rick and Morty" originally aired in the United States on Cartoon Network's late night programming block, Adult Swim.  It premiered with "The Rickshank Rickdemption," which aired unannounced on April 1, 2017 and was replayed every half hour from 8pm to 12am ET, as part of Adult Swim's annual April Fools' prank.  The episode was also simulcast as a looping live stream on Adult Swim's site.  The remaining episodes began airing on July 30, 2017.  The season will feature a total of 10 episodes.

Adult Swim (Australia): Adult Swim in Australia is an adult-oriented free-to-air television block that airs Sunday nights on 9Go! .  It was originally a separate network that shared channel space with The Comedy Channel, starting 1 January 2008.  Some Adult Swim shows have also aired on SBS2, and in October 2013 full episodes and short clips were made available on Adult Swim's Australian website, which has since become unavailable.

Junction 11 Radio: Junction11 Radio is the student radio station for the University of Reading.  They broadcast locally from the Whiteknights campus in University retail outlets and to the world over the internet live stream on a full-time basis.  The station started broadcasting in 2001 on 1287AM and transferred to solely online live stream in 2007 due to licensing costs and to ensure higher broadcast quality.

List of The Brak Show episodes: This is a list of episodes for the animated Adult Swim television series, "The Brak Show".  The pilot episode, "Mr. Bawk Ba Gawk", aired unannounced on December 21, 2000, on Cartoon Network.  The series officially premiered with "Goldfish" on September 2, 2001, on Adult Swim, and ended with three seasons and 28 episodes on December 31, 2003, with "Cardburkey".  On May 24, 2007, an additional webisode entitled "Space Adventure" was released on Adult Swim Video, no further webisodes have ever been produced.

The Rickshank Rickdemption: "The Rickshank Rickdemption" is the first episode in the third season of the American animated television sitcom "Rick and Morty", and the twenty-second episode overall in the series.  It was written by Mike McMahan and directed by Juan Meza-Leon.  The season three premiere first aired unannounced on Adult Swim in the United States on April 1, 2017 when it was watched by 676,000 American households.  On the first day of its original broadcast, "The Rickshank Rickdemption" was replayed every half hour from 8pm to 12am ET with improved ratings, as a part of Adult Swim's annual April Fools' Day joke.

Sealab 2021: Sealab 2021 is an American adult animated television series created by Adam Reed and Matt Thompson.  It was shown on Cartoon Network's late-night programming block, Adult Swim.  Cartoon Network aired the show's first three episodes in December 2000 before the official inception of the Adult Swim channel on September 2, 2001, with the final episode airing on April 25, 2005.  "Sealab 2021" is a spin-off of "Space Ghost Coast to Coast", and is one of the four original Williams Street series that premiered in 2000 before Adult Swim officially launched, the others being "Aqua Teen Hunger Force", "The Brak Show" and "Harvey Birdman, Attorney at Law".

Adult Swim: Adult Swim (stylized as [adult swim]) is the adult-oriented nighttime programming block of American children's cable network, Cartoon Network, that operates daily from 8:00 pm to 6:00 am, Eastern and Pacific Time.  It is programmed by Williams Street Productions, a subsidiary of Turner, which also developed two other programming blocks for Cartoon Network: Toonami (which later became a block on Adult Swim in 2012) and Miguzi.  The block gets its name from a phrase used by public swimming pools in the United States to label designated times when children are restricted from using the facilities in favor of adults.

Rabbot: "Rabbot" is the pilot episode and the first episode of the first season of the animated television series "Aqua Teen Hunger Force".  A rough-cut version of this episode originally aired in the United States prior to the launch of Adult Swim on December 30, 2000 on Cartoon Network unannounced, the final cut of this episode later aired on Adult Swim on September 16, 2001.  In the episode Master Shake, Frylock, and Meatwad investigate the recent destruction of Carl's car, while a giant mechanical rabbit destroys downtown.

Adult Swim Singles Program 2012: Adult Swim Singles Program 2012 is a series of free download single releases in which the Cartoon Network franchise Adult Swim released a song from a different artist every Monday from June 18, 2012 to September 10, 2012.  The series was presented by Kia, the same sponsor from Adult Swim Singles Program 2010 and Adult Swim Singles Program 2011.  On September 10, 2012, the bonus track "@deathgripz" by Death Grips was released as well as an option to download all the singles as one album.

Question: Who was the writer of the episode that was played as a looping live stream on Adult Swim's website?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_title": {
      "type": "string",
      "description": "The title of the episode."
    },
    "writer_name": {
      "type": "string",
      "description": "The name of the writer for the episode."
    },
    "streaming_details": {
      "type": "object",
      "properties": {
        "platform": {
          "type": "string",
          "description": "The platform where the episode was streamed."
        },
        "stream_type": {
          "type": "string",
          "description": "The type of stream (e.g., looping live stream)."
        }
      },
      "required": [
        "platform",
        "stream_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "episode_title",
    "writer_name",
    "streaming_details"
  ],
  "additionalProperties": false
}
