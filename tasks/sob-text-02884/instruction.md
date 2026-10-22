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
Psycho Jukebox: Psycho Jukebox is the debut solo album by Jon Fratelli, frontman of The Fratellis and formerly of Codeine Velvet Club.  Released on 25 July 2011.  It was recorded with Tony Hoffer (who produced "Costello Music" and mixed "Codeine Velvet Club") in the Sound Factory studios in Los Angeles.

The Fratellis: The Fratellis are a Scottish rock band from Glasgow, formed in 2005.  The band consists of lead vocalist and guitarist Jon Fratelli (born John Lawler), bass guitarist Barry Fratelli (born Barry Wallace), and drummer and backing vocalist Mince Fratelli (born Gordon McRory).  Their singles "Chelsea Dagger" and "Whistle for the Choir" were both top ten hits in the UK charts.

Mos Eisley Cantina: The Chalmun's Cantina (often called "Mos Eisley Cantina" or "the "Star Wars" Cantina") is a fictional bar (cantina) of the "Star Wars" universe located in the "pirate city" of Mos Eisley on the planet Tatooine.  It is the haunt of freight pilots and other dangerous characters of various alien races and contains booths, a bar counter, and some free-standing tables, and sometimes a band of musicians named Figrin D'an and the Modal Nodes.

Eyes Wide, Tongue Tied: Eyes Wide, Tongue Tied is the fourth album by Scottish rock band The Fratellis.  The album was revealed on 1 June 2015, alongside the first track "Me and the Devil" (which was given away for free from the bands website), and released on 21 August 2015.  The album was written and recorded in Los Angeles, California during November 2014 with Tony Hoffer, who also produced the band's debut album "Costello Music" and Jon Fratelli's solo album "Psycho Jukebox".

Jon Fratelli: Jon Fratelli (born John Paul Lawler, 4 March 1979, Glasgow, Scotland) is a Scottish musician and songwriter best known for his work with the band The Fratellis.  He has also played in a band called Codeine Velvet Club, and also performed as a solo artist.

Chelsea Dagger: "Chelsea Dagger" is a song by Scottish rock band The Fratellis.  It was released as the second single from their debut studio album, "Costello Music" (2006), on 28 August 2006.  It is named after Jon Fratelli's wife Heather, a burlesque dancer whose stage name – a play on Britney Spears – he borrowed for the song.  Fratelli described the tune as "a rock 'n' roll gig in an old speakeasy or something like that."

Codeine Velvet Club: Codeine Velvet Club was a Scottish alternative rock band formed in 2008 by Lou Hickey and Jon Lawler, a.k.a. Jon Fratelli from The Fratellis.  The band's debut album "Codeine Velvet Club" was released on 28 December 2009 in the UK and on 6 April 2010 in the US.

David Glen Eisley: David Glen Eisley (born September 5, 1952) is an American rock singer, songwriter, and actor.

Band Geeks: "Band Geeks" is the second part of the 15th episode of the second season, and the second half of the 35th episode overall, of the American animated television program "SpongeBob SquarePants".  It originally aired on Nickelodeon in the United States on September 7, 2001.  It was written by C. H. Greenblatt, Aaron Springer, and Merriwether Williams, and the animation was directed by Frank Weiss.  Springer served as storyboard director, and Greenblatt served as storyboard artist.  The song "Sweet Victory" by David Glen Eisley was featured in the episode and was later released on the album "" in 2005.

A Heady Tale: "A Heady Tale" is the third single by Scottish rock band, The Fratellis from their second album, "Here We Stand".  It was released on 22 December 2008.  This song is 1 of the 4 tracks on "Here We Stand" to have a heavy use of piano (the other 3 being "Mistress Mabel", "Milk And Money" & "Moriaty's Last Stand").  The B-sides "Mon Yous, Mon us but no' Them" and "When All the Lights Go Out" were also piano intensive.  Jon Fratelli has said that the B-Side "Lonesome Anti Christmas Blues" is the "most depressing Christmas song written".

Question: Which of these musicians is Scottish, David Glen Eisley or Jon Fratelli?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the musician identified as Scottish."
    },
    "is_scottish": {
      "type": "boolean",
      "description": "True if the musician is Scottish, false otherwise."
    },
    "nationality": {
      "type": "string",
      "description": "The stated nationality of the musician."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the identified nationality based on the context."
    },
    "other_musician_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the other musician mentioned in the question."
        },
        "nationality": {
          "type": "string",
          "description": "The stated nationality of the other musician."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "musician_name",
    "is_scottish",
    "nationality",
    "reasoning",
    "other_musician_details"
  ],
  "additionalProperties": false
}
