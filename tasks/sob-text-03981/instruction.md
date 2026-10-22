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
New Order (band): New Order are an English rock band formed in 1980, currently comprising Bernard Sumner, Stephen Morris, Gillian Gilbert, Phil Cunningham and Tom Chapman.  The band was formed in 1980 by Sumner, Morris, and Peter Hook, who were the remaining members of post-punk group Joy Division following the suicide of vocalist Ian Curtis.  They added Gilbert on keyboards later that year.

Stephen Morris (musician): Stephen Paul David Morris (born 28 October 1957) is an English multi-instrumentalist, composer and record producer who is best known for his work with the rock band New Order and, previously, Joy Division.  He also wrote and performed in The Other Two, a band consisting of Morris and his wife, Gillian Gilbert.  Morris also participated in the New Order spin-off band Bad Lieutenant.  He is known for his precise drumming that seamlessly weaves with New Order's and Joy Division's drum machine sounds. " Stylus Magazine" ranked Morris No. 5 on their list of "50 Greatest Rock Drummers of All Time".

Total: From Joy Division to New Order: Total: From Joy Division to New Order is a compilation album of material from Joy Division and New Order.  It was released in the United Kingdom on 6 June 2011 and is the first album to feature songs from both Joy Division and New Order in one album.  It features five Joy Division tracks, including "Love Will Tear Us Apart", and thirteen New Order tracks, including a previously unreleased track, "Hellbent".  An online "Deluxe version" also includes music videos.

Community 2: A NewOrderOnline Tribute: Community 2 is a tribute album dedicated to the work of Ian Curtis, Gillian Gilbert, Peter Hook, Stephen Morris and Bernard Sumner of the bands New Order and Joy Division that was released in 2006.

Elegia: "Elegia" is a piece composed by Peter Hook, Gillian Gilbert, Stephen Morris, and Bernard Sumner for the British rock band New Order.  Unusually for New Order, it is a dark wave instrumental in A minor with a time signature of 12/8.  It can be found on their third studio album, "Low-Life" (1985).  The band have stated that the song was written in memory of Ian Curtis, lead singer of the band's former incarnation, Joy Division.  Elegia is Greek for elegy.

Community: A NewOrderOnline Tribute: Community is a tribute album dedicated to the work of Ian Curtis, Gillian Gilbert, Peter Hook, Stephen Morris and Bernard Sumner of the bands New Order and Joy Division that was released in 2004.

Doubts Even Here: "Doubts Even Here" is the seventh track of eight on New Order's debut album "Movement", released on November 13, 1981.  After the death of Joy Division singer Ian Curtis, the surviving members formed New Order with drummer Stephen Morris's girlfriend Gillian Gilbert joining five months later.  This led to a dispute over who should fill Curtis' shoes with the lead vocalist role.  All three male members were in contention, but due to Bernard Sumner's voice being significantly different from Curtis', New Order opted for him to take the role, wanting New Order's sound to be different from Joy Division's.  Ironically with this new vocalist, in addition to "Doubts Even Here", the first track ("Dreams Never End") on the first album recorded by New Order, "Movement", is sung by bassist Peter Hook with spoken contributions by Gillian Gilbert, reading from the Bible.  The lyrics were written by Stephen Morris.

Round &amp; Round (New Order song): "Round & Round" is a song by the English band New Order from their fifth studio album "Technique" (1989).  The song was written by band members Gillian Gilbert, Peter Hook, Stephen Morris and Bernard Sumner, and the album version was produced entirely by New Order.  "Round & Round" was re-recorded for a single release, with Stephen Hague as co-producer.

New Order discography: The discography of New Order, an English rock band, consists of ten studio albums, twelve compilation albums, three live albums, five extended plays (EPs), thirty-eight singles, twelve video releases, thirty-three music videos and a number of soundtrack appearances.  New Order were formed in 1980 by singer and guitarist Bernard Sumner, bassist Peter Hook and drummer Stephen Morris.  The group began life as a continuation of their former incarnation Joy Division.  Joy Division had disbanded after the death of the lead singer Ian Curtis.  Gillian Gilbert, who was Morris' girlfriend at the time, soon joined the group and played guitar and keyboards.

Control (2007 film): Control is a 2007 British biographical film about the life of Ian Curtis, singer of the late-1970s English post-punk band Joy Division.  It is the first feature film directed by Anton Corbijn, who had worked with Joy Division as a photographer.  The screenplay by Matt Greenhalgh was based on the biography "Touching from a Distance" by Curtis's widow Deborah, who served as a co-producer on the film.  Tony Wilson, who released Joy Division's records through his Factory Records label, also served as a co-producer.  Curtis' bandmates Bernard Sumner, Peter Hook, and Stephen Morris provided incidental music for the soundtrack via their post-Joy Division incarnation New Order.  "Control" was filmed partly on location in Nottingham, Manchester, and Macclesfield, including areas where Curtis lived, and was shot in colour and then printed to black-and-white.  Its title comes from the Joy Division song "She's Lost Control", and the fact that much of the plot deals with the notion that Curtis tried to remain

Question: Total: From Joy Division to New Order is a compilation album of material from Joy Division and which English rock band formed in 1980, currently comprising Bernard Sumner, Stephen Morris, Gillian Gilbert, Phil Cunningham and Tom Chapman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the English rock band."
    },
    "band_attributes": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The general type of the band, e.g., 'rock band'."
        },
        "formed_year": {
          "type": "integer",
          "description": "The year the band was formed."
        },
        "current_member_count": {
          "type": "integer",
          "description": "The number of current members in the band."
        },
        "current_members": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the names of the current members of the band."
        }
      },
      "required": [
        "type",
        "formed_year",
        "current_member_count",
        "current_members"
      ],
      "additionalProperties": false
    },
    "compilation_album_info": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the compilation album mentioned in the question."
        },
        "material_included": {
          "type": "boolean",
          "description": "Indicates if material from this band is included in the album."
        }
      },
      "required": [
        "album_title",
        "material_included"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "band_attributes",
    "compilation_album_info"
  ],
  "additionalProperties": false
}
