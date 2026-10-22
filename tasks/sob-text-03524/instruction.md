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
Die Young (Kesha song): "Die Young" is a song by American recording artist Kesha.  It was released on September 25, 2012 as the lead single from her second studio album, "Warrior" (2012).  Kesha co-wrote the song with its producers, Dr. Luke, Benny Blanco, and Cirkut, with additional writing from Nate Ruess, the lead singer of Fun.  Kesha wrote the lyrics after traveling around the world and embarking on a spiritual journey.

Nate Ruess: Nathaniel Joseph Ruess (born February 26, 1982) is an American singer and songwriter.  He is the lead singer of the indie pop band Fun. , and previously of The Format.  As of 2015, he also performs as a solo musician.

List of number-one singles of 2013 (Australia): The ARIA Singles Chart ranks the best-performing singles in Australia.  Its data, published by the Australian Recording Industry Association, is based collectively on each single's weekly physical and digital sales.  In 2013, seventeen singles claimed the top spot, including "Thrift Shop" by Macklemore and Ryan Lewis, which started its peak position in late 2012.  Fifteen acts achieved their first number-one single in Australia, either as a lead or featured artist: Mary Lambert, Nate Ruess, Baauer, Ray Dalton, Passenger, Daft Punk, Pharrell Williams, Robin Thicke, T.I., Avicii, 2 Chainz, Redfoo, Dami Im, Taylor Henderson and John Legend.  Im and Henderson were the only Australian artists to achieve a number-one single.

Fun (band): Fun (stylized as fun.)  is an American pop rock band based in New York City.  The band was formed by Nate Ruess (former lead singer of The Format), with Andrew Dost (of Anathallo), and Jack Antonoff (of Steel Train and Bleachers).  Fun has released two albums: "Aim and Ignite" in August 2009 and "Some Nights" in February 2012.

Jens Kidman: Jens Kidman (born 8 June 1966) is a Swedish metal vocalist.  He is best known for being the lead vocalist for the Swedish extreme metal band Meshuggah.  He is famous for his very aggressive shouts and screams and for his unique stage presence.

Just Give Me a Reason: "Just Give Me a Reason" is a song recorded by American singer and songwriter Pink, featuring fun. 's lead singer Nate Ruess.  The song was chosen as the third single from Pink's sixth studio album, "The Truth About Love" (2012).  Jeff Bhasker assisted the artists in writing the song and is also the producer.  "Just Give Me a Reason" is a pop ballad about the desire to hold on to a relationship even when it appears to be breaking down.  It starts off with a simple melody played on the piano, as Pink starts to sing the first verse and chorus, the latter of which introduces drum machines and bass.  Ruess then sings the second verse, and the rest of the song is sung as a duet.  The song ends with a piano solo, similar to the intro.  It has a duration of four minutes and two seconds.

Fun discography: The discography of American indie pop band Fun consists of two studio albums, seven extended plays, 11 singles and seven music videos. Following the split of his previous band The Format, lead singer Nate Ruess formed Fun in 2008 with musicians Andrew Dost and Jack Antonoff, both of whom had previously toured with The Format.  Fun began recording sessions for their debut album in September 2008 and embarked on a North American tour the following month.  In May 2009, they issued their debut single, "At Least I'm Not as Sad (As I Used to Be)". " Aim and Ignite", the band's first full-length album, was released by Nettwerk Records on August 25, 2009 and peaked at number 71 on the United States "Billboard" 200 chart.  The album produced an additional two singles, "All the Pretty Girls" and "Walking the Dog", which were then followed by the release of the single "C'mon", a collaboration with American alternative rock band Panic!  at the Disco.

The Format: The Format was an American indie rock band formed by Nate Ruess and Sam Means.  The band announced a hiatus on February 4, 2008.  Their style can be considered a mixture of indie, alternative, punk and folk music, with elements of 1960s and 1970s pop music.  Though Means and Ruess are the foremost members of the band, they have played, toured, and recorded with Mike Schey, Mark Buzard, Don Raymond, and—for the DVD recording and summer 2007 tour—The Honorary Title's current drummer and The Format alumnus Adam Boyd.  The Format chose their name to make fun of the music industry's inclination towards a cookie-cutter "format" for a hit.

Grand Romantic: Grand Romantic is the debut studio album of Nate Ruess, lead vocalist from The Format and Fun.  It was released on June 16, 2015, by Fueled By Ramen.  The album was produced by Some Nights producer Jeff Bhasker.  Following the hiatus of Fun, Ruess announced that he would be working on material for a solo project.

The Vanity Label: The Vanity Label is an American record label created by Nate Ruess and Sam Means of The Format, the label’s only signed artist (as of 2007).  The company was created by Ruess and Means subsequent the absorption of Elektra Records into Atlantic Records Group in 2004, as The Format was dropped from the newly formed Atlantic Records Group.  The newly formed Vanity Label was created to launch their then upcoming album, and Vanity Label’s first album release, "Dog Problems".

Question: Are Jens Kidman and Nate Ruess both lead vocalists?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals are lead vocalists, false otherwise."
    },
    "individuals": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "role_description": {
            "type": "string",
            "description": "The description of their role as found in the context."
          },
          "is_lead_vocalist": {
            "type": "boolean",
            "description": "True if the individual is identified as a lead vocalist, false otherwise."
          }
        },
        "required": [
          "name",
          "role_description",
          "is_lead_vocalist"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals"
  ],
  "additionalProperties": false
}
