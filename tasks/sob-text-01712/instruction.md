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
Evžen Rošický: Evžen Rošický (15 October 1914 Olomouc - 25 June 1942 Prague) was a Czech athlete and journalist.  Stadion Evžena Rošického is a Czech stadium named after him.  During World War II, he and his father Jaroslav Rošický were part of the anti-Nazi resistance group "Captain Nemo".  Evžen Rošický and his father were arrested on 18 June 1942, and one week later, on 25 June 1942, they were both executed in Prague.

The Alan Parsons Project: The Alan Parsons Project was the collective reference to several lineups of a British progressive rock team, active between 1975 and 1990, whose rosters consisted of Alan Parsons and Eric Woolfson surrounded by a varying number of session musicians and some relatively consistent band members such as guitarist Ian Bairnson, arranger Andrew Powell, bassist and vocalist David Paton, drummer Stuart Elliott, and vocalist Lenny Zakatek.

Stuart Elliott (drummer): Stuart Elliott (born Stuart Alexander Elliott, 22 May 1953, London, England) is an English drummer, composer and producer.  He was the original drummer for Steve Harley and Cockney Rebel and during his time with this band he became a session drummer playing for top artists such as Kate Bush, Al Stewart, The Alan Parsons Project, Roger Daltrey, Paul McCartney, Claudio Baglioni among others.

When I'm with You (Steve Harley song): "When I'm with You" is a song by the British singer-songwriter Steve Harley, released as a non-album single in 1989.  It was written and produced by Harley, ex-Cockney Rebel guitarist Jim Cregan and drummer Stuart Elliott.

Paul McCartney: Sir James Paul McCartney, {'1': ", '2': ", '3': ", '4': "} (born 18 June 1942) is an English singer-songwriter, multi-instrumentalist, and composer.  He gained worldwide fame as the bass guitarist and singer for the rock band the Beatles, widely considered the most popular and influential group in the history of pop music.  His songwriting partnership with John Lennon is the most celebrated of the post-war era.  After the group disbanded in 1970, he pursued a solo career and formed the band Wings with his first wife, Linda, and Denny Laine.

Jim Keltner: James Lee Keltner (born April 27, 1942) is an American drummer known primarily for his session work.  He was characterized by Bob Dylan biographer Howard Sounes as "the leading session drummer in America".

Ian Mosley: Ian F. Mosley (born 16 June 1953, Paddington, London, England) is an English drummer.  He is best known for his long-time membership of the neo-progressive rock band Marillion, which he joined for their second album, "Fugazi", released in 1984.  He had previously been an in demand session drummer.  Mosley's abilities have been widely praised, including by former Genesis guitarist Steve Hackett, Meshuggah drummer Tomas Haake and critic John Franck of AllMusic. " Modern Drummer" has characterised him as a "drumming great".

Bobby Graham (musician): Bobby Graham (11 March 1940 – 14 September 2009) was an English session drummer, composer, arranger and record producer.  Shel Talmy, who produced The Kinks, David Bowie and The Who, described Graham as "the greatest drummer the UK has ever produced."

The Kick Inside: The Kick Inside is the debut studio album by English singer-songwriter and musician Kate Bush.  It was released on 17 February 1978 and contains her UK number one hit, "Wuthering Heights".  The album peaked at number three on the UK Albums Chart and has been certified Platinum by the British Phonographic Industry.  The production included efforts by several progressive rock veterans, including Duncan Mackay, Ian Bairnson, David Paton, Andrew Powell, and Stuart Elliott of The Alan Parsons Project, and David Gilmour of Pink Floyd.

Neil Conti: Neil Conti (born 12 February 1959) is an English drummer and music producer who was an integral member of the pop/rock band Prefab Sprout, while continuing to be in demand as a session drummer for artists and bands such as David Bowie, Mick Jagger, Annie Lennox, Cher, Level 42, Laurie Anderson, Steve Winwood, Paul Young, Youssou N'dour, Brian Eno, Robert Palmer, Deep Forest, Will Young and many more.

Question: English drummer, composer and producer, Stuart Elliott, is known for being a session drummer for what English singer-songwriter, multi-instrumentalist and composer born 18 June 1942?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "session_drummer_name": {
      "type": "string",
      "description": "The name of the session drummer."
    },
    "session_drummer_nationality": {
      "type": "string",
      "description": "The nationality of the session drummer."
    },
    "session_drummer_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Roles performed by the session drummer."
    },
    "artist_name": {
      "type": "string",
      "description": "The name of the artist for whom the drummer was a session musician."
    },
    "artist_nationality": {
      "type": "string",
      "description": "The nationality of the artist."
    },
    "artist_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key roles or professions of the artist."
    },
    "artist_birth_date": {
      "type": "string",
      "description": "The birth date of the artist."
    }
  },
  "required": [
    "session_drummer_name",
    "session_drummer_nationality",
    "session_drummer_roles",
    "artist_name",
    "artist_nationality",
    "artist_roles",
    "artist_birth_date"
  ],
  "additionalProperties": false
}
