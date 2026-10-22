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
Groovejet (If This Ain't Love): "Groovejet (If This Ain't Love)" is a song by Italian electronic music producer Spiller, featuring vocals from British singer and songwriter Sophie Ellis-Bextor.  The single was released in August 2000 by Positiva Records.  It peaked at number one in the UK, New Zealand, Ireland and Australia, as well as charting at number three on the American Hot Dance Chart.  On 15 September 2000, the song was certified gold record status by the British Phonographic Industry, and was certified platinum on 22 July 2013.  Various versions of the single were later featured on the German reissue and some UK editions of Ellis-Bextor's debut solo album, "Read My Lips".

Kiki Dee: Pauline Matthews (born 6 March 1947), better known by her stage name Kiki Dee, is an English singer born in Little Horton, Bradford, West Riding of Yorkshire.  Known for her blue-eyed soul vocals, she was the first female singer from the UK to sign with Motown's Tamla Records.

Mounira El Mahdeya: Mounira El Mahdeya (born Zakiyya Hassan) (Arabic: منيرة المهدية‎ ‎ ) was an Egyptian singer born in 1885 in Alexandria; she died in 1965.  The singer, better known under the nickname of "Sultana of the song" or "The Sultana", was considered to be the leading Egyptian singer between the two wars.

Ian Kelsey: Ian Kelsey (born 17 December 1966) is an English actor.  He is best known for his roles as Dave Glover in ITV Soap "Emmerdale", Matt Brewer in "Down to Earth", Patrick Spiller in BBC Continuing Drama "Casualty" and Howard Bellamy in daytime soap opera "Doctors", and for his 6-year long role as Detective Inspector Richard Mayne in the TV crime series "Blue Murder" alongside Caroline Quentin in her lead role as DCI Janine Lewis.

Sophie Ellis-Bextor: Sophie Michelle Ellis-Bextor (born 10 April 1979) is an English singer, songwriter and model.  She first came to prominence in the late 1990s, as the lead singer of the indie rock band Theaudience.  After the group disbanded, Ellis-Bextor went solo, achieving widespread success in the early 2000s.  Her music is a mixture of mainstream pop, disco, nu-disco, and 1980s electronic influences.

Dimash Kudaibergen: Dinmukhamed Kanatuly Kudaibergen () is a Kazakh singer born on May 24, 1994 in Aktobe, Kazakhstan.  Dimash's parents Kanat Kudaibergenovich and Svetlana Aitbayeva are honored music artists of the Republic of Kazakhstan.  Dimash is a tenor altino.  He was the 2015 Grand Prix winner of the Slavianski Bazaar in Vitebsk In the same year, he was named the "Nation's Favorite" (kazakh. " Халықтың сүйіктісі"), participant of the international festival "ABU TV song" in Istanbul, Turkey, and awarded with the Certificate of Honor of the President of the Republic of Kazakhstan for an important contribution into strengthening the unity of the people in Kazakhstan.  He placed second in "Singer 2017".

Spiller: Cristiano Spiller (born 3 April 1975) is an Italian electronic music DJ and record producer.  He is best known for his 2000 single, "Groovejet (If This Ain't Love)", featuring Sophie Ellis-Bextor.  The song reached number-one in the UK, Australia, Ireland, and New Zealand.  It sold over two million copies and was the first song to be played on an iPod.

Gloria Mann: Gloria Mann was an American pop singer born in Philadelphia, Pennsylvania.  Mann scored two hits on the U.S. "Billboard" Hot 100 in 1955.  The first was a cover version of "Earth Angel", which reached number 18.  Later that year, "Teen Age Prayer" peaked at number 19; this featured Sid Bass leading the backing orchestra.  Both were released on Sound Records.  She died in 2001.

Regina Richards: Regina Richards (born 1961), best known by her stage name Regina, is an American pop music singer born in Brooklyn, New York.  She is best known for her hit song "Baby Love," which reached Number 10 on the "Billboard" Hot 100 in 1986.  "Baby Love" was her only song to chart on the Hot 100, making her a one hit wonder.  The song also reached #50 on the UK Singles Chart that same year.

Sarah Bates (singer): Sarah Bates (née Harrop, October 1758 - 11 December 1811) was an English singer born in Lancashire.  She was married to the conductor Joah Bates.

Question:  "Groovejet " is a song by Cristiano Spiller that featured an English singer born in which year ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "main_artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the main artist."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the main artist."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "featured_singer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the featured singer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the featured singer."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the featured singer."
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "main_artist",
    "featured_singer"
  ],
  "additionalProperties": false
}
