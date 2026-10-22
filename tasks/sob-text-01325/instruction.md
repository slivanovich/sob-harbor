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
Close to Home (2005 TV series): Close to Home is an American crime drama television series co-produced by Warner Bros.  Television and Jerry Bruckheimer Television for CBS.  While in pre-production the series was known as "American Crime".  It first aired from October 4, 2005 to May 11, 2007 and starred actress Jennifer Finnigan as Annabeth Chase, a Deputy Prosecutor for Marion County, Indiana.  Created by Jim Leonard, the series was primarily filmed in Southern California.  The score composer was Michael A. Levine.

Sons of Anarchy (season 5): The fifth season of the American television drama series "Sons of Anarchy" created by Kurt Sutter about the lives of a close-knit outlaw motorcycle club operating in Charming, a fictional town in California's Central Valley.  The show centers on protagonist Jackson "Jax" Teller (Charlie Hunnam), first shown as vice president then as president of the club, who begins questioning the club and himself.

Hunter Via: Hunter M. Via (born May 2, 1976 in Charleston, West Virginia) is an American film and television editor.  After graduating from the College of Charleston with a degree in communication, and attending Full Sail University where he earned a film degree, Via entered the film industry working as an editor.  He edited several early projects by fellow Full Sail graduate Darren Lynn Bousman before landing a job as an assistant editor on the FX original series "The Shield" in 2002.  Beginning in 2004, Via took on the role of editor and ended up cutting seventeen episodes of the series through 2007.  In 2007, Via edited his first studio feature film, Frank Darabont's "The Mist".  Via went on to work on several other television shows and film, including "Sons of Anarchy", "Mother's Day", "The Craigslist Killer", and "Torchwood".  Via edited twelve episodes of the popular AMC series "The Walking Dead" and received the 61st Annual ACE Eddie Award for Best Edited One-Hour Series for Commercial Television for his work on the pilot episode.

Sons of Anarchy (season 6): The sixth season of the American television drama series "Sons of Anarchy" created by Kurt Sutter about the lives of a close-knit outlaw motorcycle club operating in Charming, a fictional town in California's Central Valley.  The show centers on protagonist Jackson "Jax" Teller (Charlie Hunnam), the president of the club, who begins questioning the club and himself.

Katey Sagal: Catherine Louise Sagal (born January 19, 1954) is an American actress and singer-songwriter.  She is best known for her role as Peggy Bundy, Al's sarcastic, lazy, bon bon-eating wife, on "Married... with Children" and for her role voicing the character Leela on the animated science-fiction series "Futurama" from 1999 to 2003 and 2008 to 2013, as well as for starring on the show "8 Simple Rules" in the role of Cate Hennessy.  In the latter role, she worked with John Ritter until his death, leading to Sagal's taking over as the series lead for the remainder of the show's run.  Sagal has been married to "Sons of Anarchy" creator Kurt Sutter since 2004.  Currently, Sagal is a series regular on CBS's Superior Donuts.

The Bastard Executioner: The Bastard Executioner is an American historical fiction drama television series, created by Kurt Sutter and aired on FX from September 15, 2015, to November 17, 2015.  On November 18, 2015, Sutter announced that FX had cancelled the series after one season.

Sons of Anarchy: Sons of Anarchy is an American crime drama television series created by Kurt Sutter, which aired from 2008 to 2014.  It follows the lives of a close-knit outlaw motorcycle club operating in Charming, a fictional town in California's Central Valley.  The show stars Charlie Hunnam as Jackson "Jax" Teller, initially the vice president, who begins questioning the club and himself.  Brotherhood, loyalty and redemption are constant themes.

List of Sons of Anarchy episodes: "Sons of Anarchy", a television drama series created by Kurt Sutter, premiered on September 3, 2008 on the cable network FX in the United States.  The series concluded on December 9, 2014, after 92 episodes broadcast over seven seasons.

The Inside (TV series): The Inside is an American crime drama television series created by Tim Minear and Howard Gordon and produced by Imagine Television.  "The Inside" follows the work of the FBI's Los Angeles Violent Crimes Unit (VCU), a division dedicated to investigating particularly dangerous crimes.  "The Inside" initially aired on the Fox Network from June 8 to July 13, 2005.  Although thirteen episodes were produced, Fox aired only seven episodes before canceling the series.  All thirteen episodes were subsequently aired on ITV4 in the UK in 2006.

Katie Findlay: Katie Findlay (born August 28, 1990) is a Canadian actress.  She is best known for her role as Rosie Larsen in the American crime drama television series "The Killing".  From 2013 to 2014, Findlay portrayed Maggie Landers in The CW's teen drama "The Carrie Diaries".  From 2014 to 2015, Findlay starred as Rebecca Sutter in the first season of the ABC series "How to Get Away with Murder".  In 2017 she joined the cast of FXX comedy series "Man Seeking Woman" in the show's third season.

Question: Hunter M. Via worked on which American crime drama television series created by Kurt Sutter, which aired from 2008 to 2014?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_title": {
      "type": "string",
      "description": "The title of the television series."
    },
    "creator_name": {
      "type": "string",
      "description": "The name of the person who created the series."
    },
    "genre": {
      "type": "string",
      "description": "The genre of the television series."
    },
    "air_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The year the series first aired."
        },
        "end_year": {
          "type": "integer",
          "description": "The year the series concluded."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    },
    "involved_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person involved with the series."
        },
        "involvement_type": {
          "type": "string",
          "description": "Description of the person's involvement with the series."
        }
      },
      "required": [
        "name",
        "involvement_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_title",
    "creator_name",
    "genre",
    "air_period",
    "involved_person"
  ],
  "additionalProperties": false
}
