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
Tanto (album): Tanto ("So Much") is the second studio album by Spanish singer-songwriter Pablo Alborán.  It was released in Spain on November 6, 2012.  The album peaked at number one in Spain and Portugal.  "Tanto" is the follow-up to Alborán's debut album "Pablo Alborán" (2011).

Caer en tentación: Caer en tentación is a Mexican telenovela produced by Giselle González for Televisa, and it started airing on Mexican broadcast channel Las Estrellas on September 18, 2017.  Based on the Argentine drama by Erika Halvorsen and Gonzalo Demaría, titled "Amar después de amar".  The series stars Silvia Navarro, Gabriel Soto, Adriana Louvier, and Carlos Ferro.

Pablo Alborán (album): Pablo Alborán is the debut album by Spanish singer-songwriter Pablo Alborán.  Produced by Manuel Illán, many of the songs included in the album had already achieved YouTube attention before its release, as home videos featuring Alborán performing in front of a webcam, alone with his guitar.  The album also includes duets with Carminho ("Perdóname"), Estrella Morente ("Desencuentro"), and Diana Navarro ("Solamente Tú").  The iTunes version adds the bonus track "Cuando te Alejas".

Palmeras en la nieve (song): "Palmeras en la nieve" (English: "Palm Trees in the Snow" ) is a song recorded by Spanish singer-songwriter Pablo Alborán for the soundtrack to the Spanish romantic drama film "Palmeras En La Nieve".  The song was released worldwide on 11 December 2015 and peaked at number 23 in Spain in February 2016.

Vívela: "Vívela" (English: "Live it" ) is a song recorded by the Spanish singer-songwriter Pablo Alborán.  The song was included on his third studio album, "Terral".  The song was released as the lead single from his second live album "Tour Terral (Tres Noches en Las Ventas)" (2015).  It was released as a digital download and CD single and peaked at number 1 on the Spanish Singles Chart in October 2015.

Pasos de cero: "Pasos de cero" (roughly "Steps from scratch") is a song recorded by Spanish singer-songwriter Pablo Alborán.  It was released as the second single from his third studio album, "Terral".  The song was written by Alborán and produced by Eric Rosse.

Se Puede Amar: "Se Puede Amar" ("You Can Love") is a song recorded by Spanish singer-songwriter Pablo Alborán.  The song was released worldwide on 22 April 2016 and peaked at number 6 in Spain; thus becoming Alborán's twelfth top ten single in Spain.

Por Fin: "Por Fin" ("Finally") is a song recorded by Spanish singer-songwriter Pablo Alborán.  The song was released as the first single from his third studio album "Terral" (2014).  The song was written by Alborán and produced by Eric Rosse.  "Por Fin" is a soft rock ballad.  Alborán received a nomination for Song of the Year at the 16th Latin Grammy Awards.

En Acústico: En Acústico is the first live album by Spanish singer-songwriter Pablo Alborán.  Following by success of his first self-named studio album, "Pablo Alborán", he released this album on November 15, 2011.  It included acoustic versions of most of the tracks in his debut album, as well as two new songs ("Te He Echado De Menos" and "No Te Olvidaré") and four bonus tracks.  The song "Perdóname" ("Forgive Me") was re-recorded featuring Portuguese singer Carminho, and was released as the first single of the album, peaking at number one on the Spanish singles chart on November 13, 2011, thus helping "En Acústico" to debut also at number one on the albums chart one week later, on November 20, 2011, and to top the Portuguese Albums Chart in January 2012.

Saturno (song): "Saturno" is a song recorded by Spanish singer-songwriter Pablo Alborán, serving as the lead single for his forthcoming third studio album.  The song was released worldwide on 8 September 2017.  The song is the main theme of the Mexican telenovela "Caer en tentación".

Question: "Saturno" is a song recorded by Spanish singer-songwriter Pablo Alborán and is the main theme of the Mexican telenovela based on the Argentine drama titled what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_information": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the song."
        },
        "artist_name": {
          "type": "string",
          "description": "The name of the artist who recorded the song."
        }
      },
      "required": [
        "title",
        "artist_name"
      ],
      "additionalProperties": false
    },
    "telenovela_information": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the Mexican telenovela."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the telenovela was produced."
        },
        "original_drama_title": {
          "type": "string",
          "description": "The title of the Argentine drama the telenovela is based on."
        }
      },
      "required": [
        "title",
        "country_of_origin",
        "original_drama_title"
      ],
      "additionalProperties": false
    },
    "song_role_in_telenovela": {
      "type": "string",
      "description": "Describes the role of the song in the telenovela."
    }
  },
  "required": [
    "song_information",
    "telenovela_information",
    "song_role_in_telenovela"
  ],
  "additionalProperties": false
}
